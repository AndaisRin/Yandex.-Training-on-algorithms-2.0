my_dict = dict()
a = int(input())
while a != 0:
    if a not in my_dict.keys():
        my_dict[a] = 1
    else:
        my_dict[a] += 1
    a = int(input())
print(my_dict[max(my_dict.keys())])
