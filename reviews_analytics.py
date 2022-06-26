
def append_txt():
	data = []
	with open('reviews.txt', 'r') as f:
	  for line in f:
	    data.append(line) 
	print(data[0])
	return data

def count_word():
	wc = {}
	for line in data :
	  words = line.strip().split(' ')
	  for word in words:
	    if word in wc:
	      wc[word] += 1
	    else:
	      wc[word] = 1
	return wc

def word_dictionary_in_txt():
	while True:
	  word = input('你想要查甚麼字')
	  if word == 'q':
	    print('感謝你查詢')
	    break
	  elif word in wc:
	    print(word, '出現過',wc[word])
	  else:
	    print('sorry,the word you inquire is not in wc')

def num_word():
for word in wc :
  if wc[word] > int(input('單詞頻率')) :
    print(word, wc[word])

def reviews_average() :
  number = 0
  count = 0
  while count < len(data)-1 :
    number = number + len(data[count])
    count = count + 1
  print(number/ len(data)) 

def count_good1():
  good = []
  for g in data:
    if 'good' in g :
      good.append(g)
  print(good[0])

def count_good2():
  goody = [1 for g in data if 'good ' in g]
  print(goody)

print('總共讀取完了共有',len(data),'筆資料')














