# # array65
# mass = [int(i) for i in input().split()]
# k = int(input())
# for xx in range(len(mass)):
#     mass[xx] = mass[xx] + mass[k]
# print(mass)

# # array66
# mass = [int(i) for i in input().split()]
#
# for xx in range(len(mass)):
#     if mass[xx] % 2 == 0:
#         k = mass[xx]
#         break
# for xx in range(len(mass)):
#     if mass[xx] % 2 == 0:
#         mass[xx] = mass[xx] + k
# print(mass)

# # array67
# mass = [int(i) for i in input().split()]
# d = len(mass)
# for xx in range(d, -1, -1):
#     if mass[xx] % 2 == 1:
#         k = mass[xx]
# for xx in range(d):
#     if mass[xx] % 2 == 1:
#         mass[xx] = mass[xx] + k

# # array68
# mass = [int(i) for i in input().split()]
# minc = mass[0]
# maks = mass[0]
# d = len(mass)
# for xx in range(d):
#     if mass[xx] > maks:
#         maks = mass[xx]
#     if mass[xx] < minc:
#         minc = mass[xx]
# kat = mass.index(maks)
# kic = mass.index(minc)
# mass[kat] = minc
# mass[kic] = maks
# print(mass)

# # array69
# mass = [int(i) for i in input().split()]
# d = len(mass)
# for xx in range(0, d - 1, 2):
#     kat = mass[xx]
#     kic = mass[xx + 1]
#     mass[xx] = kic
#     mass[xx + 1] = kat
# print(mass)

# # array70
# mass = [int(i) for i in input().split()]
# d = len(mass) // 2
# for xx in range(d):
#     ks = mass.pop(0)
#     mass.append(ks)
# print(mass)

# # array71
# mass = [int(i) for i in input().split()]
# d = len(mass)
# mas = []
# for xx in range(d - 1, -1, -1):
#     mas.append(mass[xx])
# print(mas)

#array72
#######################################################??????/

#array73,74,75,
# # array76
# mass = [int(i) for i in input().split()]
# lok = []
# for xx in range(1, len(mass) - 1):
#     if mass[xx] > mass[xx - 1] and mass[xx] > mass[xx + 1]:
#         lok.append(xx)
# for yy in lok:
#     mass[yy] = 0
# print(mass)

#array77
# mass = [int(i) for i in input().split()]
# lok = []
# for xx in range(1, len(mass) - 1):
#     if mass[xx] < mass[xx - 1] and mass[xx] < mass[xx + 1]:
#         lok.append(xx)
# for yy in lok:
#     mass[yy] = mas[yy]**2
# print(mass)

# # array78
# mass = [int(i) for i in input().split()]
# for xx in range(len(mass) - 1):
#     mass[xx] = (mass[xx] + mass[xx + 1]) / 2
# print(mass)

# # array79
# mass = [int(i) for i in input().split()]
# mass.insert(0, 0)
# mass.pop(-1)
# print(mass)

# # array80
# mass = [int(i) for i in input().split()]
# mass.pop(0)
# mass.append(0)
# print(mass)

# # array81
# mass = [int(i) for i in input().split()]
# k = int(input())
# for xx in range(k):
#     mass.pop(0)
# for xy in range(k):
#     mass.insert(0, 0)
# print(mass)

#array82
# mass = [int(i) for i in input().split()]
# k = int(input())
# for xx in range(k):
#     mass.pop(-1)
# for xy in range(k):
#     mass.append(0)
# print(mass)

# # array83
# mass = [int(i) for i in input().split()]
# mass.insert(0, mass.pop(-1))
# print(mass)

#array84
# mass = [int(i) for i in input().split()]
# mass.append(mass.pop(0))
# print(mass)

#array85
# mass = [int(i) for i in input().split()]
# k = int(input())
# for xx in range(k):
#     mass.append(mass.pop(0))
# print(mass)
# a1=mass[k:]
# a2=mass[:k]
# mass=a1+a2
#array86

# # array88
# mass = [int(i) for i in input().split()]
# k = mass.pop(-1)
# for xx in range(1, len(mass) - 1):
#     if k > mass[xx] and k <= mass[xx + 1]:
#         mass.insert(xx + 1, k)
#         break
# print(mass)

