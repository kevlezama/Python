#Given dictionary is consisted of vehicles and their weights in kilograms. 
#Contruct a list of the names of vehicles with weight below 5000 kilograms. 
#In the same list comprehension make the key names all upper case.

dict1={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
#Type your answer here.
lst1=[i.upper() for i in dict1.keys() if dict1[i] < 5000]
print(lst1)

# Using lamba 
rslt = map(lambda dict_key: dict_key.upper(), dict1.keys())
print(list(rslt))


#dic generation with list comprenhension
number = [1,2,3,4]
brands = ["Toyota","BMW","Chevrolet","Mercedez Benz"]

rslt_dict_generation = {number[i]:brands[i] for i in range(len(number))}

print(rslt_dict_generation)

advance_dict_generation = zip(number,brands)
print(dict(advance_dict_generation))







