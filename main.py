import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt
import numpy as np
import time
import sys


# Function to measure execution time of the user's function
def measure_execution_time(function, input_sizes):
    execution_times = []
    for size in input_sizes:
        start_time = time.time()
        function(size)  # Call the user-defined function
        end_time = time.time()
        execution_times.append(end_time - start_time)
    return execution_times


# Function to estimate time complexity
def estimate_complexity(input_sizes, execution_times):
    complexities = {
        "O(1)": lambda n: [1 for _ in n],
        "O(log n)": lambda n: [np.log2(x) if x > 0 else 0 for x in n],
        "O(n)": lambda n: n,
        "O(n log n)": lambda n: [x * np.log2(x) if x > 0 else 0 for x in n],
        "O(n^2)": lambda n: [x ** 2 for x in n],
        "O(n^3)": lambda n: [x ** 3 for x in n],
    }

    best_fit = None
    best_r2 = -float("inf")

    for name, func in complexities.items():
        try:
            theoretical = func(input_sizes)
            if np.std(theoretical) == 0 or np.std(execution_times) == 0:
                continue

            correlation = np.corrcoef(theoretical, execution_times)[0, 1] ** 2
            if correlation > best_r2:
                best_r2 = correlation
                best_fit = name
        except Exception:
            continue

    return best_fit, best_r2


# Function to analyze time complexity
def analyze_code():
    # Get the code from the input box
    code = code_input.get("1.0", tk.END).strip()

    if not code:
        messagebox.showerror("Error", "Please enter some code!")
        return

    try:
        # Dynamically define the user's function
        exec(code, globals())

        if "user_function" not in globals():
            messagebox.showerror(
                "Error", "Your code must define a function named 'user_function(n)'!"
            )
            return

        # Input sizes to test
        input_sizes = [100, 1000, 1000, 2000, 5000]

        # Measure execution times
        execution_times = measure_execution_time(user_function, input_sizes)

        # Estimate complexity
        best_fit, best_r2 = estimate_complexity(input_sizes, execution_times)

        # Display results in a message box
        messagebox.showinfo(
            "Result",
            f"Best Fit Complexity: {best_fit}\nR² Value: {best_r2}\nExecution Times: {execution_times}",
        )

        # Plot the results
        plt.plot(input_sizes, execution_times, label="Execution Times", marker="o")
        plt.title("Time Complexity Analysis")
        plt.xlabel("Input Size")
        plt.ylabel("Time Taken (seconds)")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


# Set up the GUI
root = tk.Tk()
root.title("Time Complexity Checker")
root.geometry("800x600")

# Add a label
label = tk.Label(
    root,
    text="Paste your code below (Your function must be named 'user_function'):",
    font=("Arial", 14),
)
label.pack(pady=10)

# Add a scrollable text box for code input
code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 12), height=15)
code_input.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Add a button to analyze the code
analyze_button = tk.Button(root, text="Analyze Time Complexity", font=("Arial", 14), command=analyze_code)
analyze_button.pack(pady=20)

# Run the GUI
root.mainloop()
