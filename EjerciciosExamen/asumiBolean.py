the_list = [True,3.1415, -1]
try:
    print((len(the_list)== 3)in the_list)
except:
    pass

try:
    print(the_list.index(-1)==2)
except:
    pass
try:
    print("True" in the_list)
except:
    pass
try:
    print(len(sorted(the_list))!= len(the_list))
except:
    pass