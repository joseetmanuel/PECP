total = -1
for i in range (-1,1):
    print(f"F total: {total}, i: {i}")
    if 2 * i<4:
        total += 1
        print(f"I total: {total}, i: {i}")
else:
    total +=2
    print(f"E total: {total}, i: {i}")
print(total)
