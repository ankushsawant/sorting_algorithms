# Sorting Algorithms Performance Comparison

A Python-based performance benchmarking tool that implements and compares five fundamental sorting algorithms using parallel execution.

## Overview

This project demonstrates the implementation and real-world performance characteristics of classic sorting algorithms. All algorithms are executed concurrently on identical datasets, providing accurate performance comparisons.

## Features

- **Parallel Execution**: Utilizes Python's `concurrent.futures` for simultaneous algorithm execution
- **Performance Metrics**: Precise timing using `time.perf_counter()` for accurate benchmarking
- **Comprehensive Logging**: Detailed execution logs saved to `sorting.log`
- **Fair Comparison**: All algorithms process the same randomly generated dataset
- **Scalable Testing**: Configurable dataset size (default: 10,000 elements)

## Algorithms Implemented

| Algorithm | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|-----------|---------------------------|-------------------------|------------------|
| Bubble Sort | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n²) | O(log n) |

### Algorithm Descriptions

- **Bubble Sort**: Repeatedly compares adjacent elements and swaps them if in wrong order
- **Insertion Sort**: Builds sorted array incrementally by inserting elements into correct positions
- **Selection Sort**: Finds minimum element and places it at the beginning of unsorted portion
- **Merge Sort**: Divide-and-conquer algorithm that recursively splits and merges subarrays
- **Quick Sort**: Divide-and-conquer using pivot-based partitioning with random pivot selection

## Requirements

- Python 3.10+ (tested up to Python 3.14)
- Standard library modules: `random`, `concurrent.futures`, `logging`, `time`

### Python 3.14 Compatibility

This project is fully compatible with Python 3.14 and includes:
- Modern type hints using PEP 604 union syntax (`|` operator)
- Secure function mapping (no `eval()` usage)
- Standard library features compatible with latest Python versions

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd sorting_algorithms
```

No additional dependencies required.

## Usage

Run the performance comparison:

```bash
python sorting.py
```

The program will:
1. Generate a random list of 10,000 integers (range: 1-100)
2. Execute all five sorting algorithms in parallel
3. Log execution times as each algorithm completes
4. Save detailed results to `sorting.log`

### Running Tests

Execute the test suite:

```bash
python -m unittest test_sorting.py -v
```

## Output

Results are logged to `sorting.log` in the following format:

```
INFO:root:bubble_sort algorithm completed in 0.12345s.
INFO:root:insertion_sort algorithm completed in 0.23456s.
INFO:root:merge_sort algorithm completed in 0.01234s.
INFO:root:quick_sort algorithm completed in 0.00987s.
INFO:root:selection_sort algorithm completed in 0.15678s.
```

## Project Structure

```
sorting_algorithms/
├── sorting.py          # Main implementation and benchmarking
├── test_sorting.py     # Test suite
├── README.md           # Project documentation
└── sorting.log         # Execution logs (generated)
```

## License

This project is open source and available for educational purposes.