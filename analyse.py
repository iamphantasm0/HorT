import collections

def analyze_file(file_path):
    # Dictionaries to store counts
    num_count = collections.defaultdict(int)
    heads_count = 0
    tails_count = 0

    # Variables to track consecutive streaks
    previous_outcome = None
    current_streak = 0
    streaks = collections.defaultdict(list)  # Stores streaks for heads and tails

    # Read the file and analyze data
    with open(file_path, 'r') as f:
        for line in f:
            try:
                # Parse the number and outcome from each line
                parts = line.split()

                # Check if the line is in the correct format (contains at least 3 parts)
                if len(parts) < 3:
                    continue

                # Attempt to convert the first part to an integer
                num = int(parts[0])
                outcome = parts[2]

                # Count the number occurrences
                num_count[num] += 1

                # Count heads or tails
                if outcome == "heads":
                    heads_count += 1
                elif outcome == "tails":
                    tails_count += 1

                # Handle streak counting
                if outcome == previous_outcome:
                    # If the outcome is the same as the previous, increment the streak
                    current_streak += 1
                else:
                    # If the outcome changes, store the previous streak and reset
                    if previous_outcome is not None:
                        streaks[previous_outcome].append(current_streak)
                    current_streak = 1  # Reset streak for the new outcome
                    previous_outcome = outcome

            except ValueError:
                # Skip lines that don't have a valid integer or expected format
                print(f"Skipping invalid line: {line.strip()}")

    # At the end, don't forget to store the last streak
    if previous_outcome is not None:
        streaks[previous_outcome].append(current_streak)

    return num_count, heads_count, tails_count, streaks


def print_analysis(num_count, heads_count, tails_count, streaks):
    # Total number of flips
    total_flips = heads_count + tails_count

    print(f"Total flips: {total_flips}")
    print(f"Heads count: {heads_count}")
    print(f"Tails count: {tails_count}")
    print("\nNumber occurrence frequency:")

    for num, count in sorted(num_count.items()):
        print(f"{num}: {count} times")

    # Print streak information
    print("\nConsecutive streaks:")
    print("Heads streaks:", streaks['heads'])
    print("Tails streaks:", streaks['tails'])

    # Calculate the longest streak
    if streaks['heads']:
        print(f"Longest heads streak: {max(streaks['heads'])}")
    if streaks['tails']:
        print(f"Longest tails streak: {max(streaks['tails'])}")


if __name__ == "__main__":
    file_path = 'output.txt'  # Replace with the actual path if needed
    num_count, heads_count, tails_count, streaks = analyze_file(file_path)
    print_analysis(num_count, heads_count, tails_count, streaks)
