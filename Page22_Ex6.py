L = 0
R = 100
current = (L + R) // 2
answer = None
print ("Загадайте число...")
while answer != '=':
    print(current, "?")
    answer = input()
    if answer == '=':
        print('Я угадал!')
        break
    elif answer == '>':
        L = current
    elif answer == '<':
        R = current
    else:
        print('Повторите ввод (>, <, =)!')
        continue
    current = (L + R) // 2
