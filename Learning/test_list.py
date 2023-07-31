'''nums=[1,2,3]
result=[i*2 for i in nums]
print(result)


def timesFive(n):
    return n * 5

rslt = [timesFive(i) for i in nums]
print(rslt)
for i in rslt:
    print(str(i)+'')

list_of_dicts1 =[{"name":"kevin"},{"name":"valeria"}]
a,b=[{"name":"kevin"},{"name":"valeria"}]
print(a)

rslt = [ "My name is: " + i["name"] for i in list_of_dicts1][0]
print(rslt)'''

# If Else in a List Comprehension
list1 = [1, 2, 3]
rslt1 = [i * 5 if i == 3 else i for i in list1]
print(rslt1)

rslt2 = [i * 5 for i in list1 if i == 3]
print(rslt2)

# Lambda 

rslt = list(map(lambda i: i*5, list1))

print(rslt)


txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

final_prices = map(TAX_RATE, txns)
list(final_prices)


