#Create an identical list from the first list using list comprehension.
lst1=[1,2,3,4,5]
#Type your answer here.
lst2=[i for i in lst1]
print(lst2)

#Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
#Type your answer here.
rng=range(1200,2000,130)
lst=[i for i in rng]
print(lst)

#Use list comprehension to contruct a new list but add 6 to each item.
#Type your answer here.
lst3=[44,54,64,74,104]
lst4=[i+6 for i in lst3]
print(lst4)

#Using list comprehension, construct a list from the squares of each element in the list.
lst5=[2, 4, 6, 8, 10, 12, 14]
#Type your answer here.
lst6=[pow(i,2) for i in lst5]
print(lst6)
lst6=[i**2 for i in lst5]
print(lst6)


#Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
lst7=[2, 4, 6, 8, 10, 12, 14]
#Type your answer here.
lst8=[pow(i,2) for i in lst7 if pow(i,2) > 50]
print(lst8)






