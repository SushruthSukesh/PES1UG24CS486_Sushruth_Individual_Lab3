# Book Club Reading Challenge & Discussion Portal — Individual Project Assignment

**Course:** Software Engineering Lab (UE24CS252AA) — Individual Project Deliverables  
**Problem Statement #55:** Book Club Reading Challenge & Discussion Portal  
**Domain:** Media, Events & Community  

---

## 👨‍💻 Student Details

| Attribute | Details |
| :--- | :--- |
| **Student Name** | **Sushruth S** |
| **SRN** | **PES1UG24CS486** |
| **Section** | **4-H** |
| **Department / Institution** | Department of Computer Science & Engineering, PES University |
| **Individual Lab 3 Repository** | [PES1UG24CS486_Sushruth_Individual_Lab3](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3) |
| **Upstream Lab 1 & 2 Repository** | [Lab1_Activity_Sushruth_S_PES1UG24CS486](https://github.com/SushruthSukesh/Lab1_Activity_Sushruth_S_PES1UG24CS486) |
| **Jira Agile Workspaces** | `Kanban_BookClub`, `Scrum_BookClub`, `BugTracker_BookClub` |

---

## 📖 About the Project

The **Book Club Reading Challenge & Discussion Portal** is a collaborative reading engagement and social forum platform designed to motivate members, encourage spoiler-free discussions, and run fair monthly book elections:

- **Personal Reading Goal Tracking:** Readers log daily/monthly page numbers, track streaks, and unlock gamified digital achievement badges.
- **Spoiler-Protected Discussion Threads:** Chapter-by-chapter discussion boards where spoiler text is concealed behind interactive blur masks and pre-sanitized in search previews until explicitly revealed by the member.
- **Role-Based Moderation for Discussion Leads:** Discussion Leads hold privileged access to curate chapter threads, pin discussion prompts, and quarantine inappropriate comments.
- **Democratic Monthly Book Selection Polls:** Tamper-resistant polling system enforcing atomic ballot commits, eliminating duplicate votes across sessions/refreshes, and broadcasting live tallies with sub-200ms latency.

---

## 📂 Repository Structure

```text
PES1UG24CS486_Sushruth_Individual_Lab3/
├── README.md                                    # Master individual project documentation
├── .gitignore                                   # Clean repository ignore file
│
├── 1-RE/                                        # a) 1-Folder for Requirements Engineering
│   ├── FR_and_NFR.md                            # Complete FRs (FR-001..008) and NFRs (NFR-001..006)
│   ├── RTM_Table.md                             # Bidirectional Requirements Traceability Matrix
│   └── Requirements_Engineering_and_RTM.pdf     # Formatted printable master deliverable PDF
│
├── 2-Architectural_Diagram/                     # b) 2-Folder for Architectural Diagram
│   ├── Architecture_Diagram.png                 # High-resolution 4-tier layered architecture diagram
│   ├── Architecture_Diagram.drawio              # Diagrams.net / Draw.io editable XML source
│   ├── Architecture_Specification.md            # Component specification & architectural justification
│   └── Architecture_Specification.pdf           # Printable formatted specification document
│
├── 3-Project_Creational_Screenshots/            # c) 3-Folder for GitHub & Jira Screenshots
│   ├── README.md                                # Screenshot inventory and verification index
│   ├── github/                                  # Repository setup & semantic commit history evidence
│   │   ├── 01_GitHub_Repository_Creation.png
│   │   ├── 02_GitHub_Commit_History_and_Workflow.png
│   │   └── 03_GitHub_Lab1_Activity_Evidence.png
│   └── jira/                                    # 13 high-resolution Jira screenshots + 3 PDF reports
│       ├── 01_Kanban_Board_Creation.png
│       ├── 02_Kanban_Requirements_Addition.png
│       ├── 03_Kanban_Epic_Creation.png
│       ├── 04_Kanban_User_Stories_Mapping.png
│       ├── 05_Kanban_Task_Subtask_Breakdown.png
│       ├── 06_Kanban_Backlog_Hierarchy.png
│       ├── 07_Scrum_Project_Setup.jpeg
│       ├── 08_Scrum_Product_Backlog_Story_Points.png
│       ├── 09_Scrum_Active_Sprint_Board.png
│       ├── 10_Scrum_Completed_Sprint_Status.png
│       ├── 11_Scrum_Burndown_Chart.png
│       ├── 12_Bug_Tracker_Workspace_Backlog.png
│       ├── 13_Defect_Inspection_BTBSC-1.png
│       ├── Sushruth_Sukesh_PES1UG24CS486-BPS#55_Kanban.pdf
│       ├── Sushruth_Sukesh_PES1UG24CS486-BPS#55_Scrum.pdf
│       └── Sushruth_Sukesh_PES1UG24CS486-BPS#55_Bug_Tracking.pdf
│
├── 4-SRS_and_Work_Breakdown_Steps/              # d) 4-Folder for SRS and WBS
│   ├── SRS_Document.md                          # IEEE Std 830-1998 Software Requirements Specification
│   ├── Work_Breakdown_Structure.md              # 6-phase hierarchical WBS with 29 story points & Gantt chart
│   └── SRS_and_Work_Breakdown_Steps.pdf         # Formatted printable SRS and WBS document
│
├── 5-Github_Copilot_Generated_Code/             # e) 5-Folder for GitHub Copilot Generated Code
│   ├── book_club_core_engine.py                 # Core domain logic engine with built-in test suite
│   ├── copilot_prompt_evidence.md               # Prompt engineering journal, reasoning & test outputs
│   └── screenshots/                             # IDE evidence of Copilot code generation & tests
│       ├── 01_Copilot_Prompt_Architecture_Scaffolding.png
│       ├── 02_Copilot_Code_Generation_Core_Engine.png
│       └── 03_Copilot_Verification_Tests_Passed.png
│
└── 6-Software_Testing_Tools/                    # f) 6-Folder for Practicing on Software Testing Tools
    ├── README.md                                # Testing workflow, test results comparison & repo links
    ├── game_application.py                      # Interactive Bookworm Word Quest game code (patched)
    ├── test_game_application.py                 # Exactly 4 automated unit test cases
    ├── game_patch.diff                          # Minimal diff showing the off-by-one bug patch
    └── vibe_coding_bugfix_guide.md              # Step-by-step Vibe Coding AI prompting & retest log
```

---

## 📑 Deliverable Map & Summary Table

| Folder | Teacher Deliverable Item | Description & Key Artifacts |
| :--- | :--- | :--- |
| [**`1-RE`**](./1-RE) | **a) Requirements Engineering** | 8 Functional Requirements (FR-001..008), 6 Non-Functional Requirements (NFR-001..006), and the complete bidirectional Requirements Traceability Matrix (RTM) linking requirements to Use Cases, Architecture components, WBS work packages, test cases, and Jira defects (`BTBSC-1` to `4`). |
| [**`2-Architectural_Diagram`**](./2-Architectural_Diagram) | **b) Architectural Diagram** | 4-Tier Layered & Event-Driven Cloud Architecture (Presentation, Edge Gateway, Domain Microservices, Persistence/Redis Cache). Exported as high-res PNG, editable Draw.io XML, and detailed Architectural Specification. |
| [**`3-Project_Creational_Screenshots`**](./3-Project_Creational_Screenshots) | **c) GitHub & Jira Screenshots** | Evidence of repository creation on GitHub, commit workflows, and **13 high-resolution Jira screenshots** covering Kanban board, Scrum sprint simulation (29 story points), burndown chart, and Bug Tracker defect inspections. Includes the 3 official Lab 2 PDF reports. |
| [**`4-SRS_and_Work_Breakdown_Steps`**](./4-SRS_and_Work_Breakdown_Steps) | **d) SRS & Work Breakdown Steps** | Complete Software Requirements Specification following **IEEE Std 830-1998**, paired with a **6-Phase Work Breakdown Structure (WBS)** detailing 21 discrete work packages, Fibonacci story point allocations, Mermaid Gantt timeline, and risk matrix. |
| [**`5-Github_Copilot_Generated_Code`**](./5-Github_Copilot_Generated_Code) | **e) GitHub Copilot Generated Code** | Complete Python domain engine (`book_club_core_engine.py`) implementing reading goals, spoiler masking, moderation RBAC, and monthly poll deduplication. Accompanied by prompt journals, screenshots, and 100% passing self-test output. |
| [**`6-Software_Testing_Tools`**](./6-Software_Testing_Tools) | **f) Software Testing Tools Practice** | Literary game application (**Bookworm Word Quest**) and **4 automated unit test cases**. Demonstrates **vibe coding** to isolate an off-by-one streak calculation bug, apply a minimal unified patch (`game_patch.diff`), and retest to achieve 4/4 passing tests. |

