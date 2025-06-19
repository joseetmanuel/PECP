empty_dictionary = {} 
print(f"empty_dictionary: {empty_dictionary}")

phone_directory = {'Emergency': 911, 'Speaking Clock': 767}
print(f"phone_directory: {phone_directory}")


print(phone_directory['Emergency'])
print('Emergency' in phone_directory, 'White House' in phone_directory)
print(f"len: {len(empty_dictionary)}")

attendance = {'Bob': True}
attendance['Bob'] = False
print("Cambio valor: ",attendance['Bob'])

phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for key in phonetic:
    print(key, end=' ') # A B
for key in phonetic.keys():
    print(key, end=' ') # A B
for value in phonetic.values():
    print(value, end=' ') # Alpha Bravo
phonetic = {'A': 'Alpha', 'B': 'Bravo'}
for item in phonetic.items():
    print(item, end=' ') # ('A', 'Alpha') ('B', 'Bravo')