#int/integer

# x=525
# y=-252
# z=1
#
# print(type(x))
# print(type(y))
# print(type(z))

#folat
# x=25.2
# y=1.25
# z=-2.2563456
#
# print(type(x))
# print(type(y))
# print(type(z))


 # x = 32e3
 # y = 525E8
 # z = -425.e7
 #
 # print(type(x))
 # print(type(y))
 # print(type(z))

# complex

# x=-2+5j
# y=2+5j
# z=-8j
# a=-2-9j
# b=5j
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))
# print(type(b))

# conversion

#int to float,complex

# x=25
# a=float(x)
# b=complex(x)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# float to int,complex

# x= 2.25
# y =-3.55
# a=int(x)
# b=complex(y)
#
# print(a)
# print(b)
#
# import random
# print(random.randrange(1,25))

 #strings
#
# print("hello")
# print('hello')
# assingning to a varible.
# a="hello"
# print(a)
# b='hello'
# print(b)

# multiline string
# x="""my_name_is_mahesh,
# iam_working_in_srt
# i_prefer_dalmia"""
# print(x)
#
# y='''my_name_is_mahesh,
# iam_working_in_srt
# i_prefer_dalmia'''
#
# print(y)
# a="hello world"
# print(len(a))
# print(a[10])
#loop through strings

# x="chenchu babu"
# for a in x:
#     print(a)
#length function

# a="chenchu babu,"
# print(len(a))

#a="chenchu mahesh"
# print("m" in a)
# name="my name is chenchu"
# print("my" in name)
# a="chenchu mahesh"
# if "m" in a:
#     print("yes,'m' is present in a")

# not in
# a= "chenchu mahesh"
# print("z" not in a)

# a="chenchu mahesh"
# if "z" not in a:
#     print("no, z is not present")
#     print("yes, z is not present")

# slicing string
# a="chenchu mahesh"
# print(a[0:5])
# print(a[0:8])
# print(a[0:9])

# slice form start
#a="chenchu mahesh"
#print(a[0:])

# slice from end
# print(a[:12])
# negative index
# a="chenchu mahesh"
# print(a[-6:-2])


# modify string
# upper case
# a="chenchu mahesh"
# print(a.upper())

# remove white space
# a=" chenchu mahesh "
# print(a.strip())

# replace string
# a="chenchu mahesh"
# print(a.replace("c","m"))
# a="chenchu,mahesh"
# print(a.split(","))
# print(a.split("n"))
# print(a.split("e"))
# print(a.split("h"))

# a="chenchu"
# print(a.split("n"))

#concatination

# a="chenchu "
# b="mahesh"
# c=a+b
# print(c)

# a="chenchu"
# b="mahesh"
# c=a+" "+b
# print(c)


#formate string

# a=5
# b="my name is chenchu iam {} feet"
# print(b.format(a))

# escape character

# a="chenchu\"mahesh\""
# print(a)

# to insert simgle quote

# a= "chenchu mahesh\'s"
# print(a)
# to insert one backslash

# a="chenchu \\ mahesh"
# print(a)

# to insert new line
# a= "chenchu\n mahesh"
# print(a)




# carriage return
# a=" chenchu\r mahesh"
# print(a)
# b="hello\rworld"
# print(b)

# toinsert tab
# a= "chenchu\tmahesh"
# print(a)
# to insert backslash
# a="chenchu\bmahesh"
# print(a)
                                      # string methods
# a="chenchu Mahesh"
# print(a.capitalize())

#if first charecter is a number

# a="25 chenchu mahesh"
# print(a.capitalize())

# casefold/lower
#a="CHENCHU mahESH"
#print(a.casefold())
#print(a.lower())

# string center()
# a="chenchu"
#b=a.center(10)
#print(b)
# c=a.center(10,"d")
# print(c)

# count()
# a="chenchu Mahesh"
# b=a.count("e")
# print(b)
# c=a.count("c",0,6)
# print(c)

# a= "i am an indian, ilove apples"
# b=a.count("i")
# print(b)

# c=a.count("a",0,15)
# print(c)

# a="chenchu"
# b=a.encode()
# print(b)

a= "i have bike , iam going"
# b=a.endswith("g")
# print(b)

# b=a.endswith("e",0,10)
# print(b)
# c=a.endswith("e",0,6)
# print(c)

# #expand tabs
# a="c\th\te\tn\tc\th\tu"
# b=a.expandtabs()
# print(b)
# c=a.expandtabs(1)
# print(c)
# print(a)
# print(a.expandtabs())
# a="my name is mahesh"
# b=a.find("name")
# print(b)
# c=a.find("n")
# print(c)
# d=a.find("m")
# print(d)
# e=a.find("s",0,10)
# print(e)
# f=a.find("r")
# print(f)
# g=a.index("r")
# print(g)



#using empty placeholder
a="my name is{fname},iam {hi} years of old,i trevel to {he}"
# b=a.format(" mahesh",28,"delhi")
# print(b)
#key pair values
# c=a.format(fname="mshesh",hi=28,he="delhi")
# print(c)

# by using index value
# a="my name is{2},iam {0} years of old,i trevel to {1}"
# d=a.format("delhi","mahesh",28)
# print(d)
# e=a.format(28,"delhi"," mahesh")
# print(e)
# a="iam chenchu mahesh"
# b=a.index("e")
# print(b)
# c=a.index("c",0,5)
# print(c)
# d=a.index("z")
# print(d)





























































