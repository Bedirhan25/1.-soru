def selection(arrr):
    for a in range(len(arrr)):
        min = a
        for b in range(a+1, len(arrr)):
            if arrr[a] > arrr[b]:
                min = b
            else:
                min = a
            if min != a:
                c = arrr[b]
                arrr[b] =arrr[a]
                arrr[a] = c
    print(arrr)

def bubble(arrb):
    for a in range(len(arrb)-1):
        if a == 10:
            break
        if arrb[a] > arrb[a+1]:
            arrb[a+1], arrb[a] = arrb[a],arrb[a+1]

    print(arrb)

def insertion(arrc):
    for a in range(1, len(arrc)):
        b = a-1
        maximum=arrc[a]
        while b >= 0 and maximum < arrc[b]:
            arrc[b+1]=arrc[b]

            b-=1
        arrc[b+1]=maximum
    print(arrc)

i = 0
arr =["", "", "", "", "", "", "", "", "", ""]
arrr =["", "", "", "", "", "", "", "", "", ""]
arrb =["", "", "", "", "", "", "", "", "", ""]
arrc =["", "", "", "", "", "", "", "", "", ""]
while i < 10:
    ar = int(input("{}.sayıyı giriniz".format(i+1)))
    arr[i] = ar
    arrb[i] = ar
    arrr[i] = ar
    arrc[i] = ar
    i += 1

print("default: ",arr)
print("selection :")
selection(arrr)

print("bubble : ")
bubble(arrb)

print("insertion : ")
insertion(arrc)
