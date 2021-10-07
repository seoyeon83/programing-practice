#2050. 알파벳 변환

engdict = {}
j = 1
for i in range(65,91) :
    engdict[chr(i)] = j
    j+=1

case = list(input())
for i in case : print(engdict[i], end=' ')
