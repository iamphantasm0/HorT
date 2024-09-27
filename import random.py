import random
import time
import os


# Function to write output to a file
def rng():
    num = random.randint(0, 700)

    # Open the file in append mode to add the result at the end of the file
    with open('output.txt', 'a') as f:
        if num % 2 == 0:
            output = f"{num} is heads\n"
        else:
            output = f"{num} is tails\n"
        
        # Write the output to both the file and the console (optional)
        f.write(output)
        print(output, end="")  # Keep the console print, without adding an extra newline

# Print Working directory
# with open('output.txt', 'w') as f:
#     f.write(os.getcwd())

# Main loop
while True:
    rng()
    # time.sleep(1)  # Add delay if needed
