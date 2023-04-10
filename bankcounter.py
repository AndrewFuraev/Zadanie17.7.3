print('Эта программа поможет вам вычислить возможный доход за год, от вложенной вами суммы в различных банках')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
name = list(per_cent.keys())
d = list(per_cent.values())
deposit = []
money = float(input('Введите сумму в рублях котроую вы хотите вложить ' ))
while money == 0 or money <0:
    print('Введенная вами сумма не должна быть равна или меньше 0')
    money = float(input('Введите сумму в рублях котроую вы хотите вложить '))
for x in d:
    n = round((x * money / 100),2)
    deposit.append(n)
print ('Доход за год составит ')
s = 0
for u in deposit:
        print (name[s], u, end=' рубля(ей), ')
        s = s + 1
print(' ')
print ('Максимальная сумма, кото'
       'рую вы можете заработать ', max(deposit), 'рубля(ей)')
