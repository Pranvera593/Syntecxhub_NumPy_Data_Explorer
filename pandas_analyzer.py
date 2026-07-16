import pandas as pd

# --- Part 1: Load and Inspect Data ---
print("--- Part 1: Loading and Inspecting Data ---")

# Define sample dataset as a dictionary
data = {
    'Name': ['Flaka', 'Arben', 'Pranvera', 'Ilir', 'Besa', 'Dardan'],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'Finance'],
    'Age': [23, 31, 21, 28, 24, 35],
    'Salary': [1200, 900, 1350, 950, 1100, 1500]
}

# Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Inspect the head of the DataFrame (first 3 rows)
print("\nFirst 3 rows (Head):")
print(df.head(3))

# Display column data types
print("\nData Types:")
print(df.dtypes)

print("-" * 45)

# --- Part 2: Compute Summary Statistics ---
print("\n--- Part 2: Summary Statistics ---")

# Calculate metrics for Salary and Age
print(f"Mean Salary: {df['Salary'].mean()}€")
print(f"Median Age: {df['Age'].median()}")
print(f"Min Salary: {df['Salary'].min()}€")
print(f"Max Salary: {df['Salary'].max()}€")
print(f"Total Employees: {df['Name'].count()}")

print("-" * 45)

# --- Part 3: Filtering and Slicing ---
print("\n--- Part 3: Filtering and Slicing ---")

# Filter: Select employees in 'IT' department with a Salary > 1150
filtered_df = df[(df['Department'] == 'IT') & (df['Salary'] > 1150)]

print("Filtered Employees (IT & Salary > 1150):")
print(filtered_df[['Name', 'Salary']])

print("-" * 45)

# --- Part 4: Saving Results ---
print("\n--- Part 4: Saving Results ---")

# Export the filtered subset to a CSV file
filtered_df.to_csv('filtered_employees.csv', index=False)
print("Successfully saved filtered results to 'filtered_employees.csv'!")