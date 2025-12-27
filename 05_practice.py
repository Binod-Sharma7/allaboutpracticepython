# list is mutable
a=[1,2,"binod"]
# prints type as list
print(type(a))
a.append("ram")
print(a)
print(a.count(1))
print(a.count("binod"))
# tuple is immutable
b=(1,2,3,"binod")
c=b.count("ram")
print(c)