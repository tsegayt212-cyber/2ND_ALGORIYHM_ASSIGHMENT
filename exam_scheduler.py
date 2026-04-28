"""
Graph Coloring for University Exam Scheduling
Uses Backtracking algorithm with Adjacency Matrix representation

Real-world applications:
- Exam Scheduling (avoiding conflicts)
- Register Allocation in compilers
- Frequency Assignment in mobile networks
- Map Coloring problems

Time Complexity: O(m^n) worst case, where m = colors, n = vertices
Backtracking prunes invalid branches to reduce exploration
"""

import random
import time


# ---------------------------------------------------------------------------
# Graph Generation
# ---------------------------------------------------------------------------

def create_graph(num_courses=50, conflict_probability=0.15):
    """
    Creates an adjacency matrix representing course conflicts.
    1 = conflict between two courses, 0 = no conflict.
    """
    graph = [[0] * num_courses for _ in range(num_courses)]

    for i in range(num_courses):
        for j in range(i + 1, num_courses):
            # Nearby courses are more likely to share students
            prob = conflict_probability + (0.1 if abs(i - j) <= 5 else 0)
            if random.random() < prob:
                graph[i][j] = 1
                graph[j][i] = 1  # Undirected graph

    return graph


# ---------------------------------------------------------------------------
# Backtracking Solver
# ---------------------------------------------------------------------------

def is_safe(graph, course, color, colors_assigned):
    """Returns True if assigning 'color' to 'course' causes no conflict."""
    for neighbor in range(len(graph)):
        if graph[course][neighbor] == 1 and colors_assigned[neighbor] == color:
            return False
    return True


def _backtrack(graph, num_colors, colors_assigned, course, deadline):
    """
    Recursive backtracking core.
    Returns True if a valid coloring is found before the deadline.
    """
    if course == len(graph):
        return True  # All courses successfully colored

    if time.time() > deadline:
        return False  # Time limit reached

    for color in range(1, num_colors + 1):
        if is_safe(graph, course, color, colors_assigned):
            colors_assigned[course] = color
            if _backtrack(graph, num_colors, colors_assigned, course + 1, deadline):
                return True
            colors_assigned[course] = 0  # Backtrack

    return False


def solve_coloring(graph, num_colors, time_limit=5.0):
    """
    Attempts to color the graph using at most num_colors colors.
    Returns a list of color assignments, or None if not possible within time_limit.
    """
    colors_assigned = [0] * len(graph)
    deadline = time.time() + time_limit

    if _backtrack(graph, num_colors, colors_assigned, 0, deadline):
        return colors_assigned
    return None


# ---------------------------------------------------------------------------
# Greedy Coloring (fast valid solution, used as upper bound)
# ---------------------------------------------------------------------------

def greedy_coloring(graph):
    """
    Greedy graph coloring — assigns each course the smallest color
    not used by any conflicting neighbor. Always produces a valid solution.

    Returns:
        Tuple of (num_colors_used, colors_assigned)
    """
    n = len(graph)
    colors = [0] * n

    for course in range(n):
        neighbor_colors = {colors[j] for j in range(n) if graph[course][j] == 1 and colors[j] != 0}
        color = 1
        while color in neighbor_colors:
            color += 1
        colors[course] = color

    return max(colors), colors


# ---------------------------------------------------------------------------
# Chromatic Number Finder
# ---------------------------------------------------------------------------

def find_chromatic_number(graph):
    """
    Finds the minimum number of colors (time slots) needed.

    Strategy:
      1. Greedy coloring gives a fast valid upper bound instantly.
      2. Backtracking tries to reduce by 1 (with a 5s time limit).

    Returns:
        Tuple of (num_colors, colors_assigned)
    """
    upper_bound, greedy_solution = greedy_coloring(graph)
    print(f"  Greedy solution: {upper_bound} slots. Trying to reduce by 1 with backtracking (5s limit)...")

    better = solve_coloring(graph, upper_bound - 1, time_limit=5.0)
    if better is not None:
        print(f"  Backtracking succeeded: reduced to {upper_bound - 1} slots.")
        return upper_bound - 1, better

    print(f"  Could not reduce further. Using {upper_bound} slots.")
    return upper_bound, greedy_solution


