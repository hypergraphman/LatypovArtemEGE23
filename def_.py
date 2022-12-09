def dostavka(chto, cost):
    if chto == 'burger':
        return 'Вы купили бургер за ' + str(cost)
    if chto == 'pizza':
        return 'Вы купили пиццу за ' + str(cost)
    return 'мы не знаем что такое ' + chto + ' но спасибо за ' + str(cost)


print(dostavka('burger', 300))
print(dostavka('pizza', 600))


def dostavka2(chto, cost):
    if chto == 'burger':
        print('Вы купили бургер за ' + str(cost))
    elif chto == 'pizza':
        print('Вы купили пиццу за ' + str(cost))
    else:
        print('мы не знаем что такое ' + chto + ' но спасибо за ' + str(cost))


dostavka2('burger', 300)
dostavka2('asdf', 100500)