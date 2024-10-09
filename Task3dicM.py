emp = {
  "name": "abc",
  "age": 23,
  "city": "Nagpur",
  "contact_info":{
         "address":"ad1",
         "mob_no": 99584545
}
}

# clear() Method

emp.clear()

print(f'emp =',emp)

# copy() Method

emp = {
  "name": "abc",
  "age": 23,
  "city": "Nagpur",
  'contact_info': {
         'address':'ad1',
         'mob_no': 99584545
}
}

emp_info = emp.copy()

print(f'emp_info:',emp_info)

print()

# fromkeys method

x = ('abc', 'xyz', 'cde')


thisdict = dict.fromkeys(x)

print(thisdict)

print(f"The new created dict with None values : " + str(thisdict))


thisdict2 = dict.fromkeys(x,2)

print()
print(f"The new created dict with 2 values : " + str(thisdict2))


# get() Method

emp = {
  "name": "abc",
  "age": 23,
  "city": "Nagpur",
  'contact_info': {
         'address':'ad1',
         'mob_no': 99584545
}
}

print(f'emp contact_info using get = {emp.get("contact_info")}')
print()
# items( method)

Dictionary1 = { 'A': 'name', 'B': 4, 'C': 'salary' }

print("Dictionary items:")


print(Dictionary1.items())
print()

# keys() Method

emp = {
  "name": "abc",
  "age": 23,
  "city": "Nagpur",
  'contact_info': {
         'address':'ad1',
         'mob_no': 99584545
}
}

print(f'key method  = {list(emp.keys())}')

print()

# pop() Method

customer = {"Rahul":8,"Aditya":1, "Madhur": 5} 

customer.pop("Rahul") 

print(customer)
print()

# setdefault() Method

emp = {
  "name": "abc",
  "age": 23,
  "city": "Nagpur",
  'contact_info': {
         'address':'ad1',
         'mob_no': 99584545
}
}

emp.setdefault(' ', 'city') 
print(emp)

print()

# values( ) method

print(emp.values())
print()

# update() method

emp.update({'id': 201})
print('apply update method =',emp)
print()