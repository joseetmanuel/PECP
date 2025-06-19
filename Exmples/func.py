try: print(saludo()) 
except: print("No haz declarado la función") 
def saludo():
    return "Hola"
print(saludo())  # "Hola"

def factorial(s = False, n = 3):
    print(s)
    return 1 if n < 2 else n * factorial(n - 1)
print(factorial(True,6)) # 720
print(factorial(n=4,s=False)) # Error de loop
print(factorial(4, n=4)) # Error de tipo


def function(a, b, c):
    print(a, b, c)
print(f"Parametros: {function(1, c=3, b=2)}")

def function():
    global variable
    variable += 1
variable = 1
function()
print("Global: ",variable)

def function(parameter):
    parameter = [2]
the_list = [1]
function(the_list)
print("Listas: ",the_list)
