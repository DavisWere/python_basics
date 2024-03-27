Cars = ['bmw', 'honda', 'benz', 'honda']
Cars.append('toyota')
Cars.count('honda')
Cars.insert(2, 'audi')
print(Cars)
Cars.pop(3)# remove  the last element of list, which is 'benz' in this case
print(Cars)
print(Cars.count('honda'))  # Output: ['bmw', 'honda', 'benz', 'toyota']
