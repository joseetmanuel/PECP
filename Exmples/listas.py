print("Asinación de listas")
list_a = [1]
list_b = list_a
list_b[0] = 0
print(list_a[0] == list_b[0]) #True
print(list_a, list_b)
list_a = [1,2,3,4]
list_b = list_a[:]
list_b[0] = 0
print(list_a[0] == list_b[0])
print(list_a, list_b)

print("\nAgregar")
the_list = []
the_list.append(1)
print(the_list)

print("\nInsertar")
the_list = [1]
the_list.insert(0, 2)
print(the_list)

print("\nEliminar")
the_list = [1]
del the_list[0]
print(the_list)

print("\nEn y no en")
the_list = [1, 'a']
print('a' in the_list, 1 not in the_list)

print("\nRecorrer")
the_list = [1,2,3]
for element in the_list:
    print(element, end=' ')

print("\nCompreción")
the_list = [x for x in range(1,4)]
print(the_list)

print("\nLargo")
the_list = [1,2,3]
print(len(the_list))


print("\nCadenas")
try:
    texto = "Hola"
    print(texto[0])
    texto[0] = "M"
    print(texto[0])
except Exception as e:
    print(e)