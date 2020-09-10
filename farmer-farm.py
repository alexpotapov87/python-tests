import locale
import pdb
# x = 240
# y = 320
# p1 = '$40'
# p2 = '$30'
# h1 = 2
# h2 = 1
x = 300
y = 380
p1 = '$70'
p2 = '$45'
h1 = 3
h2 = 1


def best_profit(acres, hours, prof_corn, prof_oat, labor_corn, labor_oat):
    pdb.set_trace()
    prof_corn = locale.atof(prof_corn.strip("$"))
    prof_oat = locale.atof(prof_oat.strip("$"))
    print(prof_corn)
    profitable_corn = prof_corn / labor_corn
    profitable_oat = prof_oat / labor_oat
    acre_to_time = hours / acres
    acres_for_corn = []
    while acre_to_time > 1:
        hours -= labor_corn
        time_left = hours
        acres -= 1
        acres_for_corn.append(acres)

    total_acres_for_corn = min(acres_for_corn)
    print(f'total_acres_for_corn is {total_acres_for_corn}')
    print(f'time_left is {time_left}')

    total_time_corn = int(hours) / int(labor_corn)
    total_time_oat = int(hours) / int(labor_oat)
    print(f'total_time_corn is {total_time_corn} hrs')
    print(f'total_time_oat is {total_time_oat} hrs')
    profits_corn = total_time_corn * int(prof_corn)
    profits_oat = total_time_oat * int(prof_oat)
    print(f'profits of corn is {profits_corn} $')
    print(f'profits of oat is {profits_oat} $')


best_profit(x, y, p1, p2, h1, h2)
