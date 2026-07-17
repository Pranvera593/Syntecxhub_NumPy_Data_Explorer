import pandas as pd
import numpy as np

# --- Part 1: Create a Messy Dataset ---
print("--- Part 1: Creating Messy Dataset ---")

# We create a dataset with missing values, wrong types, and duplicates
messy_data = {
    'Employee_ID': [101, 102, 103, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Charlie', np.nan, 'Eva'],
    'Join_Date': ['2023-01-15', '2023/02/20', '2023-03-10', '2023-03-10', '2023-05-01', '2023-06-12'],
    'Salary': ['1200', '950', np.nan, np.nan, '1100', '1500']
}

df = pd.DataFrame(messy_data)
print("Original Messy DataFrame:")
print(df)
print("-" * 50)

# --- Part 2: Detect & Handle Missing Values ---
print("\n--- Part 2: Handling Missing Values ---")

# Check how many null values we have per column
print("Missing values per column:")
print(df.isnull().sum())

# Fill missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

# Fill missing Salary with the median salary of the dataset
# First, we temporarily convert Salary to numeric to calculate the median safely
temp_salary = pd.to_numeric(df['Salary'], errors='coerce')
median_salary = temp_salary.median()
df['Salary'] = df['Salary'].fillna(median_salary)

print("\nDataFrame after filling missing values:")
print(df)
print("-" * 50)

# --- Part 3: Fix Incorrect DataTypes & Parse Dates ---
print("\n--- Part 3: Fixing DataTypes & Dates ---")

# Convert Salary column from object (string) to integer
df['Salary'] = df['Salary'].astype(int)

# Parse Join_Date column to correct datetime format
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

print("Data types after conversion:")
print(df.dtypes)
print("-" * 50)

# --- Part 4: Remove Duplicates ---
print("\n--- Part 4: Removing Duplicates ---")

# Find and drop exact duplicate rows (like Charlie at index 3)
df = df.drop_duplicates()

print("DataFrame after removing duplicates:")
print(df)
print("-" * 50)

# --- Part 5: Save Cleaned Dataset ---
print("\n--- Part 5: Saving Cleaned Data ---")

# Export the cleaned data to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)
print("Successfully saved cleaned data to 'cleaned_dataset.csv'!")