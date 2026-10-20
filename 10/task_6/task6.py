f = open('task6.csv').readlines()

a = 0
b = 0
c = 0
TotalMoneySpent = 0
TotalGoodBought = 0
MaxMoneyGained = ''
maxsold = ''
BestDay = {}

for s in f[1:]:
    print(s)
    s = s.rstrip()
    s = s.split(',')
    TotalMoneySpent += int(s[2])*int(s[3])
    TotalGoodBought += int(s[2])
    # print(s[2])
    # print(TotalMoneySpent)
    
    #print(s1)
    a+=int(s[2])*int(s[3])
    if int(s[2])>b:
        b = int(s[2])
        maxsold = s[1]
    if int(s[2])*int(s[3])>c:
        c = int(s[2])*int(s[3])
        MaxMoneyGained = s[1]
    BestDay[s[0]]=int(s[2])*int(s[3])

print(a)
print(maxsold)
print(MaxMoneyGained)
print(TotalMoneySpent/TotalGoodBought)
print(max(BestDay, key=BestDay.get))


#Понять как игнорировать некорректные записи
#понять как написать генератор файла минимум на 5000 продаж
#названия товаров выбирать из заранее заданного списка;
#часть записей должна содержать ошибки для проверки обработки исключений.