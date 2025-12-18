def hanoi(n, start, target, auxiliary):
    disk_letters = {1: 'E', 2: 'D', 3: 'C', 4: 'B', 5: 'A'}
    if n == 1:
        print(f"Перемещаем диск {disk_letters[n]} со стержня {start} на стержень {target}")
    else:
        hanoi(n - 1, start, auxiliary, target)
        print(f"Перемещаем диск {disk_letters[n]} со стержня {start} на стержень {target}")
        hanoi(n - 1, auxiliary, target, start)
while True:
    place = int(input("Изначальное положение дисков (1, 2, 3) "))
    if place > 3:
        print("так низя")
        break
    place_need_to_be = int(input("Нужное положение дисков (1, 2, 3) "))
    if place_need_to_be > 3:
        print("так низя")
        break
    auxiliary_peg = 6 - place - place_need_to_be
    hanoi(5, place, place_need_to_be, auxiliary_peg)
    break
