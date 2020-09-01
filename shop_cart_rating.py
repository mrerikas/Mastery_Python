def shopping(cart):
    rated_groceries = {'cipsai': -1, 'cola': 0.4, 'zuvis': 1,
                       'mesa': 0.5, 'obuolys': 1, 'makaronai': 0, 'kose': 1}
    rating = 0
    for item in cart:
        if item in rated_groceries.keys():
            rating = rating + rated_groceries[item]
        else:
            rated_groceries[item] = float(
                input(f'Prekei {item} neturiu indekso, sugalvok nuo -1 iki 1: '))
            while rated_groceries[item] > 1 or rated_groceries[item] < -1:
                rated_groceries[item] = float(
                    input(f'Prekei {item} neturi tokio indekso, prasau ivesto nuo -1 iki 1: '))
                rating = rating + rated_groceries[item]
    return print(f'Tavo prekiu krepselio reitingo indeksas yra {rating}.')


cart = ['morka', 'pomidorai', 'cipsai', 'zuvis', 'burokeliai', 'cola', 'kose']
shopping(cart)