---

## 🔍 Section Breakdown

### 1. Requirements Engineering (`1-RE`)
- **Functional Requirements (FR-001 to FR-008):** Defined with Priority, Preconditions, Inputs, Processing Rules, Outputs, and Acceptance Criteria.
- **Non-Functional Requirements (NFR-001 to NFR-006):** Metrics for Sub-200ms latency under 1,000 concurrent users, 99.9% uptime, AES-256 encryption, and WCAG 2.1 AA accessibility.
- **Bidirectional Traceability Matrix (RTM):** 100% requirement coverage mapped across UML Use Cases (`UC-01` to `UC-09`), Architecture components, WBS items, PyTest cases, and Jira issues (`BTBSC-1` to `BTBSC-4`).
- **Master PDF:** [`Requirements_Engineering_and_RTM.pdf`](./1-RE/Requirements_Engineering_and_RTM.pdf).

### 2. Architectural Diagram (`2-Architectural_Diagram`)
- **Architecture Pattern:** Multi-Tier Layered Architecture with Redis Pub/Sub Event-Driven Spine.
- **Layers:**
  1. *Presentation Layer:* Web, Mobile PWA, Moderation Console, Real-time Voting Tally Board.
  2. *API Gateway Layer:* TLS 1.3 Reverse Proxy, JWT RBAC Gatekeeper, WebSocket Push Gateway.
  3. *Domain Services Layer:* Spoiler Filter Service, Reading Progress Engine, Monthly Poll Engine, Moderation Service, Badge Award Engine.
  4. *Persistence Layer:* PostgreSQL with ACID transactions and unique compound constraints; Redis sub-millisecond tally cache; Cloud Object Storage.
