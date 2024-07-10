n = int(input("No of iterations: "))
uid_lst = []
uid_dict = {}

for i in range(n):
    uid = input("Enter UID: ")
    uid_lst.append(uid)
for id in uid_lst:
    flag = 0
    if len(id) != 10:
        print("Invalid")
        continue
    if id in uid_dict:
        print("Invalid")
        continue
    else:
        uid_dict[id] = 1
    upp = 0
    c = 0
    for i in id:
        if not i.isalpha() and not i.isdigit():
            print("Invalid")
            flag = 1
            break
        if id.count(i)>1:
            print("Invalid")
            flag = 1
            break
        if i.isupper():
            upp+=1
        if i.isdigit():
            c+=1
    if flag == 1:
        continue
    if c>=3 and upp>=2:
        print("Valid")
    else:
        print("Invalid")