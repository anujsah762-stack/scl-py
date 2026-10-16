
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("student_data.csv")

# Create a bar graph
plt.bar(df["Name"], df["Marks"])

# Add title and labels
plt.title("Students' Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

# Display the graph
plt.show()
