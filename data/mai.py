from time import time
import matplotlib.pyplot as plt

# Measure Execution Time
def measure_execution_time(func, *args):
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time

# Custom Function to Test
def my_test_function(n):
    total = 0
    for i in range(n):
        for j in range(n):  # Nested loop (O(n^2))
            total += i * j
    return total

# Main Program
if __name__ == "__main__":
    # Define Input Sizes
    input_sizes = [10, 100, 500, 1000, 2000]
    execution_times = []

    # Test Your Function (Replace or Add Functions to Test)
    for size in input_sizes:
        execution_times.append(measure_execution_time(my_test_function, size))

    # Plot the Results
    plt.plot(input_sizes, execution_times, marker='o', label="My Test Function (O(n^2))")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity Analysis")
    plt.legend()
    plt.grid(True)
    plt.show()
