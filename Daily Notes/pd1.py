# Pandas Series

import pandas as pd

a = pd.Series([{"name":"teja", "age": 21},{"name":"teja1", "age": 21},{"name":"teja2", "age": 21},{"name":"teja3", "age": 21}], index=["name","age","address","phonenumber"])

print(a)
print(a["name"])

df = pd.DataFrame({
    "name":["teja","sara","asif"],
    "age": [20,21,22],
    "phonenumber": [123,456,789]
})

print(df)
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()

df["name"] # rows with 1 column
df[["name", "age"]] # rows with selected columns

df.loc[0] #rows by index number
df.loc[0:1] # rows by slicing
df.loc[0:1, ["name", "age"]] # selected columns

df.iloc[0:2, 0:2] # Rows and column slicing

df["skills"] = ["python","java","C"] # add new columns with values

# Update
df.loc[0, "age"] = 30 # update age

# delete # columns
df.drop("skills", axis=1, inplace=True) # deleted the skill column and inplaced in df
df2 = df.drop("name", axis=1) # in df2 name column as deleted, df remains same

# drop rows
df.drop(0, inplace=True) # delete row 0 and inplace in df
df3 = df.drop(1)

# Rename the column name
df.rename(columns={"name":"Full Name"}, inplace=True)
df4 = df.rename(columns={"age": "Ages"})

# Filter
df[df["age"] > 20]
df[df["name"] == "pappu"]

df[(df["age"] > 20) & (df["name"] == "pappu")]


# sort
df.sort_values("Full Name", ascending=False)

df.to_csv("data.csv", index=True)
# df.to_excel("data.xlsx", index=True)
# df.to_json("data.json", index=True)
# df.to_html("data.html", index=True)

# DS
# isnull, #dropna, #drop_dulicate, #count, unique, groupby, apply, map, insert and update, merge, concate

