def do_the_mess(parameter):
    variable += parameter[0]
    return variable

the_list = [x for x in range(2,3)]
variable = -1
do_the_mess(the_list)
print(variable)