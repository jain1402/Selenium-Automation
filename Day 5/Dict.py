mydict={
    "name":"Ayush",
    "dept":"Software Engineering",
    "Company":"Flair labs",
    "Joining date":"August 2022",
    "Employee ID":"105",
}

'''print(mydict["name"])
mydict["Employee ID"]="100"  # Assign new value to ID
print(mydict)'''

# Readinfg items using loops

'''for i in mydict:
    print (i)''' # Print only keys


'''for i in mydict.values() :
    print (i)''' # Print only Values

'''for a,b in mydict.items():
    print(a,b) ''' # print both keys and value

#  Check key is present in dictionary or not

'''mydict={
    "name":"Ayush",
    "dept":"Software Engineering",
    "Company":"Flair labs",
    "Joining date":"August 2022",
    "Employee ID":"105",
}

if "name" in mydict:
    print(" it exist")
else:
    print("not exist")'''

#  Adding item to the Dictionary

mydict={
    "name":"Ayush",
    "dept":"Software Engineering",
    "company":"Flair labs",
    "Joining date":"August 2022",
    "Employee ID":"105",
}

mydict["Heigth"] = "5'6''"
print(mydict)

mydict.pop("company")
print(mydict) # will delete any item

mydict.clear() # will clear all item in dict
print(mydict)

del mydict
print(mydict) # will delete complete dict and will get name not defined error