# It is  also used to store multiple items in a single variable 
# here we use curly bracket to denote a set 
# sets are unordered ,unindexed,unchangeble and can only stores unique value (i.e. no dublicates allowed)
# still we can add or remove new items 
# it can have multiple data types 
from re import S, T


myset={10,20,30,40,10,20,30}
print(myset)
print(type(myset))
print(len(myset))
print(range(len(myset)))

myset1={'shivambhardwas',40,'hello',True,None,50,False}
print(myset1)

myset2=set((10,20,30,40,50,60,70,80,90,100))
print(myset2)

# it is very much unordered






# Access the items in a set 
# we cannot use index or a key to access items as they are unordered
# we can loop through that it the value is present or not 
# we can use in keyword to check if the items is present or  not

myset3={10,20,30,40,50,60,70}
for z in myset3:
    print(z)
print(20 in myset3) 
print(200 in myset3)  
    
    
    


# once the set  is created ,we cannot changes the items but we can definitely add the items
myset4={'shivam','kumar','singh','bhardwas','suryavansi'}
myset4.add(100)
myset4.add('banana')
print(myset4)



# Add items from one set to another 
# update () can take an iterable object 

set5={11,22,33,44}
set6={55,66,77,88}
set5.update(set6)
print(set5)

set7={12,23,34,45}
list1=[56,67]
set7.update(list1)
print(set7)

set7={111,22,333}
# set7.remove(222)  this will give error as no 222 is present
set7.remove(22)
print(set7)

# another method that will not give error is using discard
set8={1,2,3,4,5,6,7,8,9,0}
set8.discard(10)
print(set8)
b=set8.pop()
print(b)
print(set8)
set8.pop()
print(set8)




set9={234,574,4647}
# del set9
# print(set9)  this will give error as everything is deleted 


for g in set9:
    print(g)
    



# JOIN THE SETS
set10={'a','b','c'}
set11={10,20,30}
set12=set10.union(set11)
print(set12)
 
#  it removes the duplicate
# if we add 
set13={'a','b','c','c','b'}
set14={10,20,30,10,20}
set15=set13.union(set14)
print(set15)
 
set13.update(set14)
print(set13)
print(set14)

set14.update(set13)
print(set13)
print(set14)
# this will provide diff output




s={111,222,333,444}
d={444,555,666,777}
s.intersection_update(d) #modifying the set s in this case
print(s)

# ALTER METHOD
o=s.intersection_update(d)
print(s)
print(d)
print(0)


# now if in above questions x={10,20,30,40} , y={40,50,60,70,}
# if we use z= x.intersection(y) then 
# print(x) will give {40,10,50,20,30}
# print(y) will give {40,50,60,70,}
# print(z) will give {40,50}

t={10,20,30,40,50}
u={40,50,60,70}

t.symmetric_difference_update(u)
print(t)     # x is modified common part not included
print(u)     #modified the t in this

f=t.symmetric_difference(u)
print(t)
print(u)
print(f)













