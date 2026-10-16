import pandas as pd

data = pd.DataFrame({
    "Name": ["Anita", "Bikash", "Suman", "Rita", "Kiran"],
    "Age": [15, 16, 15, 14, 16],
    "Class": [10, 10, 9, 9, 10],
    "Marks": [85, 78, 92, 88, 81]
})

df=pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)
print("CSV file created successfully.")