# # array89
# mass = [int(i) for i in input().split()]
# mass = sorted(mass)
# print(mass)

# # array90
# mass = [int(i) for i in input().split()]
# k = int(input())
# mass.pop(k)
# print(mass)

# # array91
# mass = [int(i) for i in input().split()]
# k, m = map(int, input().split())
# for xx in range(k, m):
#     mass.pop(k)
# print(mass)

# # array92
# mass = [int(i) for i in input().split()]
# kk = []
# for xx in mass:
#     if xx % 2 == 1:
#         kk.append(xx)
# for yy in kk:
#     mass.remove(yy)
# print(mass)

# # array93
# mass = [int(i) for i in input().split()]
# kk = []
# for xx in range(0, len(mass), 2):
#     kk.append(mass[xx])
# for yy in kk:
#     mass.remove(yy)
# print(mass)

#array94
# mass = [int(i) for i in input().split()]
# kk = []
# for xx in range(1, len(mass), 2):
#     kk.append(mass[xx])
# for yy in kk:
#     mass.remove(yy)
# print(mass)



# # array101
# mass = [int(o) for o in input().split()]
# k = int(input())
# for xx in range(len(mass)):
#     if xx == k:
#         mass.insert(k, 0)
# print(mass)

#array102
# mass = [int(o) for o in input().split()]
# k = int(input())
# for xx in range(len(mass)):
#     if xx == k:
#         mass.insert(k+1, 0)
# print(mass)

# # array103
# mass = [int(o) for o in input().split()]
# mn = mass.index(min(mass))
# mass.insert(mn, 0)
# mk = mass.index(max(mass))
# mass.insert(mk + 1, 0)
# print(mass)

# # array104
# mass = [int(i) for i in input().split()]
# k, m = map(int, input().split())
# for xx in range(m):
#     mass.insert(k, 0)
# print(mass)

#array105
# mass = [int(i) for i in input().split()]
# k, m = map(int, input().split())
# for xx in range(m):
#     mass.insert(k+1, 0)
# print(mass)

# # array106
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(0, len(mass), 2):
#     ms.append(mass[xx])
# for xx in ms:
#     mass.append(xx)
# print(mass)

#array107
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(1, len(mass), 2):
#     ms.append(mass[xx])
# for xx in ms:
#     mass.append(xx)
# for xx in ms:
#     mass.append(xx)
# print(mass)

# # array108
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(len(mass)):
#     if mass[xx] > 0:
#         ms.append(xx)
# for xx in ms:
#     mass.insert(xx, 0)
# print(mass)

#array109
# # array108
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(len(mass)):
#     if mass[xx] < 0:
#         ms.append(xx)
# for xx in ms:
#     mass.insert(xx, 0)
# print(mass)

#array110
# # array108
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(len(mass)):
#     if mass[xx] % 2 == 0:
#         ms.append(mass[xx])
# for xx in ms:
#     mass.append(xx)
# print(mass)

#array111

# # array108
# mass = [int(i) for i in input().split()]
# ms = []
# for xx in range(len(mass)):
#     if mass[xx] % 2 == 1:
#         ms.append(mass[xx])
# for xx in ms:
#     mass.append(xx)
# for xx in ms:
#     mass.append(xx)
# print(mass)

# # array112
# mass = [int(i) for i in input().split()]
# for xx in range(len(mass)):
#     for yy in range(len(mass) - 1):
#         if mass[yy] > mass[yy + 1]:
#             a = mass[yy]
#             b = mass[yy + 1]
#             mass[yy] = b
#             mass[yy + 1] = a
# print(mass)

# # array113
# mass = [int(i) for i in input().split()]
# for xx in range(len(mass)):
#     min = mass[xx]
#     for yy in range(xx, len(mass)):
#         if mass[yy] > min:
#             min = mass[yy]

#array114
#array115

#array116
#array95
# mass=[int(i) for i in input().split()]
# a=[]
# b=[]
# for xx in range(len(mass)-1):
#     if mass[xx]==mass[xx+1]:
#         a.append(xx)
# for xx in range(len(mass)):
#     if xx in a:
#         continue
#     else:
#         b.append(mass[xx])
# print(a)
# print(b)

#array96
#array97
#array98
#array99
#ARRAY100