''' A set is a collection whic is unordered and unindexed
    In python set is written in curely brackets {}
    A set is Mutable
'''
# myset = {"Ayush","Jain", "age", "profession", "department"}
# print(myset)

#  update and Add items to the set
'''myset = {"Ayush","Jain", "age", "profession", "department"}

myset.add("location")
myset.add(1)
myset.update(["QA engineer", "flair labs"])

print(myset)'''

# Remove , clear items of the set and Delete the complete set 
'''myset1={1, 'age', 'department', 'QA engineer', 'profession', 'location', 'Jain', 'Ayush', 'flair labs'}

myset1.remove(1)
# myset1.clear()
print(myset1)'''

# del myset1
# print(myset1)


''' join 2 set 
( we use two methods )
1. Union
2. Update
'''
myset = {"A","B", "C", "D", "E"}
myset1={1, 'age', 'department', 'QA engineer', 'profession', 'location', 'Jain', 'Ayush', 'flair labs'}

myset2=myset.union(myset1)

print(myset2)

myset1.update(myset)

print(myset1)