luku = int(input('Anna kokonaisluku: '))
if luku == 1:
    print(str(luku) + ' ei ole alkuluku.')
elif luku > 1:
    for n in range(2,luku):
        if (luku % n) == 0:
            print(str(luku) + ' ei ole alkuluku.')
            break
    else:
        print(str(luku) + ' on alkuluku.')
else:
    print(str(luku) + ' ei ole alkuluku.')