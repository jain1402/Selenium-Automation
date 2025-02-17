# Method 1

s = " welcome to python"
rev_str = ""
for i in s:
    rev_str= i+ rev_str
print("New reverse string is:",rev_str)

# Method 2

s = " welcome to python"

rev_str=s[::-1]

print(rev_str)