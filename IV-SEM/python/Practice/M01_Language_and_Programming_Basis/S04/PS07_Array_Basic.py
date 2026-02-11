import  array
arr = array.array("i",[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)


'''
list:
1. use [] to create a list.
2. List is mutable.
3.List allows duplicate values.
4.List is heterogeneous.
5.List is indexed
'''
li = [12,25.4,6+5j, "Hello", 12,25.4]
print(li,type(li))
print(li[5])
print(li[3:6:1])
print(li[::-1])
print(len(li)) 
li.append(100)
print(li)
li.insert(2, "World")
print(li)
li.insert(-9, "hehehe")
print(li)



n = int(input())
count = 0
if n == 0:
    count = 1
else:
    count += 1
print(count)
