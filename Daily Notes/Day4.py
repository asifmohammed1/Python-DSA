# Dict: key-value, get(), items(), keys(), values()

a = {"name": "Asif", "age": 21, "city": "Mumbai"}

data = [{"Name": "a", "Age": 21, "Number": 124, "Address": "Mumbai", "Skills": "Python"},
        {"Name": "b", "Age": 25, "Number": 456, "Address": "Goa", "Skills": "Java"},
        {"Name": "c", "Age": 30, "Number": 789, "Address": "Hyderbad", "Skills": "c lang"}]


data1 = [["asif",25, 124], ["A", 45, "hyd"], ["B", 65, "delh"]] # nested list

# print(a.values())
# print(a.keys())

print(a.items())

print(a["name"])

a["skill"] = "python"

print(a)

print(a.get('skill'))

l = [1,2,3,4]

for k,v in a.items():
        print(f"{k} : {v}")


a.pop("age")

print(a)

print(data)

el = []
for i in data:
        if i["Skills"] == "Python":
                el.append(i["Name"])
        else:
                pass

print(el)


