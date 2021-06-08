# Remove duplicate elemnts without using set()

list = [1,2,3,4,2,1,6,3,7,4,9]
res = []
[res.append(i) for i in list if i not in res]
print(res)