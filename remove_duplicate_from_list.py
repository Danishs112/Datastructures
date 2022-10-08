print("Hello world")

lst = [1,2,3,2,3,4,5,6,4,6]
count = 0
result_lst = []
hashMap ={}
for i in lst:
    hashMap[i] = lst.count(i)
print(hashMap)

for i in hashMap.keys():
    if hashMap[i] == 1 and hashMap[i] != 0:
        result_lst.append(i)
print(result_lst)