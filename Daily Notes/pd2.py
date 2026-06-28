import pandas as pd

df = pd.DataFrame({
    "name":["teja","sara","asif"],
    "age": [20,21,22],
    "phonenumber": [123,456,789],
    "Skills": ["python","java","dot"],
    "address":["hyd", None,"Mub"]
})

df.isnull() # check all null values
df.isnull().sum() # check with columns

df["address"] = df["address"].fillna("") # fill empty string in null values
df.dropna(inplace=True)

df.drop_duplicates(inplace=True) # delete the duplicates

df["age"].value_counts() # count the values of the age

df["age"].unique() # find the unique values

# groupby
df.groupby("Skills")["age"].mean()

df['age'].sum()
df['age'].mean()
df['age'].max()
df['age'].min()
df['age'].count()

def testfun(n):
    return n*2

# l = list(df["age"])
# rl = []
# for i in l:
#     rl.append(testfun(i))
#
# df["age"] = rl

# apply
df["age"] = df["age"].apply(testfun)

# map
gender = {
    "sara":"Female"
}
df["Gender"] = df["name"].map(gender)
