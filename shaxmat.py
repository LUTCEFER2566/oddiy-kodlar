
#print(mass)
# mass=list(map(str,input().split()))
tosh,joy=input().split()
# tosh=mass[0]
# joy=mass[1]
joy=joy.replace('A','1')
joy=joy.replace('B','2')
joy=joy.replace('C','3')
joy=joy.replace('D','4')
joy=joy.replace('E','5')
joy=joy.replace('F','6')
joy=joy.replace('G','7')
joy=joy.replace('H','8') 
farz1=["44","45","54","55"]
farz2=["33","34","35","36","44","46","54","56","63","64","65","66"]

if tosh=="Ruh":
    print(14)
elif tosh=='Shoh':
    shox1=["11", "18", "81", "88"]
    shox2=["12","13","14","15","16","17","21","31","41","51","61","71",
           "82","83","84","85","86","87","28","38","48","58","68","78"]
    if joy in shox1:
        print(3)
    elif joy in shox2:
        print(5)
    else:
        print(8)
elif tosh=='Farzin':
    if joy[0]=='1' or joy[0]=='8' or joy[1]=='1' or joy[1]=='8' :
        print(21)
    elif joy in farz1:
        print(27)
    elif joy in farz2:
        print(25)
    else:
        print(23)
elif tosh=='Fil':
    if joy[0]=='1' or joy[0]=='8'or joy[1]=='1' or joy[1]=='8':
        print(7)
    elif joy in farz1:
        print(13)
    elif joy in farz2:
        print(11)
    else:
        print(9)
elif tosh=='Ot':
    ot1=["11","18","81","88"]
    ot2=['21','12','71','17','82','28','78','87']
    ot3=['13','14','15','16','83','84','85','86','31','41',
         '51','61','38','48','58','68','27','72','22','77']
    ot4=['23','24','25','26','73','74','75','76','32','42','52','62','37','47','57','67']
    if joy in ot1:
        print(2)
    elif joy in ot2:
        print(3)
    elif joy in ot3:
        print(4)
    elif joy in ot4:
        print(6)
    else:
        print(8)
