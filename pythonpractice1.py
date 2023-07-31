# name = input("Enter your name")
# print(name.capitalize())
# print(name.casefold())
# print(name.center(3))
# print(name.count('i',0,5))
# print(name.encode())
# print(name.find("i"))
# print(type(name)) 
# print(name[::-1])
mylist = ["indexabale" , "Changable" , "allow duplicate valies"]
print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist[::-1])
print(mylist[1::-1])
mylist[1]= "Nithya Learning"
print(mylist)
mylist.append("July Learnings")   
print(mylist)   
mylist.insert(2,"Latest Learnings")
print(mylist)
sortedlist = mylist.sort()
print(mylist)
#print(mylist.reverse())
# #print(mylist.count[1])
#print(mylist.remove)
for i in mylist:
    print(i)
for i in range(len(mylist)):
    print(i)
print("******************************************* Tuple**********************************************************")
mytuple = ("indeaxbale" , "Unchangeable" , " Allow duplicate values")
print(mytuple)
print(mytuple.count("Unchangeable"))
print(mytuple[0])   
print(len(mytuple))
print("******************************************* Set**********************************************************")
myset = {"Unordered" ,"unindexed" ,"Does not allow duplicate values"}
print(myset)
myset.add("my set createed on july 2oth")
myset2 = {1,2,3,4}
print(myset)
myset.update(myset2)
print(myset)
myset.symmetric_difference
print(myset)
print(len(myset))
print("******************************************* Dictionaries**********************************************************")
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(Dict)
print(Dict.get(1))
print(Dict.keys())
print(Dict.values())
print(Dict.items())
Dict[4] = 'Nithya'
print(Dict)
print("******************************************* ifelse**********************************************************")
a = [1, 2, 3, 4]
 
while a:
    print(a.pop())