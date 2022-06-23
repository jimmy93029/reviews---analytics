data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) 

number = 0
count = 0
while count < len(data)-1 :
  number = number + len(data[count])
  count = count + 1
print(number/ len(data)) 

good = []
for g in data:
	if 'good' in g :
	  good.append(g)
print(good[0])

goody = [1 for g in data if 'good ' in g]
print(goody)


print('總共讀取完了共有',len(data),'筆資料')


