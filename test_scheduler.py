"""
Non-interactive test for exam_scheduler.py
Runs with default 50 courses in automatic mode.
"""

import random
import time
from exam_scheduler import (
    create_graph,
    greedy_coloring,
    find_chromatic_number,
    display_matrix,
    display_result,
    conflict_report,
)


def run_test():
    print("=" * 60)
    print("  UNIVERSITY EXAM SCHEDULER — Graph Coloring (Backtracking)")
    print("=" * 60)

    num_courses = 50
    print(f"\nGenerating conflict graph for {num_courses} courses...")
    random.seed(42)
    graph = create_graph(num_courses, conflict_probability=0.15)

    total_conflicts = sum(graph[i][j] for i in range(num_courses) for j in range(i + 1, num_courses))
    print(f"Total courses (vertices) : {num_courses}")
    print(f"Total conflicts (edges)  : {total_conflicts}")

    display_matrix(graph)

    print("\nSearching for minimum time slots...")
    start_time = time.time()

    num_colors, colors_assigned = find_chromatic_number(graph)
    elapsed = time.time() - start_time

    print(f"Result: {num_colors} time slots needed")

    display_result(colors_assigned, num_colors)

    print("\nConflict Verification Report:")
    conflict_report(graph, colors_assigned)

    print(f"\nExecution time: {elapsed:.4f} seconds")

    print(f"""
{'='*60}
COMPLEXITY ANALYSIS
{'='*60}
Worst case time complexity : O(m^n)
  m = number of colors (time slots) = {num_colors}
  n = number of vertices (courses)  = {num_courses}

Backtracking prunes branches where a conflict is detected
early, avoiding the full O(m^n) search in most cases.

REAL-WORLD APPLICATIONS OF GRAPH COLORING:
  - Exam Scheduling       (this program)
  - Register Allocation   (compilers assign CPU registers)
  - Frequency Assignment  (mobile network channels)
  - Map Coloring          (adjacent regions, different colors)
{'='*60}
""")


if __name__ == "__main__":
    run_test()