# ---------------------------------------------------------------------------
# Display Functions
# ---------------------------------------------------------------------------

def display_matrix(graph, max_display=15):
    """Prints the adjacency matrix, truncated for readability."""
    n = len(graph)
    d = min(n, max_display)

    print(f"\nAdjacency Matrix (showing first {d} of {n} courses):")
    print("      ", end="")
    for i in range(d):
        print(f"C{i+1:02d} ", end="")
    print("...")

    for i in range(d):
        print(f"C{i+1:02d} [  ", end="")
        for j in range(d):
            print(f"{graph[i][j]}   ", end="")
        print("...]")
    print("  ...")


def display_result(colors_assigned, num_colors):
    """Prints the final exam schedule grouped by time slot."""
    n = len(colors_assigned)

    print(f"\n{'='*50}")
    print("EXAM SCHEDULE — TIME SLOT ASSIGNMENTS")
    print(f"{'='*50}")

    slots = {}
    for idx, slot in enumerate(colors_assigned):
        slots.setdefault(slot, []).append(idx + 1)

    for slot in sorted(slots):
        print(f"\nTime Slot {slot}:")
        for course in slots[slot]:
            print(f"  Course {course:2d}  →  Slot {slot}")

    print(f"\n{'='*50}")
    print(f"Total courses scheduled : {n}")
    print(f"Time slots used         : {num_colors}")
    print(f"{'='*50}")


def conflict_report(graph, colors_assigned):
    """Verifies the solution and reports any conflicts."""
    n = len(graph)
    found = 0

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1 and colors_assigned[i] == colors_assigned[j]:
                print(f"  CONFLICT: Course {i+1} and Course {j+1} share Slot {colors_assigned[i]}")
                found += 1

    if found == 0:
        print("  No conflicts detected. Schedule is valid.")
    else:
        print(f"  {found} conflict(s) found.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  UNIVERSITY EXAM SCHEDULER — Graph Coloring (Backtracking)")
    print("=" * 60)

    # Number of courses
    try:
        num_courses = int(input("\nEnter number of courses (default 50): ").strip() or "50")
        if num_courses < 1:
            num_courses = 50
    except ValueError:
        num_courses = 50

    print(f"\nGenerating conflict graph for {num_courses} courses...")
    random.seed(42)
    graph = create_graph(num_courses, conflict_probability=0.15)

    total_conflicts = sum(graph[i][j] for i in range(num_courses) for j in range(i + 1, num_courses))
    print(f"Total courses (vertices) : {num_courses}")
    print(f"Total conflicts (edges)  : {total_conflicts}")

    display_matrix(graph)

    # Mode selection
    print("\nOptions:")
    print("  A - Find minimum time slots automatically (Chromatic Number)")
    print("  B - Enter number of time slots manually")
    choice = input("Choose option (A/B, default A): ").strip().upper() or "A"

    start_time = time.time()
    num_colors = None
    colors_assigned = None

    if choice == "B":
        try:
            num_colors = int(input("Enter number of time slots: ").strip())
            print(f"\nSolving with {num_colors} time slots (backtracking, 10s limit)...")
            colors_assigned = solve_coloring(graph, num_colors, time_limit=10.0)
        except ValueError:
            print("Invalid input. Defaulting to automatic mode.")
            choice = "A"

    if choice == "A":
        print("\nSearching for minimum time slots...")
        num_colors, colors_assigned = find_chromatic_number(graph)

    elapsed = time.time() - start_time

    if colors_assigned:
        display_result(colors_assigned, num_colors)
        print("\nConflict Verification Report:")
        conflict_report(graph, colors_assigned)
        print(f"\nExecution time: {elapsed:.4f} seconds")
    else:
        print(f"\nNo valid schedule found with {num_colors} time slot(s).")
        print("Try increasing the number of time slots.")

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
    main()
