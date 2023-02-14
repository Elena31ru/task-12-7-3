per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = [0, 0, 0, 0]
deposit[0] = money / 100 * per_cent['ТКБ']
deposit[1] = money / 100 * per_cent['СКБ']
deposit[2] = money / 100 * per_cent['ВТБ']
deposit[3] = money / 100 * per_cent['СБЕР']
print(deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))
