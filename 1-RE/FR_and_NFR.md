# Requirements Engineering: Functional & Non-Functional Requirements

**Course:** Software Engineering Lab — Individual Project Assignment  
**Problem Statement #55:** Book Club Reading Challenge & Discussion Portal  
**Domain:** Media, Events & Community  
**Student:** Sushruth S | **SRN:** PES1UG24CS486  
**Institution:** PES University, Department of Computer Science & Engineering  

---

## 1. Executive Summary & Domain Scope

The **Book Club Reading Challenge & Discussion Portal** is a collaborative community platform designed to elevate individual and group reading engagement. It provides gamified reading challenge tracking, spoiler-protected chapter discussion forums, role-based community moderation, and tamper-resistant democratic monthly voting for upcoming community reads.

This document formalizes the complete set of **Functional Requirements (FR)** and **Non-Functional Requirements (NFR)** derived from stakeholder analysis, domain constraints, and earlier lab milestones.

---

## 2. Functional Requirements (FR)

| Req ID | Requirement Name | Priority | Primary Actor | Description & Processing Rules | Acceptance Criteria |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **FR-001** | Spoiler Content Masking & Reveal Interaction | **High** | Club Member | The system shall obscure any comment or snippet tagged with `[spoiler]` tags using a client-side CSS blur mask. The content shall remain hidden until the user explicitly clicks the "Reveal Spoiler" button or marks the associated chapter as completed. Search preview snippets must also omit or mask spoiler content. | **Pass:** Spoiler text rendered blurred; clicking unmasks comment; search preview replaces spoiler with `[Spoiler Content Hidden]`.<br>**Fail:** Text visible in plaintext on load or in search results (Ref: Defect BTBSC-1). |
| **FR-002** | Reading Progress & Goal Tracking | **High** | Club Member | The system shall allow members to set daily and monthly reading page goals, log integer page increments, enforce non-negative and upper-bound validation against total book pages, and dynamically compute the completion percentage. | **Pass:** Progress gauge and statistics increment immediately on valid integer page submission; rejects negative values and values exceeding book page limit.<br>**Fail:** Negative page values accepted (Ref: Defect BTBSC-2). |
| **FR-003** | Chapter Discussion Moderation & RBAC | **High** | Discussion Lead | The system shall enforce Role-Based Access Control (RBAC) so that only verified Discussion Leads and Admins can create chapter-specific discussion threads, pin prompts, close threads, and delete flagged toxic comments. Regular members are restricted to reading, replying, and reporting. | **Pass:** Discussion Lead UI displays moderation controls; regular member requests to moderation endpoints return `403 Forbidden`.<br>**Fail:** Regular members can access pin/delete actions (Ref: Defect BTBSC-3). |
| **FR-004** | Democratic Monthly Book Selection Poll | **High** | Club Member | The system shall allow each authenticated member to cast exactly one vote in the active monthly poll from nominated titles. The system must enforce atomic ballot writing and prevent duplicate votes across browser sessions or page refreshes. | **Pass:** Vote recorded; confirmation banner displayed; voting buttons permanently disabled for that cycle; duplicate submission returns `409 Conflict`.<br>**Fail:** Multiple votes accepted from same user (Ref: Defect BTBSC-4). |
| **FR-005** | Gamified Milestone Badge Award Engine | **Medium** | Club Member | The system shall monitor member reading milestones (e.g., first 100 pages, 500 pages, completing first book, 7-day reading streak) and automatically award digital achievement badges to their public profile. | **Pass:** Badge appears in user showcase within 5 seconds of milestone trigger event; trigger cannot fire duplicate badges for the same tier.<br>**Fail:** Badge not awarded or awarded repeatedly. |
| **FR-006** | User Authentication & Profile Management | **High** | Club Member / Lead | The system shall authenticate users via secure email/password or OAuth 2.0, generate stateless JWT session tokens, and maintain user profiles including reading history, current books, and earned badges. | **Pass:** Successful login returns signed JWT; invalid credentials return `401 Unauthorized`; passwords salted and hashed with Argon2id.<br>**Fail:** Plaintext passwords stored or session hijackable. |
| **FR-007** | Real-Time Poll Results Broadcasting | **Medium** | Club Member | The system shall broadcast aggregated monthly poll vote counts to all connected clients in real time using WebSocket channels whenever a valid vote is registered. | **Pass:** Client leaderboard chart increments within 200 ms of ballot commit without requiring manual page reload.<br>**Fail:** Client requires browser refresh to see updated vote tally. |
| **FR-008** | Automated Content Moderation & Toxicity Filter | **Low** | System / Lead | The system shall run newly posted comments through an automated profanity and toxicity filter. Flagged comments are quarantined in a moderation queue for Discussion Lead review before public display. | **Pass:** Comments containing prohibited vocabulary are flagged with status `PENDING_REVIEW` and excluded from public thread view.<br>**Fail:** Abusive content immediately visible to general members. |

