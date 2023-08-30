# Lamda
a = [1, 2, 3]

map_rslt = map(lambda i: i * 5, a)
print(map_rslt)

map_to_list_rslt = list(map_rslt)
print(map_to_list_rslt)

# coming from list comprehesion 
print('coming from list comprehesion')
rslt_list = [i * 5 if i == 3 else i for i in a]
print(rslt_list)

# using lambda and map
print('coming from list comprehesion with using lambda and map')
map_rslt_2 = map(lambda i: i * 5 if i == 3 else i, a)
map_rslt_2_list = list(map_rslt_2)
print(map_rslt_2_list)

# coming from list comprehesion with if condition and if filter
print('coming from list comprehesion with if condition and if filter')
rslt = [i*5 if i ==3 else i for i in a if i > 1]
print(rslt)

# Appling lambda map and filter to get the same result
print('Appling lambda map and filter to get the same result') 
avanced_rslt = [map(lambda i: i * 5 if i == 3 else i, a)]
print(avanced_rslt)
x = list(avanced_rslt[0])
print(x)

avanced_rslt_2 =[map(lambda i: i * 5 if i == 3 else i, filter(lambda i: i >1, a))]
print(list(avanced_rslt_2[0]))







