# Software Requirements Specification (SRS)

**Standard:** IEEE Std 830-1998 Format  
**Project:** Book Club Reading Challenge & Discussion Portal  
**Problem Statement #55** | **Domain:** Media, Events & Community  
**Student:** Sushruth S | **SRN:** PES1UG24CS486  
**Institution:** PES University, Department of Computer Science & Engineering  

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) establishes the complete functional and non-functional requirements for the **Book Club Reading Challenge & Discussion Portal**. It serves as the contractual baseline between stakeholders, domain architects, developers, and quality assurance engineers.

### 1.2 Scope of the Software Product
The portal is a specialized social reading and community platform that:
- Facilitates personal reading goal tracking (daily/monthly page increments and streak metrics).
- Provides spoiler-shielded chapter discussion threads where plot points remain concealed until explicit member interaction.
- Enables Discussion Leads to pin thought-provoking discussion prompts and moderate toxic comments using Role-Based Access Control.
- Executes democratic monthly book selection polls featuring tamper-proof duplicate vote prevention and sub-200ms real-time results synchronization.
- Awards gamified digital milestone badges to motivate continuous literary participation.

### 1.3 Definitions, Acronyms, and Abbreviations
- **SRS:** Software Requirements Specification
- **RTM:** Requirements Traceability Matrix
- **RBAC:** Role-Based Access Control
- **JWT:** JSON Web Token
- **FR:** Functional Requirement
- **NFR:** Non-Functional Requirement
- **WBS:** Work Breakdown Structure
- **ACID:** Atomicity, Consistency, Isolation, Durability
- **BTBSC:** Bug Tracker Book Club (Jira Defect Key prefix)

### 1.4 References
- IEEE Std 830-1998: *Recommended Practice for Software Requirements Specifications*.
- PES University CSE SE Lab 1 Problem Statement #55 Guideline Document.
- Jira Agile Reports (Kanban, Scrum, Bug Tracking: `BTBSC-1` to `BTBSC-4`).

---

## 2. Overall Description

### 2.1 Product Perspective
The Book Club Portal is a cloud-native, responsive web application operating on a 4-Tier Layered Architecture with event-driven WebSocket and Redis messaging extensions. It interfaces with external book catalog APIs (e.g., Open Library API) for automatic book cover and synopsis retrieval.

### 2.2 User Classes and Characteristics
- **Club Member:** Primary end-user. Logs daily reading pages, joins chapter discussions, casts one vote in monthly polls, unlocks achievement badges.
- **Discussion Lead:** Elevated privileged member. Creates chapter discussion threads, pins prompts, closes discussions, deletes flagged inappropriate comments, and accesses moderation audit logs.
- **System Administrator / Backend Engine:** Secondary actor. Issues authentication tokens, evaluates milestone badge criteria asynchronously, maintains Redis tally caches, and executes atomic database transactions.

### 2.3 Operating Environment
- **Server Platform:** Linux / Containerized Docker runtime, Python 3.12 / Node.js backend.
- **Database Engine:** PostgreSQL 16 relational database with connection pooling (PgBouncer).
- **In-Memory Cache:** Redis 7 for real-time pub/sub and tally caching.
- **Client Platforms:** Modern web browsers (Google Chrome 110+, Mozilla Firefox 110+, Apple Safari 16+, Microsoft Edge) on desktop, tablet, and mobile devices (screen width $\ge 375\text{px}$).

### 2.4 Design and Implementation Constraints
- High peak concurrency during monthly poll closing hours requires sub-200ms response times.
- Zero duplicate vote tolerance: Enforced via unique compound database keys `UNIQUE(user_id, poll_id)`.
- Client and server-side spoiler isolation: Content tagged with `[spoiler]` must not leak in search results or unmasked DOM nodes.
- Strict compliance with WCAG 2.1 Level AA accessibility standards.

---

## 3. Specific Requirements

