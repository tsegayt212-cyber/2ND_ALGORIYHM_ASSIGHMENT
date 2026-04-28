# Graph Coloring — University Exam Scheduling

> Q6 Algorithm Design Assignment — Backtracking Graph Coloring with Adjacency Matrix

📄 **[View Full PDF Report](https://tsegayt212-cyber.github.io/2ND_ALGORIYHM_ASSIGHMENT/Q6_Graph_Coloring_Report.pdf)**

---

## Problem Context

A university must schedule final exams so that no student sits two exams at the same time.
If two courses share students, they conflict and cannot share the same time slot.

| Graph Element | Meaning |
|---|---|
| Vertices | Courses (50 total) |
| Edges | Conflicts (shared students) |
| Colors | Exam time slots |

---

## Project Structure

```
2ND_ALGORIYHM_ASSIGHMENT/
├── exam_scheduler.py        # Main interactive program
├── test_scheduler.py        # Non-interactive test runner
├── generate_pdf_report.py   # Generates the PDF report
├── report.html              # HTML report
├── docs/
│   ├── Q6_Graph_Coloring_Report.pdf
│   └── screenshots/
└── README.md
```

---

## Algorithm

Backtracking — tries each color per course, checks safety, recurses, backtracks on conflict.

```python
def _backtrack(graph, num_colors, colors_assigned, course, deadline):
    if course == len(graph):
        return True                        # All courses colored

    for color in range(1, num_colors + 1):
        if is_safe(graph, course, color, colors_assigned):
            colors_assigned[course] = color
            if _backtrack(graph, num_colors, colors_assigned, course + 1, deadline):
                return True
            colors_assigned[course] = 0    # Backtrack

    return False
```

**Strategy:**
1. Greedy Coloring — instant valid upper bound
2. Backtracking — tries to reduce by 1 color (5s limit)
3. Returns best result found

---

## Program Output

```
============================================================
  UNIVERSITY EXAM SCHEDULER — Graph Coloring (Backtracking)
============================================================

Generating conflict graph for 50 courses...
Total courses (vertices) : 50
Total conflicts (edges)  : 203

Adjacency Matrix (showing first 15 of 50 courses):
      C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 ...
C01 [  0   0   1   0   1   0   0   0   1   0   1   0   0   1   0   ...]
C02 [  0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   ...]
C03 [  1   0   0   0   0   0   1   0   0   0   0   0   1   0   0   ...]
C04 [  0   0   0   0   0   1   0   0   1   0   0   0   0   0   1   ...]
C05 [  1   1   0   0   0   0   0   1   0   0   0   0   1   0   0   ...]
C06 [  0   0   0   1   0   0   1   0   1   0   0   0   0   0   0   ...]
C07 [  0   0   1   0   0   1   0   0   0   1   0   0   0   0   0   ...]
C08 [  0   0   0   0   1   0   0   0   0   0   1   0   0   0   0   ...]
C09 [  1   0   0   1   0   1   0   0   0   0   0   0   0   1   0   ...]
C10 [  0   0   0   0   0   0   1   0   0   0   1   1   0   0   0   ...]
C11 [  1   0   0   0   0   0   0   1   0   1   0   0   0   0   0   ...]
C12 [  0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   ...]
C13 [  0   0   1   0   1   0   0   0   0   0   0   0   0   0   0   ...]
C14 [  1   0   0   0   0   0   0   0   1   0   0   0   0   0   0   ...]
C15 [  0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   ...]
  ...

Searching for minimum time slots...
  Greedy solution: 7 slots. Trying to reduce by 1 with backtracking (5s limit)...
  Backtracking succeeded: reduced to 6 slots.
Result: 6 time slots needed

==================================================
EXAM SCHEDULE — TIME SLOT ASSIGNMENTS
==================================================

Time Slot 1:
  Course  1  →  Slot 1
  Course  2  →  Slot 1
  Course  4  →  Slot 1
  Course  7  →  Slot 1
  Course  8  →  Slot 1
  Course 12  →  Slot 1
  Course 13  →  Slot 1
  Course 17  →  Slot 1
  Course 18  →  Slot 1
  Course 23  →  Slot 1
  Course 24  →  Slot 1
  Course 32  →  Slot 1
  Course 36  →  Slot 1
  Course 39  →  Slot 1

Time Slot 2:
  Course  3  →  Slot 2
  Course  5  →  Slot 2
  Course  6  →  Slot 2
  Course 10  →  Slot 2
  Course 14  →  Slot 2
  Course 15  →  Slot 2
  Course 16  →  Slot 2
  Course 26  →  Slot 2
  Course 27  →  Slot 2
  Course 34  →  Slot 2

Time Slot 3:
  Course  9  →  Slot 3
  Course 11  →  Slot 3
  Course 19  →  Slot 3
  Course 20  →  Slot 3
  Course 22  →  Slot 3
  Course 25  →  Slot 3
  Course 31  →  Slot 3
  Course 37  →  Slot 3
  Course 38  →  Slot 3
  Course 44  →  Slot 3
  Course 45  →  Slot 3
  Course 47  →  Slot 3
  Course 50  →  Slot 3

Time Slot 4:
  Course 21  →  Slot 4
  Course 28  →  Slot 4
  Course 29  →  Slot 4
  Course 30  →  Slot 4
  Course 35  →  Slot 4
  Course 41  →  Slot 4

Time Slot 5:
  Course 33  →  Slot 5
  Course 40  →  Slot 5
  Course 46  →  Slot 5
  Course 48  →  Slot 5

Time Slot 6:
  Course 42  →  Slot 6
  Course 43  →  Slot 6
  Course 49  →  Slot 6

==================================================
Total courses scheduled : 50
Time slots used         : 6
==================================================

Conflict Verification Report:
  No conflicts detected. Schedule is valid.

Execution time: 0.0029 seconds

============================================================
COMPLEXITY ANALYSIS
============================================================
Worst case time complexity : O(m^n)
  m = number of colors (time slots) = 6
  n = number of vertices (courses)  = 50

Backtracking prunes branches where a conflict is detected
early, avoiding the full O(m^n) search in most cases.

REAL-WORLD APPLICATIONS OF GRAPH COLORING:
  - Exam Scheduling       (this program)
  - Register Allocation   (compilers assign CPU registers)
  - Frequency Assignment  (mobile network channels)
  - Map Coloring          (adjacent regions, different colors)
============================================================
```

---

## Complexity

| | Value |
|---|---|
| Worst case | O(m^n) |
| m = time slots | 6 |
| n = courses | 50 |
| Actual runtime | 0.0029 seconds |

---

## Real-World Applications

- 🎓 **Exam Scheduling** — this project
- ⚙️ **Register Allocation** — compiler optimization
- 📡 **Frequency Assignment** — mobile networks
- 🗺️ **Map Coloring** — geographic regions

---

## Usage

```bash
python exam_scheduler.py       # interactive
python test_scheduler.py       # auto run
python generate_pdf_report.py  # generate PDF
```

---

## Academic Context

**Course:** Design and Analysis of Algorithms  
**Assignment:** Q6 — Graph Coloring (Exam Scheduling)  
**Institution:** Aksum University — Department of Computer Science  

## References

- Cormen, T. H. et al. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Knuth, D. E. (1998). *The Art of Computer Programming*, Vol. 3. Addison-Wesley.
