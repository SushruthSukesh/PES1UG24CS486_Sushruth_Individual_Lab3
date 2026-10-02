# GitHub Copilot Code Generation & Engineering Evidence

**Problem Statement #55:** Book Club Reading Challenge & Discussion Portal  
**Student:** Sushruth S | **SRN:** PES1UG24CS486  
**Course:** Software Engineering Lab — Individual Project Assignment  
**Target Repository:** [`PES1UG24CS486_Sushruth_Individual_Lab3`](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3)  
**Implementation File:** [`book_club_core_engine.py`](./book_club_core_engine.py)  

---

## 1. Executive Summary

This deliverable captures the prompt engineering process, code synthesis, and architectural defect remediation achieved using **GitHub Copilot**. The synthesized component (`book_club_core_engine.py`) implements the four core domain modules and directly resolves the four Jira defects (`BTBSC-1` through `BTBSC-4`) logged during Lab 2.

---

## 2. GitHub Copilot Prompt Engineering Journal

### Prompt 1: System Scaffolding & Domain Entities
> **Copilot Prompt:**  
> *"Create clean Python 3.12 dataclasses and enums for a Book Club Reading Challenge portal (Problem Statement #55). Include UserRole (MEMBER, DISCUSSION_LEAD, ADMIN), User, Book, and Comment dataclasses with UTC timestamps and moderation status."*

**Copilot Output Summary:**
Generated `UserRole`, `User`, `Book`, and `Comment` dataclasses with default factory lambdas for timestamps and typed attributes.

---

### Prompt 2: FR-001 & Defect BTBSC-1 Fix (Spoiler Filter & Search Preview Sanitization)
> **Copilot Prompt:**  
> *"Implement `SpoilerFilterEngine` with regex-based masking for `[spoiler]...[/spoiler]` tags. Fix Jira Defect BTBSC-1 where spoiler text leaks in search previews by providing a `sanitize_search_snippet(text, max_length)` function that strips spoiler tags and substitutes `[Spoiler Content Hidden]`."*

**Copilot Output Summary:**
- Implemented compiled regex `SPOILER_PATTERN = re.compile(r"\[spoiler\](.*?)\[/spoiler\]", re.IGNORECASE | re.DOTALL)`.
- `render_comment()`: Conditionally masks content with `[BLURRED SPOILER: Click to reveal]` unless user has marked chapter read.
- `sanitize_search_snippet()`: Pre-sanitizes strings before truncation, preventing any confidential spoiler text leakage in search result previews.

---

### Prompt 3: FR-002 & Defect BTBSC-2 Fix (Reading Progress Bounds Validation)
> **Copilot Prompt:**  
> *"Implement `ReadingProgressTracker` for daily/monthly page tracking. Fix Jira Defect BTBSC-2 where negative page inputs were accepted. Ensure `log_pages(pages, session_date)` raises `ValueError` if `pages <= 0` or if `pages > remaining_pages`. Increment streak days and dynamically calculate completion percentage."*

**Copilot Output Summary:**
- Validated integer type and strictly asserted $0 < \text{pages} \le \text{remaining\_pages}$.
- Added automatic milestone badge triggering for 100 pages, 500 pages, and completed books (FR-005).

---

### Prompt 4: FR-003 & Defect BTBSC-3 Fix (Discussion Moderation RBAC)
> **Copilot Prompt:**  
> *"Implement `DiscussionThreadModerator` with strict Role-Based Access Control. Fix Jira Defect BTBSC-3 where regular club members could trigger moderation actions. Methods `pin_prompt` and `delete_comment` must verify that `user.role` is `DISCUSSION_LEAD` or `ADMIN`, raising `PermissionError` with `403 Forbidden` if a regular member attempts them."*

**Copilot Output Summary:**
- Guard helper `_require_moderator_privilege(user, action)` strictly prevents privilege escalation.
- Maintained an immutable audit log array recording actor, timestamp, and moderation reason.

---

### Prompt 5: FR-004 & Defect BTBSC-4 Fix (Democratic Monthly Poll Duplicate Vote Prevention)
> **Copilot Prompt:**  
> *"Implement `MonthlyPollVotingEngine` for democratic monthly book selection. Fix Jira Defect BTBSC-4 where refreshing the session allowed duplicate votes. Store ballots in a dictionary mapping `user_id -> candidate` and verify `user_id not in self.ballots` before recording, raising `ValueError` with `409 Conflict` on duplicate attempts. Emulate real-time tally retrieval for Redis."*

**Copilot Output Summary:**
- Enforced atomic check-and-insert on ballots dictionary.
- Maintained real-time tally hash matching Redis in-memory speed (sub-millisecond computation).

---

## 3. How to Run the Generated Code

Execute the self-contained verification suite directly from your terminal:

```bash
python 5-Github_Copilot_Generated_Code/book_club_core_engine.py
```

### Expected Output:
```text
======================================================================
Running Book Club Reading Portal Core Verification Suite
======================================================================

[TEST 1] FR-001: Testing Spoiler Filter & Search Sanitization...
  -> PASSED: Spoiler masked and search preview properly sanitized (BTBSC-1 FIXED).

[TEST 2] FR-002: Testing Reading Progress Tracker & Bounds Validation...
  -> PASSED: Negative page count rejected with ValueError (BTBSC-2 FIXED).
  -> PASSED: Overflow page count rejected gracefully.

[TEST 3] FR-005: Testing Milestone Badge Engine...
  -> PASSED: Badges successfully awarded: {'CENTURION_READER_100_PAGES', 'CHALLENGE_BOOK_COMPLETED'}

[TEST 4] FR-003: Testing Discussion Moderation & RBAC Enforcement...
  -> PASSED: Regular member blocked from moderation controls (BTBSC-3 FIXED).
  -> PASSED: Discussion Lead successfully executed moderation actions.

[TEST 5] FR-004: Testing Democratic Monthly Poll & Duplicate Vote Guard...
  -> PASSED: Duplicate vote rejected with 409 Conflict (BTBSC-4 FIXED).
  -> PASSED: Poll standings accurately computed in real-time.

======================================================================
ALL CORE UNIT & INTEGRATION CHECKS PASSED SUCCESSFULLY (100% GREEN)
======================================================================
```
