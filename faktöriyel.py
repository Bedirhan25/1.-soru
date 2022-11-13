def faktöriyel(sayi):
    sayix = 1
    while sayi > 0:
        sayix = sayi * sayix
        sayi -= 1
    return sayix

a=int(input("sayi gir"))
print (faktöriyel(a))
