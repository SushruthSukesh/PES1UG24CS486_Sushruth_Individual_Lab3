"""Book Club Reading Challenge & Discussion Portal — Core Domain Logic Engine.

Course: Software Engineering Lab — Individual Project Assignment
Problem Statement #55: Book Club Reading Challenge & Discussion Portal
Domain: Media, Events & Community
Student: Sushruth S | SRN: PES1UG24CS486 | Section: 4-H
Institution: PES University, Department of Computer Science & Engineering

Generated with GitHub Copilot assistance.
Implements:
  - FR-001: Spoiler Content Masking & Search Sanitization (Fixes Jira Defect BTBSC-1)
  - FR-002: Reading Progress & Challenge Goal Tracking (Fixes Jira Defect BTBSC-2)
  - FR-003: Chapter Discussion Moderation & RBAC (Fixes Jira Defect BTBSC-3)
  - FR-004: Democratic Monthly Poll Voting with Duplicate Guard (Fixes Jira Defect BTBSC-4)
  - FR-005: Gamified Milestone Badge Award Engine
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List, Optional, Set


# ============================================================================
# 1. Enums & Domain Data Structures
# ============================================================================

class UserRole(str, Enum):
    """User privilege roles for Role-Based Access Control (RBAC)."""
    MEMBER = "CLUB_MEMBER"
    DISCUSSION_LEAD = "DISCUSSION_LEAD"
    ADMIN = "SYSTEM_ADMIN"


@dataclass
class User:
    user_id: str
    username: str
    role: UserRole
    badges: Set[str] = field(default_factory=set)


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    total_pages: int


@dataclass
class Comment:
    comment_id: str
    thread_id: str
    author_id: str
    author_role: UserRole
    raw_content: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    is_pinned: bool = False
    is_deleted: bool = False


# ============================================================================
# 2. FR-001: Spoiler Filter & Masking Engine (Fixes Defect BTBSC-1)
# ============================================================================

class SpoilerFilterEngine:
    """Handles masking of [spoiler] tagged comments and sanitizes search previews.

    Defect Remediated: BTBSC-1
    Root Cause: Raw text in search previews exposed spoiler content without filter.
    Fix: sanitize_search_snippet replaces [spoiler] blocks with [Spoiler Content Hidden].
    """

    SPOILER_PATTERN = re.compile(r"\[spoiler\](.*?)\[/spoiler\]", re.IGNORECASE | re.DOTALL)

    @classmethod
    def has_spoiler(cls, text: str) -> bool:
        """Return True if content contains spoiler tags."""
        return bool(cls.SPOILER_PATTERN.search(text))

    @classmethod
    def render_comment(cls, text: str, user_has_read_chapter: bool, explicitly_revealed: bool = False) -> str:
        """Render comment masking spoiler text unless unmasked or chapter read."""
        if user_has_read_chapter or explicitly_revealed:
            return cls.SPOILER_PATTERN.sub(r"\1", text)
        return cls.SPOILER_PATTERN.sub(r"[BLURRED SPOILER: Click to reveal]", text)

    @classmethod
    def sanitize_search_snippet(cls, text: str, max_length: int = 120) -> str:
        """Sanitize text for search preview snippets, preventing spoiler leaks (BTBSC-1 fix)."""
        sanitized = cls.SPOILER_PATTERN.sub("[Spoiler Content Hidden]", text)
        if len(sanitized) > max_length:
            return sanitized[:max_length].rstrip() + "..."
        return sanitized


# ============================================================================
# 3. FR-002 & FR-005: Reading Progress & Badge Engine (Fixes Defect BTBSC-2)
# ============================================================================

class ReadingProgressTracker:
    """Tracks personal daily and monthly page goals with bounds validation.

    Defect Remediated: BTBSC-2
    Root Cause: Server lacked input bounds checking, accepting negative page counts.
    Fix: Validates 0 < pages_to_add <= remaining_pages; raises ValueError on violation.
    """

    def __init__(self, user: User, book: Book) -> None:
        self.user = user
        self.book = book
        self.pages_read: int = 0
        self.streak_days: int = 0
        self.last_log_date: Optional[str] = None

    @property
    def remaining_pages(self) -> int:
        return self.book.total_pages - self.pages_read

    @property
    def completion_percentage(self) -> float:
        if self.book.total_pages == 0:
            return 0.0
        return round((self.pages_read / self.book.total_pages) * 100, 2)

    @property
    def is_completed(self) -> bool:
        return self.pages_read >= self.book.total_pages

    def log_pages(self, pages: int, session_date: str) -> float:
        """Log pages read with strict input validation (BTBSC-2 fix)."""
        if not isinstance(pages, int):
            raise TypeError("Page count must be an integer.")
        if pages <= 0:
            raise ValueError(f"Invalid page count: {pages}. Pages logged must be greater than zero.")
        if pages > self.remaining_pages:
            raise ValueError(
                f"Page count ({pages}) exceeds remaining pages ({self.remaining_pages}) in '{self.book.title}'."
            )

        self.pages_read += pages
        self._update_streak(session_date)
        self._evaluate_milestone_badges()
        return self.completion_percentage

    def _update_streak(self, session_date: str) -> None:
        if self.last_log_date != session_date:
            self.streak_days += 1
            self.last_log_date = session_date

    def _evaluate_milestone_badges(self) -> None:
        """Award gamified achievement badges upon reaching milestones (FR-005)."""
        if self.pages_read >= 100:
            self.user.badges.add("CENTURION_READER_100_PAGES")
        if self.pages_read >= 500:
            self.user.badges.add("MASTER_READER_500_PAGES")
        if self.is_completed:
            self.user.badges.add("CHALLENGE_BOOK_COMPLETED")
        if self.streak_days >= 7:
            self.user.badges.add("SEVEN_DAY_READING_STREAK")


# ============================================================================
# 4. FR-003: Chapter Discussion Moderation & RBAC (Fixes Defect BTBSC-3)
# ============================================================================

class DiscussionThreadModerator:
    """Enforces Role-Based Access Control for chapter thread curation and moderation.

    Defect Remediated: BTBSC-3
    Root Cause: API checked authentication but not user role claims, allowing regular members to moderate.
    Fix: Enforces role check (DISCUSSION_LEAD or ADMIN); raises PermissionError on violation.
    """

    def __init__(self, thread_id: str, chapter_title: str) -> None:
        self.thread_id = thread_id
        self.chapter_title = chapter_title
        self.comments: Dict[str, Comment] = {}
        self.is_locked: bool = False
        self.audit_log: List[str] = []

    def post_comment(self, user: User, content: str, comment_id: str) -> Comment:
        """Any authenticated member may post a comment."""
        if self.is_locked:
            raise PermissionError("Thread is locked for new comments.")
        comment = Comment(
            comment_id=comment_id,
            thread_id=self.thread_id,
            author_id=user.user_id,
            author_role=user.role,
            raw_content=content
        )
        self.comments[comment_id] = comment
        return comment

    def pin_prompt(self, user: User, comment_id: str) -> None:
        """Discussion Leads may pin a discussion prompt (BTBSC-3 fix)."""
        self._require_moderator_privilege(user, action="pin_prompt")
        if comment_id not in self.comments:
            raise KeyError(f"Comment {comment_id} not found.")
        self.comments[comment_id].is_pinned = True
        self.audit_log.append(f"Prompt {comment_id} pinned by {user.username} at {datetime.now(timezone.utc)}")

    def delete_comment(self, user: User, comment_id: str, reason: str) -> None:
        """Discussion Leads may delete inappropriate or flagged comments (BTBSC-3 fix)."""
        self._require_moderator_privilege(user, action="delete_comment")
        if comment_id not in self.comments:
            raise KeyError(f"Comment {comment_id} not found.")
        self.comments[comment_id].is_deleted = True
        self.comments[comment_id].raw_content = "[This comment was removed by a Discussion Lead]"
        self.audit_log.append(f"Comment {comment_id} deleted by {user.username}. Reason: {reason}")

    def _require_moderator_privilege(self, user: User, action: str) -> None:
        if user.role not in (UserRole.DISCUSSION_LEAD, UserRole.ADMIN):
            raise PermissionError(
                f"403 Forbidden: User '{user.username}' with role '{user.role.value}' "
                f"lacks permission to perform moderation action '{action}'."
            )


# ============================================================================
# 5. FR-004 & NFR-001: Democratic Monthly Poll Engine (Fixes Defect BTBSC-4)
# ============================================================================

class MonthlyPollVotingEngine:
    """Manages monthly book selection voting with strict duplicate-vote prevention.

    Defect Remediated: BTBSC-4
    Root Cause: Tally was incremented before committing unique voter constraint.
    Fix: Enforces atomic ballot recording with composite key (user_id, poll_id).
    """

    def __init__(self, poll_id: str, month_label: str, candidates: List[str]) -> None:
        self.poll_id = poll_id
        self.month_label = month_label
        self.candidates: List[str] = candidates
        self.ballots: Dict[str, str] = {}  # user_id -> candidate
        self.tallies: Dict[str, int] = {c: 0 for c in candidates}
        self.is_closed: bool = False

    def cast_vote(self, user: User, candidate: str) -> Dict[str, int]:
        """Cast exactly one vote per user per poll cycle (BTBSC-4 fix)."""
        if self.is_closed:
            raise RuntimeError("Voting window has closed for this monthly poll cycle.")
        if candidate not in self.tallies:
            raise ValueError(f"Unknown candidate '{candidate}'. Valid options: {self.candidates}")

        # Strict atomic check: Prevent duplicate vote from same user
        if user.user_id in self.ballots:
            existing_candidate = self.ballots[user.user_id]
            raise ValueError(
                f"409 Conflict: User '{user.username}' (ID: {user.user_id}) has already voted "
                f"for '{existing_candidate}' in poll '{self.poll_id}'."
            )

        # Record ballot atomically and increment tally
        self.ballots[user.user_id] = candidate
        self.tallies[candidate] += 1
        return self.get_standings()

    def get_standings(self) -> Dict[str, int]:
        """Return current real-time vote standings (sub-200ms Redis emulation)."""
        return dict(self.tallies)

    def get_winner(self) -> str:
        """Return winning book candidate with highest vote tally."""
        return max(self.tallies, key=self.tallies.get)


# ============================================================================
# 6. Verification Self-Test Suite
# ============================================================================

def run_self_tests() -> None:
    """Execute complete automated test suite validating all 4 bug remediations."""
    print("=" * 70)
    print("Running Book Club Reading Portal Core Verification Suite")
    print("=" * 70)

    # 1. Test FR-001 & BTBSC-1 (Spoiler filter & search preview sanitization)
    print("\n[TEST 1] FR-001: Testing Spoiler Filter & Search Sanitization...")
    comment_text = "I love the twist where [spoiler]Dumbledore dies on page 596[/spoiler]!"
    assert SpoilerFilterEngine.has_spoiler(comment_text) is True
    masked = SpoilerFilterEngine.render_comment(comment_text, user_has_read_chapter=False)
    assert "[BLURRED SPOILER: Click to reveal]" in masked
    assert "Dumbledore" not in masked

    unmasked = SpoilerFilterEngine.render_comment(comment_text, user_has_read_chapter=True)
    assert "Dumbledore dies" in unmasked

    # Verify BTBSC-1 Fix (Search preview sanitization)
    snippet = SpoilerFilterEngine.sanitize_search_snippet(comment_text)
    assert "[Spoiler Content Hidden]" in snippet
    assert "Dumbledore" not in snippet
    print("  -> PASSED: Spoiler masked and search preview properly sanitized (BTBSC-1 FIXED).")

    # 2. Test FR-002 & BTBSC-2 (Reading progress bounds check)
    print("\n[TEST 2] FR-002: Testing Reading Progress Tracker & Bounds Validation...")
    user = User("u-486", "Sushruth", UserRole.MEMBER)
    book = Book("b-101", "Dune", "Frank Herbert", total_pages=400)
    tracker = ReadingProgressTracker(user, book)

    # Valid progress
    pct = tracker.log_pages(50, "2026-10-02")
    assert pct == 12.5
    assert tracker.pages_read == 50

    # Verify BTBSC-2 Fix (Negative page rejection)
    try:
        tracker.log_pages(-25, "2026-10-02")
        assert False, "Should have raised ValueError for negative page count"
    except ValueError as e:
        assert "Invalid page count: -25" in str(e)
        print("  -> PASSED: Negative page count rejected with ValueError (BTBSC-2 FIXED).")

    # Verify bounds check against remaining pages
    try:
        tracker.log_pages(500, "2026-10-02")
        assert False, "Should have rejected page count exceeding book total"
    except ValueError as e:
        assert "exceeds remaining pages" in str(e)
        print("  -> PASSED: Overflow page count rejected gracefully.")

    # 3. Test FR-005 (Milestone Badges)
    print("\n[TEST 3] FR-005: Testing Milestone Badge Engine...")
    tracker.log_pages(50, "2026-10-03")  # Total 100 pages
    assert "CENTURION_READER_100_PAGES" in user.badges
    tracker.log_pages(300, "2026-10-04")  # Total 400 pages (completed book)
    assert "CHALLENGE_BOOK_COMPLETED" in user.badges
    print(f"  -> PASSED: Badges successfully awarded: {user.badges}")

    # 4. Test FR-003 & BTBSC-3 (Discussion Moderation RBAC)
    print("\n[TEST 4] FR-003: Testing Discussion Moderation & RBAC Enforcement...")
    member = User("u-486", "Sushruth", UserRole.MEMBER)
    lead = User("u-001", "Professor_Admin", UserRole.DISCUSSION_LEAD)
    thread = DiscussionThreadModerator("th-ch1", "Chapter 1: The Gathering")

    c1 = thread.post_comment(member, "Great opening chapter!", "c-1")

    # Verify BTBSC-3 Fix (Regular member cannot pin/delete)
    try:
        thread.pin_prompt(member, "c-1")
        assert False, "Regular member should not be able to pin prompt"
    except PermissionError as e:
        assert "403 Forbidden" in str(e)
        print("  -> PASSED: Regular member blocked from moderation controls (BTBSC-3 FIXED).")

    # Lead can pin and delete
    thread.pin_prompt(lead, "c-1")
    assert thread.comments["c-1"].is_pinned is True
    thread.delete_comment(lead, "c-1", reason="Violates spoiler policy")
    assert thread.comments["c-1"].is_deleted is True
    print("  -> PASSED: Discussion Lead successfully executed moderation actions.")

    # 5. Test FR-004 & BTBSC-4 (Monthly Poll Duplicate Vote Guard)
    print("\n[TEST 5] FR-004: Testing Democratic Monthly Poll & Duplicate Vote Guard...")
    poll = MonthlyPollVotingEngine("poll-oct-2026", "October 2026 Selection", ["Project Hail Mary", "Neuromancer", "Klara and the Sun"])
    voter1 = User("u-101", "Alice", UserRole.MEMBER)
    voter2 = User("u-102", "Bob", UserRole.MEMBER)

    poll.cast_vote(voter1, "Project Hail Mary")
    poll.cast_vote(voter2, "Neuromancer")
    standings = poll.get_standings()
    assert standings["Project Hail Mary"] == 1
    assert standings["Neuromancer"] == 1

    # Verify BTBSC-4 Fix (Duplicate vote rejected after refresh)
    try:
        poll.cast_vote(voter1, "Neuromancer")
        assert False, "Duplicate vote should be rejected"
    except ValueError as e:
        assert "409 Conflict" in str(e)
        print("  -> PASSED: Duplicate vote rejected with 409 Conflict (BTBSC-4 FIXED).")

    assert poll.get_winner() in ["Project Hail Mary", "Neuromancer"]
    print("  -> PASSED: Poll standings accurately computed in real-time.")

    print("\n" + "=" * 70)
    print("ALL CORE UNIT & INTEGRATION CHECKS PASSED SUCCESSFULLY (100% GREEN)")
    print("=" * 70)


if __name__ == "__main__":
    run_self_tests()
