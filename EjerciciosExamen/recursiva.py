def walk(top, foo = 0):
    if top > 0:
        foo = walk(top -1, foo+top)
    return top
    
print(walk(2))