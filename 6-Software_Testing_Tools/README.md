# Software Testing Tools Practice: Vibe Coding Bug Fix & Retest

**Student Name:** Sushruth S | **SRN:** PES1UG24CS486  
**Course:** Software Engineering Lab — Individual Project Assignment  
**Problem Statement #55:** Book Club Reading Challenge & Discussion Portal  
**Target Repository:** [`https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3`](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3)  

---

## 1. Directory Structure

```text
6-Software_Testing_Tools/
├── README.md                          # Testing process documentation, test results table & links
├── game_application.py                # Complete game application source code (patched)
├── test_game_application.py           # Exactly 4 automated unit test cases
├── game_patch.diff                    # Unified diff showing the bug fix patch
└── vibe_coding_bugfix_guide.md        # Step-by-step Vibe Coding AI prompting & retest log
```

---

## 2. What the Game Application Does

**Bookworm Word Quest** is a literary word-guessing puzzle game where players deduce hidden book titles or terminology within 6 attempts. Each guess evaluates letter accuracy (exact match, present, or absent), computes dynamic base scores based on remaining attempts and difficulty, and awards consecutive win streak bonuses (50% bonus at 3+ wins, 100% bonus at 5+ wins).

---

## 3. How to Test

Follow these steps to execute the test suite in your local environment:

1. **Navigate to the repository folder:**
   ```bash
   cd 6-Software_Testing_Tools
   ```
2. **Execute the automated test suite (runs all 4 test cases):**
   ```bash
   python test_game_application.py
   ```
3. **Run tests with verbose test case descriptions:**
   ```bash
   python -m unittest -v test_game_application.py
   ```

---

## 4. How to Fix the Bug (The Vibe Coding Process)

1. **Locate the Failing Test:** Run `python test_game_application.py` and inspect the stack trace. `test_case_4_streak_bonus_multiplier` fails with `AssertionError: 0 != 250`.
2. **Prompt the AI Assistant:** Provide the failing test assertion, expected vs. actual values, and the `calculate_streak_bonus` function snippet to your AI coding assistant (GitHub Copilot / Gemini / Claude).
3. **Analyze the Root Cause:** The AI identifies that line 68 uses `current_streak > 3` instead of `current_streak >= 3`, inadvertently dropping the 1.5x bonus for players with a streak of exactly 3.
4. **Apply the Minimal Patch:** Update the operator to `>= 3` and calculate `int(base_points * 0.5)` (as captured in [`game_patch.diff`](./game_patch.diff)).
5. **Retest & Verify:** Re-run `python test_game_application.py` to confirm that all 4 test cases pass (100% green).

---

## 5. Test Results Comparison Table

| Test Case | Description / Verification Target | Before Fix | After Fix |
| :--- | :--- | :---: | :---: |
| **Test Case 1** | `test_case_1_guess_validation`: Character matching feedback (`CORRECT`, `PRESENT`, `ABSENT`) | **PASS** | **PASS** |
| **Test Case 2** | `test_case_2_base_score_calculation`: Base score formula based on remaining attempts | **PASS** | **PASS** |
| **Test Case 3** | `test_case_3_boundary_limit_handling`: Boundary condition when 6 attempts are exhausted | **PASS** | **PASS** |
| **Test Case 4** | `test_case_4_streak_bonus_multiplier`: 50% bonus multiplier at 3 consecutive wins | <font color="#DC2626">**FAIL**</font> | <font color="#059669">**PASS**</font> |

- **Bug Found:** Off-by-one threshold condition (`current_streak > 3` instead of `>= 3`) caused streak bonuses for 3 consecutive wins to evaluate to 0 instead of 250 points.
- **Fix Applied:** Changed comparison operator to `current_streak >= 3` and verified integer precision bonus calculation.
- **Repository Link After Fixing:** [`https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3`](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3)
