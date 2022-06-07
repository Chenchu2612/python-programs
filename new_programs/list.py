# python list

#names = chenchu,mahesh,delhi,agra,benz,bmw,audi,porshe,apple,ipod,oneplus.

# list=["chenchu","mahesh","apple","ipod"]
# print(list)
# list1=["ramu","somu","mamu","ipod"]
# print(list1)

# length of a list

# a=["chenchu","ramu","somu","ramesh","kailash","meera"]
# print(len(a))
#
# b=["audi","benz","bmw","porshe","rover"]
# print(len(b))
# a=["chenhu",40,True,]
# print(a)
# print(len(a))

# type()
# a=["chenchu","ramu","somu","prabu"]
# print(type(a))
# b= ["chenhcu",25,True]
# print(type(b))

# a=list((True,False,"ramu","somuu",52))
# print(a)

# a=list(("chenchu","mahesh",True,25,"delhi","bmw"))
# print(a)

### ACCES LIST ITEMS :

# a=["chenhcu","dinesh","ramu","somu",25,True]
# print(a)
# print(a[0])
# print(a[2])
# print(a[5])

## NEGITIVE INDEXING:

# my_list=["chenhcu","audi","benz","porshe",True,25]
# print(my_list[-1])
# print(my_list[-3])
# print(my_list[-4])

# my_list=["chenchu","ramu","somu","kiran",True,25,36]
# print(my_list[2:5])
# print(my_list[1:3])

# print(my_list[:4])
# print(my_list[4:])

## RANGE OF NEGATIVE INDEX

# my_list=["chenchu","ramu","somu","kiran",True,25,36]
# print(my_list[-4:-1])
# print(my_list[-5:-2])
# print(my_list[:-2])
# print(my_list[-5:])

# my_list=["chenchu","ramu","somu","kiran",True,25,36]
#
# if "ramu" in my_list:
#     print("yes, ramu is present in my_list")

# my_list=["chenchu","ramu","somu","giri","ravi"]
# my_list[2]="bmw"
# print(my_list)


# my_list=["chenchu","mahesh","ramu"]
# my_list[1]="babu"
# print(my_list)

# my_list=["chenchu","audi","benz","porshe","range_rover",True,25]
# # audi,benz replace with tata,jaguar
# my_list[1:3]= "tata","jaguar"
# print(my_list)

# my_list = ["chenchu", "audi", "benz", "porshe", "range_rover", True, 25]
# range_rover replaced with land_rover,jaguar
# my_list[4:5]="land_rover","jaguar"
# print(my_list)

# va="a","b"
# print(va)

# my_list=["cut","put","but","car","more","sore","horse"]
# insert more items than you replace
# remove "but","car" and place "chenchu","mahesh","ramu","somu"

# my_list[2:4]="chenchu","mahesh","ramu","somu"
# print(my_list)

# insert less items than you replace
# remove "but","car","more" insert "ram","giri"
# my_list[2:5]= "ram", "giri"
# print(my_list)

# insert() method
# my_list=["cut","put","but","car","more","sore","horse"]

# my_list.insert(2,"monkey")
# print(my_list)

# my_list.insert(5,"ramesh_sir")
# print(my_list)

### ADD LIST ITEMS  ###

# APPEND()
# my_list=["cut","put","but","car","more","sore","horse"]
# my_list.append("ghattmneni")
# print(my_list)
# my_list.append("konidela")
# print(my_list)
# what happends if we add more than one item by using append method
# my_list.append("dog","bag")
# print(my_list)

# INSERT() METHOD

# my_list=["cut","put","but","car","more","sore","horse"]
# my_list.insert(3,"monkey")
# print(my_list)

# my_list.insert(3,"ramesh")
# print(my_list)

# can we insert morethan one item
#
# my_list.insert(1,"ramu")
# print(my_list)

 ##  ETENDS METHOD

# my_list1=["chenchu","mahesh","ramesh","ramu"]
# my_list2=["delhi","agra","hyderbad"]
# my_list1.extend(my_list2)
# print(my_list1)

# any iterable

# my_list1=["chenchu","mahesh","ramesh","ramu"]
# my_tuple2=("delhi","agra","hyderbad")
# my_list1.extend(my_tuple2)
# print(my_list1)
# print(my_tuple2)
# my_set={"benz","bmw","audi"}
# my_list1.extend(my_set)
# print(my_list1)


## REMOVE LIST ITEMS

# my_list1=["chenchu","mahesh","ramesh","ramu"]
# my_list1.remove("ramesh")
# print(my_list1)

 # my_list1.remove("ramu","mahesh") # it cuse error bcoz it removes only one element

# pop method
# a=["chenchu","hari","ramu","somu"]
# a.pop(1)
# print(a)
# a.pop()
# print(a)

# a=["chenchu","ramu","somu","indra","aadi","samba"]
# del a[2]
# print(a)

# del a
# print(a)

# clear
# a.clear()
# print(a)


## LOOP lists

# FOR LOOP

# a=["chenchu","ramu","somu","mahesh","ramesh","kailash","damo"]
# for x in a:
#     print(x)
# b= ["delhi","agra","punjab","banglore","goa"]
# x=[1,2,3,]
# for  x in b:
#     print(x)
# loop thoorugh inde number
# a=["chenchu","ramu","somu","mahesh","ramesh","kailash","damo"]

# for i in range(len(a)):
    # print(a[i])

# print(range(len(a)))
# print(range(6))
# print(len(a))

# for b in range(len(a)):
#     print(a[b])
# a=["chenchu","ramu","somu","mahesh","ramesh","kailash","damo"]

# z=0
# while z<len(a):
#     print(a[z])
#     z=z+1
# [print(x) for x in a]

# fruits=["apple","banana","cherry","pineapple"]
# newlist=[]

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
#
# print(newlist)

# sort list

# a=["chnchu","adi",15,"naresh","suresh","venki",25,]
# a.sort()
# print(a)
# above is not supported for multi varibles(string,int) in a single list
a=["chenchu","mahesh","ramu","somu"]
# a.sort()
# print(a)
# b=[5,9,10,16,95,25]
# b.sort()
# print(b)
# sort desending

# a.sort(reverse=True)
# print(a)

# a=[2,5,8,25,1,0,19,7]
# a.sort(reverse=True)
# print(a)

# a=["Zoo","Jeep","grape","apple","dog","ball"]
# a.sort()
# print(a)

# a.sort(key=str.lower)
# print(a)

# a.reverse()
# print(a)

# my_list=["car","bike","zeep","cycle","train"]
# ist=my_list.copy()
# print(list)

# a=["chenchu","audi","benz","porshe","bmw"]
# b=a.copy()
# print(b)

# c=list(a)
# print(c)

# c=list(a)
# print(c)


# join lists

a=["python","dzango","jeep","car"]
b=["bus","bmw","benz","boat"]
# c=a+b
# print(c)
# a.extend(b)
# print(a)

for x in a :
     a.append(b)

print(x)

password = input("password")
print("password is :")



























