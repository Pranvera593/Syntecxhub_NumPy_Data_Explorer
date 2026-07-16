import numpy as np
import time


print("--- Part 1: Array Creation and Indexing/Slicing ---")

# 1. Create a NumPy array with 10 numbers
dataset = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original Dataset:", dataset)

# 2. Indexing: Get the first and last elements
first_element = dataset[0]
last_element = dataset[-1]
print("First Element:", first_element)
print("Last Element:", last_element)

# 3. Slicing: Get the first three elements
first_three = dataset[0:3]
print("First Three Elements:", first_three)

# 4. Slicing: Get all elements from index 5 to the end
from_fifth_to_end = dataset[5:]
print("Elements from Index 5 to End:", from_fifth_to_end)


print("\n--- Part 2: Statistical Operations ---")

# 1. Finding the Mean (Average)
mean_value = np.mean(dataset)
print("Mean Value:", mean_value)

# 2. Finding the Max and Min values
max_value = np.max(dataset)
min_value = np.min(dataset)
print("Max Value:", max_value)
print("Min Value:", min_value)

# 3. Sum of all elements
total_sum = np.sum(dataset)
print("Sum of Elements:", total_sum)

# 4. Multiplying all elements by 2 (Vectorized Operation)
doubled_dataset = dataset * 2
print("Doubled Dataset:", doubled_dataset)

print("\n--- Part 3: Advanced Concepts & 2D Arrays ---")

# 1. Creating a 2D Array (3x3 Matrix)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("2D Matrix:\n", matrix)

# Axis-wise operations (axis=0 for columns, axis=1 for rows)
print("Sum of each column (axis=0):", np.sum(matrix, axis=0))
print("Mean of each row (axis=1):", np.mean(matrix, axis=1))

# 2. Reshaping (Converting 1D array to a 2D array)
array_1d = np.array([10, 20, 30, 40, 50, 60])
array_2d = array_1d.reshape(2, 3)  # Converts into 2 rows and 3 columns
print("\nAfter Reshaping (1D -> 2D 2x3):\n", array_2d)

# 3. Broadcasting (Adding a 1D array to a 2D array)
add_vector = np.array([1, 2, 3])
broadcasting_result = array_2d + add_vector
print("After Broadcasting (adding [1, 2, 3] to each row):\n", broadcasting_result)

print("\n--- Part 4: Save & Load Operations ---")

# Saving the array to a file
np.save('saved_dataset.npy', dataset)
print("Array successfully saved to disk as 'saved_dataset.npy'!")

# Loading the array back from disk
loaded_dataset = np.load('saved_dataset.npy')
print("Array loaded back from disk:", loaded_dataset)

print("\n--- Part 5: Performance Comparison ---")

# Creating a large dataset with 1 million numbers
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Measuring Python list performance
start_time = time.time()
python_list_result = [x * 2 for x in python_list]
python_time = time.time() - start_time
print(f"Time taken by Python List: {python_time:.6f} seconds")

# Measuring NumPy array performance
start_time = time.time()
numpy_array_result = numpy_array * 2
numpy_time = time.time() - start_time
print(f"Time taken by NumPy Array: {numpy_time:.6f} seconds")

# Displaying the speed difference
speedup = python_time / numpy_time
print(f"NumPy is approximately {speedup:.1f}x faster than standard Python Lists!")