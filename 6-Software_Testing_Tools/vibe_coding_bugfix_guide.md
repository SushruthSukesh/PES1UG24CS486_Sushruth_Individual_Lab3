# Vibe Coding Bug Fix Guide & Retesting Report

**Course:** Software Engineering Lab — Individual Project Assignment  
**Student:** Sushruth S | **SRN:** PES1UG24CS486  
**Folder:** `6-Software_Testing_Tools`  
**Target Repository:** [`PES1UG24CS486_Sushruth_Individual_Lab3`](https://github.com/SushruthSukesh/PES1UG24CS486_Sushruth_Individual_Lab3)  

---

## 1. Overview of the Testing Process

The software testing practice deliverable demonstrates modern **"Vibe Coding"** methodology:
1. **Execute Initial Test Suite:** Run the 4 automated unit test cases on the baseline application code.
2. **Identify Failing Test:** Observe which test case fails and record the exact traceback and error assertion.
3. **Prompt the AI Assistant:** Feed the failing test case, error message, and source code snippet to the AI coding assistant.
4. **Inspect & Apply Minimal Patch:** Review the proposed fix to verify correctness, then apply the patch.
5. **Retest & Verify:** Re-run the full test suite to confirm all 4 tests pass with zero regressions.

---

## 2. Step 1: Initial Test Run (Before Fix)

Running `python test_game_application.py` against the unpatched codebase produced the following failure:

```text
test_case_1_guess_validation (test_game_application.TestBookwormGameApplication) ... ok
test_case_2_base_score_calculation (test_game_application.TestBookwormGameApplication) ... ok
test_case_3_boundary_limit_handling (test_game_application.TestBookwormGameApplication) ... ok
test_case_4_streak_bonus_multiplier (test_game_application.TestBookwormGameApplication) ... FAIL

======================================================================
FAIL: test_case_4_streak_bonus_multiplier (test_game_application.TestBookwormGameApplication)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_game_application.py", line 58, in test_case_4_streak_bonus_multiplier
    self.assertEqual(
AssertionError: 0 != 250 : Expected streak bonus of 250 for streak=3, but got 0.

----------------------------------------------------------------------
Ran 4 tests in 0.002s

FAILED (failures=1)
```

### Analysis of the Bug:
- **Failing Test:** `test_case_4_streak_bonus_multiplier`
- **Error:** `AssertionError: 0 != 250`
- **Root Cause:** In `calculate_streak_bonus()`, the condition for the 50% bonus was coded as:
  ```python
  elif current_streak > 3:
      return (base_points * 50) // 100
  ```
  Because it used strict inequality (`> 3`) rather than greater-than-or-equal-to (`>= 3`), any player with a streak of exactly 3 received **0 bonus points** instead of the required **50% bonus**.

---

## 3. Step 2: The "Vibe Coding" AI Prompt

The following prompt was submitted to the AI coding assistant:

> **Vibe Coding Prompt:**  
> *"I have a Python game function `calculate_streak_bonus(current_streak, base_points)` where `test_case_4_streak_bonus_multiplier` fails with:*  
> `AssertionError: 0 != 250 : Expected streak bonus of 250 for streak=3, but got 0.`  
> *Here is the code:*  
> ```python
> def calculate_streak_bonus(current_streak: int, base_points: int) -> int:
>     if current_streak >= 5:
>         return (base_points * 100) // 100
>     elif current_streak > 3:
>         return (base_points * 50) // 100
>     return 0
> ```  
> *Diagnose the off-by-one bug and generate a clean, minimal patch to fix the logic."*

---

## 4. Step 3: AI Diagnosis & Patch Generation

### AI Diagnosis:
> *"The bug is an off-by-one boundary condition on line 4. The requirement specifies that a streak of 3 or 4 earns a 50% bonus. The condition `current_streak > 3` evaluates to False when `current_streak == 3`. Changing the operator to `>= 3` ensures streaks of 3 receive the bonus."*

### Patch Applied (`game_patch.diff`):
```diff
--- game_application.py.orig
+++ game_application.py
@@ -66,5 +66,5 @@
     if current_streak >= 5:
         return int(base_points * 1.0)
-    elif current_streak > 3:
-        return (base_points * 50) // 100
+    elif current_streak >= 3:
+        return int(base_points * 0.5)
     return 0
```

---

## 5. Step 4: Retesting (After Fix)

Re-running the test suite with `python test_game_application.py` after applying the patch:

```text
test_case_1_guess_validation (test_game_application.TestBookwormGameApplication.test_case_1_guess_validation)
Test Case 1: Character matching feedback (CORRECT, PRESENT, ABSENT). ... ok
test_case_2_base_score_calculation (test_game_application.TestBookwormGameApplication.test_case_2_base_score_calculation)
Test Case 2: Base score calculation formula. ... ok
test_case_3_boundary_limit_handling (test_game_application.TestBookwormGameApplication.test_case_3_boundary_limit_handling)
Test Case 3: Boundary limit when max attempts (6) are exhausted. ... ok
test_case_4_streak_bonus_multiplier (test_game_application.TestBookwormGameApplication.test_case_4_streak_bonus_multiplier)
Test Case 4: Streak bonus multiplier calculation for consecutive wins. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

**Final Outcome:** 4 of 4 tests passing (100% green).
