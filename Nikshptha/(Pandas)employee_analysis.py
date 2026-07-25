import pandas as pd
df = pd.read_csv("employees.csv")
print(df)

# 1. Read the CSV file

df = pd.read_csv("employees.csv")

print("=" * 60)
print("Original Data")
print(df)

# 2. Display the Data

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

# 3. Select Data

print("\nName Column")
print(df["Name"])

print("\nName and Salary")
print(df[["Name", "Salary"]])

print("\nFirst Employee using loc")
print(df.loc[0])

print("\nThird Employee using iloc")
print(df.iloc[2])

print("\nFirst Three Employees (Name & Department)")
print(df.loc[:2, ["Name", "Department"]])


# 4. Add New Column

df["Bonus"] = df["Salary"] * 0.10

print("\nBonus Column Added")
print(df)

# 5. Update Values

df["Salary"] = df["Salary"] + 5000

print("\nSalary Increased by 5000")
print(df[["Name", "Salary"]])

# 6. Delete Data

df.drop(columns=["Bonus"], inplace=True)

df = df[df["ID"] != 109]

print("\nAfter Removing Bonus Column and Employee ID 109")
print(df)

# 7. Rename Columns

df.rename(columns={
    "Department": "Dept",
    "Experience": "Exp"
}, inplace=True)

print("\nRenamed Columns")
print(df.columns)

# 8. Filter Data

print("\nAge > 30")
print(df[df["Age"] > 30])

print("\nSalary > 60000")
print(df[df["Salary"] > 60000])

print("\nDepartment = IT")
print(df[df["Dept"] == "IT"])

print("\nCity = Warangal")
print(df[df["City"] == "Warangal"])

# 9. Multiple Conditions

print("\nIT Employees with Salary > 60000 and Experience >=5")

print(df[
    (df["Dept"] == "IT") &
    (df["Salary"] > 60000) &
    (df["Exp"] >= 5)
])


# 10. Sort Data

print("\nSalary Ascending")
print(df.sort_values(by="Salary"))

print("\nSalary Descending")
print(df.sort_values(by="Salary", ascending=False))

print("\nSort by Age")
print(df.sort_values(by="Age"))

# 11. Handle Missing Values

print("\nMissing Values")
print(df.isnull())

print("\nCount Missing Values")
print(df.isnull().sum())

average_age = df["Age"].mean()

df["Age"].fillna(average_age, inplace=True)

print("\nMissing Age Filled with Average")
print(df)

# 12. Remove Missing Values

df_no_missing = df.dropna()

print("\nRows without Missing Values")
print(df_no_missing)

# 13. Remove Duplicate Records

df = df.drop_duplicates()

print("\nAfter Removing Duplicates")
print(df)

# 14. Count Values

print("\nEmployees in each Department")
print(df["Dept"].value_counts())

# 15. Unique Values

print("\nUnique Cities")
print(df["City"].unique())

# 16. Group By

print("\nAverage Salary by Department")
print(df.groupby("Dept")["Salary"].mean())

# 17. Aggregate Functions

print("\nTotal Salary")
print(df["Salary"].sum())

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nHighest Salary")
print(df["Salary"].max())

print("\nLowest Salary")
print(df["Salary"].min())

print("\nTotal Employees")
print(df["Name"].count())

# 18. Apply Function

df["Tax"] = df["Salary"].apply(lambda salary: salary * 0.05)

print("\nTax Column")
print(df[["Name", "Salary", "Tax"]])

# 19. Map Values

df["Gender"] = df["Gender"].map({
    "M": "Male",
    "F": "Female"
})

print("\nGender Converted")
print(df[["Name", "Gender"]])

# 20. String Operations

print("\nUppercase Names")
print(df["Name"].str.upper())

print("\nLowercase Names")
print(df["Name"].str.lower())

print("\nLength of Names")
print(df["Name"].str.len())

# 21. Boolean Column

df["Senior"] = df["Exp"] >= 5

print("\nSenior Column")
print(df[["Name", "Exp", "Senior"]])

# 22. Insert Column

df.insert(2, "Country", "India")

print("\nCountry Column Inserted")
print(df.head())

# 23. Set Index

df.set_index("ID", inplace=True)

print("\nID as Index")
print(df)

df.reset_index(inplace=True)

print("\nReset Index")
print(df)

# 24. Iterate Data

print("\nPrinting Rows")

for index, row in df.iterrows():
    print(row)

print("\nColumn Names")

for column in df.columns:
    print(column)

# BONUS CHALLENGE

print("\nEmployee with Highest Salary")
print(df.loc[df["Salary"].idxmax()])

print("\nCity with Most Employees")
print(df["City"].value_counts().idxmax())

print("\nAverage Salary of IT Employees")
print(df[df["Dept"] == "IT"]["Salary"].mean())

print("\nNumber of Female Employees")
print((df["Gender"] == "Female").sum())

print("\nEmployees with Experience > 5")
print(df[df["Exp"] > 5])

print("\nEmployees whose Name Starts with 'A'")
print(df[df["Name"].str.startswith("A")])

print("\nEmployees with Salary between 55000 and 70000")
print(df[df["Salary"].between(55000, 70000)])

print("\nYoungest Employee")
print(df.loc[df["Age"].idxmin()])

print("\nOldest Employee")
print(df.loc[df["Age"].idxmax()])

# Save Cleaned Data

df.to_csv("employees_cleaned.csv", index=False)

print("\nCleaned Data Saved Successfully.")