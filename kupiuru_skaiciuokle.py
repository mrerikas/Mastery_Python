
def kupiuru_skaiciuokle(suma):
    kupiuru_skaicius = 0
    kupiuros = [1, 5, 10, 20, 50, 100, 200, 500]
    kupiuros.reverse()
    while suma != 0:
        for kupiura in kupiuros:
            if kupiura <= suma:
                suma -= kupiura
                kupiuru_skaicius += 1
                break
    return kupiuru_skaicius


print(kupiuru_skaiciuokle(499))
