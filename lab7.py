nums = [10, 23, 45, 7, 89]
vvodnum = int(input("Введите любое число: "))
print(f"Исходный список: {nums}")
print(f"Введенное число: {vvodnum}")
if vvodnum in nums:
    print("Ого, вы угадали число!")
else:
    print("Такого числа нет")

spis = [13, 23, 55, 30, 8, 13]
prosm = []
for item in spis:
    if item in prosm:
        print(f"Повторяющийся элемент: {item}")
    else:
        prosm.append(item)

days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница")
vvod = int(input("Сколько выходных вы хотите? "))
weekend = days[-vvod:]
workdays = days[:-vvod]
print(f"Ваши выходные дни: {','.join(weekend)}")
print(f"Ваши рабочие дни: {','.join(workdays)}")

