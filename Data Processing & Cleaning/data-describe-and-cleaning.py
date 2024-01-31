# Import the necessary libraries
import pandas as pd

# Read the dataset into a Pandas DataFrame
data = pd.read_csv('"C:\Users\Admin\Documents\Data Intelligence Engineer project\Task Files\Data Intelligence Engineer - test assignment dataset - Mealco.csv"')  # Replace 'your_dataset.csv' with the actual file path

# Check the first few rows of the dataset to understand its structure
print(data.head())

# Check for missing values and data types
print(data.info())

# Convert the "Order Timestamp" column to datetime data type
data['Order Timestamp'] = pd.to_datetime(data['Order Timestamp'])

# Check the data after converting the timestamp
print(data.head())
