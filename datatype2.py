''' dict- store data in key value pair ,
 key cannot be duplicate, 
 indexing and slicing are not allowed ,
 not order preserved'''

ab = {}
print(type(ab))
xy = {'name': "anuj", 'age':22,'address':"indore",'roll':2253}
print(xy)
print(xy['name'])
print(xy.get('age'))
print(xy.keys())
print(xy.values())
print(xy.items())
print('--' * 20)
li = ['ram','sita','gita','laxman','savita',2678,132]
for k in li:
    print(k)

# print('--' * 20)
# for k in xy:
#     print(k,xy[k])
# print('--' * 20)
# for i,j in xy.items():
#     print(i,'=',j)

# print('--' * 20)
# print(xy)
# print('deleted last :',xy.popitem())
# print('deleted pair:',xy.pop('age'))
# print(xy)
# xy['age'] = 23
# print(xy)
# xy['address'] = "bhopal"
# print(xy)


# fruits = {'Apple', 'Banana', 'Orange','Mango','Grapes','Kiwi','Papaya','Guava',
#           'watermelon','pomegranate','pineapple','cherry','strawberry','blueberry',
#           'velvet apple'}
# vagetables = {'potato', 'tomato', 'onion','cabbage','cauliflower','carrot','beetroot',
#               'radish','spinach','broccoli','capsicum','cucumber','pumpkin'}

# grains = {'wheat', 'rice', 'barley','oats','maize','millet','rye','sorghum'}

# foods ={'Junk' : 'maida', 'Healthy' : 'oats', 'Fruits' : fruits,
#          'Vagetables' : vagetables, 'Grains' : grains}
# print(foods)
# print(foods.get('Fruits'))
# for k,v in foods.items():
#     print(k,'=',v)
# print('--' * 20)
# print(foods['Fruits'])

'''tuple- is immutable, it means we cannot add or remove elements from the tuple.
tuple is ordered collection of elements, indexing and slicing are allowed.'''
t = (1, 2, 3 , 4, 5, 6, 7, 8, 9)
print(type(t))
print(t)
tt =('name : anuj','age : 22', 'indore', 2253)
print(tt)
print(tt[1])
address = (tt[3])
print(address)
print(tt[1:2])
city = ('indore', 'bhopal', 'delhi', 'mumbai', 'kolkata', 'chennai', 'bangalore', 'hyderabad', 'pune', 'jaipur')
print(city[8])
