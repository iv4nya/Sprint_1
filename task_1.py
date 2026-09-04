time = '1h 45m, 360s, 25m, 30m, 120s, 2h 60s'

splittime = time.replace(',', '').split()
summa = 0
print(splittime)

for i in splittime:
    if 'h' in i:
        summa += int(i.replace('h', '')) * 60
    elif 'm' in i:
        summa += int(i.replace('m', ''))
    elif 's' in i:
        summa += int(i.replace('s', '')) // 60

print(summa)

    

        