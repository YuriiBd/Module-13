tickets = int(input('Введите количество билетов '))
T = [i for i in range(tickets)]
P = []
for i in T:
    age = int(input(f'Введите возраст {i + 1} человека '))
    if age < 18:
        price = 0
    elif 18 < age < 25:
        price = 990
    else:
        price = 1390
    P.append(price)
if len(P) > 3:
    sum1 = int(sum(P)) / 100 * 90
    print(f"Общая стоимость ваших билетов c учетом скидки: {sum1} руб.")
else:
    sum2 = int(sum(P))
    print(f"Общая стоимость ваших билетов: {sum2} руб.")
