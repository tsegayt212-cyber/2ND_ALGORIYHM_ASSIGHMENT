# Graph Coloring — University Exam Scheduling

> Q6 Algorithm Design Assignment — Backtracking Graph Coloring with Adjacency Matrix

---

## Project Overview

A Python project that solves the **Graph Coloring** problem for university exam scheduling using a **Backtracking** algorithm on a 50×50 adjacency matrix.

| Algorithm | Complexity | Approach |
|---|---|---|
| Greedy Coloring | O(n²) | Fast upper bound |
| Backtracking | O(m^n) worst case | Optimal reduction |

---

## Project Structure

```
2nd-algorithm-assignment/
├── exam_scheduler.py        # Main interactive program
├── test_scheduler.py        # Non-interactive test runner
├── generate_pdf_report.py   # Generates docs/Q6_Graph_Coloring_Report.pdf
├── report.html              # HTML report (auto-opens PDF dialog)
├── docs/
│   ├── Q6_Graph_Coloring_Report.pdf   # Full PDF report
│   └── screenshots/                   # Program output screenshots
└── README.md
```

---

## Problem Context

A university must schedule final exams so that no student sits two exams at the same time.

- **Vertices** = Courses (50 total)
- **Edges** = Conflicts (shared students between courses)
- **Colors** = Exam time slots (minimum = chromatic number)

---

## Algorithm

### Backtracking Graph Coloring

```python
def _backtrack(graph, num_colors, colors_assigned, course, deadline):
    if course == len(graph):
        return True                    # All courses colored

    for color in range(1, num_colors + 1):
        if is_safe(graph, course, color, colors_assigned):
            colors_assigned[course] = color
            if _backtrack(graph, num_colors, colors_assigned, course + 1, deadline):
                return True
            colors_assigned[course] = 0   # Backtrack

    return False
```

### Strategy
1. **Greedy Coloring** — instant valid solution as upper bound
2. **Backtracking** — tries to reduce by 1 color (5s time limit)
3. Returns the best result found

---

## Complexity

| | Value |
|---|---|
| Worst case | O(m^n) |
| m = colors | ~5 for 50 courses |
| n = courses | 50 |
| Backtracking | Prunes on first conflict |

---

## Usage

```bash
# Interactive mode
python exam_scheduler.py

# Non-interactive test
python test_scheduler.py

# Generate PDF report
python generate_pdf_report.py
```

---

## Sample Output

```
============================================================
  UNIVERSITY EXAM SCHEDULER — Graph Coloring (Backtracking)
============================================================

Total courses (vertices) : 50
Total conflicts (edges)  : 203

Greedy solution: 6 slots. Trying to reduce by 1 (5s limit)...
Backtracking succeeded: reduced to 5 slots.

Time Slot 1:  Course 2, 3, 8, 12 ...
Time Slot 2:  Course 1, 4, 9, 16 ...
...

No conflicts detected. Schedule is valid.
Execution time: 0.0312 seconds
```

---

## Real-World Applications

- 🎓 **Exam Scheduling** — this project
- ⚙️ **Register Allocation** — compiler optimization
- 📡 **Frequency Assignment** — mobile networks
- 🗺️ **Map Coloring** — geographic regions

---

## Requirements

- Python 3.x
- `reportlab` (for PDF generation only): `pip install reportlab`

---

## Academic Context

**Course:** Design and Analysis of Algorithms  
**Assignment:** Q6 — Graph Coloring (Exam Scheduling)  
**Language:** Python  
**Data Structure:** Adjacency Matrix (50×50)

---

## References

- Cormen, T. H. et al. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Knuth, D. E. (1998). *The Art of Computer Programming*, Vol. 3. Addison-Wesley.
