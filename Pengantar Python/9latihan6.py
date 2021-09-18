n = int(input("Banyak bilangan : "))
list = []

print("masukan bilangan dibawah ini: ")

a = int(input())
list.append(a)
max = 0
min = list[0]
sum = list[0]

for i in range(1,n):

    b = int(input())
    list.append(b)
    sum += b

for i in range(0,n):
    if max < list[i]:
        max = list[i]
    
    if min > list[i]:
        min = list[i]

print("max: {}, min: {}, rataan: {}".format(max, min, sum/n))