---

## 3. Non-Functional Requirements (NFR)

| Req ID | Quality Attribute | Target Standard & Metric | Acceptance Criteria | Rationale & Architectural Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Performance & Scalability | - Sub-200 ms response time for 95th percentile under 1,000 concurrent voting users.<br>- Read queries served in &lt; 50 ms. | **Pass:** Load tests confirm 1,000 concurrent poll voters experience &lt; 200 ms latency with zero transaction collisions.<br>**Fail:** P95 latency exceeds 1,500 ms or connection drops exceed 0.1%. | High-traffic voting occurs near monthly poll deadlines; Redis in-memory caching and connection pooling prevent database bottlenecks. |
| **NFR-002** | Security & Availability | - 99.9% uptime during active reading challenge cycles (&le; 43.8 mins downtime/month).<br>- AES-256 encryption at rest; TLS 1.3 in transit.<br>- Argon2id password hashing. | **Pass:** Zero plaintext credentials; automated failover test resumes service within 60 seconds; SSL Labs test scores Grade A+.<br>**Fail:** Plaintext PII in logs, lack of HTTPS, or unscheduled downtime &gt; 44 mins. | Protects member privacy, prevents credential leakage, and ensures continuous service availability during community events. |
| **NFR-003** | Usability & Accessibility | - Fully responsive design across Desktop (&ge;1280px), Tablet (&ge;768px), and Mobile (&ge;375px).<br>- WCAG 2.1 Level AA compliance. | **Pass:** Contrast ratio &ge; 4.5:1; fully navigable via keyboard; screen reader compatible tags on all spoiler buttons.<br>**Fail:** Mobile layout breaks or accessibility audit fails. | Book club members read and discuss books across varied devices (smartphones, tablets, e-readers). |
| **NFR-004** | Data Integrity & Consistency | - Strict ACID transactions for poll voting.<br>- Unique compound database constraint on `(user_id, poll_id)`. | **Pass:** Stress testing 50 concurrent duplicate submissions from single account records exactly 1 vote and 49 conflict errors.<br>**Fail:** Race condition results in duplicate ballot records. | Guarantees fair, democratic book selection and eliminates voting fraud. |
| **NFR-005** | Maintainability & Modularity | - Layered modular architecture with loose coupling.<br>- Comprehensive OpenAPI 3.0 / Swagger documentation.<br>- &gt;80% automated unit and integration test coverage. | **Pass:** All pull requests pass automated CI tests; API documentation auto-generates from code annotations.<br>**Fail:** Untested core modules or tightly coupled spaghetti codebase. | Enables independent scaling of discussion and voting services and smooth onboarding for student developers. |
| **NFR-006** | Auditability & Observability | - Structured JSON logging for all moderation actions (delete, pin, flag) and authentication events.<br>- Distributed tracing with OpenTelemetry. | **Pass:** Every lead moderation action generates an immutable audit record containing `timestamp`, `actor_id`, `target_comment_id`, and `reason`.<br>**Fail:** Unaudited comment deletions or missing audit logs. | Ensures accountability in community moderation and rapid troubleshooting of production defects. |

---

## 4. Traceability Summary

All 8 Functional Requirements and 6 Non-Functional Requirements are mapped bidirectionally to:
1. **Lab 1 Deliverables:** UML Use Cases (`UC-01` to `UC-09`) and Sequence Flows.
2. **Lab 2 Agile Artifacts:** Epics, Kanban Board items, Scrum Backlog (29 Story Points), and Jira Bug Reports (`BTBSC-1` to `BTBSC-4`).
3. **Lab 3 Engineering Deliverables:** Architecture Subsystems, IEEE 830 SRS, Work Breakdown Structure (WBS), Copilot Engine, and Testing Suites.
