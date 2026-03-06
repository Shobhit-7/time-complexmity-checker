# ⏱️ Time Complexity Checker

A **Time Complexity Analyzer** that allows users to paste any **Python function** and estimate its **time complexity** based on execution time for multiple input sizes.

The tool dynamically runs the provided code, measures execution time, and generates a **visual graph** to show how the algorithm scales as the input size increases.

---

## 🚀 Features

- **Dynamic Code Execution**  
  Users can paste any Python function and the system dynamically executes it for different input sizes.

- **Time Complexity Estimation**  
  The system compares execution times with common theoretical complexities such as:
  - O(1)
  - O(log n)
  - O(n)
  - O(n log n)
  - O(n²)

- **Execution Time Visualization**  
  Generates a graph of **input size vs execution time** to visually represent algorithm performance.

- **Timeout Handling**  
  Prevents infinite loops or long-running programs by enforcing execution time limits.

- **Interactive GUI**  
  A simple and user-friendly **Tkinter GUI** allows users to easily paste code and analyze complexity.

---

## 🛠️ Technologies Used

- **Python** – Core programming language  
- **Tkinter** – GUI development  
- **Matplotlib** – Plotting execution time graphs  
- **NumPy** – Mathematical calculations  
- **Signal** – Timeout handling  
- **cProfile (Optional)** – Performance profiling  

---

## ⚙️ How It Works

### 1️⃣ Code Input

The user pastes a Python function inside the GUI text editor.

The function must follow this format:

```python
def user_function(n):
```

where **n represents the input size**.

---

### 2️⃣ Execution Time Measurement

The system runs the function with multiple input sizes such as:

```
n = 10
n = 100
n = 1000
n = 5000
```

and records the **execution time for each run**.

---

### 3️⃣ Time Complexity Estimation

The recorded times are compared with theoretical complexity models like:

- O(n)
- O(n log n)
- O(n²)

The system selects the **best matching complexity**.

---

### 4️⃣ Results Display

The application shows:

- Estimated **Time Complexity**
- Execution times for different input sizes
- A **graph of input size vs execution time**

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Shobhit-7/time-complexity-checker.git
```

Navigate to the project directory:

```bash
cd time-complexity-checker
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## 📄 Requirements

Your `requirements.txt` should contain:

```
matplotlib
numpy
```

> Note: Tkinter usually comes pre-installed with Python.

---

## ▶️ Usage

Run the application:

```bash
python time_complexity_checker.py
```

Steps:

1. Paste your Python function in the editor  
2. Click **Analyze Time Complexity**  
3. View:
   - Estimated Complexity
   - Execution Times
   - Performance Graph

---

## 💻 Example Code

Example function:

```python
def user_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

The tool will analyze how execution time grows with increasing **n**.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Submit a pull request  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Shobhit Shukla**

If you like this project, consider ⭐ starring the repository.
