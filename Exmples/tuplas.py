empty_tuple = () # tuple() tiene el mismo significado
print(f"empty_tuple: {empty_tuple}")

try:
    one_element_tuple = tuple(1) # no debe reemplazarse con (1)!
    print(f"one_element_tuple: {one_element_tuple}")
except:
    print("que no leiste el comentario?")

one_element_tuple = 1, # el mismo efecto que el anterior
print(f"one_element_tuple: {one_element_tuple}")

two_element_tuple = (1, 2.5)
print(f"two_element_tuple: {two_element_tuple}")

two_element_tuple = 1, 2.5 # el mismo efecto que el anterior
print(f"two_element_tuple: {two_element_tuple}")

print("len:",len((1, 2.2, '3', True)))

print("Cortar:",(1,2,3)[4:5])