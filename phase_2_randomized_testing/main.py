import random

from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)


def run_trial(trial_number):
    values = sorted(random.randint(1, 100) for _ in range(20))

    if random.random() < 0.5:
        target = random.choice(values)
        expected_to_be_present = True
    else:
        target = 101
        expected_to_be_present = False

    print(f"\nTrial {trial_number}")
    print(f"Sorted list: {values}")
    print(f"Target: {target}")
    print(f"Expected present: {expected_to_be_present}")

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

    for name, index in results:
        if expected_to_be_present:
            acceptable = (
                0 <= index < len(values) and values[index] == target
            )
        else:
            acceptable = index == -1

        status = "PASS" if acceptable else "FAIL"
        print(f"{name}: index={index}, {status}")
        assert acceptable, f"{name} failed in trial {trial_number}"

    print("All results acceptable.")
    return expected_to_be_present


def main():
    present_trials = 0
    absent_trials = 0
    trial_number = 0

    # Run at least 10 trials and observe both search outcomes.
    while trial_number < 10 or present_trials == 0 or absent_trials == 0:
        trial_number += 1

        if run_trial(trial_number):
            present_trials += 1
        else:
            absent_trials += 1

    print(f"\nAll {trial_number} randomized trials passed.")
    print(f"Present-target trials: {present_trials}")
    print(f"Absent-target trials: {absent_trials}")


if __name__ == "__main__":
    main()
