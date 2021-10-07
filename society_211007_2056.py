#2056. 연월일달력

testCase = int(input())
case = []
day31 = ['01', '03', '05', '07', '08', '10']
day30 = ['04', '06', '09', '11']


for i in range(testCase) :
    case.append(input())

for i in range(testCase) :
    year = case[i][:4]
    month =  case[i][4:6]
    day = case[i][6:]

    if ((month in day31) and int(day) <= 31) or ((month in day30) and int(day) <= 30) or ((month == '02') and int(day) <= 28) :
        print("#%d %s/%s/%s" %(i+1, year, month, day))
    else : print("#%d -1" %(i+1))
