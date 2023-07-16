# satr = input()
# satr = satr.replace(' ', '')
# print(satr)
# d = len(satr)
# k = int(d ** (0.5))
# print(k, k + 1)
# mass = []
#
# for xx in range(k):
#     mn = []
#
#     for xy in range(xx * (k + 1), (xx + 1) * (k + 1)):
#         try:
#             mn.append(satr[xy])
#         except:
#             break
#     mass.append(mn)
# for aaa in mass:
#     print(aaa)


a = input()
amal = ['+', '-', '*', '/', '=']
mass = []
s = ''
print(a[-1],a[-2],a[-3])
for xx in a:

    if xx not in amal:
        s = s + xx
    else:
        mass.append(s)
        s = ''
k=-1
s=''
mass.append(s)
print(mass)

