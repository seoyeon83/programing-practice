testCase = int(input())
case=[]

for i in range(testCase) :
    case.append(list(map(int,input().split(' '))))

for i in range(testCase) :
    print("#%d %d %d" %(i+1, case[i][0]//case[i][1],case[i][0]%case[i][1]))
