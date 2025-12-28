# 📌 NumPy Basics – Beginner Notes

## 📖 What is NumPy?
**NumPy** is a powerful **Python library** used for working with **arrays** and numerical data.

It also provides functions for:
- 🔢 Linear Algebra  
- 📐 Fourier Transform  
- 🧮 Matrices and Mathematical Operations  

### 🧠 Key Facts
- Created in **2005** by **Travis Oliphant**
- Open-source and free to use
- NumPy stands for **Numerical Python**

---

## ❓ Why Use NumPy?
Python has built-in **lists** that can act like arrays, but they are:
- ❌ Slow for large datasets
- ❌ Not memory efficient

✅ **NumPy is faster, more efficient, and optimized** for numerical operations.

---

## ⚡ Why is NumPy Faster Than Python Lists?
NumPy arrays:
- Are stored in **continuous (contiguous) memory**
- Store **same type of elements**

### Benefits:
- 🚀 Faster execution
- ⚙️ Efficient memory usage
- 🔁 Supports vectorized operations (no loops)

📌 Python lists store elements at different memory locations, which slows down processing.

---

## 🧑‍💻 Which Language is NumPy Written In?
- NumPy is written **partially in Python**
- Performance-critical parts are written in:
  - **C**
  - **C++**

This provides:
- 🐍 Python simplicity
- ⚡ C-level speed

---

## 📦 Installation of NumPy
Install NumPy using `pip`:

```bash
pip install numpy

---

## 4️⃣ Difference Between Copy and View in NumPy

The main difference between a **copy** and a **view** of an array is:

- **Copy** → Creates a **new array**
- **View** → Creates a **reference (view) of the original array**

---

### 🔹 NumPy Copy
- Copy **owns its own data**
- Changes in the copy **do NOT affect** the original array
- Changes in the original array **do NOT affect** the copy

#### Example:
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()

copy_arr[0] = 99

print("Original Array:", arr)
print("Copied Array:", copy_arr)


## 🎲 What is Random Seed in NumPy?

In NumPy, a **random seed** is used to **control the randomness** of random number generation.

👉 Setting a seed ensures that **random numbers are reproducible** — meaning you get the **same output every time** you run the code.

---

## 🔹 Why Do We Need a Random Seed?
Random numbers are used in:
- Data science experiments
- Machine learning models
- Testing and debugging
- Simulations

Without a seed:
- Output changes every time

With a seed:
- Output remains **constant and predictable**

---

## 🔹 Setting a Random Seed in NumPy

Use:
```python
np.random.seed(value)


## 🔹 Dot Product in NumPy

The **dot product** is one of the most important operations in mathematics, data analysis, and machine learning.

It is used to:
- Combine two vectors
- Perform matrix multiplication
- Calculate similarity between vectors
- Build ML & Deep Learning models

---

## 📌 What is Dot Product?

### For Vectors
The dot product of two vectors is the **sum of the products of corresponding elements**.

### Formula:
\[
A \cdot B = a_1b_1 + a_2b_2 + \dots + a_nb_n
\]

---

## 🧮 Example 1: Dot Product of Two Vectors

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)
print(result)


## 🔢 Comparison Operators and Sorting in NumPy

NumPy provides powerful **comparison** and **sorting** operations that are widely used in:
- Data analysis
- Filtering datasets
- Machine learning preprocessing
- Statistical analysis

---

# 🔹 1. Comparison Operators in NumPy

### 📌 What are Comparison Operators?
Comparison operators are used to **compare array elements** and return **Boolean values (True / False)**.

NumPy performs **element-wise comparison**.

---

## ✅ Common Comparison Operators

| Operator | Meaning |
|-------|--------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

## 🧮 Example 1: Element-wise Comparison

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr > 25)


## 🖼️ Image to NumPy Array

In data science, machine learning, and computer vision, images are converted into
**NumPy arrays** so that we can perform:
- Mathematical operations
- Image processing
- Feature extraction
- Model training (CNNs, ML models)

---

## 📌 Why Convert Image to NumPy Array?

An image is essentially:
- A grid of pixels
- Each pixel has numerical values

👉 NumPy allows:
- Fast computation
- Easy slicing & reshaping
- Compatibility with ML libraries

📌 **Images = Numbers = NumPy Arrays**

---

## 🔹 Method 1: Using Pillow (PIL) – Most Common

### Step 1: Install Pillow
```bash
pip install pillow


