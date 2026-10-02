"""Bookworm Word Quest — Interactive Literary Puzzle Game.

Software Engineering Lab — Individual Project Assignment
Student: Sushruth S | SRN: PES1UG24CS486 | Problem Statement #55
Deliverable: 6-Folder for Practicing on Software Testing Tools

Game Overview:
A word-guessing puzzle game where players solve mystery book titles or literary terms
within a maximum number of attempts, earning dynamic scores and streak multipliers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class PlayerState:
    player_name: str
    target_word: str
    max_attempts: int = 6
    attempts_used: int = 0
    current_streak: int = 0
    total_score: int = 0
    is_solved: bool = False
    is_game_over: bool = False


def validate_guess(guess: str, target: str) -> List[Tuple[str, str]]:
    """Evaluate guess against target word.

    Returns a list of tuples: (letter, status)
    where status is 'CORRECT' (right letter & spot),
    'PRESENT' (right letter, wrong spot), or 'ABSENT'.
    """
    guess = guess.strip().upper()
    target = target.strip().upper()

    if len(guess) != len(target):
        raise ValueError(f"Guess length ({len(guess)}) must match target word length ({len(target)}).")

    result: List[Tuple[str, str]] = []
    target_chars = list(target)

    # First pass: check for exact matches
    status_map = ["ABSENT"] * len(guess)
    for i, char in enumerate(guess):
        if char == target[i]:
            status_map[i] = "CORRECT"
            target_chars[i] = None  # Consume character

    # Second pass: check for present characters in wrong spot
    for i, char in enumerate(guess):
        if status_map[i] == "ABSENT" and char in target_chars:
            status_map[i] = "PRESENT"
            target_chars[target_chars.index(char)] = None

    for i, char in enumerate(guess):
        result.append((char, status_map[i]))

    return result


def calculate_base_score(attempts_used: int, max_attempts: int, difficulty_multiplier: float = 1.0) -> int:
    """Calculate base score for a solved round.

    Formula: ((max_attempts - attempts_used + 1) * 100) * difficulty_multiplier
    """
    if attempts_used > max_attempts:
        return 0
    remaining_attempts = (max_attempts - attempts_used) + 1
    raw_points = remaining_attempts * 100 * difficulty_multiplier
    return int(raw_points)


def calculate_streak_bonus(current_streak: int, base_points: int) -> int:
    """Calculate streak multiplier bonus.

    Rules:
      - Streak < 3: 0 bonus (1.0x)
      - Streak >= 3 and < 5: 50% bonus (1.5x)
      - Streak >= 5: 100% bonus (2.0x)

    VIBE CODING BUG FIX:
    Bug in baseline: Used integer division `(base_points * 50) // 100` with condition `current_streak > 3`
    instead of `current_streak >= 3`, which dropped the 1.5x multiplier for streaks of exactly 3.
    Fixed: Correctly uses `current_streak >= 3` and calculates bonus as `int(base_points * 0.5)`.
    """
    if current_streak >= 5:
        return int(base_points * 1.0)  # +100% bonus
    elif current_streak >= 3:
        return int(base_points * 0.5)  # +50% bonus
    return 0


def process_turn(state: PlayerState, guess: str, difficulty_multiplier: float = 1.0) -> Dict[str, object]:
    """Execute a single guessing turn, update game state, and return feedback."""
    if state.is_game_over:
        raise RuntimeError("Game is already over. Start a new round.")

    guess = guess.strip().upper()
    state.attempts_used += 1

    feedback = validate_guess(guess, state.target_word)

    if guess == state.target_word.upper():
        state.is_solved = True
        state.is_game_over = True
        state.current_streak += 1

        base = calculate_base_score(state.attempts_used, state.max_attempts, difficulty_multiplier)
        bonus = calculate_streak_bonus(state.current_streak, base)
        round_score = base + bonus
        state.total_score += round_score

        return {
            "status": "WIN",
            "attempts_used": state.attempts_used,
            "round_score": round_score,
            "base_score": base,
            "streak_bonus": bonus,
            "current_streak": state.current_streak,
            "feedback": feedback
        }

    if state.attempts_used >= state.max_attempts:
        state.is_solved = False
        state.is_game_over = True
        state.current_streak = 0  # Streak reset on loss

        return {
            "status": "LOSS",
            "attempts_used": state.attempts_used,
            "round_score": 0,
            "current_streak": 0,
            "feedback": feedback
        }

    return {
        "status": "IN_PROGRESS",
        "attempts_remaining": state.max_attempts - state.attempts_used,
        "feedback": feedback
    }