### 3.1 External Interface Requirements
- **User Interfaces:** Clean, glassmorphic dark-mode web application built with responsive CSS, semantic HTML5 tags, high contrast ratios ($\ge 4.5:1$), and keyboard accessible controls (`tabindex`, `aria-label`).
- **Software Interfaces:**
  - RESTful HTTP/2 API Gateway exposing JSON endpoints.
  - WebSocket interface for bidirectional real-time tally updates (`/ws/polls/{id}`).
  - Open Library REST API for ISBN and cover image fetching.
- **Communications Interfaces:** HTTPS (TLS 1.3 only) across all external endpoints; WSS for encrypted WebSocket channels.

### 3.2 System Features & Functional Requirements

#### 3.2.1 Feature 1: Spoiler Content Masking & Chapter Unmasking (FR-001)
- **Input:** Discussion comment text containing `[spoiler]...[/spoiler]` tags.
- **Processing:** Server tags entity with `has_spoiler=true`. Client applies CSS blur filter mask. Search index pipeline removes spoiler text replacing with `[Spoiler Content Hidden]`.
- **Output:** Blurred comment box with "Reveal Spoiler" interactive button.
- **Error Handling / Remediation:** Prevents defect **BTBSC-1** where search preview leaked raw spoiler content.

#### 3.2.2 Feature 2: Reading Progress & Challenge Goal Tracking (FR-002)
- **Input:** User ID, Book ID, integer page count completed.
- **Processing:** Validates $0 < \text{pages} \le \text{book.total\_pages} - \text{current\_page}$. Updates user profile, increments active streak, computes completion percentage.
- **Output:** Updated progress gauge, remaining page tally, completion status.
- **Error Handling / Remediation:** Rejects negative numbers and page counts exceeding book length (Remediates **BTBSC-2**).

#### 3.2.3 Feature 3: Discussion Moderation & RBAC (FR-003)
- **Input:** Moderator action (pin thread, delete comment, lock thread) with JWT bearer token.
- **Processing:** Verifies token signature and checks role claim (`role == 'DISCUSSION_LEAD'`). If valid, commits moderation state and appends immutable audit log.
- **Output:** Moderated thread state; returns `403 Forbidden` if user is regular member (Remediates **BTBSC-3**).

#### 3.2.4 Feature 4: Democratic Monthly Poll Voting (FR-004)
- **Input:** User ID, Poll ID, Candidate Book ID.
- **Processing:** Executes atomic database transaction checking `ballots` table for existing `(user_id, poll_id)` record. If clean, inserts ballot, increments Redis tally counter, and emits WebSocket event.
- **Output:** Vote confirmation receipt; button locks; returns `409 Conflict` on duplicate attempt (Remediates **BTBSC-4**).

#### 3.2.5 Feature 5: Gamified Milestone Badge Award Engine (FR-005)
- **Input:** Reading progress event trigger (e.g., total pages logged $\ge 500$, books finished $\ge 1$).
- **Processing:** Asynchronous worker evaluates unlocked badge criteria against user history.
- **Output:** New badge entity added to user profile badge showcase.

---

## 4. Non-Functional Requirements (NFRs)

- **Performance (NFR-001):** 95% of monthly poll vote requests processed in $< 200\text{ms}$ under 1,000 concurrent users.
- **Security & Availability (NFR-002):** System availability $\ge 99.9\%$ ($\le 43.8\text{ mins}$ unscheduled downtime/month). All database columns storing user credentials encrypted with AES-256; passwords hashed with Argon2id.
- **Usability (NFR-003):** Fluid responsive layout from $375\text{px}$ to $1920\text{px}$, passing WCAG 2.1 AA accessibility guidelines.
- **Data Integrity (NFR-004):** Full ACID compliance; compound unique index on ballots table ensures zero duplicate vote anomalies.
- **Maintainability (NFR-005):** Modular design pattern with OpenAPI 3.0 specification and $\ge 85\%$ test coverage.
- **Auditability (NFR-006):** Structured JSON logs recorded for all moderation events with timestamp, user ID, and target post ID.
