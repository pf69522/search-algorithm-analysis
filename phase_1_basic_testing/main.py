from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)


def run_test(test_name, values, target):
    values = sorted(values)
    print(f"\n{test_name}: list={values}, target={target}")

    results = [
        (
            "Recursive binary search",
            recursive_binary_search(values, target, 0, len(values) - 1),
        ),
        (
            "Iterative binary search",
            iterative_binary_search(values, target),
        ),
        ("Sequential search", sequential_search(values, target)),
    ]

    for algorithm_name, index in results:
        if index == -1:
            acceptable = target not in values
        else:
            acceptable = (
                0 <= index < len(values) and values[index] == target
            )

        status = "PASS" if acceptable else "FAIL"
        found = index != -1
        print(
            f"{algorithm_name}: found={found}, "
            f"index={index}, {status}"
        )
        assert acceptable, f"{algorithm_name} failed: {test_name}"


def main():
    values = [3, 5, 8, 12, 14, 18, 21]

    run_test("Middle target", values, 12)
    run_test("Absent target", values, 9)
    run_test("First element", values, 3)
    run_test("Last element", values, 21)
    run_test("One element, present", [7], 7)
    run_test("One element, absent", [7], 9)
    run_test("Empty list", [], 7)
    run_test("Duplicate values", [3, 5, 5, 5, 8], 5)

    print("\nAll 24 search checks passed.")


if __name__ == "__main__":
    main()
