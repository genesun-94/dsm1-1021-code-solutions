person = {
    "first_name": "Gene",
    "last_name": "Sun",
    "hobby": "gaming"
}

print(person)

first_name = person["first_name"]

last_name = person.get("last_name")

middle_name = person.get("middle_name")

print(first_name, middle_name, last_name)
#I expect "Gene Sun" as the output.
#Output was "Gene None Sun" - interesting how it still returned "None" for middle_name.

person["job"] = "Financial QA/Content Analyst"
print(person["job"])

person["hobby"] = "DJing"
print(person["hobby"])

person.pop("last_name")
print(person)
