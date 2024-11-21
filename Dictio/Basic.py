#create dict

dict1={'name':'Athul','age':24,'address':'Thodupuzha'}
print(dict1)
#another method for creation

dict2=dict(name="athul",age=24)
print(dict2)

#display method

print(dict2['name'])
print(dict2.get('age'))

#display key
print(dict1.keys())

#display values

print(dict1.values())

#insert

dict1['phone']=9883777654
print(dict1)

#dict items

x=dict1.items()
print(x)

#pop item
dict1.pop("name")
print(dict1)

#pop last
dict1.popitem()
print(dict1)

#clr

print(dict1.clear())
#delte
del dict1
print(dict1)