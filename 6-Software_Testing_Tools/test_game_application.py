"""Automated Test Suite for Bookworm Word Quest Game Application.

Software Engineering Lab — Individual Project Assignment
Student: Sushruth S | SRN: PES1UG24CS486
Course: Software Engineering Lab 3 — Practicing on Software Testing Tools

Contains 4 automated unit test cases:
  1. test_case_1_guess_validation: Validates exact, present, and absent letter matching.
  2. test_case_2_base_score_calculation: Verifies remaining attempts and difficulty scoring.
  3. test_case_3_boundary_limit_handling: Verifies loss state when 6 attempts are exhausted.
  4. test_case_4_streak_bonus_multiplier: Verifies 1.5x streak bonus at streak count = 3.
"""

import unittest
from game_application import (
    PlayerState,
    validate_guess,
    calculate_base_score,
    calculate_streak_bonus,
    process_turn,
)


class TestBookwormGameApplication(unittest.TestCase):
    """Test suite consisting of exactly 4 individual test cases."""

    def test_case_1_guess_validation(self):
        """Test Case 1: Character matching feedback (CORRECT, PRESENT, ABSENT)."""
        target = "DUNE"
        guess = "DATE"
        feedback = validate_guess(guess, target)
        
        # 'D' matches position 0 -> CORRECT
        self.assertEqual(feedback[0], ('D', 'CORRECT'))
        # 'A' is not in DUNE -> ABSENT
        self.assertEqual(feedback[1], ('A', 'ABSENT'))
        # 'T' is not in DUNE -> ABSENT
        self.assertEqual(feedback[2], ('T', 'ABSENT'))
        # 'E' matches position 3 -> CORRECT
        self.assertEqual(feedback[3], ('E', 'CORRECT'))

    def test_case_2_base_score_calculation(self):
        """Test Case 2: Base score calculation formula."""
        # Solved on attempt 2 out of 6 -> remaining attempts = (6 - 2 + 1) = 5
        # 5 * 100 * 1.0 = 500 points
        score_normal = calculate_base_score(attempts_used=2, max_attempts=6, difficulty_multiplier=1.0)
        self.assertEqual(score_normal, 500)

        # Solved on attempt 1 out of 6 with 1.5x hard difficulty multiplier -> 6 * 100 * 1.5 = 900
        score_hard = calculate_base_score(attempts_used=1, max_attempts=6, difficulty_multiplier=1.5)
        self.assertEqual(score_hard, 900)

    def test_case_3_boundary_limit_handling(self):
        """Test Case 3: Boundary limit when max attempts (6) are exhausted."""
        state = PlayerState(player_name="Reader486", target_word="HOBBIT", max_attempts=6)

        # Submit 5 incorrect guesses
        for _ in range(5):
            turn = process_turn(state, "WIZARD")
            self.assertEqual(turn["status"], "IN_PROGRESS")
            self.assertFalse(state.is_game_over)

        # 6th incorrect guess -> Boundary hit, loss state triggered
        final_turn = process_turn(state, "WIZARD")
        self.assertEqual(final_turn["status"], "LOSS")
        self.assertTrue(state.is_game_over)
        self.assertFalse(state.is_solved)
        self.assertEqual(state.current_streak, 0)
        self.assertEqual(state.total_score, 0)

    def test_case_4_streak_bonus_multiplier(self):
        """Test Case 4: Streak bonus multiplier calculation for consecutive wins.

        Rule: Streak of 3 consecutive wins must award a 50% streak bonus (1.5x base score).
        In the unpatched baseline code, this test fails because streak >= 3 was implemented
        as streak > 3, returning 0 bonus points instead of 250 points for a base score of 500.
        """
        base_points = 500
        streak_count = 3

        bonus = calculate_streak_bonus(current_streak=streak_count, base_points=base_points)
        expected_bonus = 250  # 50% of 500 base points

        self.assertEqual(
            bonus,
            expected_bonus,
            f"Expected streak bonus of {expected_bonus} for streak={streak_count}, but got {bonus}."
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
