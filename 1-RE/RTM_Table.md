# Requirements Traceability Matrix (RTM)

**Project:** Book Club Reading Challenge & Discussion Portal (Problem Statement #55)  
**Student:** Sushruth S | **SRN:** PES1UG24CS486  
**Course:** Software Engineering Lab — Individual Project Assignment  
**Institution:** PES University, Department of Computer Science & Engineering  

---

## 1. RTM Purpose & Scope

The **Requirements Traceability Matrix (RTM)** establishes bidirectional traceability across all phases of the software development lifecycle:
- **Forward Traceability:** Ensures every requirement from Lab 1 and Lab 2 is realized in the software architecture, work breakdown structure (WBS), implementation code, and verified by test cases.
- **Backward Traceability:** Ensures that every architectural module, test case, and code artifact traces directly to an authorized business requirement, preventing scope creep and unverified code paths.

---

## 2. Complete Bidirectional RTM Table

| Req ID | Requirement Summary | Type / Priority | UML Use Case (Lab 1) | Architecture Component (Lab 3) | WBS Work Package (Lab 3) | Jira Issue / Defect (Lab 2) | Story Points | Test Case ID & Method | Verification Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| **FR-001** | Spoiler Content Masking & Reveal Interaction | Functional / **High** | `UC-02`, `UC-07` | Spoiler Filter & Masking Service; Client CSS Blur Engine | `WP-3.1` | `BTBSC-1`, `KB-101` | 5 | `TC-FR001-01` (Unit: CSS Blur Mask)<br>`TC-FR001-02` (Integration: Search Preview Sanitizer) | **Verified (PASSED)** |
| **FR-002** | Reading Progress & Goal Tracking | Functional / **High** | `UC-01` | Reading Progress Engine; User Dashboard UI | `WP-3.2` | `BTBSC-2`, `KB-102` | 5 | `TC-FR002-01` (Unit: Positive Integer Validation)<br>`TC-FR002-02` (Unit: Progress % Formula) | **Verified (PASSED)** |
| **FR-003** | Chapter Discussion Moderation & RBAC | Functional / **High** | `UC-03` | Moderation Service; RBAC Gatekeeper; Forum UI | `WP-3.3` | `BTBSC-3`, `KB-103` | 5 | `TC-FR003-01` (Unit: RBAC Lead Permission)<br>`TC-FR003-02` (Integration: Quarantined Delete) | **Verified (PASSED)** |
| **FR-004** | Democratic Monthly Book Selection Poll | Functional / **High** | `UC-04`, `UC-08`, `UC-09` | Poll & Voting Service; Persistence Transaction Layer | `WP-3.4` | `BTBSC-4`, `KB-104` | 5 | `TC-FR004-01` (Unit: Single Vote Per User)<br>`TC-FR004-02` (Stress: Duplicate Vote Race Test) | **Verified (PASSED)** |
| **FR-005** | Gamified Milestone Badge Award Engine | Functional / **Medium** | `UC-01`, `UC-06` | Gamification & Badge Service; Event Bus | `WP-3.5` | `KB-105`, `SC-205` | 3 | `TC-FR005-01` (Unit: Threshold Milestone Event)<br>`TC-FR005-02` (Integration: Profile Showcase) | **Verified (PASSED)** |
| **FR-006** | User Authentication & Profile Management | Functional / **High** | `UC-08` | API Gateway Auth Middleware; User Service | `WP-2.1` | `KB-106`, `SC-206` | 3 | `TC-FR006-01` (Security: Argon2id Hash Verify)<br>`TC-FR006-02` (API: JWT Expiration Check) | **Verified (PASSED)** |
| **FR-007** | Real-Time Poll Results Broadcasting | Functional / **Medium** | `UC-09` | WebSocket Gateway; Redis Pub/Sub Engine | `WP-3.6` | `KB-107`, `SC-207` | 3 | `TC-FR007-01` (Perf: Broadcast Latency &lt; 200ms)<br>`TC-FR007-02` (E2E: Client Multi-Socket Sync) | **Verified (PASSED)** |
| **FR-008** | Automated Content Moderation & Toxicity Filter | Functional / **Low** | `UC-03` | Toxicity Filter Engine; Moderation Queue | `WP-3.7` | `KB-108`, `SC-208` | 2 | `TC-FR008-01` (Unit: Regex & Lexicon Match)<br>`TC-FR008-02` (Workflow: Quarantine Pending) | **Verified (PASSED)** |
| **NFR-001** | Sub-200ms Polling Latency under 1,000 Concurrent Users | NFR (Perf) / **High** | `UC-04`, `UC-09` | In-Memory Redis Cache; Connection Pool | `WP-4.1` | `NFR-101`, `SC-209` | 3 | `TC-NFR001-01` (Load: JMeter 1,000 Users P95)<br>`TC-NFR001-02` (Latency: Redis In-Memory Get) | **Verified (PASSED)** |
| **NFR-002** | 99.9% Uptime & AES-256 Encryption at Rest | NFR (Sec) / **High** | System-Wide | TLS 1.3 Reverse Proxy; KMS Encrypted DB | `WP-4.2` | `NFR-102`, `SC-210` | 3 | `TC-NFR002-01` (Security: TLS 1.3 Cipher Scan)<br>`TC-NFR002-02` (Reliability: Container Health Probe) | **Verified (PASSED)** |
| **NFR-003** | WCAG 2.1 AA Accessibility & Responsive UI | NFR (Usability) / **Medium** | `UC-01` to `UC-04` | Responsive Client Layout; ARIA Mask Tags | `WP-4.3` | `NFR-103` | 2 | `TC-NFR003-01` (Audit: Axe Accessibility Scan)<br>`TC-NFR003-02` (Cross-Device: Mobile/Desktop) | **Verified (PASSED)** |
| **NFR-004** | ACID Compliance & Duplicate Vote Prevention | NFR (Integrity) / **High** | `UC-04` | PostgreSQL Relational Layer; Unique Constraint | `WP-4.4` | `BTBSC-4`, `NFR-104` | 3 | `TC-NFR004-01` (Integration: DB Unique Index)<br>`TC-NFR004-02` (Chaos: Atomic Commit Rollback) | **Verified (PASSED)** |
| **NFR-005** | Modular API Design & Maintainability | NFR (Design) / **Medium** | System-Wide | FastAPI / Flask Modular Blueprints; OpenAPI 3.0 | `WP-4.5` | `NFR-105` | 2 | `TC-NFR005-01` (Linter: Flake8 & MyPy Typing)<br>`TC-NFR005-02` (Coverage: PyTest &gt; 85%) | **Verified (PASSED)** |
| **NFR-006** | Audit Trail for Moderation & Auth Events | NFR (Audit) / **Low** | `UC-03`, `UC-08` | OpenTelemetry Logger; PostgreSQL Audit Table | `WP-4.6` | `NFR-106` | 2 | `TC-NFR006-01` (Integration: Immutable Audit Log)<br>`TC-NFR006-02` (Verification: Lead Deletion Stamp) | **Verified (PASSED)** |

---

## 3. Jira Defect Resolution Traceability (Lab 2 $\to$ Lab 3)

| Jira Bug Key | Summary of Defect | Root Cause Analysis | Code / Architecture Fix | Test Verification |
| :--- | :--- | :--- | :--- | :--- |
| **BTBSC-1** | Spoiler content visible in search preview | Search indexing and snippet generation rendered raw markdown without parsing `[spoiler]` tags. | Added `sanitize_search_snippet()` pipeline in `SpoilerFilterEngine` to substitute spoiler blocks with `[Spoiler Content Hidden]`. | `TC-FR001-02` validates that search results never contain spoiler text. |
| **BTBSC-2** | Negative page count accepted in reading progress | Reading form input lacked server-side bounds validation. | Implemented boundary check in `ReadingProgressTracker.log_pages()` requiring $0 < \text{pages} \le \text{remaining\_pages}$. | `TC-FR002-01` verifies `ValueError` raised on negative integers. |
| **BTBSC-3** | Regular member can access discussion moderation controls | API endpoint `/api/threads/{id}/moderate` checked only token presence, not user role claims. | Added RBAC decorator `@require_role('DISCUSSION_LEAD')` and enforced authorization checks. | `TC-FR003-01` confirms `403 Forbidden` response for non-lead users. |
| **BTBSC-4** | Duplicate vote accepted after session refresh | Vote tally was incremented in memory before database commit; client token not tied to poll ID. | Created composite primary key `(user_id, poll_id)` on `ballots` table with atomic transactional upsert. | `TC-FR004-02` confirms second vote attempt returns `409 Conflict`. |

---

## 4. Verification Summary Statistics

- **Total Requirements:** 14 (8 Functional Requirements + 6 Non-Functional Requirements)
- **Total Test Cases Mapped:** 28 discrete unit, integration, performance, and security test cases
- **Requirements Coverage:** **100%**
- **Sprint Story Points Committed (Scrum Backlog):** 29 Story Points across core features (Sprint 1 velocity: 20 pts completed, Sprint 2 remainder: 9 pts)
- **Defects Remediated & Verified:** 4 out of 4 (100% bug fix resolution)
