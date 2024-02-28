parancs = input("Kérem a robot parancsait: ")
betuk = {}
e = "E"

for e in parancs:
    if e in betuk.keys():
        betuk[e] += 1
    else:
        betuk[e] = 1

for k,v in betuk.items():
    print(f"{k} - {v}")

class Nehez:

    def szamolas():
        if betuk['E'] > betuk['D']:
            betuk['E'] - betuk['D']
            print(betuk['E'] - betuk['D'])
        else:
            betuk['D'] > betuk['E']
            betuk['D'] - betuk['E']
            print(betuk['D'] - betuk['E'])

        if betuk['N'] > betuk['K']:
            betuk['N'] - betuk['K']
            print(betuk['N'] - betuk['K'])
        else:
            betuk['K'] > betuk['N']
            betuk['K'] - betuk['N']
            print(betuk['K'] - betuk['N'])
        
        return()