- **Artifacts:** [`Architecture_Diagram.png`](./2-Architectural_Diagram/Architecture_Diagram.png), [`Architecture_Diagram.drawio`](./2-Architectural_Diagram/Architecture_Diagram.drawio), and [`Architecture_Specification.pdf`](./2-Architectural_Diagram/Architecture_Specification.pdf).

### 3. Project Creation Evidence (`3-Project_Creational_Screenshots`)
- **GitHub Setup:** Screenshots of repo creation, branch structure, and semantic commit history.
- **Jira Kanban Setup (`Kanban_BookClub`):** 4 Epics, 7 Discrete requirements, user stories, task/subtask breakdowns, and backlog hierarchy.
- **Jira Scrum Setup (`Scrum_BookClub`):** 29 Fibonacci Story Points backlog, Sprint 1 active board progression, completed sprint status, and official Jira Burndown Chart.
- **Jira Bug Tracking (`BugTracker_BookClub`):** Workspace logging defects `BTBSC-1` (Spoiler in search), `BTBSC-2` (Negative pages), `BTBSC-3` (Member moderation bypass), and `BTBSC-4` (Duplicate voting).

### 4. IEEE 830 SRS & Work Breakdown Structure (`4-SRS_and_Work_Breakdown_Steps`)
- **SRS Document:** Formatted to IEEE Std 830-1998 covering overall product perspective, user characteristics, external interfaces, and functional feature specs.
- **WBS Plan:** 6 Lifecycle phases with 21 detailed work packages, predecessor dependencies, story points, and Mermaid Gantt project schedule.
- **Master PDF:** [`SRS_and_Work_Breakdown_Steps.pdf`](./4-SRS_and_Work_Breakdown_Steps/SRS_and_Work_Breakdown_Steps.pdf).

