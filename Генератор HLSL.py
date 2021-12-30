import math

# Инициализация массива точек
p = [];

p.append ([-300 , -300 , 0, 268 ])
p.append ([450 , -300 , 0, 171 ])
p.append ([-300 , -150 , 0, 118 ])
p.append ([0 , -150 , 0, 131 ])
p.append ([450 , -150 , 0, 642 ])
p.append ([0 , 0 , 0, 121 ])
p.append ([-300 , 150 , 0, 120 ])
p.append ([-300 , 300 , 0, 43 ])
p.append ([0 , 300 , 0, 52 ])

#Создание нерегулярной сетки
n = 7 #Количество узлов на одной оси
size = 900
h = int(size/(n-1))  #Шаг
unreg = [0] * n;
for i in range(0, n):
    unreg[i] = [0] * n
    for j in range(0, n):
        unreg[i][j] = [0] * n
        for k in range(0, n):
            unreg[i][j][k] = [0] * 2

for i in range(0, len(p)):
    unreg[(p[i][0] // h + n // 2)][(p[i][1] // h + n // 2)][(p[i][2] // h + n // 2)][0] = p[i][3]
    unreg[(p[i][0] // h + n // 2)][(p[i][1] // h + n // 2)][(p[i][2] // h + n // 2)][1] = 1

if True:
    #Вывод массива
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                print(int(unreg[j][k][i][0]),end = " ")
            print("")
        print("")
        print("")
        print("")


#Восстановление регулярной сетки
def interpolate():
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if (unreg[i][j][k][1] == 0):

                    #Углы
                    if (i == 0 and j == 0 and k == 0):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/3
                    elif (i == (n - 1) and j == 0 and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/3
                    elif (i == 0 and j == (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k+1][0])/3
                    elif (i == 0 and j == 0 and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/3
                    elif (i == 0 and j == (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k-1][0])/3
                    elif (i == (n - 1) and j == 0 and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/3
                    elif (i == (n - 1) and j == (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k+1][0])/3
                    elif (i == (n - 1) and j == (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k-1][0])/3

                    #Ребра
                    elif (i != 0 and i != (n - 1) and j == 0 and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i != 0 and i != (n - 1) and j == 0 and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/4
                    elif (i != 0 and i != (n - 1) and j == (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i != 0 and i != (n - 1) and j == (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j][k-1][0])/4



                    elif (i == 0 and j != 0 and j != (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i == (n - 1) and j != 0 and j != (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i == 0 and j != 0 and j != (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/4
                    elif (i == (n - 1) and j != 0 and j != (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/4



                    elif (i == 0 and j == 0 and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i == (n - 1) and j == 0 and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i == 0 and j == (n - 1) and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/4
                    elif (i == (n - 1) and j == (n - 1) and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/4

                    #Грани
                    elif (i != 0 and i != (n - 1) and j != 0 and j != (n - 1) and k == 0):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k+1][0])/5
                    elif (i != 0 and i != (n - 1) and j != 0 and j != (n - 1) and k == (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][j][k-1][0])/5
                    elif (i != 0 and i != (n - 1) and j == 0 and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/5
                    elif (i != 0 and i != (n - 1) and j == (n - 1) and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/5
                    elif (i == 0 and j != 0 and j != (n - 1) and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/5
                    elif (i == (n - 1) and j != 0 and j != (n - 1) and k != 0 and k != (n - 1)):
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/5

                    #Внутри куба
                    else:
                        unreg[i][j][k][0] = (unreg[i-1][j][k][0] + unreg[i+1][j][k][0] + unreg[i][j-1][k][0] + unreg[i][j+1][k][0] + unreg[i][k-1][k][0] + unreg[i][j][k+1][0])/6



for i in range(0, 1000):
    interpolate();

if True:
    #Вывод массива
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                print(int(unreg[i][j][k][0]),end = " ")
            print("")
        print("")

print("")

if False:
    #Генератор кода
    print("Код HLSL")
    print("")
    print("float f = 0;")
    for i in range(0, n-1):
        if (i == 0):
            print("if",end = "")
        else:
            print("} else if",end = "")
        print("( (wPos[0] >=", -size/2 + i*h,") && (wPos[0] <",-size/2 + (i + 1)*h ,")){")
        for j in range(0, n-1):
            print("")
            if (j == 0):
                print("    if",end = "")
            else:
                print("    } else if",end = "")
            print("( (wPos[1] >=", -size/2 + j*h,") && (wPos[1] <",-size/2 + (j + 1)*h ,")){")
            for k in range(0, n-1):
                print("")
                if (k == 0):
                    print("        if",end = "")
                else:
                    print("        } else if",end = "")
                print("((wPos[2] >=", -size/2 + k*h,") && (wPos[2] <",-size/2 + (k + 1)*h ,")){")

                print("             f = (",int(unreg[i][j][k][0]),"*(",-size/2 + (i + 1)*h,"- wPos[0])/",h,"*(",-size/2 + (j + 1)*h,"- wPos[1])/",h,"*(",-size/2 + (k + 1)*h,"- wPos[2])/",h,"+")
                print("            ",int(unreg[i+1][j][k][0]),"*(wPos[0] -",-size/2 + i*h,")/",h,"*(",-size/2 + (j + 1)*h,"- wPos[1])/",h,"*(",-size/2 + (k + 1)*h,"- wPos[2])/",h,"+")
                print("            ",int(unreg[i][j+1][k][0]),"*(",-size/2 + (i + 1)*h,"- wPos[0])/",h,"*(wPos[1] -",-size/2 + j*h,")/",h,"*(",-size/2 + (k + 1)*h,"- wPos[2])/",h,"+")
                print("            ",int(unreg[i][j][k+1][0]),"*(",-size/2 + (i + 1)*h,"- wPos[0])/",h,"*(",-size/2 + (j + 1)*h,"- wPos[1])/",h,"*(wPos[2] -",-size/2 + k*h,")/",h,"+")
                print("            ",int(unreg[i+1][j+1][k][0]),"*(wPos[0] -",-size/2 + i*h,")/",h,"*(wPos[1] -",-size/2 + j*h,")/",h,"*(",-size/2 + (k + 1)*h,"- wPos[2])/",h,"+")
                print("            ",int(unreg[i+1][j][k+1][0]),"*(wPos[0] -",-size/2 + i*h,")/",h,"*(",-size/2 + (j + 1)*h,"- wPos[1])/",h,"*(wPos[2] -",-size/2 + k*h,")/",h,"+")
                print("            ",int(unreg[i][j+1][k+1][0]),"*(",-size/2 + (i + 1)*h,"- wPos[0])/",h,"*(wPos[1] -",-size/2 + j*h,")/",h,"*(wPos[2] -",-size/2 + k*h,")/",h,"+")
                print("            ",int(unreg[i+1][j+1][k+1][0]),"*(wPos[0] -",-size/2 + i*h,")/",h,"*(wPos[1] -",-size/2 + j*h,")/",h,"*(wPos[2] -",-size/2 + k*h,")/",h,");")
                            
            print("        }")
        print("    }")
    print("}")
    print("return f;")

