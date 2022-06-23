data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) 

number = 0
count = 0
while count < 100000 :
  number = number + len(data[count])
  count = count + 1
print(number/ len(data)) 


print('總共讀取完了共有',len(data),'筆資料')
