import random

mas = []
mas.append(random.randint(1, 9))

while len(mas) < 4:
    massiv_ichida_bor = random.randint(1, 8)
    if massiv_ichida_bor in mas:
        pass
    else:
        mas.append(massiv_ichida_bor)
print(mas)
for urinishlar_soni in range(10):
    ms=[int(i) for i in input().split()]
    n=0
    k=0
    for xx in range(4):
        if ms[xx]==mas[xx]:
            n+=1
    for xy in range(4):
        if ms[xy] in mas:
            k+=1
    if n==4:
        print(f"siz kiritgan massiv{ms} \ntog'ri massiv {mas}")
    print(n,k-n)
print(f"\ntog'ri massiv {mas}")
