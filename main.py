disk_letters = {1: 'E', 2: 'D', 3: 'C', 4: 'B', 5: 'A'}
def print_towers(towers):
    max_height = max(len(tower) for tower in towers)
    for level in range(max_height - 1, -1, -1):
        row = []
        for tower in towers:
            if level < len(tower):
                row.append(tower[level] + "|")
            else:
                row.append(" |")
        print(" ".join(row))
    base = ["__"] * len(towers)
    print(" ".join(base))
def hanoi(n, start, target, auxiliary, towers):
    if n == 1:
        disk = towers[start].pop()
        towers[target].append(disk)
        print(f"Перемещаем диск {disk_letters[n]} со стержня {start + 1} на стержень {target + 1}")
        print_towers(towers)
    else:
        hanoi(n - 1, start, auxiliary, target, towers)
        disk = towers[start].pop()
        towers[target].append(disk)
        print(f"Перемещаем диск {disk_letters[n]} со стержня {start + 1} на стержень {target + 1}")
        print_towers(towers)
        hanoi(n - 1, auxiliary, target, start, towers)
while True:
    place = int(input("Изначальное положение дисков (1, 2, 3) "))
    if place > 3 or place < 1:
        print("так низя")
        break
    place_need_to_be = int(input("Нужное положение дисков (1, 2, 3) "))
    if place_need_to_be > 3 or place_need_to_be < 1:
        print("так низя")
        break
    towers = [[], [], []]
    for i in range(5, 0, -1):
        towers[place - 1].append(disk_letters[i])
    auxiliary_peg = 3 - (place - 1) - (place_need_to_be - 1)
    hanoi(5, place - 1, place_need_to_be - 1, auxiliary_peg, towers)
    break
