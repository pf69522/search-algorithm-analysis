
import csv
import platform
import random
import time
from pathlib import Path
from statistics import median

from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)


def verify_result(values, target, index):
    if index == -1:
        assert target not in values, "A present target was missed."
    else:
        assert 0 <= index < len(values), "Invalid index."
        assert values[index] == target, "Index points to wrong value."


def main():
    data_sizes = [5_000, 50_000, 100_000, 150_000, 1_000_000]
    number_of_trials = 10
    results = []

    print(f"Python: {platform.python_version()}")
    print(f"System: {platform.platform()}")
    print("Times are medians in microseconds.\n")

    for size in data_sizes:
        recursive_times = []
        iterative_times = []
        sequential_times = []
        present_trials = 0

        for trial in range(number_of_trials):
            # Generate and sort before starting any timer.
            values = sorted(
                random.randint(1, 1_000_000)
                for _ in range(size)
            )

            if random.random() < 0.5:
                target = random.choice(values)
                present_trials += 1
            else:
                target = 1_000_001

            low = 0
            high = len(values) - 1

            start = time.perf_counter()
            index = recursive_binary_search(values, target, low, high)
            elapsed = (time.perf_counter() - start) * 1_000_000
            recursive_times.append(elapsed)
            verify_result(values, target, index)

            start = time.perf_counter()
            index = iterative_binary_search(values, target)
            elapsed = (time.perf_counter() - start) * 1_000_000
            iterative_times.append(elapsed)
            verify_result(values, target, index)

            start = time.perf_counter()
            index = sequential_search(values, target)
            elapsed = (time.perf_counter() - start) * 1_000_000
            sequential_times.append(elapsed)
            verify_result(values, target, index)

            print(f"Size {size:,}: trial {trial + 1}/10 passed")

        assert all(
            len(times) == number_of_trials
            for times in (
                recursive_times,
                iterative_times,
                sequential_times,
            )
        )

        results.append([
            size,
            median(recursive_times),
            median(iterative_times),
            median(sequential_times),
        ])

        print(
            f"Present trials: {present_trials}; "
            f"absent trials: {number_of_trials - present_trials}\n"
        )

    print(
        f"{'Size':>12} {'Recursive':>14} "
        f"{'Iterative':>14} {'Sequential':>14}"
    )

    for size, recursive, iterative, sequential in results:
        print(
            f"{size:>12,} {recursive:>14.3f} "
            f"{iterative:>14.3f} {sequential:>14.3f}"
        )

    # Save only after all 50 trials pass verification.
    output_path = Path(__file__).resolve().parent / "results.csv"

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "data_size",
            "recursive_binary_us",
            "iterative_binary_us",
            "sequential_us",
        ])
        writer.writerows(results)

    print("\nAll 50 trials passed.")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()