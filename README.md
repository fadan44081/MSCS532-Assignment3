
# MSCS532 Assignment 3 – Algorithm Efficiency and Scalability

## 📌 Overview

This assignment explores two key concepts in algorithm design and data structures:

1. **Randomized Quicksort vs Deterministic Quicksort**
2. **Hash Tables using Chaining**

The objective is to analyze algorithm efficiency, scalability, and robustness through both **theoretical analysis** and **empirical experiments**.

---

# ⚙️ Requirements

To run this project, you need:

- Python 3.x installed on your system
- A terminal (Command Prompt, PowerShell, or VS Code terminal)

To verify Python installation:

```bash
python --version

Part 1 – Quicksort Analysis
File:
assignment3_part1.py
What it does:
Implements:
Randomized Quicksort
Deterministic Quicksort (first-element pivot)
Generates different types of input arrays:
Random
Sorted
Reverse sorted
Repeated elements
Measures execution time for both algorithms
Prints a comparison table
Run the program:
python assignment3_part1.py
Example Output:
Size   Distribution     Randomized QS (s)   Deterministic QS (s)
----------------------------------------------------------------
100    Random           0.0004              0.00008
100    Sorted           0.00015             0.00037
...
What to observe:
Compare execution times
Notice how performance changes with input type
Identify worst-case behavior of deterministic quicksort
🔹 Part 2 – Hash Table with Chaining
File:
assignment3_part2.py
What it does:
Implements a hash table supporting:
Insert
Search
Delete
Uses chaining (lists) to handle collisions
Tracks load factor
Dynamically resizes when the table becomes too full
Run the program:
python assignment3_part2.py
Example Output:
Inserting values...
Search apple: 10
Search banana: 20
Deleting banana...
Search banana after delete: None
Current load factor: 0.3
What to observe:
Correct insertion and retrieval
Successful deletion
Load factor calculation


📊 Summary of Findings

🔹 Part 1 – Quicksort Analysis

Theoretical Findings:
Randomized Quicksort:
Expected time complexity: O(n log n)
Avoids worst-case behavior through random pivot selection
Deterministic Quicksort:
Average case: O(n log n)
Worst case: O(n²)
Experimental Findings:
On random arrays:
Both algorithms perform similarly
On sorted and reverse-sorted arrays:
Deterministic Quicksort becomes significantly slower
Randomized Quicksort remains efficient
On repeated elements:
Both algorithms slow down slightly due to partition inefficiency

Key Insight:
Randomization significantly improves algorithm robustness and prevents consistent worst-case performance.

🔹 Part 2 – Hash Table with Chaining

Key Concepts:
Hash function maps keys to indices
Collisions handled using chaining (linked lists / arrays)
Load factor:
𝛼=𝑛/𝑚
Where:
n = number of elements
m = table size
Time Complexity:
Insert: O(1) average, O(n) worst-case
Search: O(1) average, O(n) worst-case
Delete: O(1) average, O(n) worst-case

Observations:

Performance depends on load factor
Higher load factor → more collisions → slower operations
Resizing improves efficiency by reducing collisions
Key Insight:

Chaining provides a simple and effective way to handle collisions while maintaining good average-case performance.

Author
Fathiya Adan
