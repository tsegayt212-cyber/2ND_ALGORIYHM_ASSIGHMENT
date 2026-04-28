# Graph Coloring for University Exam Scheduling

A Python implementation of the Graph Coloring problem using Backtracking algorithm to solve university exam scheduling conflicts.

## Problem Context

Universities must schedule final exams so that no student has two exams at the same time. If two courses share students, they cannot be assigned the same time slot.

This is modeled as a graph where:
- **Vertices** = Courses
- **Edges** = Course conflicts (shared students)
- **Colors** = Exam time slots

## Features

- 50×50 Adjacency Matrix representation
- Backtracking algorithm for graph coloring
- Automatic chromatic number detection (minimum time slots needed)
- Manual time slot specification option
- Conflict verification report
- Execution time measurement
- Random graph generation with realistic conflict patterns

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Usage

### Interactive Mode

```bash
python exam_scheduler.py
```

Follow the prompts to:
1. Enter number of courses (default: 50)
2. Choose automatic chromatic number detection or manual time slot entry

### Non-Interactive Test

```bash
python test_scheduler.py
```

Runs with default settings (50 courses, automatic mode).

## Program Structure

### Core Functions

- `create_graph()` - Generates adjacency matrix with realistic conflicts
- `is_safe()` - Checks if color assignment is valid
- `solve_coloring()` - Main backtracking solver
- `solve_coloring_util()` - Recursive backtracking utility
- `find_chromatic_number()` - Finds minimum colors needed
- `display_matrix()` - Shows adjacency matrix
- `display_result()` - Displays final schedule
- `conflict_report()` - Verifies solution validity

## Algorithm Complexity

**Worst case:** O(m^n)
- m = number of colors (time slots)
- n = number of vertices (courses)

Backtracking significantly reduces exploration by pruning invalid branches early, avoiding the full exponential search in practical cases.

## Real-World Applications

1. **Exam Scheduling** - Avoiding student conflicts
2. **Register Allocation** - Compiler optimization
3. **Frequency Assignment** - Mobile network channels
4. **Map Coloring** - Geographic region coloring

## Sample Output

```
==================================================
EXAM SCHEDULE - TIME SLOT ASSIGNMENTS
==================================================

Time Slot 1:
  Course  2 → Slot 1
  Course  3 → Slot 1
  Course  6 → Slot 1
  ...

Time Slot 2:
  Course  1 → Slot 2
  Course  4 → Slot 2
  ...

==================================================
Total courses scheduled : 50
Time slots used         : 5
==================================================
```

## Implementation Details

- Uses 2D list for adjacency matrix (50×50)
- Conflict probability: 15% base + 10% bonus for nearby courses
- Generates realistic conflict patterns
- Validates solution with conflict checking
- Provides detailed complexity analysis

## Author

Created for Q6 - Graph Coloring (Exam Scheduling) Assignment
