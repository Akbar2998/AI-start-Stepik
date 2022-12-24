a = input()
count = 0
a_index = []
b_index = []
for i in range(len(a)):
    if a[i] == "a":
        a_index.append(i)
    elif a[i] == "b":
        b_index.append(i)
for x in range(len(a_index)):
    for j in range(len(b_index)):
        if a_index[x] < b_index[j]:
            count += 1
print(count)