### 5. GitHub Copilot Generated Code (`5-Github_Copilot_Generated_Code`)
- **Implementation File:** [`book_club_core_engine.py`](./5-Github_Copilot_Generated_Code/book_club_core_engine.py)
- **Defects Remediated via Copilot:**
  - `BTBSC-1`: Added `sanitize_search_snippet()` to obscure `[spoiler]` text before search caching.
  - `BTBSC-2`: Added strict bounds guard ($0 < \text{pages} \le \text{remaining}$) in `log_pages()`.
  - `BTBSC-3`: Enforced `_require_moderator_privilege()` asserting `DISCUSSION_LEAD` role before pin/delete.
  - `BTBSC-4`: Enforced unique voter check in `cast_vote()`, raising `409 Conflict` on duplicate submissions.
- **Verification Execution:**
  ```bash
  python 5-Github_Copilot_Generated_Code/book_club_core_engine.py
  ```
  *Result: 5 of 5 self-test checks passed (100% green).*

### 6. Software Testing Tools Practice (`6-Software_Testing_Tools`)
- **Game Application:** **Bookworm Word Quest** (`game_application.py`)
- **What it does:** Interactive literary word puzzle where players guess hidden book titles within 6 attempts, earning points based on remaining attempts and multiplier bonuses for consecutive win streaks.
- **How to Test:**
  ```bash
  python 6-Software_Testing_Tools/test_game_application.py
  ```
- **How to Fix the Bug (Vibe Coding):**
  - **Failing Test:** `test_case_4_streak_bonus_multiplier` failed with `AssertionError: 0 != 250`.
  - **Prompted AI:** Fed failing test case and `calculate_streak_bonus()` code to AI coding assistant.
  - **Diagnosis:** Off-by-one condition `current_streak > 3` dropped the 1.5x bonus for streak of exactly 3.
  - **Patch:** Applied minimal patch changing operator to `>= 3` ([`game_patch.diff`](./6-Software_Testing_Tools/game_patch.diff)).
  - **Retest:** All 4 test cases passed with zero regressions.

#### Test Results Comparison Table:
| Test Case | Method Name | Before Patch | After Patch |
| :--- | :--- | :---: | :---: |
| **Test 1** | `test_case_1_guess_validation` | **PASS** | **PASS** |
| **Test 2** | `test_case_2_base_score_calculation` | **PASS** | **PASS** |
| **Test 3** | `test_case_3_boundary_limit_handling` | **PASS** | **PASS** |
| **Test 4** | `test_case_4_streak_bonus_multiplier` | <font color="#DC2626">**FAIL**</font> | <font color="#059669">**PASS**</font> |

- **Repository Link After Fixing:** [https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3)

---

## ✅ Submission Checklist

- [x] **Master README:** Comprehensive documentation covering all individual project assignment instructions.
- [x] **1-RE:** Functional Requirements, Non-Functional Requirements, RTM Table, and PDF.
- [x] **2-Architectural_Diagram:** High-resolution diagram (PNG), editable Draw.io XML, and specification document.
- [x] **3-Project_Creational_Screenshots:** 3 GitHub creation screenshots + 13 Jira board/defect screenshots + 3 PDF reports.
- [x] **4-SRS_and_Work_Breakdown_Steps:** IEEE 830 SRS document + 6-phase WBS with 29 story points & Gantt chart + PDF.
- [x] **5-Github_Copilot_Generated_Code:** Core domain engine (`book_club_core_engine.py`), prompts, and verified test suite.
- [x] **6-Software_Testing_Tools:** Game application code, 4 unit test cases, vibe coding bug fix, patch diff, and retest report.
- [x] **Git Repository:** Pushed and synchronized to [`PES1UG24CS486_Sushruth_Individual_Lab3`](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3).
