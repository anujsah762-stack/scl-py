
import matplotlib.pyplot as plt

# Daily expenses
expenses = [200, 150, 100, 250, 100]
categories = ["Food", "Transport", "Snacks", "Education", "Other"]

# Create a pie chart
plt.pie(expenses, labels=categories, autopct="%1.1f%%")

# Add title
plt.title("Daily Expenses of a Person")

# Display the chart
plt.show()
