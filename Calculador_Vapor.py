import numpy as np
import math
#------------------------Paquetes------------------------------------#
#El proposito de este programa es obtener datos de las tablas de vapor
print("CREADO POR ABRAHAM RODARTE DE LA FUENTE")
print("ESTUDIANTE DE INGENIERÍA QUÍMICA EN LA UNIVERSIDAD DE GUANAJUATO")
print("CON AMOR PARA LA DCNE")
Dato= None
while True:

    print("---------------------------------------Inicio del programa------------------------------------")
    print("Lista de tablas:")
    print("[1] AGUA SATURADA (TABLA DE TEMPERATURAS)")
    print("[2] AGUA SATURADA (TABLA DE PRESIONES)")
    print("[3] VAPOR SOBRECALENTADO")
    print("[4] AGUA LIQUIDA COMPRIMIDA")
    print("[5] HIELO SATURADO VAPOR DE AGUA")
    print("[6] Cerrar el programa")
    print("Solo se pueden ingresar valores como: 1 2 3 4 5")
    DATO = input("¿Qué tipo de tabla desea analizar?:\n")

    #Aqui definiremos las funciones parainterpolar
        #Función para creas vectores de 4 números
    def Vectores(xData,yData,x_int):
        i=0
        Lon = len(xData)
        for x in xData:
            if x_int <= x:
                if i==1 or x <= xData[0]:
                    xint=[xData[0],xData[1],xData[2], xData[3]]
                    yint=[yData[0],yData[1],yData[2], yData[3]]
                    break
                if i==Lon-1:
                    xint=[xData[Lon-4],xData[Lon-3],xData[Lon-2],xData[Lon-1]]
                    yint=[yData[Lon-4],yData[Lon-3],yData[Lon-2], yData[Lon-1]]
                    break
                xint=[xData[i-2], xData[i-1],xData[i], xData[i+1]]
                yint=[yData[i-2], yData[i-1],yData[i], yData[i+1]]
                break
            i=i+1
        if x_int >= xData[-1]:
            xint=[xData[Lon-4],xData[Lon-3],xData[Lon-2],xData[Lon-1]]
            yint=[yData[Lon-4],yData[Lon-3],yData[Lon-2], yData[Lon-1]]
        return xint, yint

        #Interpolación de Newton
    def InterNewton(x,y,xint):
        n = len(x)
        a = np.zeros(n)
        difDiv = np.zeros((n-1,n-1))

        a[0] = y[0]
        #Comienza la tabla de diferencias divididas
        for i in range(0,n-1):
            try:
                difDiv[i,0] = (y[i+1]-y[i])/(x[i+1]-x[i])
            except ZeroDivisionError:
                difDiv[i,0] = (y[i+1]-y[i])/0.000000001
                print("Varios valores en el eje x son iguales")
        for j in range(1,n-1):
            for i in range(0,n-j-1):
                difDiv[i,j] = (difDiv[i+1, j-1]- difDiv[i,j-1])/(x[j+i+1]-x[i])
        for i in range(1, n):
            a[i] = difDiv[0,i-1]
        #Evaluar el Polinomio
        yint = a[0]
        prodx = 1
        for l in range(1,n):
            prodx = prodx*(xint-x[l-1])
            yint = yint + a[l]*prodx
        return yint


    #Una vez identificada la tabla pasamos a interpolar el dato que le demos al programa

    if DATO == "1":
        T_Lista = [0.01,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200,205,210,215,220,225,230,235,240,245,250,255,260,265,270,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,360,365,370,373.95]
        P_Lista = [0.6117,0.8725,1.2281,1.7057,2.3392,3.1698,4.2469,5.6291,7.3851,9.5953,12.352,15.763,19.947,25.043,31.202,38.597,47.416,57.868,70.183,84.609,101.42,120.9,143.38,169.18,198.67,232.23,270.28,313.22,361.53,415.68,476.16,543.49,618.23,700.93,792.18,892.6,1002.8,1123.5,1255.2,1398.8,1554.9,1724.3,1907.7,2105.9,2319.6,2549.7,2797.1,3062.6,3347,3651.2,3976.2,4322.9,4692.3,5085.3,5503,5946.4,6416.6,6914.6,7441.8,7999,8587.9,9209.4,9865,10556,11284,12051,12858,13707,14601,15541,16529,17570,18666,19822,21044,22064]
        VE_LS_Lista = [0.001,0.0010001,0.0010002,0.001001,0.001002,0.001003,0.001004,0.001006,0.001008,0.00101,0.001012,0.001015,0.001017,0.00102,0.001023,0.001026,0.001029,0.001032,0.001036,0.00104,0.001043,0.001047,0.001052,0.001056,0.00106,0.001065,0.00107,0.001075,0.00108,0.001085,0.001091,0.001096,0.001102,0.001108,0.001114,0.001121,0.001127,0.001134,0.001141,0.001149,0.001157,0.001164,0.001173,0.001181,0.00119,0.001199,0.001209,0.001219,0.001229,0.00124,0.001252,0.001263,0.001276,0.001289,0.001303,0.001317,0.001333,0.001349,0.001366,0.001384,0.001404,0.001425,0.001447,0.001472,0.001499,0.001528,0.00156,0.001597,0.001638,0.001685,0.001741,0.001808,0.001895,0.002015,0.002217,0.003106]
        VE_VS_Lista = [206,147.03,106.32,77.885,57.762,43.34,32.879,25.205,19.515,15.251,12.026,9.5639,7.667,6.1935,5.0396,4.1291,3.4053,2.8261,2.3593,1.9808,1.672,1.4186,1.2094,1.036,0.89133,0.77012,0.66808,0.58179,0.5085,0.446,0.39248,0.34648,0.3068,0.27244,0.2426,0.21659,0.19384,0.1739,0.15636,0.14089,0.12721,0.11508,0.10429,0.09468,0.086094,0.078405,0.071505,0.0653,0.059707,0.054656,0.050085,0.045941,0.042175,0.038748,0.035622,0.032767,0.030153,0.027756,0.025554,0.023528,0.021659,0.019932,0.018333,0.016849,0.01547,0.014183,0.012979,0.011848,0.010783,0.009772,0.008806,0.007872,0.00695,0.006009,0.004953,0.003106]
        EI_LS_Lista = [0,21.019,42.02,62.98,83.913,104.83,125.73,146.63,167.53,188.43,209.33,230.24,251.16,272.09,293.04,313.99,334.97,355.96,376.97,398,419.06,440.15,461.27,482.42,503.6,524.83,546.1,567.41,588.77,610.19,631.66,653.19,674.79,696.46,718.2,740.02,761.92,783.91,806,828.18,850.46,872.86,895.38,918.02,940.79,963.7,986.76,1010,1033.4,1056.9,1080.7,1104.7,1128.8,1153.3,1177.9,1202.9,1228.8,1253.7,1279.7,1306,1332.7,1360,1387.7,1416.1,1445.1,1475,1505.7,1537.5,1570.7,1605.5,1642.4,1682.2,1726.2,1777.2,1844.5,2015.7]
        EI_EVAP_Lista = [2374.9,2360.8,2346.6,2332.5,2318.4,2304.3,2290.2,2276,2261.9,2247.7,2233.4,2219.1,2204.7,2190.3,2175.8,2161.3,2146.6,2131.9,2117,2102,2087,2071.8,2056.4,2040.9,2025.3,2009.5,1993.4,1977.3,1960.9,1944.2,1927.4,1910.3,1893,1875.4,1857.5,1839.4,1820.9,1802.1,1783,1763.6,1743.7,1723.5,1702.9,1681.9,1660.5,1638.6,1616.1,1593.2,1569.8,1545.7,1521.1,1495.8,1469.9,1443.2,1415.7,1387.4,1358.2,1328.1,1296.9,1264.5,1230.9,1195.9,1159.3,1121.1,1080.9,1038.5,993.5,945.5,893.8,837.3,775.9,706.4,625.7,526.4,385.6,0]
        EI_VS_Lista = [2374.9,2381.8,2388.7,2395.5,2402.3,2409.1,2415.9,2422.7,2429.4,2436.1,2442.7,2449.3,2455.9,2462.4,2468.9,2475.3,2481.6,2487.8,2494,2500.1,2506,2511.9,2517.7,2523.3,2528.9,2534.3,2539.5,2544.7,2549.6,2554.4,2559.1,2563.5,2567.8,2571.9,2575.7,2579.4,2582.8,2586,2589,2591.7,2594.2,2596.4,2598.3,2599.9,2601.3,2602.3,2602.9,2603.2,2603.1,2602.7,2601.8,2600.5,2598.7,2596.5,2593.7,2590.3,2586.4,2581.8,2576.5,2570.5,2563.6,2555.8,2547.1,2537.2,2526,2513.4,2499.2,2483,2464.5,2443.2,2418.3,2388.6,2351.9,2303.6,2230.1,2015.7]
        EA_LS_Lista = [0.001,21.02,42.022,62.982,83.915,104.83,125.74,146.64,167.53,188.44,209.34,230.26,251.18,272.12,293.07,314.03,335.02,356.02,377.04,398.09,419.17,440.28,461.42,482.59,503.81,525.07,546.38,567.75,589.16,610.64,632.18,653.79,675.47,697.24,719.08,741.02,763.05,785.19,807.43,829.78,852.26,874.87,897.61,920.5,943.55,966.76,990.14,1013.7,1037.5,1061.5,1085.7,1110.1,1134.8,1159.8,1185.1,1210.7,1236.7,1263.1,1289.8,1317.1,1344.8,1373.1,1402,1431.6,1462,1493.4,1525.8,1559.4,1594.6,1631.7,1671.2,1714,1761.5,1817.2,1891.2,2084.3]
        EA_EVAP_Lista = [2500.9,2489.1,2477.2,2465.4,2453.5,2441.7,2429.8,2417.9,2406,2394,2382,2369.8,2357.7,2345.4,2333,2320.6,2308,2295.3,2282.5,2269.6,2256.4,2243.1,2229.7,2216,2202.1,2188.1,2173.7,2159.1,2144.3,2129.2,2113.8,2098,2082,2065.6,2048.8,2031.7,2014.2,1996.2,1977.9,1959,1939.8,1920,1899.7,1878.8,1857.4,1835.4,1812.8,1789.5,1765.5,1740.8,1715.3,1689,1661.8,1633.7,1604.6,1574.5,1543.2,1510.7,1476.9,1441.6,1404.8,1366.3,1325.9,1283.4,1238.5,1191,1140.3,1086,1027.4,963.4,892.7,812.9,720.1,605.5,443.1,0]
        EA_VS_Lista = [2500.9,2510.1,2519.2,2528.3,2537.4,2546.5,2555.6,2564.6,2573.5,2582.4,2591.3,2600.1,2608.8,2617.5,2626.1,2634.6,2643,2651.4,2659.6,2667.6,2675.6,2683.4,2691.1,2698.6,2706,2713.1,2720.1,2726.9,2733.5,2739.8,2745.9,2751.8,2757.5,2762.8,2767.9,2772.7,2777.2,2781.4,2785.3,2788.8,2792,2794.8,2797.3,2799.3,2801,2802.2,2802.9,2803.2,2803,2802.2,2801,2799.1,2796.6,2793.5,2789.7,2785.2,2779.9,2773.7,2766.7,2758.7,2749.6,2739.4,2727.9,2715,2700.6,2684.3,2666,2645.4,2622,2595.1,2563.9,2526.9,2481.6,2422.7,2334.3,2084.3]
        ER_LS_Lista = [0,0.0763,0.1511,0.2245,0.2965,0.3672,0.4368,0.5051,0.5724,0.6386,0.7038,0.768,0.8313,0.8937,0.9551,1.0158,1.0756,1.1346,1.1929,1.2504,1.3072,1.3634,1.4188,1.4737,1.5279,1.5816,1.6346,1.6872,1.7392,1.7908,1.8418,1.8924,1.9426,1.9923,2.0417,2.0906,2.1392,2.1875,2.2355,2.2831,2.3305,2.3776,2.4245,2.4712,2.5176,2.5639,2.61,2.656,2.7018,2.7476,2.7933,2.839,2.8847,2.9304,2.9762,3.0221,3.0681,3.1144,3.1608,3.2076,3.2548,3.3024,3.3506,3.3994,3.4491,3.4998,3.5516,3.605,3.6602,3.7179,3.7788,3.8442,3.9165,4.0004,4.1119,4.407]
        ER_EVAP_Lista = [9.1556,8.9487,8.7488,8.5559,8.3696,8.1895,8.0152,7.8466,7.6832,7.5247,7.371,7.2218,7.0769,6.936,6.7989,6.6655,6.5355,6.4089,6.2853,6.1647,6.047,5.9319,5.8193,5.7092,5.6013,5.4956,5.3919,5.2901,5.1901,5.0919,4.9953,4.9002,4.8066,4.7143,4.6233,4.5335,4.4448,4.3572,4.2705,4.1847,4.0997,4.0154,3.9318,3.8489,3.7664,3.6844,3.6028,3.5216,3.4405,3.3596,3.2788,3.1979,3.1169,3.0358,2.9542,2.8723,2.7898,2.7066,2.6225,2.5374,2.4511,2.3633,2.2737,2.1821,2.0881,1.9911,1.8906,1.7857,1.6756,1.5585,1.4326,1.2942,1.1373,0.9489,0.689,0] 
        ER_VS_Lista = [9.1556,9.0249,8.8999,8.7803,8.6661,8.5567,8.452,8.3517,8.2556,8.1633,8.0748,7.9898,7.9082,7.8296,7.754,7.6812,7.6111,7.5435,7.4782,7.4151,7.3542,7.2952,7.2382,7.1829,7.1292,7.0771,7.0265,6.9773,6.9294,6.8827,6.8371,6.7927,6.7492,6.7067,6.665,6.6242,6.5841,6.5447,6.5059,6.4678,6.4302,6.393,6.3563,6.32,6.284,6.2483,6.2128,6.1775,6.1424,6.1072,6.0721,6.0369,6.0017,5.9662,5.9305,5.8944,5.8579,5.821,5.7834,5.745,5.7059,5.6657,5.6243,5.5816,5.5372,5.4908,5.4422,5.3907,5.3358,5.2765,5.2114,5.1384,5.0537,4.9493,4.8009,4.407]
        print("Lista de variables:")
        print("[1] TEMPERATURA [°C] ")
        print("[2] PRESION DE SATURACIÓN [kPa]")
        print("[3] VOLUMEN ESPECIFICO LIQUIDO SATURADO [m3/kg]")
        print("[4] VOLUMEN ESPECIFICO VAPOR SATURADO [m3/kg]")
        print("[5] ENERGIA INTERNA LIQUIDO SATURADO [kJ/kg]")
        print("[6] ENERGIA INTERNA EVAPORACION [kJ/kg]")
        print("[7] ENTALPIA LIQUIDO SATURADO[kJ/kg]")
        print("[8] ENTALPIA EVAPORACION [kJ/kg]")
        print("[9] ENTROPIA LIQUIDO SATURADO [kJ/kg*K]")
        print("[10] ENTROPIA EVAPORACION [kJ/kg*K]")
        print("[11] ENTROPIA VAPOR SATURADO [kJ/kg*K]")

        xData_Nombre = None
        while True:
            xData_Nombre = input("¿Qué variable conoce?:\n") #Esto es para definir cual sera nuestro eje x en la interpolación
            if xData_Nombre == "1":
                X = T_Lista
                u = "°C"
                LI =0.01
                LS = 373.95
                break
            elif xData_Nombre == "2":
                X = P_Lista
                u = "kPa"
                LI =0.6117
                LS =22064
                break
            elif xData_Nombre == "3":
                X = VE_LS_Lista
                u = "m3/kg"
                LI = 0.001
                LS = 0.003106
                break
            elif xData_Nombre == "4":
                X = VE_VS_Lista
                u = "m3/kg"
                LI = 0.003106
                LS =206
                break
            elif xData_Nombre == "5" :
                X = EI_LS_Lista
                u = "kJ/kg"
                LI = 0
                LS = 2015.7
                break
            elif xData_Nombre == "6" :
                X = EI_EVAP_Lista
                u = "kJ/kg"
                LI = 0
                LS = 2374.9
                break
            
            elif xData_Nombre =="7":
                X = EA_LS_Lista
                u = "kJ/kg"
                LI =0.001
                LS =2084.3
                break
            
            elif xData_Nombre == "8" :
                X = EA_EVAP_Lista
                u = "kJ/kg"
                LI =0
                LS =2500.9
                break
            elif xData_Nombre == "9":
                X = ER_LS_Lista
                u = "kJ/kg*K"
                LI =0
                LS =4.4071
                break
            elif xData_Nombre == "10" :
                X = ER_EVAP_Lista
                u = "kJ/kg*K"
                LI = 0
                LS = 9.1556
                break
            elif xData_Nombre == "11":
                X = ER_VS_Lista
                u = "kJ/kg*K"
                LI = 4.4070
                LS =9.1556
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo.Solo se aceptan valores como: 1 2 3 4 5")
        
        x_int: None
        while True:
            try: 
                x_int = float(input("¿Cual es su valor en "+ u +"?:\n"))
                break
            except ValueError:
                print("El valor no es aceptable")
            
        print("ALERTAS:")
        if x_int < LI:
            print("El valor esta fuera de los limites de las tablas")
        elif x_int > LS:
            print("El valor esta fuera de los limites de las tablas")
        else:
            print("Ninguna")
        if xData_Nombre == "4":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="6":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="8":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="10":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="11":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]      
        else:
            xVector, Falso = Vectores(X,X, x_int)
        i = 0
        for x in X:
            if x == xVector[0]:
                x1 = i
            if x == xVector[1]:
                x2 = i
            if x == xVector[2]:
                x3 = i
            if x == xVector[3]:
                x4 = i
            i = i+1
            
                


        print("Lista de variables:")
        print("[1] TEMPERATURA [°C] ")
        print("[2] PRESION DE SATURACIÓN [kPa]")
        print("[3] VOLUMEN ESPECIFICO LIQUIDO SATURADO [m3/kg]")
        print("[4] VOLUMEN ESPECIFICO VAPOR SATURADO [m3/kg]")
        print("[5] ENERGIA INTERNA LIQUIDO SATURADO [kJ/kg]")
        print("[6] ENERGIA INTERNA EVAPORACION [kJ/kg]")
        print("[7] ENERGIA INTERNA VAPOR SATURADO [kJ/kg]")
        print("[8] ENTALPIA LIQUIDO SATURADO[kJ/kg]")
        print("[9] ENTALPIA EVAPORACION [kJ/kg]")
        print("[10] ENTALPIA VAPOR SATURADO [kJ/kg]")
        print("[11] ENTROPIA LIQUIDO SATURADO [kJ/kg*K]")
        print("[12] ENTROPIA EVAPORACION [kJ/kg*K]")
        print("[13] ENTROPIA VAPOR SATURADO [kJ/kg*K]")
        yData_Nombre = None
        while True:
            yData_Nombre = input("¿Qué variable quiere conocer?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
            if yData_Nombre == "1":
                Y = T_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.2f}".format(R)
                u = "°C"
                break
            elif yData_Nombre == "2":
                Y = P_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kPa"
                break
            elif yData_Nombre == "3":
                Y = VE_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.6f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "4":
                Y = VE_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)            
                Resultado = "{:.6f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "5" :
                Y = EI_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)           
                Resultado = "{:.3f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "6" :
                Y = EI_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "7" :
                Y = EI_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre =="8":
                Y = EA_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.2f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "9" :
                Y = EA_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "10" :
                Y = EA_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "11":
                Y = ER_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "12" :
                Y = ER_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "13":
                Y = ER_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4 5")

        print("El resultado es " + Resultado + " " + u)

    if DATO == "2":
        T_Lista = [6.97,13.02,17.5,21.08,24.08,28.96,32.87,40.29,45.81,53.97,60.06,64.96,69.09,75.86,81.32,91.76,99.61,99.97,105.97,111.35,116.04,120.21,123.97,127.41,130.58,133.52,136.27,138.86,141.3,143.61,147.9,151.83,155.46,158.83,161.98,164.95,167.75,170.41,172.94,175.35,177.66,179.88,184.06,187.96,191.6,195.04,198.29,205.72,212.38,218.41,223.95,233.85,242.56,250.35,263.94,275.59,285.83,295.01,303.35,311,318.08,324.68,330.85,336.67,342.16,347.36,352.29,356.99,361.47,365.75,369.83,373.71,373.95]
        P_Lista = [1,1.5 ,2.0 ,2.5 ,3.0 ,4.0 ,5.0 ,7.5 ,10 ,15 ,20 ,25 ,30 ,40 ,50 ,75 ,100 ,101.325 ,125 ,150 ,175 ,200 ,225 ,250 ,275 ,300 ,325 ,350 ,375 ,400 ,450 ,500 ,550 ,600 ,650 ,700 ,750 ,800 ,850 ,900 ,950 ,1000 ,1100 ,1200 ,1300 ,1400 ,1500 ,1750 ,2000 ,2250 ,2500 ,3000 ,3500 ,4000 ,5000 ,6000 ,7000 ,8000 ,9000 ,10000 ,11000 ,12000 ,13000 ,14000 ,15000 ,16000 ,17000 ,18000 ,19000 ,20000 ,21000 ,22000 ,22064 ]
        VE_LS_Lista = [0.001,0.001001,0.001001,0.001002,0.001003,0.001004,0.001005,0.001008,0.00101,0.001014,0.001017,0.00102,0.001022,0.001026,0.00103,0.001037,0.001043,0.001043,0.001048,0.001053,0.001057,0.001061,0.001064,0.001067,0.00107,0.001073,0.001076,0.001079,0.001081,0.001084,0.001088,0.001093,0.001097,0.001101,0.001104,0.001108,0.001111,0.001115,0.001118,0.001121,0.001124,0.001127,0.001133,0.001138,0.001144,0.001149,0.001154,0.001166,0.001177,0.001187,0.001197,0.001217,0.001235,0.001252,0.001286,0.001319,0.001352,0.001384,0.001418,0.001452,0.001488,0.001526,0.001566,0.00161,0.001657,0.00171,0.00177,0.00184,0.001926,0.002038,0.002207,0.002703,0.003106]
        VE_VS_Lista = [129.9,87.964,66.99,54.242,45.654,34.791,28.185,19.233,14.67,10.02,7.6481,6.2034,5.2287,3.9933,3.2403,2.2172,1.6941,1.6734,1.375,1.1594,1.0037,0.88578,0.79329,0.71873,0.65732,0.60582,0.56199,0.52422,0.49133,0.46242,0.41392,0.37483,0.34261,0.3156,0.2926,0.27278,0.25552,0.24035,0.2269,0.21489,0.20411,0.19436,0.17745,0.16326,0.15119,0.14078,0.13171,0.11344,0.099587,0.088717,0.079952,0.066667,0.057061,0.049779,0.039448,0.032449,0.027378,0.023525,0.020489,0.018028,0.015988,0.014264,0.012781,0.011487,0.010341,0.009312,0.008374,0.007504,0.006677,0.005862,0.004994,0.003644,0.003106]
        EI_LS_Lista = [29.302,54.686 ,73.431 ,88.422 ,100.98 ,121.39 ,137.75 ,168.74 ,191.79 ,225.93 ,251.40 ,271.93 ,289.24 ,317.58 ,340.49 ,384.36 ,417.40 ,418.95 ,444.23 ,466.97 ,486.82 ,504.50 ,520.47 ,535.08 ,548.57 ,561.11 ,572.84 ,583.89 ,594.32 ,604.22 ,622.65 ,639.54 ,655.16 ,669.72 ,683.37 ,696.23 ,708.4,719.97 ,731,741.55,751.67,761.39,779.78,796.96,813.1,828.35,842.82,876.12,906.12,933.54,958.87,1004.6,1045.4,1082.4,1148.1,1205.8,1258,1306,1350.9,1393.3,1433.9,1473,1511,1548.4,1585.5,1622.6,1660.2,1699.1,1740.3,1785.8,1841.6,1951.7,2015.7]
        EI_EVAP_Lista = [2355.2,2338.1 ,2325.5 ,2315.4 ,2306.9 ,2293.1 ,2282.1 ,2261.1 ,2245.4 ,2222.1 ,2204.6 ,2190.4 ,2178.5 ,2158.8 ,2142.7 ,2111.8 ,2088.2 ,2087.0 ,2068.8 ,2052.3 ,2037.7 ,2024.6 ,2012.7 ,2001.8 ,1991.6 ,1982.1 ,1973.1 ,1964.6 ,1956.6 ,1948.9 ,1934.5 ,1921.2 ,1908.8 ,1897.1 ,1886.1 ,1875.6 ,1865.6 ,1856.1 ,1846.9 ,1838.1 ,1829.6 ,1821.4 ,1805.7 ,1790.9 ,1776.8 ,1763.4 ,1750.6 ,1720.6 ,1693.0 ,1667.3 ,1643.2 ,1598.5 ,1557.6 ,1519.3 ,1448.9 ,1384.1 ,1323.0 ,1264.5 ,1207.6 ,1151.8 ,1096.6 ,1041.3 ,985.5 ,928.7 ,870.3 ,809.4 ,745.1 ,675.9 ,598.9 ,509.0 ,391.9 ,140.8 ,0 ]
        EI_VS_Lista = [2384.5,2392.8 ,2398.9 ,2403.8 ,2407.9 ,2414.5 ,2419.8 ,2429.8 ,2437.2 ,2448.0 ,2456.0 ,2462.4 ,2467.7 ,2476.3 ,2483.2 ,2496.1 ,2505.6 ,2506.0 ,2513.0 ,2519.2 ,2524.5 ,2529.1 ,2533.2 ,2536.8 ,2540.1 ,2543.2 ,2545.9 ,2548.5 ,2550.9 ,2553.1 ,2557.1 ,2560.7 ,2563.9 ,2566.8 ,2569.4 ,2571.8 ,2574.0 ,2576,2577.9,2579.6,2581.3,2582.8,2585.5,2587.8,2589.9,2591.8,2593.4,2596.7,2599.1,2600.9,2602.1,2603.2,2603,2601.7,2597,2589.9,2581,2570.5,2558.5,2545.2,2530.4,2514.3,2496.6,2477.1,2455.7,2432,2405.4,2375,2339.2,2294.8,2233.5,2092.4,2015.7]
        EA_LS_Lista = [29.303,54.688 ,73.433 ,88.424 ,100.98 ,121.39 ,137.75 ,168.75 ,191.81 ,225.94 ,251.42 ,271.96 ,289.27 ,317.62 ,340.54 ,384.44 ,417.51 ,419.06 ,444.36 ,467.13 ,487.01 ,504.71 ,520.71 ,535.35 ,548.86 ,561.43 ,573.19 ,584.26 ,594.73 ,604.66 ,623.14 ,640.09 ,655.77 ,670.38 ,684.08 ,697.00 ,709.24 ,720.87,731.95,742.56,752.74,762.51,781.03,798.33,814.59,829.96,844.55,878.16,908.47,936.21,961.87,1008.3,1049.7,1087.4,1154.5,1213.8,1267.5,1317.1,1363.7,1407.8,1450.2,1491.3,1531.4,1571,1610.3,1649.9,1690.3,1732.2,1776.8,1826.6,1888,2011.1,2084.3]
        EA_EVAP_Lista = [2484.4,2470.1 ,2459.5 ,2451.0 ,2443.9 ,2432.3 ,2423.0 ,2405.3 ,2392.1 ,2372.3 ,2357.5 ,2345.5 ,2335.3 ,2318.4 ,2304.7 ,2278.0 ,2257.5 ,2256.5 ,2240.6 ,2226.0 ,2213.1 ,2201.6 ,2191.0 ,2181.2 ,2172.0 ,2163.5 ,2155.4 ,2147.7 ,2140.4 ,2133.4 ,2120.3 ,2108.0 ,2096.6 ,2085.8 ,2075.5 ,2065.8 ,2056.4 ,2047.5,2038.8,2030.5,2022.4,2014.6,1999.6,1985.4,1971.9,1958.9,1946.4,1917.1,1889.8,1864.3,1840.1,1794.9,1753,1713.5,1639.7,1570.9,1505.2,1441.6,1379.3,1317.6,1256.1,1194.1,1131.3,1067,1000.5,931.1,857.4,777.8,689.2,585.5,450.4,161.5,0]
        EA_VS_Lista = [2513.7,2524.7 ,2532.9 ,2539.4 ,2544.8 ,2553.7 ,2560.7 ,2574.0 ,2583.9 ,2598.3 ,2608.9 ,2617.5 ,2624.6 ,2636.1 ,2645.2 ,2662.4 ,2675.0 ,2675.6 ,2684.9 ,2693.1 ,2700.2 ,2706.3 ,2711.7 ,2716.5 ,2720.9 ,2724.9 ,2728.6 ,2732.0 ,2735.1 ,2738.1 ,2743.4 ,2748.1 ,2752.4 ,2756.2 ,2759.6 ,2762.8 ,2765.7 ,2768.3,2770.8,2773,2775.2,2777.1,2780.7,2783.8,2786.5,2788.9,2791,2795.2,2798.3,2800.5,2801.9,2803.2,2802.7,2800.8,2794.2,2784.6,2772.6,2758.7,2742.9,2725.5,2706.3,2685.4,2662.7,2637.9,2610.8,2581,2547.7,2510,2466,2412.1,2338.4,2172.6,2084.3]
        ER_LS_Lista = [0.1059,0.1956 ,0.2606 ,0.3118 ,0.3543 ,0.4224 ,0.4762 ,0.5763 ,0.6492 ,0.7549 ,0.8320 ,0.8932 ,0.9441 ,1.0261 ,1.0912 ,1.2132 ,1.3028 ,1.3069 ,1.3741 ,1.4337 ,1.4850 ,1.5302 ,1.5706 ,1.6072 ,1.6408 ,1.6717 ,1.7005 ,1.7274 ,1.7526 ,1.7765 ,1.8205 ,1.8604 ,1.8970 ,1.9308 ,1.9623 ,1.9918 ,2.0195 ,2.0457,2.0705,2.0941,2.1166,2.1381,2.1785,2.2159,2.2508,2.2835,2.3143,2.3844,2.4467,2.5029,2.5542,2.6454,2.7253,2.7966,2.9207,3.0275,3.122,3.2077,3.2866,3.3603,3.4299,3.4964,3.5606,3.6232,3.6848,3.7461,3.8082,3.872,3.9396,4.0146,4.1071,4.2942,4.407]
        ER_EVAP_Lista = [8.869,8.6314 ,8.4621 ,8.3302 ,8.2222 ,8.0510 ,7.9176 ,7.6738 ,7.4996 ,7.2522 ,7.0752 ,6.9370 ,6.8234 ,6.6430 ,6.5019 ,6.2426 ,6.0562 ,6.0476 ,5.9100 ,5.7894 ,5.6865 ,5.5968 ,5.5171 ,5.4453 ,5.3800 ,5.3200 ,5.2645 ,5.2128 ,5.1645 ,5.1191 ,5.0356 ,4.9603 ,4.8916 ,4.8285 ,4.7699 ,4.7153 ,4.6642 ,4.616,4.5705 ,4.5273 ,4.4862 ,4.4470 ,4.3735 ,4.3058 ,4.2428 ,4.1840 ,4.1287 ,4.0033 ,3.8923 ,3.7926 ,3.7016 ,3.5402 ,3.3991 ,3.2731 ,3.0530 ,2.8627 ,2.6927 ,2.5373 ,2.3925 ,2.2556 ,2.1245 ,1.9975 ,1.8730 ,1.7497 ,1.6261 ,1.5005 ,1.3709 ,1.2343 ,1.0860 ,0.9164 ,0.7005 ,0.2496 ,0 ] 
        ER_VS_Lista = [8.9749,8.8270 ,8.7227 ,8.6421 ,8.5765 ,8.4734 ,8.3938 ,8.2501 ,8.1488 ,8.0071 ,7.9073 ,7.8302 ,7.7675 ,7.6691 ,7.5931 ,7.4558 ,7.3589 ,7.3545 ,7.2841 ,7.2231 ,7.1716 ,7.1270 ,7.0877 ,7.0525 ,7.0207 ,6.9917 ,6.9650 ,6.9402 ,6.9171 ,6.8955 ,6.8561 ,6.8207 ,6.7886 ,6.7593 ,6.7322 ,6.7071 ,6.6837 ,6.6616,6.6409 ,6.6213 ,6.6027 ,6.5850 ,6.5520 ,6.5217 ,6.4936 ,6.4675 ,6.4430 ,6.3877 ,6.3390 ,6.2954 ,6.2558 ,6.1856 ,6.1244 ,6.0696 ,5.9737 ,5.8902 ,5.8148 ,5.745,5.6791,5.6159 ,5.5544 ,5.4939 ,5.4336 ,5.3728 ,5.3108 ,5.2466 ,5.1791 ,5.1064 ,5.0256 ,4.9310 ,4.8076 ,4.5439 ,4.4070 ]
        print("Lista de variables:")
        print("[1] TEMPERATURA DE SATURACION [°C] ")
        print("[2] PRESION [kPa]")
        print("[3] VOLUMEN ESPECIFICO LIQUIDO SATURADO [m3/kg]")
        print("[4] VOLUMEN ESPECIFICO VAPOR SATURADO [m3/kg]")
        print("[5] ENERGIA INTERNA LIQUIDO SATURADO [kJ/kg]")
        print("[6] ENERGIA INTERNA EVAPORACION [kJ/kg]")
        print("[7] ENTALPIA LIQUIDO SATURADO[kJ/kg]")
        print("[8] ENTALPIA EVAPORACION [kJ/kg]")
        print("[9] ENTROPIA LIQUIDO SATURADO [kJ/kg*K]")
        print("[10] ENTROPIA EVAPORACION [kJ/kg*K]")
        print("[11] ENTROPIA VAPOR SATURADO [kJ/kg*K]")

        xData_Nombre = None
        while True:
            xData_Nombre = input("¿Qué variable conoce?:\n") #Esto es para definir cual sera nuestro eje x en la interpolación
            if xData_Nombre == "1":
                X = T_Lista
                u = "°C"
                LI =6.97
                LS = 373.95
                break
            elif xData_Nombre == "2":
                X = P_Lista
                u = "kPa"
                LI = 1.0
                LS = 22064
                break
            elif xData_Nombre == "3":
                X = VE_LS_Lista
                u = "m3/kg"
                LI = 0.001
                LS = 0.003106
                break
            elif xData_Nombre == "4":
                X = VE_VS_Lista
                u = "m3/kg"
                LI =0.003106
                LS =129.19
                break
            elif xData_Nombre == "5" :
                X = EI_LS_Lista
                u = "kJ/kg"
                LI = 29.302
                LS = 2015.7
                break
            elif xData_Nombre == "6" :
                X = EI_EVAP_Lista
                u = "kJ/kg"
                LI = 0
                LS = 2355.2
                break
            
            elif xData_Nombre =="7":
                X = EA_LS_Lista
                u = "kJ/kg"
                LI = 29.303
                LS = 2084.3
                break
            elif xData_Nombre == "8" :
                X = EA_EVAP_Lista
                u = "kJ/kg"
                LI = 0
                LS =2484.4
                break
            elif xData_Nombre == "9":
                X = ER_LS_Lista
                u = "kJ/kg*K"
                LI = 0.1059
                LS = 4.407
                break
            elif xData_Nombre == "10" :
                X = ER_EVAP_Lista
                u = "kJ/kg*K"
                LI = 0
                LS = 8.869
                break
            elif xData_Nombre == "11":
                X = ER_VS_Lista
                u = "kJ/kg*K"
                LI = 4.407
                LS = 8.9749
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo.Solo se aceptan valores como: 1 2 3 4 5")
        
        x_int: None
        while True:
            try: 
                x_int = float(input("¿Cual es su valor en "+ u +"?:\n"))
                break
            except ValueError:
                print("El valor no es aceptable")
            
        print("ALERTAS:")
        if x_int < LI:
            print("El valor esta fuera de los limites de las tablas")
        elif x_int > LS:
            print("El valor esta fuera de los limites de las tablas")
        else:
            print("Ninguna")

        if xData_Nombre == "4":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="6":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="8":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="10":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="11":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]       
        else:
            xVector, Falso = Vectores(X,X, x_int)
        i = 0
        for x in X:
            if x == xVector[0]:
                x1 = i
            if x == xVector[1]:
                x2 = i
            if x == xVector[2]:
                x3 = i
            if x == xVector[3]:
                x4 = i
            i = i+1

        print("Lista de variables:")
        print("[1] TEMPERATURA DE SATURACION [°C] ")
        print("[2] PRESION [kPa]")
        print("[3] VOLUMEN ESPECIFICO LIQUIDO SATURADO [m3/kg]")
        print("[4] VOLUMEN ESPECIFICO VAPOR SATURADO [m3/kg]")
        print("[5] ENERGIA INTERNA LIQUIDO SATURADO [kJ/kg]")
        print("[6] ENERGIA INTERNA EVAPORACION [kJ/kg]")
        print("[7] ENERGIA INTERNA VAPOR SATURADO [kJ/kg]")
        print("[8] ENTALPIA LIQUIDO SATURADO[kJ/kg]")
        print("[9] ENTALPIA EVAPORACION [kJ/kg]")
        print("[10] ENTALPIA VAPOR SATURADO [kJ/kg]")
        print("[11] ENTROPIA LIQUIDO SATURADO [kJ/kg*K]")
        print("[12] ENTROPIA EVAPORACION [kJ/kg*K]")
        print("[13] ENTROPIA VAPOR SATURADO [kJ/kg*K]")
        
        yData_Nombre = None
        while True:
            yData_Nombre = input("¿Qué variable quiere conocer?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
            if yData_Nombre == "1":
                Y = T_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y       
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int) 
                Resultado = "{:.2f}".format(R)
                u = "°C"
                break
            elif yData_Nombre == "2":
                Y = P_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kPa"
                break
            elif yData_Nombre == "3":
                Y = VE_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.6f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "4":
                Y = VE_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)               
                Resultado = "{:.6f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "5" :
                Y = EI_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)             
                Resultado = "{:.3f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "6" :
                Y = EI_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "7" :
                Y = EI_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre =="8":
                Y = EA_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.2f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "9" :
                Y = EA_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "10" :
                Y = EA_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "11":
                Y = ER_LS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "12" :
                Y = ER_EVAP_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "13":
                Y = ER_VS_Lista
                if xData_Nombre == "4":
                    Y = Y[::-1]
                elif xData_Nombre == "6":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4 5")

        print("El resultado es " + Resultado + " " + u)

    elif DATO == "5":
        T_Lista = [0,0.1,-2,-4,-6,-8,-10,-12,-14,-16,-18,-20,-22,-24,-26,-28,-30,-32,-34,-36,-38,-40]
        P_Lista = [0.61169, 0.61115,0.51772,0.43748,0.36873,0.30998,0.2599,0.21732,0.18121,0.15068,0.12492,0.10326,0.0851,0.06991,0.05725,0.04673,0.03802,0.03082,0.0249,0.02004,0.01608,0.01285]
        VE_LS_Lista = [0.001091,0.0010911,0.0010912,0.00109,0.0010901,0.0010902,0.00108901,0.00108902,0.001088,0.00108801,0.00108802,0.001087,0.00108701,0.00108702,0.00108703,0.001086,0.00108601,0.00108602,0.001085,0.00108501,0.00108502,0.001084]
        VE_VS_Lista = [205.99, 206.17,241.62,283.84,334.27,394.66,467.17,554.47,659.88,787.51,942.51,1131.3,1362,1644.7,1992.2,2421,2951.7,3610.9,4432.4,5460.1,6750.5,8376.7]
        EI_LS_Lista = [-333.4,-333.43,-337.63,-341.8,-345.94,-350.04,-354.12,-358.17,-362.18,-366.17,-370.13,-374.06,-377.95,-381.82,-385.66,-389.47,-393.25,-397,-400.72,-404.4,-408.07,-411.7]
        EI_SUB_Lista = [2707.9,2707.9,2709.4,2710.8,2712.2,2713.5,2714.8,2716.1,2717.3,2718.6,2719.7,2720.9,2722,2723.1,2724.2,2725.2,2726.2,2727.2,2728.1,2729,2729.9,2730.7]
        EI_VS_Lista = [2374.5,2374.5,2371.8,2369,2366.2,2363.5,2360.7,2357.9,2355.2,2352.4,2349.6,2346.8,2344.1,2341.3,2338.5,2335.7,2332.9,2330.2,2327.4,2324.6,2321.8,2319]
        EA_LS_Lista = [-333.4,-333.43,-337.63,-341.8,-345.93,-350.04,-354.12,-358.17,-362.18,-366.17,-370.13,-374.06,-377.95,-381.82,-385.66,-389.47,-393.25,-397,-400.72,-404.4,-408.07,-411.7]
        EA_SUB_Lista = [2833.9,2833.9,2834.5,2835,2835.4,2835.8,2836.2,2836.6,2836.9,2837.2,2837.5,2837.7,2837.9,2838.1,2838.2,2838.3,2838.4,2838.4,2838.5,2838.4,2838.4,2838.3]
        EA_VS_Lista = [2500.5,2500.5,2496.8,2493.2,2489.5,2485.8,2482.1,2478.4,2474.7,2471,2467.3,2463.6,2459.9,2456.2,2452.5,2448.8,2445.1,2441.4,2437.7,2434,2430.3,2426.6]
        ER_LS_Lista = [-1.2202,-1.2204,-1.2358,-1.2513,-1.2667,-1.2821,-1.2976,-1.313,-1.3284,-1.3439,-1.3593,-1.3748,-1.3903,-1.4057,-1.4212,-1.4367,-1.4521,-1.4676,-1.4831,-1.4986,-1.5141,-1.5296]
        ER_SUB_Lista = [10.374,10.375,10.453,10.533,10.613,10.695,10.778,10.862,10.947,11.033,11.121,11.209,11.3,11.391,11.484,11.578,11.673,11.77,11.869,11.969,12.071,12.174] 
        ER_VS_Lista = [9.154,9.154,9.218,9.282,9.347,9.413,9.48,9.549,9.618,9.689,9.761,9.835,9.909,9.985,10.063,10.141,10.221,10.303,10.386,10.47,10.557,10.644]
        print("Lista de variables:")
        print("[1] TEMPERATURA [°C] ")
        print("[2] PRESION SATURACION [kPa]")
        print("[3] VOLUMEN ESPECIFICO HIELO SATURADO [m3/kg]")
        print("[4] VOLUMEN ESPECIFICO VAPOR SATURADO [m3/kg]")
        print("[5] ENERGIA INTERNA HIELO SATURADO [kJ/kg]")
        print("[6] ENERGIA INTERNA SUBLIMACION [kJ/kg]")
        print("[7] ENERGIA INTERNA VAPOR SATURADO [kJ/kg]")
        print("[8] ENTALPIA HIELO SATURADO[kJ/kg]")
        print("[9] ENTALPIA SUBLIMACION [kJ/kg]")
        print("[10] ENTALPIA VAPOR SATURADO [kJ/kg]")
        print("[11] ENTROPIA HIELO SATURADO [kJ/kg*K]")
        print("[12] ENTROPIA SUBLIMACION [kJ/kg*K]")
        print("[13] ENTROPIA VAPOR SATURADO [kJ/kg*K]")
        xData_Nombre = None
        while True:
            xData_Nombre = input("¿Qué variable conoce?:\n") #Esto es para definir cual sera nuestro eje x en la interpolación
            if xData_Nombre == "1":
                X = T_Lista
                u = "°C"
                LI =-40
                LS = 0
                break
            elif xData_Nombre == "2":
                X = P_Lista
                u = "kPa"
                LI = 0.01285
                LS = 0.61169
                break
            elif xData_Nombre == "3":
                X = VE_LS_Lista
                u = "m3/kg"
                LI = 0.001084
                LS = 0.001091
                break
            elif xData_Nombre == "4":
                X = VE_VS_Lista
                u = "m3/kg"
                LI =205.99 
                LS =8376.7
                break
            elif xData_Nombre == "5" :
                X = EI_LS_Lista
                u = "kJ/kg"
                LI = -411.7
                LS = -333.4
                break
            elif xData_Nombre == "6" :
                X = EI_SUB_Lista
                u = "kJ/kg"
                LI = 2707.9
                LS = 2730.7
                break
            elif xData_Nombre == "7" :
                X = EI_VS_Lista
                u = "kJ/kg"
                LI = 2319.0
                LS =2374.5
                break
            elif xData_Nombre =="8":
                X = EA_LS_Lista
                u = "kJ/kg"
                LI =-411.7
                LS = -333.4
                break
            elif xData_Nombre == "9" :
                X = EA_SUB_Lista
                u = "kJ/kg"
                LI = 2833.4
                LS =2838.9
                break
            elif xData_Nombre == "10" :
                X = EA_VS_Lista
                u = "kJ/kg"
                LI = 2426.6
                LS = 2500.5
                break
            elif xData_Nombre == "11":
                X = ER_LS_Lista
                u = "kJ/kg*K"
                LI = -1.5296
                LS = -1.2202
                break
            elif xData_Nombre == "12" :
                X = ER_SUB_Lista
                u = "kJ/kg*K"
                LI = 10.374
                LS = 12.174
                break
            elif xData_Nombre == "13":
                X = ER_VS_Lista
                u = "kJ/kg*K"
                LI = 9.154
                LS =10.644
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo.Solo se aceptan valores como: 1 2 3 4 5")
        
        x_int: None
        while True:
            try: 
                x_int = float(input("¿Cual es su valor en "+ u +"?:\n"))
                break
            except ValueError:
                print("El valor no es aceptable")
        
            
        print("ALERTAS:")
        if x_int < LI:
            print("El valor esta fuera de los limites de las tablas")
        elif x_int > LS:
            print("El valor esta fuera de los limites de las tablas")
        else:
            print("Ninguna")
        
        if xData_Nombre == "1":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="2":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="3":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="5":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="7":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="8":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="10":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]
        elif xData_Nombre =="11":
            X = X[::-1] 
            xVector, Falso = Vectores(X,X, x_int)
            xVector = xVector[::-1]       
        else:
            xVector, Falso = Vectores(X,X, x_int)
        i = 0
        for x in X:
            if x == xVector[0]:
                x1 = i
            if x == xVector[1]:
                x2 = i
            if x == xVector[2]:
                x3 = i
            if x == xVector[3]:
                x4 = i
            i = i+1

 

        yData_Nombre = None
        while True:
            yData_Nombre = input("¿Qué variable quiere conocer?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
            if yData_Nombre == "1":
                Y = T_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y       
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int) 
                Resultado = "{:.2f}".format(R)
                u = "°C"
                break
            elif yData_Nombre == "2":
                Y = P_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.5f}".format(R)
                u = "kPa"
                break
            elif yData_Nombre == "3":
                Y = VE_LS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.6f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "4":
                Y = VE_VS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)               
                Resultado = "{:.2f}".format(R)
                u = "m3/kg"
                break
            elif yData_Nombre == "5" :
                Y = EI_LS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)              
                Resultado = "{:.2f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "6" :
                Y = EI_SUB_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "7" :
                Y = EI_VS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre =="8":
                Y = EA_LS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.2f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "9" :
                Y = EA_SUB_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "10" :
                Y = EA_VS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.1f}".format(R)
                u = "kJ/kg"
                break
            elif yData_Nombre == "11":
                Y = ER_LS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.4f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "12" :
                Y = ER_SUB_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.3f}".format(R)
                u = "kJ/kg*K"
                break
            elif yData_Nombre == "13":
                Y = ER_VS_Lista
                if xData_Nombre == "1":
                    Y = Y[::-1]
                elif xData_Nombre == "2":
                    Y = Y[::-1]
                elif xData_Nombre == "3":
                    Y = Y[::-1]
                elif xData_Nombre == "5":
                    Y = Y[::-1]
                elif xData_Nombre == "7":
                    Y = Y[::-1]
                elif xData_Nombre == "8":
                    Y = Y[::-1]
                elif xData_Nombre == "10":
                    Y = Y[::-1]
                elif xData_Nombre == "11":
                    Y = Y[::-1]
                else:
                    Y = Y
                yVector = [Y[x1],Y[x2],Y[x3],Y[x4]]
                R =  InterNewton(xVector,yVector,x_int)
                Resultado = "{:.3f}".format(R)
                u = "kJ/kg*K"
                break
            else:
                print("Variable no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4 5")

        print("El resultado es " + Resultado + " " + u)

    elif DATO == "4":
        P_Lista = [5, 10, 15, 20 , 30, 50]
        T1_Lista = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,263.94,280,300,311,320,340,342.16,360,365.75,380]
        T_Lista = [T1_Lista, T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista]
        V1_Lista = [0.0009977,0.0009996,0.0010057,0.0010149,0.0010267,0.001041,0.0010576,0.0010769,0.0010988,0.001124,0.0011531,0.0011868,0.0012268,0.0012755,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862,0.0012862]
        V2_Lista = [0.0009952,0.0009973,0.0010035,0.0010127,0.0010244,0.0010385,0.0010549,0.0010738,0.0010954,0.00112,0.0011482,0.0011809,0.0012192,0.0012653,0.0012754,0.0013226,0.001398,0.0014522,0.0014522,0.0014522,0.0014522,0.0014522,0.0014522,0.0014522]
        V3_Lista = [0.0009928,0.0009951,0.0010013,0.0010105,0.0010221,0.0010361,0.0010522,0.0010708,0.001092,0.001116,0.0011435,0.0011752,0.0012121,0.001256,0.0012656,0.0013096,0.0013783,0.0014249,0.0014733,0.0016311,0.0016572,0.0016572,0.0016572,0.0016572]
        V4_Lista = [0.0009904,0.0009929,0.0009992,0.0010084,0.0010199,0.0010337,0.0010496,0.0010679,0.0010886,0.0011122,0.001139,0.0011697,0.0012053,0.0012472,0.0012563,0.0012978,0.0013611,0.0014034,0.001445,0.0015693,0.001576,0.0018248,0.0020378,0.0020378]
        V5_Lista = [0.0009857,0.0009886,0.0009951,0.0010042,0.0010155,0.001029,0.0010445,0.0010623,0.0010823,0.0011049,0.0011304,0.0011595,0.0011927,0.0012314,0.0012397,0.001277,0.0013322,0.0013679,0.0014014,0.0014932,0.0015044,0.0016276,0.0016837,0.0018729]
        V6_Lista = [0.0009767,0.0009805,0.0009872,0.0009962,0.0010072,0.0010201,0.0010349,0.0010517,0.0010704,0.0010914,0.0011149,0.0011412,0.0011708,0.0012044,0.0012115,0.001243,0.0012879,0.0013158,0.0013409,0.0014049,0.0014126,0.0014848,0.0015118,0.0015884]
        V_Lista = [V1_Lista, V2_Lista, V3_Lista ,V4_Lista, V5_Lista, V6_Lista]
        U1_Lista = [0.04,83.61,166.92,250.29,333.82,417.65,501.91,586.8,672.55,759.47,847.92,938.39,1031.6,1128.5,1148.1,1148.1,1148.1,1148.1,1148.1,1148.1,1148.1,1148.1,1148.1,1148.1]
        U2_Lista = [0.12,83.31,166.33,249.43,332.69,416.23,500.18,584.72,670.06,756.48,844.32,934.01,1026.2,1121.6,1140.8,1221.8,1329.4,1393.3,1393.3,1393.3,1393.3,1393.3,1393.3,1393.3]
        U3_Lista = [0.18,83.01,165.75,248.58,331.59,414.85,498.5,582.69,667.63,753.58,840.84,929.81,1021,1115.1,1134,1213.4,1317.6,1378.4,1431.9,1567.9,1585.5,1585.5,1585.5,1585.5]
        U4_Lista = [0.23,82.71,165.17,247.75,330.5,413.5,496.85,580.71,665.28,750.78,837.49,925.77,1016.1,1109,1127.6,1205.6,1307.2,1365.9,1416.6,1540.2,1552.4,1703.6,1785.8,1785.8]
        U5_Lista = [0.29,82.11,164.05,246.14,328.4,410.87,493.66,576.9,660.74,745.4,831.11,918.15,1006.9,1097.8,1116,1191.5,1288.9,1344.6,1391.7,1502.4,1514.8,1626.8,1667.5,1782]
        U6_Lista = [0.29,80.93,161.9,243.08,324.42,405.94,487.69,569.77,652.33,735.49,819.45,904.39,990.55,1078.2,1095.4,1167.7,1259.6,1311.2,1354.3,1452.9,1463.8,1556.5,1587.4,1667.1]            
        U_Lista = [U1_Lista, U2_Lista, U3_Lista ,U4_Lista, U5_Lista, U6_Lista]
        H1_Lista = [5.03,88.61,171.95,255.36,338.96,422.85,507.19,592.18,678.04,765.09,853.68,944.32,1037.7,1134.9,1154.5,1154.5,1154.5,1154.5,1154.5,1154.5,1154.5,1154.5,1154.5,1154.5]
        H2_Lista = [10.07,93.28,176.37,259.55,342.94,426.62,510.73,595.45,681.01,767.68,855.8,945.82,1038.3,1134.3,1153.6,1235,1343.3,1407.9,1407.9,1407.9,1407.9,1407.9,1407.9,1407.9]
        H3_Lista = [15.07,97.93,180.77,263.74,346.92,430.39,514.28,598.75,684.01,770.32,858,947.43,1039.2,1134,1153.1,1233,1338.3,1399.8,1454,1592.4,1610.3,1610.3,1610.3,1610.3]
        H4_Lista = [20.03,102.57,185.16,267.92,350.9,434.17,517.84,602.07,687.05,773.02,860.27,949.16,1040.2,1134,1152.8,1231.5,1334.4,1394,1445.5,1571,1583.4,1740.1,1826.6,1826.6]
        H5_Lista = [29.86,111.77,193.9,276.26,358.86,441.74,525,608.76,693.21,778.55,865.02,952.93,1042.7,1134.7,1153.1,1229.8,1328.9,1385.6,1433.7,1547.1,1559.9,1675.6,1718,1838.2]
        H6_Lista = [49.13,129.95,211.25,292.88,374.78,456.94,539.43,622.36,705.85,790.06,875.19,961.45,1049.1,1138.4,1156.2,1229.9,1324,1377,1421.4,1523.1,1534.3,1630.7,1663,1746.5]
        H_Lista = [H1_Lista, H2_Lista, H3_Lista ,H4_Lista, H5_Lista, H6_Lista]
        S1_Lista = [0.0001 ,0.2954 ,0.5705 ,0.8287 ,1.0723 ,1.3034 ,1.5236 ,1.7344 ,1.9374 ,2.1338 ,2.3251 ,2.5127 ,2.6983 ,2.8841 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ,2.9207 ]
        S2_Lista = [0.0003,0.2943,0.5685,0.826,1.0691,1.2996,1.5191,1.7293,1.9316,2.1271,2.3174,2.5037,2.6876,2.871,2.907,3.0565,3.2488,3.3603,3.3603,3.3603,3.3603,3.3603,3.3603,3.3603]
        S3_Lista = [0.0004,0.2932,0.5666,0.8234,1.0659,1.2958,1.5148,1.7243,1.9259,2.1206,2.31,2.4951,2.6774,2.8586,2.8943,3.041,3.2279,3.3343,3.4263,3.6555,3.6848,3.6848,3.6848,3.6848]
        S4_Lista = [0.0005 ,0.2921 ,0.5646 ,0.8208 ,1.0627 ,1.2920 ,1.5105 ,1.7194 ,1.9203 ,2.1143 ,2.3027 ,2.4867,2.6676,2.8469 ,2.8821 ,3.0265 ,3.2091 ,3.3122 ,3.3996 ,3.6086 ,3.6340 ,3.8787 ,4.0146 ,4.0146 ]
        S5_Lista = [0.0003,0.2897,0.5607,0.8156,1.0564,1.2847,1.502,1.7098,1.9094,2.102,2.2888,2.4707,2.6491,2.825,2.8595,3.0001,3.1761,3.2741,3.3558,3.5438,3.5646,3.7499,3.8165,4.0026]
        S6_Lista = [-0.001,0.2845,0.5528,0.8055,1.0442,1.2705,1.4859,1.6916,1.8889,2.079,2.2628,2.4414,2.6156,2.7864,2.8197,2.9547,3.1218,3.2135,3.2888,3.4575,3.4758,3.6301,3.6809,3.8102]
        S_Lista = [S1_Lista, S2_Lista, S3_Lista ,S4_Lista, S5_Lista, S6_Lista]
        RP = None
        while True:
            RP = input("¿Conoce la Presion? (si/no):\n")
            if RP == "si":
                break
            elif RP == "no":
                break
            else:
                print("Respuesta no aceptable (si/no)")
        if RP == "si":
            P= None
            while True:
                try: 
                    P= float(input("¿Cual es su valor en MPa?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            PVector, P1Vector = Vectores(P_Lista,P_Lista,P)
            j = 0
            for p in P_Lista:
                if p == PVector[0]:
                    P1 =j
                if p == PVector[1]:
                    P2 =j
                if p == PVector[2]:
                    P3 =j
                if p == PVector[3]:
                    P4 =j
                j = j+1
            print("Lista de propiedades:")
            print("[1] TEMPERATURA [°C]")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg]")
            print("[4] ENTALPIA [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg*K]")
            PropiedadConocida = None
            while True:
                PropiedadConocida = input("¿Qué propiedad conoce?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if PropiedadConocida == "1":
                    PRO_Lista = T_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = " °C"
                    break
                elif PropiedadConocida == "2":
                    PRO_Lista = V_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = " m3/kg"
                    break
                elif PropiedadConocida == "3":
                    PRO_Lista = U_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = " kJ/kg"
                    break
                elif PropiedadConocida == "4":
                    PRO_Lista = H_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = " kJ/kg"
                    break
                elif PropiedadConocida == "5":
                    PRO_Lista = S_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = " kJ/kg*K"
                    break
                    
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")
            PRO= None
            while True:
                try: 
                    PRO= float(input("¿Cual es su valor en " + u +"?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            
            print("Lista de propiedades:")
            print("[1] TEMPERATURA [°C]")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg]")
            print("[4] ENTALPIA [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg*K]")
            Propiedad = None
            while True:
                Propiedad = input("¿Qué propiedad quiere conocer?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if Propiedad == "1":
                    T1 = T_Lista[P1]
                    T2 = T_Lista[P2]
                    T3 = T_Lista[P3]
                    T4 = T_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,T1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,T2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,T3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,T4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 0.0111*P**3-0.6512*P**2+17.236*P+192.65
                    LI = 0
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.1f}".format(Resultado)
                    u = " °C" 
                    break
                elif Propiedad == "2":
                    V1 = V_Lista[P1]
                    V2 = V_Lista[P2]
                    V3 = V_Lista[P3]
                    V4 = V_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,V1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,V2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,V3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,V4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = (2e-7)*P**3-(5e-6)*P**2+(7e-5)*P + 0.001
                    LI = (7e-10)*P**2-(5e-7)*P+0.001
                    if Resultado < LI:
                        n = True
                    elif Resultado > LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.7f}".format(Resultado)
                    u = " m3/kg"
                    break
                elif Propiedad == "3":
                    U1 = U_Lista[P1]
                    U2 = U_Lista[P2]
                    U3 = U_Lista[P3]
                    U4 = U_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,U1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,U2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,U3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,U4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LI = (3e-6)*P**3-0.0004*P**2+0.0214*P-0.0568
                    if P < 30:
                        LS = 0.0815*P**3-3.504*P**2+87.343*P+788.8
                    elif P == 30:
                        LS = 0.29
                    else:
                        LS =0.29
                    if Resultado < LI:
                        n = True
                    elif Resultado > LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.2f}".format(Resultado)
                    u = " kJ/kg"
                    break
                elif Propiedad == "4":
                    H1 = H_Lista[P1]
                    H2 = H_Lista[P2]
                    H3 = H_Lista[P3]
                    H4 = H_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,H1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,H2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,H3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,H4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 0.0865*P**3-3.616*P**2+89.777*P+785
                    LI = -0.0007*P**2+1.164*P-0.0312
                    if Resultado < LI:
                        n = True
                    elif Resultado > LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.2f}".format(Resultado)
                    u = " kJ/kg"
                    break
                elif Propiedad == "5":
                    S1 = S_Lista[P1]
                    S2 = S_Lista[P2]
                    S3 = S_Lista[P3]
                    S4 = S_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,S1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,S2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,S3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,S4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 0.0002*P**3-0.0071*P**2+0.1666*P+2.2456
                    LI = (-2e-6)*P**2+(7e-5)*P-0.0002
                    if Resultado < LI or Resultado > LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.4f}".format(Resultado)
                    u = " kJ/kg*K"
                    break
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")
            print("El resultado es: "+ Resultado + u)
            
            Ts = 0.0111*P**3-0.6512*P**2+17.236*P+192.65
            ts = "{:.2f}".format(Ts)
            print("La temperatura de saturación es de " + ts + " °C")
            print("Alertas:")
            if P<5:
                print("La presión esta fuera de los datos de las tablas")
            elif P>50:
                print("La presión esta fuera de los datos de las tablas")
            else:
                print("NINGUNA POR LA PRESION")
            if n == True:
                print("Los valores calculados estan fuera del rango de la tabla")
            elif n==False:
                print("NINGUNA POR LOS LIMITES")
            
        elif RP == "no":
            T= None
            while True:
                try: 
                    T= float(input("¿Cual es su Temperatura en °C?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            print("Alerta")
            if T < 0:
                print("La temperatura es menor a la tabulada")
            if T >380:
                print("La temperatura es mayor a la tabulada")
            else:
                print("NINGUNA")
            TVector, T1vector = Vectores(T1_Lista, T1_Lista, T)
            print("Lista de propiedades:")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg[")
            print("[4] ENTALPIA [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg]")
            Propiedad1 = None
            while True:
                Propiedad1 = input("¿Qué propiedad conoce?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if Propiedad1 == "2":
                    PRO_Lista = V_Lista
                    u = " m3/kg"
                    break
                elif Propiedad1 == "3":
                    PRO_Lista = U_Lista
                    u = " kJ/kg"
                    break
                elif Propiedad1 == "4":
                    PRO_Lista = H_Lista
                    u = " kJ/kg"
                    break
                elif Propiedad1 == "5":
                    PRO_Lista = S_Lista
                    u = " kJ/kg*K"
                    break
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")
            PRO= None
            while True:
                try: 
                    PRO= float(input("¿Cual es su valor en" + u + "?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            i = 0
            for t in T1_Lista:
                if t == TVector[0]:
                    T1 =i
                if t == TVector[1]:
                    T2 =i
                if t == TVector[2]:
                    T3 =i
                if t == TVector[3]:
                    T4 =i
                i = i+1
            Lista1 = PRO_Lista[0]
            Lista2 = PRO_Lista[1]
            Lista3 = PRO_Lista[2]
            Lista4 = PRO_Lista[3]
            Lista5 = PRO_Lista[4]
            Lista6 = PRO_Lista[5]
            VectorLista1 = [Lista1[T1], Lista1[T2], Lista1[T3], Lista1[T4]]
            VectorLista2 = [Lista2[T1], Lista2[T2], Lista2[T3], Lista2[T4]]
            VectorLista3 = [Lista3[T1], Lista3[T2], Lista3[T3], Lista3[T4]]
            VectorLista4 = [Lista4[T1], Lista4[T2], Lista4[T3], Lista4[T4]]
            VectorLista5 = [Lista5[T1], Lista5[T2], Lista5[T3], Lista5[T4]]
            VectorLista6 = [Lista6[T1], Lista6[T2], Lista6[T3], Lista6[T4]]
            Valor1 = InterNewton(TVector, VectorLista1, T )
            Valor2 = InterNewton(TVector, VectorLista2, T )
            Valor3 = InterNewton(TVector, VectorLista3, T )
            Valor4 = InterNewton(TVector, VectorLista4, T )
            Valor5 = InterNewton(TVector, VectorLista5, T )
            Valor6 = InterNewton(TVector, VectorLista6, T )
            Valores = [Valor1,Valor2,Valor3,Valor4,Valor5,Valor6]
            Valores = Valores[::-1] 
            xVector, Falso = Vectores(Valores,Valores, PRO)
            xVector = xVector[::-1]
            i = 0
            for x in Valores:
                if x == xVector[0]:
                    x1 = i
                if x == xVector[1]:
                    x2 = i
                if x == xVector[2]:
                    x3 = i
                if x == xVector[3]:
                    x4 = i
                i = i+1
            
            P_Lista = P_Lista[::-1]
            yVector = [P_Lista[x1],P_Lista[x2],P_Lista[x3],P_Lista[x4]]


            P =InterNewton(xVector,yVector,PRO)
            print( "La presión es de {:.2f} Mpa".format(P))
            print("Alertas:")
            if P < 5:
                print("La presión es menor a la tabulada")
            elif P>50:
                print("La presión es mayor a la tabulada")
            else:
                print("NINGUNA")
            Ts = 0.0111*P**3-0.6512*P**2+17.236*P+192.65
            ts = "{:.2f}".format(Ts)
            print("La temperatura de saturación es de "+ts+" °C")

    elif DATO == "3":
        P_Lista = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.5, 15.0, 17.5, 20.0, 25, 30.0, 35.0, 40.0, 50.0, 60.0]
        T1_Lista = [45.81,50,81.32,99.61,100,120.21,133.52,143.61,150,151.83,158.83,170.41,179.88,187.96,195.04,200,201.37,207.11,212.38,223.95,225,233.85,242.56,250,250.35,257.44,263.94,275,275.59,285.83,295.01,300,303.35,311,325,327.81,342.16,350,354.67,365.75,375,400,425,450,500,550,600,650,700,800,900,1000,1100,1200,1300]
        T_Lista = [T1_Lista, T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista,T1_Lista, T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista,T1_Lista, T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista,T1_Lista, T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista, T1_Lista ,T1_Lista, T1_Lista ]
        V1_Lista = [14.670,14.867,16.329,17.178,17.196,18.133,18.750,19.217,19.513,19.598,19.922,20.458,20.896,21.269,21.597,21.826,21.889,22.155,22.398,22.933,22.981,23.390,23.792,24.136,24.152,24.480,24.780,25.291,25.318,25.791,26.215,26.446,26.601,26.954,27.601,27.731,28.393,28.755,28.971,29.482,29.909,31.063,32.217,33.371,35.680,37.989,40.296,42.602,44.911,49.527,54.143,58.758,63.373,67.989,72.604]
        V2_Lista = [2.889,2.932,3.2403,3.415,3.4187,3.610,3.735,3.830,3.8897,3.907,3.972,4.081,4.169,4.244,4.310,4.3562,4.369,4.422,4.471,4.579,4.589,4.671,4.752,4.8206,4.824,4.890,4.950,5.052,5.058,5.153,5.238,5.2841,5.315,5.386,5.516,5.542,5.674,5.747,5.790,5.893,5.978,6.2094,6.441,6.672,7.1338,7.596,8.058,8.519,8.9813,9.9047,10.828,11.7513,12.6745,13.5977,14.5209]
        V3_Lista = [1.623,1.600,1.618,1.6941,1.6959,1.793,1.857,1.906,1.9367,1.945,1.979,2.034,2.078,2.116,2.149,2.1724,2.179,2.206,2.230,2.284,2.289,2.331,2.371,2.4062,2.408,2.441,2.471,2.523,2.525,2.573,2.616,2.6389,2.654,2.690,2.755,2.768,2.834,2.871,2.892,2.944,2.987,3.1027,3.219,3.334,3.5655,3.796,4.0279,4.259,4.490,4.9519,5.4137,5.8755,6.3372,6.7988,7.2605]
        V4_Lista = [0.67708,0.69069,0.78339,0.83268,0.83371,0.88578,0.91918,0.94416,0.95986,0.96434,0.98142,1.00950,1.03232,1.05171,1.06865,1.08049,1.08376,1.09743,1.10995,1.13739,1.13988,1.16081,1.18137,1.19890,1.19972,1.21641,1.23169,1.25766,1.25905,1.28305,1.30455,1.31623,1.32407,1.34195,1.37465,1.38121,1.41469,1.43297,1.44385,1.46966,1.49119,1.54934,1.60743,1.66546,1.78142,1.89726,2.01302,2.12871,2.24434,2.47550,2.70656,2.93755,3.16848,3.39938,3.63026]
        V5_Lista = [0.42659,0.43741,0.50847,0.54455,0.54529,0.58241,0.60582,0.62317,0.63402,0.63711,0.64886,0.66810,0.68368,0.69688,0.70839,0.71643,0.71865,0.72791,0.73639,0.75495,0.75663,0.77076,0.78463,0.79645,0.79701,0.80824,0.81853,0.83600,0.83693,0.85307,0.86751,0.87535,0.88061,0.89261,0.91455,0.91895,0.94139,0.95364,0.96093,0.97821,0.99263,1.03155,1.07041,1.10922,1.18672,1.26410,1.34139,1.41862,1.49580,1.65004,1.80417,1.95824,2.11226,2.26624,2.42019]
        V6_Lista = [0.29771,0.30760,0.36979,0.39974,0.40034,0.43028,0.44881,0.46242,0.47088,0.47328,0.48240,0.49727,0.50926,0.51939,0.52820,0.53434,0.53603,0.54310,0.54957,0.56370,0.56497,0.57571,0.58624,0.59520,0.59562,0.60414,0.61193,0.62515,0.62585,0.63805,0.64897,0.65489,0.65886,0.66793,0.68448,0.68780,0.70473,0.71396,0.71945,0.73248,0.74334,0.77265,0.80190,0.83109,0.88936,0.94751,1.00558,1.06358,1.12152,1.23730,1.35298,1.46859,1.58414,1.69966,1.81516]
        V7_Lista = [0.21449,0.22454,0.28474,0.31189,0.31243,0.33854,0.35432,0.36577,0.37283,0.37483,0.38240,0.39467,0.40452,0.41282,0.42002,0.42503,0.42641,0.43217,0.43743,0.44891,0.44994,0.45865,0.46718,0.47443,0.47477,0.48166,0.48795,0.49863,0.49919,0.50904,0.51784,0.52261,0.52581,0.53311,0.54644,0.54911,0.56273,0.57015,0.57457,0.58504,0.59377,0.61731,0.64079,0.66422,0.71095,0.75756,0.80409,0.85055,0.89696,0.98966,1.08227,1.17480,1.26728,1.35972,1.45214]
        V8_Lista = [0.17802,0.18504,0.23140,0.25432,0.25478,0.27744,0.29121,0.30118,0.30731,0.30905,0.31560,0.32618,0.33463,0.34172,0.34786,0.35212,0.35329,0.35818,0.36265,0.37236,0.37323,0.38059,0.38779,0.39390,0.39419,0.39999,0.40529,0.41427,0.41474,0.42302,0.43041,0.43442,0.43711,0.44323,0.45441,0.45665,0.46806,0.47428,0.47798,0.48674,0.49405,0.51374,0.53337,0.55295,0.59200,0.63093,0.66976,0.70853,0.74725,0.82457,0.90179,0.97893,1.05603,1.13309,1.21012]
        V9_Lista = [0.03793,0.05524,0.14299,0.17321,0.17375,0.19796,0.21087,0.21964,0.22486,0.22632,0.23175,0.24035,0.24710,0.25272,0.25754,0.26088,0.26180,0.26561,0.26908,0.27661,0.27729,0.28297,0.28851,0.29321,0.29343,0.29788,0.30194,0.30880,0.30917,0.31548,0.32111,0.32416,0.32620,0.33086,0.33935,0.34105,0.34971,0.35442,0.35722,0.36386,0.36939,0.38429,0.39912,0.41390,0.44332,0.47263,0.50186,0.53102,0.56011,0.61820,0.67619,0.73411,0.79197,0.84980,0.90761]
        V10_Lista = [-0.05546,-0.03153,0.08488,0.12131,0.12193,0.14848,0.16150,0.16989,0.17474,0.17607,0.18097,0.18854,0.19437,0.19915,0.20322,0.20602,0.20679,0.20997,0.21286,0.21910,0.21966,0.22434,0.22890,0.23275,0.23293,0.23657,0.23989,0.24549,0.24579,0.25093,0.25551,0.25799,0.25965,0.26343,0.27031,0.27169,0.27869,0.28250,0.28477,0.29013,0.29459,0.30661,0.31856,0.33046,0.35411,0.37765,0.40111,0.42451,0.44783,0.49438,0.54083,0.58721,0.63354,0.67983,0.72610]
        V11_Lista = [-0.13460,-0.10480,0.03886,0.08231,0.08303,0.11316,0.12709,0.13568,0.14050,0.14180,0.14653,0.15364,0.15897,0.16326,0.16687,0.16934,0.17001,0.17280,0.17531,0.18070,0.18119,0.18521,0.18912,0.19241,0.19256,0.19567,0.19850,0.20326,0.20352,0.20788,0.21176,0.21386,0.21526,0.21846,0.22427,0.22543,0.23134,0.23455,0.23646,0.24097,0.24472,0.25482,0.26485,0.27482,0.29464,0.31434,0.33395,0.35349,0.37297,0.41184,0.45059,0.48928,0.52792,0.56652,0.60509]
        V12_Lista = [-1.54172,-1.33134,-0.37693,-0.13042,-0.12664,0.01335,0.06362,0.08854,0.10028,0.10319,0.11280,0.12464,0.13182,0.13680,0.14060,0.14303,0.14368,0.14629,0.14857,0.15335,0.15378,0.15729,0.16069,0.16356,0.16369,0.16641,0.16888,0.17306,0.17328,0.17710,0.18050,0.18233,0.18356,0.18634,0.19139,0.19240,0.19751,0.20029,0.20194,0.20584,0.20909,0.21782,0.22650,0.23511,0.25216,0.26907,0.28597,0.30281,0.31951,0.35288,0.38614,0.41933,0.45247,0.48558,0.51866]
        V13_Lista = [-0.15743,-0.13099,0.00004,0.04135,0.04205,0.07121,0.08469,0.09292,0.09746,0.09868,0.10308,0.10955,0.11427,0.11800,0.12109,0.12318,0.12374,0.12606,0.12814,0.13254,0.13293,0.13617,0.13929,0.14190,0.14202,0.14447,0.14669,0.15042,0.15062,0.15402,0.15703,0.15866,0.15975,0.16222,0.16670,0.16759,0.17213,0.17459,0.17605,0.17950,0.18237,0.19007,0.19770,0.20527,0.22029,0.23518,0.24999,0.26473,0.27941,0.30865,0.33780,0.36687,0.39589,0.42488,0.45383]
        V14_Lista = [-0.39823,-0.34238,-0.07901,-0.00438,-0.00318,0.04408,0.06354,0.07444,0.08011,0.08159,0.08675,0.09391,0.09885,0.10260,0.10562,0.10763,0.10817,0.11037,0.11232,0.11642,0.11678,0.11977,0.12263,0.12502,0.12513,0.12737,0.12939,0.13279,0.13296,0.13605,0.13878,0.14025,0.14123,0.14346,0.14750,0.14831,0.15239,0.15460,0.15591,0.15901,0.16159,0.16849,0.17532,0.18210,0.19551,0.20879,0.22200,0.23515,0.24822,0.27426,0.30020,0.32606,0.35188,0.37766,0.40341]
        V15_Lista = [-0.47472,-0.41085,-0.11065,-0.02631,-0.02496,0.02782,0.04922,0.06101,0.06706,0.06863,0.07405,0.08145,0.08644,0.09017,0.09314,0.09508,0.09561,0.09773,0.09959,0.10347,0.10381,0.10661,0.10928,0.11150,0.11160,0.11367,0.11554,0.11867,0.11883,0.12166,0.12416,0.12551,0.12641,0.12845,0.13213,0.13287,0.13659,0.13860,0.13979,0.14261,0.14495,0.15122,0.15742,0.16355,0.17568,0.18769,0.19962,0.21148,0.22326,0.24674,0.27012,0.29342,0.31667,0.33989,0.36308]
        V16_Lista = [-1.77853,-1.54106,-0.48214,-0.21546,-0.21140,-0.06198,-0.00880,0.01739,0.02964,0.03266,0.04257,0.05457,0.06159,0.06627,0.06968,0.07178,0.07233,0.07449,0.07632,0.07995,0.08026,0.08278,0.08512,0.08705,0.08714,0.08892,0.09052,0.09318,0.09332,0.09571,0.09781,0.09894,0.09969,0.10139,0.10445,0.10506,0.10813,0.10979,0.11077,0.11309,0.11500,0.12012,0.12516,0.13015,0.13999,0.14970,0.15931,0.16884,0.17835,0.19722,0.21597,0.23466,0.25330,0.27190,0.29048]
        V17_Lista = [-0.76521,-0.67640,-0.24727,-0.12144,-0.11940,-0.03904,-0.00646,0.01120,0.02006,0.02232,0.03001,0.03999,0.04627,0.05066,0.05395,0.05600,0.05654,0.05866,0.06045,0.06398,0.06428,0.06667,0.06886,0.07063,0.07071,0.07233,0.07376,0.07613,0.07625,0.07836,0.08020,0.08118,0.08183,0.08331,0.08596,0.08649,0.08914,0.09056,0.09140,0.09338,0.09502,0.09938,0.10366,0.10789,0.11620,0.12437,0.13245,0.14046,0.14841,0.16420,0.17988,0.19549,0.21105,0.22658,0.24207]
        V18_Lista = [-0.85138,-0.75818,-0.29928,-0.16022,-0.15793,-0.06687,-0.02919,-0.00854,0.00187,0.00454,0.01359,0.02533,0.03264,0.03769,0.04140,0.04369,0.04428,0.04660,0.04852,0.05220,0.05251,0.05491,0.05706,0.05876,0.05884,0.06036,0.06170,0.06388,0.06399,0.06591,0.06757,0.06845,0.06904,0.07036,0.07272,0.07319,0.07554,0.07680,0.07754,0.07929,0.08073,0.08456,0.08830,0.09198,0.09919,0.10626,0.11325,0.12017,0.12702,0.14061,0.15410,0.16751,0.18087,0.19420,0.20750]
        V19_Lista = [-0.79264,-0.71010,-0.29603,-0.16630,-0.16413,-0.07688,-0.03989,-0.01927,-0.00876,-0.00606,0.00318,0.01526,0.02286,0.02812,0.03199,0.03438,0.03499,0.03740,0.03939,0.04316,0.04347,0.04590,0.04804,0.04970,0.04978,0.05126,0.05255,0.05461,0.05472,0.05651,0.05805,0.05887,0.05941,0.06062,0.06278,0.06320,0.06533,0.06647,0.06714,0.06871,0.07001,0.07343,0.07677,0.08004,0.08644,0.09270,0.09886,0.10495,0.11098,0.12292,0.13476,0.14653,0.15824,0.16992,0.18157]
        V20_Lista = [-1.45495,-1.29517,-0.51906,-0.28983,-0.28610,-0.13956,-0.08050,-0.04883,-0.03315,-0.02918,-0.01583,0.00103,0.01117,0.01793,0.02274,0.02563,0.02636,0.02919,0.03147,0.03567,0.03600,0.03859,0.04081,0.04251,0.04258,0.04406,0.04533,0.04733,0.04743,0.04915,0.05061,0.05138,0.05189,0.05302,0.05502,0.05542,0.05738,0.05842,0.05903,0.06047,0.06165,0.06477,0.06780,0.07076,0.07652,0.08213,0.08766,0.09312,0.09850,0.10916,0.11972,0.13020,0.14064,0.15103,0.16140]
        V21_Lista = [-1.34628,-1.21102,-0.52751,-0.31142,-0.30780,-0.16220,-0.10071,-0.06671,-0.04952,-0.04513,-0.03021,-0.01104,0.00069,0.00857,0.01420,0.01757,0.01843,0.02172,0.02436,0.02914,0.02951,0.03238,0.03478,0.03656,0.03664,0.03817,0.03945,0.04144,0.04154,0.04321,0.04462,0.04535,0.04583,0.04691,0.04879,0.04916,0.05100,0.05197,0.05254,0.05388,0.05497,0.05784,0.06062,0.06332,0.06858,0.07369,0.07870,0.08363,0.08852,0.09816,0.10769,0.11715,0.12655,0.13592,0.14527]
        V22_Lista = [-0.56715,-0.52317,-0.27561,-0.18237,-0.18070,-0.10879,-0.07450,-0.05386,-0.04278,-0.03986,-0.02963,-0.01560,-0.00635,0.00024,0.00519,0.00826,0.00905,0.01216,0.01472,0.01951,0.01990,0.02288,0.02540,0.02728,0.02737,0.02897,0.03031,0.03235,0.03245,0.03412,0.03549,0.03619,0.03665,0.03766,0.03939,0.03973,0.04138,0.04225,0.04276,0.04394,0.04490,0.04742,0.04983,0.05217,0.05667,0.06102,0.06527,0.06944,0.07355,0.08165,0.08964,0.09756,0.10543,0.11326,0.12107]
        V23_Lista = [-2.973499,-2.679728,-1.194340,-0.724228,-0.716356,-0.399556,-0.265984,-0.192333,-0.155233,-0.145769,-0.113746,-0.072948,-0.048347,-0.032105,-0.020714,-0.014031,-0.012351,-0.005997,-0.001030,0.007563,0.008212,0.012998,0.016723,0.019316,0.019427,0.021492,0.023125,0.025469,0.025581,0.027378,0.028787,0.029492,0.029946,0.030931,0.032594,0.032910,0.034457,0.035262,0.035730,0.036812,0.037689,0.039958,0.042114,0.044187,0.048157,0.051966,0.055665,0.059287,0.062850,0.069856,0.076750,0.083571,0.090341,0.097075,0.103781]
        V24_Lista = [-6.352118,-5.716444,-2.518963,-1.517386,-1.500696,-0.832630,-0.554185,-0.402161,-0.326207,-0.306920,-0.241992,-0.160270,-0.111820,-0.080371,-0.058691,-0.046173,-0.043054,-0.031387,-0.022431,-0.007424,-0.006323,0.001608,0.007490,0.011384,0.011547,0.014492,0.016711,0.019702,0.019840,0.021960,0.023525,0.024279,0.024755,0.025766,0.027418,0.027726,0.029212,0.029975,0.030417,0.031431,0.032248,0.034344,0.036315,0.038194,0.041767,0.045172,0.048463,0.051676,0.054829,0.061011,0.067082,0.073079,0.079025,0.084934,0.090817]
        V25_Lista = [-14.945348,-13.343804,-5.534557,-3.215464,-3.177638,-1.694321,-1.099711,-0.784007,-0.629453,-0.590614,-0.461273,-0.302253,-0.210638,-0.152636,-0.113540,-0.091386,-0.085921,-0.065713,-0.050486,-0.025701,-0.023927,-0.011396,-0.002444,0.003263,0.003496,0.007651,0.010671,0.014555,0.014728,0.017313,0.019124,0.019967,0.020489,0.021575,0.023284,0.023595,0.025072,0.025816,0.026243,0.027216,0.027991,0.029960,0.031791,0.033524,0.036793,0.039885,0.042861,0.045755,0.048589,0.054132,0.059562,0.064919,0.070224,0.075492,0.080733]
        V26_Lista = [-24.931541,-22.288808,-9.337414,-5.457785,-5.394289,-2.896419,-1.889304,-1.352556,-1.089131,-1.022855,-0.801900,-0.529689,-0.372591,-0.273070,-0.206012,-0.168050,-0.158692,-0.124134,-0.098164,-0.056141,-0.053153,-0.032184,-0.017439,-0.008225,-0.007853,-0.001308,0.003320,0.009022,0.009267,0.012812,0.015137,0.016165,0.016784,0.018028,0.019877,0.020202,0.021702,0.022440,0.022860,0.023807,0.024556,0.026436,0.028162,0.029782,0.032811,0.035655,0.038378,0.041018,0.043597,0.048629,0.053547,0.058391,0.063183,0.067938,0.072667]
        V27_Lista = [-18.036463,-16.340449,-7.608308,-4.757486,-4.709152,-2.740602,-1.892415,-1.417931,-1.176611,-1.114774,-0.904621,-0.634719,-0.470856,-0.362398,-0.286407,-0.241989,-0.230851,-0.188935,-0.156470,-0.101519,-0.097463,-0.068236,-0.046666,-0.032596,-0.032016,-0.021645,-0.014098,-0.004542,-0.004127,0.001911,0.005826,0.007515,0.008510,0.010440,0.013070,0.013496,0.015321,0.016138,0.016583,0.017546,0.018275,0.020030,0.021588,0.023019,0.025630,0.028033,0.030306,0.032491,0.034612,0.038724,0.042720,0.046641,0.050510,0.054342,0.058147]
        V28_Lista = [-77.421719,-70.099147,-32.457453,-20.208091,-20.000733,-11.570477,-7.951895,-5.934214,-4.910789,-4.648930,-3.760491,-2.623945,-1.937662,-1.485869,-1.171044,-0.987935,-0.942149,-0.770437,-0.638219,-0.416688,-0.400491,-0.284718,-0.200732,-0.147014,-0.144827,-0.106110,-0.078615,-0.045089,-0.043677,-0.023819,-0.011855,-0.007029,-0.004311,0.000633,0.006455,0.007275,0.010341,0.011481,0.012047,0.013165,0.013938,0.015671,0.017150,0.018477,0.020828,0.022945,0.024921,0.026804,0.028621,0.032121,0.035503,0.038808,0.042062,0.045279,0.048469]
        V29_Lista = [-19.538118,-17.940197,-9.286451,-6.208382,-6.154349,-3.875958,-2.828406,-2.214174,-1.890852,-1.806532,-1.514632,-1.124500,-0.876005,-0.704610,-0.580055,-0.505048,-0.485936,-0.412745,-0.354447,-0.251519,-0.243653,-0.185541,-0.140618,-0.110043,-0.108758,-0.085325,-0.067697,-0.044498,-0.043463,-0.028172,-0.018011,-0.013591,-0.010989,-0.005979,0.000585,0.001591,0.005581,0.007148,0.007932,0.009456,0.010460,0.012463,0.013947,0.015204,0.017385,0.019305,0.021073,0.022742,0.024342,0.027405,0.030348,0.033215,0.036029,0.038806,0.041556]
        V30_Lista = [-59.098580,-54.226257,-27.899184,-18.572770,-18.409340,-11.531020,-8.380180,-6.538021,-5.570509,-5.318489,-4.447169,-3.286032,-2.549224,-2.042794,-1.675989,-1.455738,-1.399707,-1.185536,-1.015471,-0.716749,-0.694024,-0.526744,-0.398384,-0.311710,-0.308082,-0.242219,-0.193101,-0.129289,-0.126473,-0.085273,-0.058499,-0.047083,-0.040449,-0.027921,-0.012232,-0.009937,-0.001309,0.001785,0.003244,0.005862,0.007397,0.009950,0.011498,0.012721,0.014793,0.016571,0.018185,0.019695,0.021134,0.023870,0.026484,0.029020,0.031504,0.033952,0.036371]
        V31_Lista = [-459.339762,-417.303628,-198.681224,-126.038594,-124.797968,-73.900535,-51.665362,-39.101270,-32.664204,-31.008545,-25.359849,-18.044386,-13.558971,-10.565645,-8.453640,-7.212355,-6.900199,-5.722048,-4.805418,-3.244619,-3.128919,-2.293368,-1.675078,-1.271898,-1.255322,-0.959195,-0.745219,-0.478490,-0.467077,-0.304511,-0.204356,-0.163406,-0.140208,-0.097853,-0.048401,-0.041629,-0.017754,-0.010033,-0.006615,-0.000961,0.001978,0.006005,0.007886,0.009176,0.011143,0.012736,0.014140,0.015430,0.016643,0.018922,0.021075,0.023150,0.025172,0.027157,0.029115]
        V32_Lista = [3644.322307,3302.922425,1541.478300,964.563742,954.771626,555.607246,383.403134,287.030667,238.016487,225.458273,182.789731,128.038494,94.857987,72.948483,57.641631,48.720781,46.487822,38.104207,31.637997,20.779544,19.984361,14.295560,10.164364,7.522105,7.414596,5.512752,4.165741,2.533492,2.465222,1.512961,0.952390,0.732128,0.610550,0.396577,0.167356,0.138803,0.048429,0.024874,0.016051,0.004907,0.001792,0.002798,0.005299,0.006737,0.008691,0.010175,0.011445,0.012590,0.013654,0.015628,0.017473,0.019240,0.020954,0.022630,0.024279]
        V33_Lista = [-2040.112895,-1845.386203,-847.307266,-524.297402,-518.842976,-297.675768,-203.252525,-150.830794,-124.331895,-117.564235,-94.648985,-65.469331,-47.956760,-36.494458,-28.551899,-23.955255,-22.809134,-18.524722,-15.243950,-9.797693,-9.402867,-6.600109,-4.596117,-3.334686,-3.283800,-2.390808,-1.768620,-1.031839,-1.001590,-0.586707,-0.351245,-0.261618,-0.213153,-0.130271,-0.047142,-0.037518,-0.009336,-0.003063,-0.000975,0.001250,0.001701,0.002105,0.003434,0.004957,0.006933,0.008348,0.009523,0.010565,0.011523,0.013278,0.014904,0.016450,0.017942,0.019398,0.020827]
        V34_Lista = [-1708.780892,-1548.076516,-719.953478,-449.356638,-444.768527,-257.947695,-177.532359,-132.609234,-109.793754,-103.952446,-84.121812,-58.722585,-43.366949,-33.250062,-26.197032,-22.094114,-21.068186,-17.220890,-14.259359,-9.302158,-8.940176,-6.356363,-4.488591,-3.299742,-3.251497,-2.400172,-1.800318,-1.078819,-1.048824,-0.632793,-0.390897,-0.296881,-0.245356,-0.155581,-0.061616,-0.050207,-0.015054,-0.006352,-0.003204,0.000609,0.001641,0.001911,0.002538,0.003692,0.005623,0.006985,0.008089,0.009053,0.009930,0.011521,0.012980,0.014360,0.015686,0.016976,0.018239]
        V35_Lista = [703.150038,635.648843,290.402501,179.095887,177.219392,101.257092,68.931386,51.028791,41.995837,39.691099,31.895264,21.990671,16.063025,12.192986,9.517463,7.972013,7.587077,6.149790,5.051287,3.233089,3.101614,2.170059,1.506417,1.090168,1.073407,0.779768,0.575842,0.335368,0.325526,0.190885,0.114845,0.086001,0.070434,0.043865,0.017283,0.014206,0.005162,0.003122,0.002434,0.001692,0.001560,0.001731,0.002009,0.002487,0.003890,0.005118,0.006108,0.006957,0.007717,0.009073,0.010296,0.011441,0.012534,0.013590,0.014620]
        V36_Lista = [50.548498,46.123769,22.653213,14.608184,14.469184,8.705206,6.139773,4.672644,3.914955,3.719326,3.049372,2.175280,1.635217,1.272874,1.016257,0.865084,0.827030,0.683294,0.571378,0.380867,0.366764,0.265112,0.190308,0.141915,0.139935,0.104759,0.079648,0.048968,0.047679,0.029640,0.018990,0.014809,0.012505,0.008471,0.004222,0.003706,0.002133,0.001761,0.001634,0.001507,0.001503,0.001633,0.001816,0.002086,0.002952,0.003955,0.004833,0.005591,0.006265,0.007456,0.008519,0.009504,0.010439,0.011339,0.012213]
        V_Lista = [V1_Lista, V2_Lista, V3_Lista ,V4_Lista, V5_Lista, V6_Lista, V7_Lista, V8_Lista, V9_Lista ,V10_Lista, V11_Lista, V12_Lista, V13_Lista, V14_Lista, V15_Lista ,V16_Lista, V17_Lista, V18_Lista, V19_Lista, V20_Lista, V21_Lista ,V22_Lista, V23_Lista, V24_Lista, V25_Lista, V26_Lista, V27_Lista ,V28_Lista, V29_Lista, V30_Lista, V31_Lista, V32_Lista, V33_Lista ,V34_Lista, V35_Lista, V36_Lista]
        U1_Lista = [2437.2,2443.3,2488.6,2514.9,2515.5,2544.6,2563.9,2578.6,2587.9,2590.6,2600.8,2617.8,2631.7,2643.6,2654.1,2661.4,2663.4,2671.9,2679.8,2697.0,2698.6,2711.8,2724.9,2736.1,2736.6,2747.3,2757.2,2774.0,2774.9,2790.5,2804.6,2812.3,2817.5,2829.3,2851.0,2855.4,2877.8,2890.0,2897.4,2914.8,2929.5,2969.3,3009.5,3050.2,3132.9,3217.3,3303.3,3391.1,3480.8,3665.4,3856.9,4055.3,4260.0,4470.9,4687.4]
        U2_Lista = [2421.3,2429.8,2483.2,2510.9,2511.5,2541.5,2561.3,2576.2,2585.7,2588.4,2598.8,2616.0,2630.1,2642.1,2652.6,2660.0,2662.0,2670.6,2678.5,2695.8,2697.4,2710.7,2723.8,2735.1,2735.6,2746.4,2756.3,2773.2,2774.1,2789.8,2803.9,2811.6,2816.8,2828.6,2850.4,2854.8,2877.2,2889.5,2896.9,2914.4,2929.0,2968.9,3009.2,3049.9,3132.6,3217.0,3303.1,3390.9,3480.6,3665.2,3856.8,4055.2,4259.9,4470.8,4687.3]
        U3_Lista = [2436.4,2439.5,2478.0,2505.6,2506.2,2537.4,2557.8,2573.2,2582.9,2585.7,2596.3,2613.7,2627.9,2640.1,2650.7,2658.2,2660.3,2668.9,2676.9,2694.3,2695.9,2709.3,2722.6,2733.9,2734.4,2745.3,2755.2,2772.2,2773.1,2788.8,2803.0,2810.7,2815.9,2827.8,2849.6,2854.0,2876.4,2888.8,2896.1,2913.7,2928.3,2968.3,3008.7,3049.4,3132.2,3216.6,3302.8,3390.7,3480.4,3665.0,3856.7,4055.0,4259.8,4470.7,4687.2]
        U4_Lista = [2373.4,2385.5,2459.1,2493.7,2494.4,2529.1,2550.9,2567.0,2577.1,2580.0,2591.0,2609.0,2623.6,2636.1,2647.0,2654.6,2656.7,2665.5,2673.6,2691.4,2693.0,2706.6,2720.0,2731.4,2731.9,2742.9,2752.9,2770.0,2770.9,2786.8,2801.0,2808.8,2814.0,2826.0,2847.9,2852.3,2874.9,2887.3,2894.7,2912.3,2927.1,2967.2,3007.7,3048.5,3131.4,3215.9,3302.2,3390.2,3479.9,3664.7,3856.3,4054.8,4259.6,4470.5,4687.1]
        U5_Lista = [2368.9,2378.1,2445.2,2481.6,2482.4,2519.8,2543.2,2560.3,2571.0,2574.0,2585.5,2604.2,2619.3,2632.1,2643.2,2651.0,2653.1,2662.1,2670.3,2688.4,2690.0,2703.8,2717.3,2728.9,2729.4,2740.5,2750.6,2767.9,2768.8,2784.8,2799.2,2807.0,2812.3,2824.3,2846.3,2850.8,2873.5,2885.9,2893.3,2911.0,2925.8,2966.0,3006.6,3047.5,3130.6,3215.3,3301.6,3389.7,3479.5,3664.3,3856.0,4054.5,4259.4,4470.3,4686.9]
        U6_Lista = [2235.5,2263.4,2408.3,2461.6,2462.6,2508.5,2534.6,2553.1,2564.4,2567.6,2579.6,2599.1,2614.7,2627.8,2639.2,2647.2,2649.4,2658.6,2667.0,2685.3,2687.0,2701.0,2714.7,2726.4,2727.0,2738.1,2748.3,2765.7,2766.7,2782.8,2797.2,2805.1,2810.4,2822.5,2844.6,2849.1,2871.9,2884.4,2891.9,2909.7,2924.5,2964.9,3005.6,3046.6,3129.8,3214.6,3301.0,3389.2,3479.0,3663.9,3855.7,4054.3,4259.2,4470.2,4686.7]
        U7_Lista = [1987.2,2048.5,2339.1,2426.8,2428.3,2492.0,2523.8,2544.8,2557.3,2560.7,2573.6,2593.9,2610.0,2623.5,2635.2,2643.3,2645.5,2654.9,2663.4,2682.1,2683.8,2698.0,2711.9,2723.8,2724.4,2735.7,2746.0,2763.6,2764.5,2780.8,2795.4,2803.3,2808.6,2820.8,2843.1,2847.5,2870.5,2883.0,2890.5,2908.3,2923.2,2963.7,3004.5,3045.7,3129.0,3213.9,3300.4,3388.7,3478.6,3663.6,3855.4,4054.0,4259.0,4470.0,4686.6]
        U8_Lista = [2295.5,2305.2,2388.9,2437.4,2438.4,2487.1,2516.4,2537.2,2549.9,2553.4,2566.8,2588.1,2604.9,2619.0,2631.0,2639.4,2641.7,2651.3,2660.0,2679.0,2680.7,2695.1,2709.2,2721.2,2721.8,2733.2,2743.6,2761.4,2762.3,2778.7,2793.4,2801.4,2806.8,2819.0,2841.5,2846.0,2869.0,2881.6,2889.1,2907.0,2921.9,2962.5,3003.4,3044.6,3128.2,3213.2,3299.8,3388.1,3478.1,3663.2,3855.1,4053.8,4258.8,4469.8,4686.4]
        U9_Lista = [1922.3,1979.9,2273.7,2373.5,2375.3,2452.4,2491.7,2517.6,2532.7,2536.8,2552.2,2576.0,2594.4,2609.4,2622.3,2631.1,2633.5,2643.6,2652.7,2672.4,2674.2,2689.1,2703.6,2715.9,2716.5,2728.1,2738.8,2756.9,2757.8,2774.5,2789.4,2797.5,2802.9,2815.3,2838.0,2842.6,2865.9,2878.6,2886.2,2904.2,2919.3,2960.2,3001.3,3042.8,3126.6,3211.9,3298.7,3387.1,3477.2,3662.5,3854.5,4053.3,4258.3,4469.4,4686.1]
        U10_Lista = [1182.3,1334.7,2052.1,2257.9,2261.3,2396.6,2456.0,2491.4,2510.8,2516.0,2534.7,2562.4,2582.8,2599.2,2612.9,2622.3,2624.9,2635.4,2645.0,2665.5,2667.4,2682.8,2697.7,2710.4,2711.0,2723.0,2733.9,2752.4,2753.3,2770.3,2785.5,2793.7,2799.2,2811.8,2834.7,2839.3,2862.9,2875.7,2883.4,2901.5,2916.7,2957.9,2999.3,3040.9,3125.0,3210.5,3297.5,3386.1,3476.3,3661.7,3853.9,4052.7,4257.9,4469.0,4685.8]
        U11_Lista = [457.8,694.1,1806.2,2120.9,2126.0,2326.5,2410.2,2457.8,2483.0,2489.6,2512.9,2546.1,2569.5,2587.8,2602.8,2612.9,2615.6,2626.9,2637.0,2658.4,2660.3,2676.3,2691.7,2704.7,2705.3,2717.6,2728.8,2747.6,2748.6,2765.9,2781.3,2789.7,2795.3,2808.1,2831.3,2836.0,2859.7,2872.7,2880.4,2898.7,2914.1,2955.5,2997.1,3039.0,3123.4,3209.1,3296.3,3385.0,3475.3,3661.0,3853.3,4052.2,4257.5,4468.7,4685.5]
        U12_Lista = [-5912.5,-4858.5,-52.6,1200.8,1220.2,1937.5,2196.7,2325.5,2386.1,2401.1,2450.6,2511.2,2547.5,2572.3,2590.9,2602.7,2605.8,2618.3,2629.2,2651.6,2653.6,2669.9,2685.6,2698.9,2699.5,2712.0,2723.5,2742.7,2743.8,2761.5,2777.2,2785.7,2791.4,2804.4,2827.9,2832.6,2856.6,2869.7,2877.5,2895.9,2911.4,2953.1,2995.0,3037.1,3121.8,3207.6,3295.1,3384.1,3474.4,3660.3,3852.7,4051.7,4257.0,4468.3,4685.1]
        U13_Lista = [-1254.0,-808.3,1256.8,1820.7,1829.6,2173.6,2309.7,2383.5,2420.9,2430.6,2463.8,2508.9,2539.2,2561.8,2579.8,2591.6,2594.8,2607.7,2619.1,2643.0,2645.1,2662.5,2679.0,2692.9,2693.5,2706.5,2718.3,2738.0,2739.0,2757.0,2773.0,2781.6,2787.4,2800.5,2824.3,2829.1,2853.4,2866.6,2874.5,2893.1,2908.7,2950.8,2992.9,3035.2,3120.1,3206.2,3293.9,3383.1,3473.5,3659.5,3852.1,4051.2,4256.6,4467.9,4684.8]
        U14_Lista = [40.0,283.2,1508.6,1898.5,1905.1,2174.3,2293.3,2362.6,2399.4,2409.1,2443.0,2490.4,2523.0,2547.6,2567.1,2579.9,2583.4,2597.3,2609.5,2634.8,2637.0,2655.2,2672.4,2686.7,2687.4,2700.7,2712.8,2732.9,2734.0,2752.4,2768.6,2777.4,2783.3,2796.6,2820.8,2825.7,2850.2,2863.6,2871.5,2890.4,2906.0,2948.3,2990.6,3033.0,3118.5,3205.0,3292.7,3381.9,3472.6,3658.8,3851.5,4050.7,4256.2,4467.6,4684.5]
        U15_Lista = [-3530.4,-2843.4,411.3,1331.3,1346.0,1916.2,2141.5,2261.8,2321.6,2336.8,2388.5,2455.7,2498.4,2528.6,2551.7,2566.4,2570.2,2585.8,2599.1,2626.2,2628.5,2647.6,2665.5,2680.3,2681.0,2694.8,2707.1,2727.8,2728.9,2747.7,2764.3,2773.2,2779.2,2792.7,2817.3,2822.2,2847.0,2860.5,2868.5,2887.5,2903.3,2945.9,2988.5,3031.2,3116.9,3203.5,3291.5,3380.9,3471.7,3658.0,3850.9,4050.2,4255.7,4467.2,4684.2]
        U16_Lista = [3443.4,3145.8,2137.5,2066.9,2067.3,2140.5,2216.4,2275.8,2312.3,2322.5,2360.0,2416.9,2458.3,2490.3,2515.9,2532.6,2537.1,2555.0,2570.6,2602.1,2604.8,2626.7,2646.9,2663.3,2664.1,2679.1,2692.5,2714.6,2715.7,2735.5,2752.9,2762.2,2768.4,2782.5,2807.9,2813.0,2838.6,2852.5,2860.7,2880.2,2896.4,2939.8,2983.0,3026.2,3112.8,3200.1,3288.5,3378.2,3469.3,3656.2,3849.4,4049.0,4254.7,4466.3,4683.4]
        U17_Lista = [-7355.9,-6322.5,-1253.5,272.4,297.5,1290.9,1699.7,1922.9,2035.2,2063.9,2161.2,2287.0,2365.3,2419.1,2458.7,2483.1,2489.4,2514.2,2534.7,2574.1,2577.3,2603.2,2626.3,2644.7,2645.5,2662.1,2676.7,2700.4,2701.6,2722.7,2741.0,2750.8,2757.3,2772.0,2798.4,2803.7,2830.1,2844.4,2852.9,2872.8,2889.3,2933.6,2977.5,3021.2,3108.6,3196.6,3285.5,3375.6,3467.0,3654.3,3847.9,4047.7,4253.6,4465.3,4682.6]
        U18_Lista = [-12735.7,-11160.4,-3368.8,-995.8,-956.7,595.9,1234.7,1581.9,1755.5,1799.6,1948.8,2138.9,2254.6,2332.3,2388.1,2421.8,2430.4,2463.6,2490.5,2540.5,2544.6,2575.9,2603.0,2624.0,2624.9,2643.5,2659.5,2685.3,2686.6,2709.1,2728.5,2738.8,2745.6,2761.0,2788.5,2793.9,2821.3,2836.0,2844.7,2865.2,2882.1,2927.2,2971.8,3016.1,3104.5,3193.1,3282.5,3372.9,3464.7,3652.5,3846.4,4046.4,4252.5,4464.4,4681.8]
        U19_Lista = [-11181.0,-9896.5,-3277.2,-1115.9,-1079.3,413.7,1058.7,1421.5,1607.1,1654.9,1818.2,2031.3,2164.1,2255.0,2321.0,2361.1,2371.4,2411.1,2443.4,2503.1,2507.9,2544.9,2576.5,2600.6,2601.7,2622.7,2640.6,2668.9,2670.3,2694.6,2715.3,2726.2,2733.4,2749.6,2778.2,2783.9,2812.2,2827.4,2836.4,2857.4,2874.7,2920.8,2966.1,3011.0,3100.3,3189.6,3279.4,3370.2,3462.4,3650.6,3844.8,4045.1,4251.4,4463.5,4680.9]
        U20_Lista = [-37761.1,-33460.6,-12457.6,-6214.1,-6112.3,-2120.1,-519.6,331.4,749.0,854.1,1205.1,1639.9,1894.2,2058.4,2171.8,2237.7,2254.2,2316.5,2365.2,2450.2,2456.7,2505.5,2545.1,2574.1,2575.3,2599.7,2620.0,2651.4,2653.0,2679.3,2701.4,2713.0,2720.6,2737.7,2767.7,2773.6,2802.9,2818.6,2827.8,2849.4,2867.2,2914.2,2960.3,3005.8,3096.0,3185.9,3276.4,3367.7,3460.0,3648.8,3843.3,4043.9,4250.4,4462.6,4680.1]
        U21_Lista = [-72296.2,-64167.3,-24705.6,-13117.6,-12929.7,-5610.8,-2717.7,-1198.4,-460.6,-276.0,336.4,1083.3,1510.4,1779.9,1961.7,2065.1,2090.8,2186.1,2258.8,2380.9,2389.9,2456.0,2507.0,2542.8,2544.4,2573.4,2597.0,2632.3,2634.1,2662.8,2686.6,2699.0,2707.1,2725.1,2756.6,2762.7,2793.3,2809.5,2819.0,2841.2,2859.4,2907.5,2954.4,3000.6,3091.8,3182.3,3273.3,3365.2,3457.7,3646.9,3841.8,4042.6,4249.3,4461.6,4679.3]
        U22_Lista = [-45538.9,-40822.8,-17014.6,-9494.3,-9368.4,-4302.7,-2165.2,-984.8,-389.2,-237.1,278.2,937.1,1336.6,1601.9,1789.3,1899.9,1927.8,2033.8,2117.3,2263.8,2275.0,2358.3,2424.5,2471.6,2473.6,2511.8,2542.5,2587.7,2589.9,2625.5,2654.0,2668.4,2677.8,2698.2,2733.2,2740.0,2773.0,2790.4,2800.5,2824.1,2843.3,2893.7,2942.4,2989.9,3083.1,3175.2,3267.2,3359.7,3453.0,3643.2,3838.8,4040.1,4247.1,4459.8,4677.7]
        U23_Lista = [-113669.8,-102056.5,-43723.5,-25490.0,-25186.3,-13038.9,-7978.9,-5216.1,-3835.2,-3484.5,-2303.3,-814.6,70.1,646.0,1044.4,1275.2,1332.9,1549.0,1715.7,1997.5,2018.4,2169.7,2283.7,2360.6,2363.8,2423.1,2468.7,2531.7,2534.7,2581.0,2616.2,2633.5,2644.5,2668.2,2707.7,2715.1,2751.3,2770.1,2781.0,2806.2,2826.6,2879.5,2930.0,2979.0,3074.3,3167.9,3261.0,3354.3,3448.3,3639.5,3835.7,4037.5,4245.0,4457.9,4676.1]
        U24_Lista = [-285950.3,-256647.0,-110236.9,-64938.5,-64187.7,-34300.4,-21981.6,-15314.4,-12006.0,-11168.9,-8362.2,-4861.2,-2810.1,-1493.6,-596.0,-82.8,44.5,517.2,876.2,1466.9,1509.5,1812.5,2031.2,2171.8,2177.6,2280.7,2356.1,2453.9,2458.3,2524.0,2570.5,2592.3,2605.9,2634.3,2679.6,2687.9,2727.9,2748.3,2760.1,2787.1,2808.8,2864.6,2917.2,2967.8,3065.4,3160.5,3254.7,3349.0,3443.6,3635.7,3832.7,4035.0,4242.8,4456.1,4674.5]
        U25_Lista = [-863976.2,-768866.9,-309928.8,-176248.6,-174086.2,-89997.9,-56851.5,-39478.5,-31057.3,-28952.1,-21980.7,-13516.5,-8718.4,-5725.8,-3737.0,-2623.8,-2351.0,-1350.4,-606.2,579.5,662.7,1241.9,1643.2,1890.8,1900.8,2075.2,2197.8,2348.7,2355.2,2449.8,2512.9,2541.2,2558.5,2593.7,2647.6,2657.2,2702.5,2725.0,2737.9,2767.1,2790.4,2849.2,2904.0,2956.3,3056.3,3153.0,3248.4,3343.4,3438.8,3632.0,3829.6,4032.4,4240.7,4454.2,4672.9]
        U26_Lista = [-1430305.9,-1276479.1,-526638.5,-304246.6,-300622.5,-158678.7,-101952.9,-71927.6,-57269.9,-53592.5,-41369.6,-26413.9,-17859.2,-12484.5,-8891.6,-6871.7,-6375.7,-4552.3,-3192.4,-1019.2,-866.4,195.9,928.7,1377.2,1395.1,1706.6,1921.7,2178.0,2188.7,2340.1,2434.6,2474.9,2498.6,2545.2,2611.6,2623.0,2674.6,2699.6,2713.7,2745.5,2770.6,2833.1,2890.4,2944.5,3047.0,3145.4,3242.0,3338.0,3434.0,3628.2,3826.5,4029.9,4238.5,4452.4,4671.3]
        U27_Lista = [-1046803.3,-947875.6,-439043.5,-273238.7,-270429.9,-156142.3,-106992.2,-79539.3,-65593.9,-62022.7,-49895.1,-34345.2,-24925.5,-18703.9,-14353.9,-11815.9,-11180.1,-8790.6,-6943.7,-3828.8,-3599.6,-1952.7,-744.1,39.3,71.5,644.8,1058.9,1577.4,1599.8,1921.2,2125.5,2212.1,2262.6,2358.8,2485.6,2505.6,2588.8,2624.9,2644.3,2685.5,2716.3,2789.6,2854.3,2913.7,3023.2,3126.1,3225.8,3324.1,3422.0,3618.8,3818.9,4023.5,4233.1,4447.7,4667.3]
        U28_Lista = [-5391483.6,-4880529.3,-2255477.1,-1402119.9,-1387680.7,-800918.1,-549288.8,-409083.3,-338006.3,-319825.5,-258161.0,-179332.3,-131777.3,-100498.2,-78720.0,-66062.6,-62899.0,-51039.9,-41915.9,-26649.1,-25534.3,-17573.6,-11810.8,-8133.5,-7984.0,-5340.6,-3468.7,-1196.2,-1100.9,234.8,1032.2,1350.9,1529.4,1850.9,2220.8,2271.6,2455.7,2520.9,2552.4,2612.6,2652.9,2740.6,2814.6,2880.8,2998.4,3106.2,3209.3,3310.1,3409.8,3609.3,3811.2,4017.1,4227.7,4443.1,4663.3]
        U29_Lista = [-1522235.8,-1397460.4,-721910.3,-481738.3,-477523.1,-299822.4,-218154.5,-170284.7,-145093.5,-138524.7,-115788.4,-85411.8,-66072.6,-52739.8,-43055.2,-37225.5,-35740.4,-30054.7,-25528.0,-17542.5,-16932.7,-12430.3,-8954.3,-6592.0,-6492.8,-4685.3,-3328.0,-1546.8,-1467.6,-299.1,473.2,807.5,1003.7,1379.4,1865.6,1939.2,2226.5,2336.5,2390.7,2493.6,2559.4,2684.3,2772.2,2845.4,2972.4,3085.8,3192.5,3295.8,3397.5,3599.7,3803.5,4010.7,4222.3,4438.5,4659.2]
        U30_Lista = [-5517988.0,-5063365.1,-2605877.4,-1734745.0,-1719476.0,-1076691.8,-782117.9,-609844.4,-519347.9,-495772.9,-414258.4,-305610.4,-236653.7,-189251.3,-154914.7,-134296.0,-129050.6,-109000.3,-93079.2,-65114.7,-62987.6,-47330.7,-35320.0,-27212.9,-26873.7,-20716.2,-16127.2,-10171.3,-9908.8,-6070.8,-3582.8,-2524.5,-1910.5,-754.1,684.3,893.2,1670.4,1944.0,2071.2,2294.8,2421.4,2617.9,2725.6,2807.3,2945.3,3064.7,3175.3,3281.4,3385.1,3590.1,3795.7,4004.3,4216.9,4433.8,4655.2]
        U31_Lista = [-212377235.7,-192672876.6,-90674094.6,-57067181.7,-56495292.4,-33120423.4,-22982894.5,-17286385.0,-14380146.8,-13634297.1,-11095673.4,-7825276.2,-5833350.3,-4512007.8,-3584890.1,-3042572.1,-2906547.4,-2394665.5,-1998338.4,-1328686.1,-1279379.1,-925140.2,-665698.9,-498293.4,-491449.4,-369829.4,-282886.8,-176127.0,-171613.3,-108019.9,-69749.2,-54414.0,-45839.1,-30464.7,-13245.9,-10989.5,-3408.9,-1166.7,-234.6,1174.2,1799.9,2428.5,2607.8,2721.2,2887.3,3020.8,3140.0,3251.9,3359.9,3570.7,3780.2,3991.5,4206.1,4424.6,4647.2]
        U32_Lista = [646216347.0,585463027.8,272395910.2,170088752.6,168353941.4,97706845.5,67288607.1,50290931.1,41655993.5,39444922.7,31937322.3,22317667.5,16498605.6,12662592.1,9986752.1,8429331.7,8039782.9,6578431.6,5452842.9,3566806.2,3428953.1,2444197.4,1731180.3,1276530.2,1258061.6,931851.8,701533.8,423679.7,412099.8,251106.3,157007.6,120263.9,100065.2,64719.9,27362.7,22779.8,8522.4,4942.1,3642.6,2092.5,1738.1,2068.9,2452.9,2618.9,2824.0,2974.5,3103.4,3221.7,3334.3,3551.2,3764.6,3978.6,4195.2,4415.3,4639.2]
        U33_Lista = [-22565085.2,-19932312.3,-7310160.3,-3738600.7,-3682028.4,-1544666.7,-764163.0,-387230.4,-218491.7,-178331.0,-52992.3,76326.5,130831.1,152735.6,158997.8,158208.0,157399.6,151811.1,144263.9,123057.1,120963.5,103060.9,85888.8,72231.5,71618.4,59835.9,50161.4,36248.5,35594.9,25601.1,18641.8,15559.6,13739.3,10255.6,5889.3,5267.0,3072.7,2406.6,2138.9,1786.3,1702.8,1914.9,2253.3,2497.5,2755.3,2925.8,3065.6,3190.9,3308.3,3531.6,3749.0,3965.8,4184.4,4406.1,4631.2]
        U34_Lista = [-406715228.7,-368092390.8,-169768709.0,-105372879.8,-104283934.3,-60064657.9,-41131718.8,-30597367.2,-25263344.3,-23899859.9,-19278732.6,-13381854.6,-9833247.3,-7504942.1,-5887912.0,-4950253.8,-4716206.2,-3840229.7,-3168098.0,-2048710.2,-1967328.0,-1388344.0,-972524.9,-709575.5,-698941.5,-511889.8,-380929.6,-224774.5,-218327.0,-129432.3,-78390.6,-58757.7,-48067.4,-29601.5,-10625.2,-8363.3,-1506.6,148.4,740.9,1461.9,1677.0,1855.0,2097.5,2364.2,2681.6,2875.1,3026.8,3159.5,3282.0,3511.8,3733.3,3952.9,4173.7,4396.9,4623.3]
        U35_Lista = [66501556.1,59939231.7,26715277.2,16200300.0,16024433.2,8962942.8,6005854.8,4388191.8,3579600.9,3374305.8,2683538.0,1816158.0,1304718.6,975283.3,750372.1,621841.6,590017.2,471977.2,382751.0,237638.7,227307.4,154970.9,104654.2,73863.2,72639.8,51471.6,37142.8,20847.5,20200.2,11582.4,7002.5,5358.4,4503.2,3120.0,1912.5,1796.4,1536.1,1522.6,1533.7,1585.6,1638.6,1787.8,1960.3,2160.3,2528.1,2769.5,2947.1,3095.6,3228.7,3472.2,3702.0,3927.4,4152.2,4378.6,4607.5]
        U36_Lista = [53746190.6,48616371.9,22319168.0,13807416.8,13663685.8,7835951.8,5348361.0,3967605.6,3269784.7,3091586.9,2488294.7,1720341.0,1259665.6,958290.6,749559.7,628811.6,598711.8,486225.0,400129.7,257318.8,246973.0,173571.6,121147.4,88186.5,86857.7,63551.9,47332.8,28158.0,27371.8,16601.8,10505.9,8191.4,6942.1,4811.8,2693.9,2452.2,1764.4,1628.0,1590.8,1578.0,1609.7,1745.2,1892.9,2055.1,2393.2,2664.6,2866.8,3031.3,3175.4,3432.6,3670.9,3902.0,4130.9,4360.5,4591.8]
        U_Lista = [U1_Lista, U2_Lista, U3_Lista ,U4_Lista, U5_Lista, U6_Lista, U7_Lista, U8_Lista, U9_Lista ,U10_Lista, U11_Lista, U12_Lista, U13_Lista, U14_Lista, U15_Lista ,U16_Lista, U17_Lista, U18_Lista, U19_Lista, U20_Lista, U21_Lista ,U22_Lista, U23_Lista, U24_Lista, U25_Lista, U26_Lista, U27_Lista ,U28_Lista, U29_Lista, U30_Lista, U31_Lista, U32_Lista, U33_Lista ,U34_Lista, U35_Lista, U36_Lista]
        H1_Lista = [2583.9,2592.0,2651.9,2686.8,2687.5,2726.0,2751.4,2770.7,2783.0,2786.5,2800.0,2822.3,2840.6,2856.2,2870.0,2879.6,2882.3,2893.4,2903.7,2926.3,2928.4,2945.7,2962.9,2977.5,2978.2,2992.2,3005.0,3026.9,3028.1,3048.4,3066.7,3076.7,3083.4,3098.7,3126.9,3132.5,3161.6,3177.5,3187.0,3209.6,3228.5,3280.0,3331.9,3384.1,3489.7,3597.0,3706.3,3817.3,3929.9,4160.6,4398.3,4642.8,4893.8,5150.8,5413.4]
        H2_Lista = [2570.3,2579.7,2645.2,2681.6,2682.4,2722.1,2748.1,2767.7,2780.2,2783.8,2797.4,2820.0,2838.5,2854.2,2868.1,2877.8,2880.5,2891.7,2902.1,2924.8,2926.9,2944.3,2961.5,2976.2,2976.9,2990.9,3003.8,3025.8,3027.0,3047.4,3065.8,3075.8,3082.5,3097.9,3126.1,3131.8,3160.9,3176.8,3186.3,3208.9,3227.8,3279.3,3331.2,3383.5,3489.3,3596.8,3706.0,3817.0,3929.7,4160.4,4398.2,4642.7,4893.7,5150.7,5413.3]
        H3_Lista = [2564.3,2572.7,2637.2,2675.0,2675.8,2716.9,2743.7,2763.9,2776.6,2780.2,2794.1,2817.1,2835.8,2851.7,2865.7,2875.5,2878.2,2889.5,2900.0,2922.8,2924.9,2942.4,2959.7,2974.5,2975.2,2989.3,3002.3,3024.3,3025.5,3046.0,3064.5,3074.5,3081.2,3096.7,3125.0,3130.7,3159.9,3175.8,3185.4,3208.0,3227.0,3278.6,3330.5,3382.9,3488.7,3596.3,3705.6,3816.7,3929.4,4160.2,4398.0,4642.6,4893.6,5150.6,5413.3]
        H4_Lista = [2527.0,2538.4,2618.0,2660.7,2661.6,2706.3,2734.7,2755.8,2769.1,2772.9,2787.3,2810.9,2830.1,2846.4,2860.7,2870.7,2873.5,2885.0,2895.6,2918.8,2921.0,2938.7,2956.2,2971.2,2971.9,2986.2,2999.3,3021.6,3022.8,3043.4,3062.0,3072.1,3078.9,3094.4,3122.9,3128.6,3157.9,3173.9,3183.5,3206.2,3225.3,3277.0,3329.1,3381.6,3487.7,3595.4,3704.8,3815.9,3928.8,4159.8,4397.7,4642.3,4893.3,5150.4,5413.1]
        H5_Lista = [2438.7,2461.3,2588.5,2642.3,2643.3,2694.2,2724.9,2747.3,2761.2,2765.1,2780.1,2804.6,2824.3,2841.1,2855.7,2865.9,2868.7,2880.5,2891.3,2914.9,2917.0,2935.1,2952.8,2967.9,2968.6,2983.0,2996.2,3018.7,3019.9,3040.7,3059.4,3069.6,3076.4,3092.0,3120.7,3126.4,3155.9,3172.0,3181.6,3204.5,3223.6,3275.5,3327.7,3380.3,3486.6,3594.5,3704.0,3815.2,3928.2,4159.3,4397.3,4642.0,4893.1,5150.2,5413.0]
        H6_Lista = [2317.7,2355.6,2549.3,2619.2,2620.5,2680.1,2714.1,2738.1,2752.8,2757.0,2772.6,2798.0,2818.4,2835.5,2850.5,2860.9,2863.8,2875.8,2886.8,2910.8,2912.9,2931.2,2949.2,2964.5,2965.2,2979.8,2993.1,3015.8,3017.0,3038.0,3056.9,3067.1,3074.0,3089.7,3118.5,3124.3,3153.8,3170.0,3179.7,3202.6,3221.8,3273.9,3326.3,3379.0,3485.5,3593.6,3703.3,3814.6,3927.6,4158.9,4396.9,4641.7,4892.9,5150.0,5412.8]
        H7_Lista = [2060.2,2132.1,2474.9,2580.4,2582.2,2660.7,2700.8,2727.7,2743.6,2748.1,2764.8,2791.3,2812.3,2829.9,2845.2,2855.8,2858.7,2870.9,2882.1,2906.5,2908.7,2927.3,2945.5,2961.0,2961.7,2976.5,2990.0,3012.9,3014.1,3035.3,3054.3,3064.6,3071.5,3087.3,3116.3,3122.1,3151.8,3168.1,3177.8,3200.8,3220.1,3272.4,3325.0,3377.8,3484.5,3592.7,3702.5,3813.9,3927.0,4158.4,4396.6,4641.4,4892.6,5149.8,5412.6]
        H8_Lista = [2269.1,2305.8,2505.4,2583.1,2584.5,2652.5,2691.0,2718.0,2734.4,2739.0,2756.2,2783.8,2805.6,2823.9,2839.7,2850.6,2853.6,2866.1,2877.6,2902.4,2904.7,2923.5,2941.9,2957.6,2958.3,2973.2,2986.8,3009.9,3011.2,3032.5,3051.6,3062.0,3069.0,3084.9,3114.0,3119.9,3149.8,3166.1,3175.8,3199.0,3218.3,3270.8,3323.5,3376.5,3483.4,3591.8,3701.7,3813.2,3926.4,4157.9,4396.2,4641.1,4892.4,5149.6,5412.5]
        H9_Lista = [1638.5,1754.2,2310.2,2478.5,2481.3,2599.7,2655.7,2691.2,2711.4,2716.9,2737.2,2768.3,2792.1,2811.7,2828.3,2839.8,2842.9,2856.0,2867.9,2893.6,2895.9,2915.4,2934.3,2950.4,2951.2,2966.4,2980.3,3003.9,3005.2,3026.9,3046.4,3056.9,3064.0,3080.1,3109.6,3115.5,3145.7,3162.2,3172.0,3195.4,3214.9,3267.7,3320.7,3374.0,3481.3,3589.9,3700.1,3811.9,3925.3,4157.0,4395.5,4640.5,4891.9,5149.3,5412.2]
        H10_Lista = [1528.6,1646.2,2231.3,2418.6,2421.9,2557.7,2622.7,2663.7,2686.9,2693.2,2716.2,2750.9,2777.1,2798.3,2816.1,2828.3,2831.6,2845.4,2857.9,2884.7,2887.1,2907.1,2926.6,2943.1,2943.9,2959.5,2973.7,2997.7,2999.0,3021.1,3040.9,3051.6,3058.8,3075.1,3105.0,3111.0,3141.5,3158.2,3168.1,3191.7,3211.3,3264.5,3317.8,3371.3,3479.1,3588.1,3698.6,3810.6,3924.1,4156.1,4394.8,4640.0,4891.4,5148.9,5411.9]
        H11_Lista = [1103.4,1262.1,2057.0,2310.7,2315.0,2494.9,2578.0,2628.8,2656.8,2664.3,2691.4,2731.4,2760.6,2783.8,2803.1,2816.1,2819.6,2834.2,2847.3,2875.3,2877.8,2898.6,2918.7,2935.6,2936.4,2952.4,2966.9,2991.5,2992.8,3015.3,3035.4,3046.3,3053.6,3070.2,3100.4,3106.5,3137.4,3154.2,3164.2,3188.0,3207.8,3261.3,3314.9,3368.7,3477.0,3586.4,3697.0,3809.1,3922.9,4155.2,4394.0,4639.4,4891.0,5148.5,5411.6]
        H12_Lista = [-8347.0,-6962.1,-658.5,980.2,1005.4,1940.5,2277.4,2444.5,2523.1,2542.5,2606.5,2684.8,2731.7,2763.7,2787.8,2803.0,2807.0,2823.2,2837.3,2866.4,2869.0,2890.2,2910.6,2927.9,2928.7,2945.0,2959.9,2985.0,2986.3,3009.3,3029.8,3040.9,3048.3,3065.2,3095.8,3102.0,3133.1,3150.1,3160.2,3184.1,3204.1,3258.1,3312.2,3366.3,3474.8,3584.3,3695.5,3808.1,3921.7,4154.3,4393.3,4638.8,4890.5,5148.1,5411.3]
        H13_Lista = [-532.8,-182.0,1501.4,1995.3,2003.4,2326.2,2463.4,2541.8,2583.1,2593.9,2632.0,2685.4,2722.5,2750.7,2773.6,2788.7,2792.8,2809.4,2824.2,2855.1,2857.8,2880.3,2901.9,2919.9,2920.7,2937.6,2952.9,2978.6,2980.0,3003.4,3024.2,3035.4,3042.9,3060.0,3091.1,3097.3,3128.8,3146.0,3156.2,3180.4,3200.5,3254.9,3309.2,3363.5,3472.6,3582.6,3693.9,3806.5,3920.5,4153.4,4392.6,4638.2,4890.0,5147.7,5410.9]
        H14_Lista = [-2165.5,-1624.5,953.4,1693.9,1705.9,2175.7,2367.5,2473.3,2527.5,2541.5,2589.9,2655.3,2699.0,2731.3,2756.8,2773.5,2777.9,2795.9,2811.7,2844.3,2847.2,2870.7,2893.1,2911.7,2912.6,2930.0,2945.7,2972.0,2973.4,2997.3,3018.5,3029.9,3037.5,3054.9,3086.4,3092.6,3124.6,3141.9,3152.2,3176.6,3196.9,3251.6,3306.2,3360.8,3470.4,3580.7,3692.3,3805.2,3919.4,4152.4,4391.9,4637.6,4889.6,5147.3,5410.6]            
        H15_Lista = [-3935.5,-3188.9,353.8,1360.8,1377.0,2006.8,2258.9,2395.3,2464.0,2481.6,2541.7,2621.1,2672.5,2709.6,2738.3,2756.7,2761.6,2781.3,2798.3,2833.1,2836.1,2860.8,2884.0,2903.3,2904.2,2922.1,2938.2,2965.2,2966.6,2991.0,3012.6,3024.2,3032.0,3049.6,3081.5,3087.9,3120.2,3137.7,3148.1,3172.7,3193.2,3248.4,3303.4,3358.3,3468.3,3578.9,3690.7,3803.8,3918.2,4151.5,4391.1,4637.1,4889.1,5147.0,5410.3]
        H16_Lista = [-59186.4,-50969.7,-14758.4,-5899.0,-5766.3,-976.1,645.5,1404.3,1742.8,1823.9,2081.4,2368.3,2517.1,2605.2,2662.6,2695.1,2703.2,2733.6,2757.7,2801.9,2805.5,2834.0,2859.9,2880.9,2881.9,2901.2,2918.5,2947.3,2948.8,2974.7,2997.4,3009.6,3017.7,3036.1,3069.2,3075.8,3109.0,3127.0,3137.7,3162.9,3183.8,3240.1,3296.0,3351.6,3462.8,3574.6,3686.8,3799.7,3915.2,4149.2,4389.3,4635.6,4887.9,5146.0,5410.3]
        H17_Lista = [-15914.9,-13828.4,-3877.1,-1038.8,-993.2,767.2,1456.4,1818.6,1995.7,2040.2,2189.1,2375.4,2487.0,2561.5,2615.1,2647.6,2655.9,2688.4,2715.1,2765.9,2770.1,2803.2,2832.9,2856.5,2857.6,2879.0,2897.8,2928.6,2930.2,2957.6,2981.5,2994.3,3002.8,3022.0,3056.4,3063.2,3097.6,3116.1,3127.1,3152.9,3174.4,3231.7,3288.5,3344.9,3457.2,3569.6,3682.8,3797.1,3912.2,4146.9,4387.5,4634.2,4886.7,5145.1,5408.8]
        H18_Lista = [-23796.0,-20908.7,-6946.7,-2867.1,-2801.0,-225.3,797.5,1338.8,1604.1,1670.9,1894.0,2172.0,2336.5,2444.6,2520.8,2566.1,2577.6,2621.7,2657.2,2722.2,2727.4,2767.8,2802.7,2829.7,2830.9,2854.8,2875.5,2908.9,2910.6,2939.8,2965.0,2978.4,2987.3,3007.3,3043.1,3050.2,3085.8,3104.9,3116.2,3142.8,3164.7,3223.2,3280.9,3338.1,3451.7,3565.0,3678.9,3793.7,3909.3,4144.6,4385.7,4632.7,4885.6,5144.1,5408.0]
        H19_Lista = [-23575.5,-20811.1,-7268.0,-3208.9,-3142.4,-518.6,548.9,1124.8,1411.1,1483.7,1728.2,2037.8,2224.5,2348.9,2437.6,2490.7,2504.2,2556.2,2598.1,2674.9,2681.0,2728.2,2768.6,2799.4,2800.8,2827.7,2850.8,2887.3,2889.2,2920.6,2947.5,2961.7,2971.1,2992.1,3029.4,3036.8,3073.6,3093.3,3104.9,3132.2,3154.7,3214.5,3273.2,3331.2,3446.0,3560.3,3674.9,3790.2,3906.3,4142.3,4383.9,4631.2,4884.4,5143.2,5407.2]
        H20_Lista = [-36447.2,-32395.3,-12357.7,-6263.4,-6163.0,-2188.5,-563.1,314.5,750.2,860.5,1231.5,1697.9,1975.9,2158.5,2286.5,2361.8,2380.9,2453.2,2510.4,2612.0,2619.9,2679.7,2728.9,2765.4,2767.0,2798.0,2824.0,2864.4,2866.4,2900.5,2929.2,2944.2,2954.1,2976.2,3015.3,3022.9,3061.1,3081.5,3093.5,3121.6,3144.6,3205.7,3265.4,3324.2,3440.4,3555.7,3670.9,3786.7,3903.3,4140.0,4382.1,4629.8,4883.2,5142.2,5406.5]
        H21_Lista = [-83540.8,-74226.9,-28908.9,-15542.5,-15325.4,-6848.8,-3483.6,-1710.0,-846.4,-629.9,89.3,969.9,1476.1,1797.2,2014.9,2139.3,2170.2,2285.5,2373.8,2523.3,2534.5,2616.3,2680.1,2725.3,2727.2,2764.1,2794.2,2839.5,2841.8,2878.9,2909.7,2925.7,2936.2,2959.6,3000.5,3008.5,3048.2,3069.3,3081.7,3110.6,3134.3,3196.7,3257.5,3317.2,3434.7,3550.8,3666.9,3783.4,3900.3,4137.7,4380.2,4628.3,4882.1,5141.3,5405.7]
        H22_Lista = [-82284.6,-73640.4,-30570.9,-17294.1,-17074.2,-8322.6,-4710.4,-2749.5,-1773.0,-1525.4,-692.6,354.7,976.6,1382.1,1663.5,1827.3,1868.3,2022.9,2143.0,2349.4,2364.9,2479.3,2568.4,2630.8,2633.5,2683.5,2723.5,2781.8,2784.6,2830.4,2867.0,2885.6,2897.7,2924.1,2969.5,2978.2,3021.3,3043.9,3057.1,3087.8,3112.9,3178.3,3241.4,3302.9,3423.1,3541.3,3658.8,3776.4,3894.3,4133.1,4376.6,4625.4,4879.7,5139.4,5404.1]
        H23_Lista = [-161440.4,-144763.2,-61544.2,-35837.6,-35411.7,-18455.1,-11459.9,-7667.9,-5782.8,-5305.3,-3701.9,-1693.8,-509.6,256.1,782.7,1086.3,1162.0,1444.8,1662.1,2027.1,2053.9,2248.4,2394.3,2492.2,2496.3,2571.7,2629.6,2709.8,2713.5,2772.6,2817.7,2839.9,2854.1,2884.7,2935.7,2945.4,2992.5,3016.9,3031.1,3063.9,3090.4,3159.2,3224.8,3288.3,3411.4,3531.6,3650.6,3769.4,3888.3,4128.5,4373.0,4622.5,4877.4,5137.4,5402.6]
        H24_Lista = [-400308.3,-358842.4,-152734.4,-89560.8,-88517.8,-47167.0,-30255.8,-21156.7,-16661.3,-15526.6,-11730.8,-7021.1,-4280.0,-2530.9,-1344.4,-668.9,-501.9,117.3,585.6,1351.5,1406.5,1796.1,2075.5,2254.3,2261.6,2392.3,2487.6,2611.0,2616.5,2699.6,2758.7,2786.5,2803.8,2840.3,2898.8,2909.6,2961.5,2988.1,3003.4,3038.6,3066.9,3139.4,3207.7,3273.3,3399.5,3521.8,3642.4,3762.6,3882.2,4123.8,4369.3,4619.6,4875.0,5135.5,5401.0]
        H25_Lista = [-501984.4,-450171.9,-192905.2,-114027.2,-112723.7,-60953.8,-39688.4,-28196.5,-22497.4,-21055.7,-16221.6,-10189.7,-6652.1,-4378.3,-2825.2,-1935.6,-1715.0,-894.0,-269.5,761.1,835.7,1366.3,1750.0,1996.8,2007.0,2187.8,2319.6,2489.0,2496.5,2608.3,2685.6,2721.1,2742.9,2787.8,2857.1,2869.6,2928.1,2957.3,2974.0,3012.0,3042.2,3118.8,3190.2,3258.0,3387.4,3512.0,3634.1,3755.2,3876.1,4119.2,4365.7,4616.7,4872.7,5133.6,5399.5]
        H26_Lista = [-1381973.8,-1235240.3,-516184.8,-300821.3,-297296.8,-158662.2,-102781.2,-73007.6,-58399.4,-54724.7,-42476.1,-27394.1,-18697.3,-13193.1,-9488.3,-7393.2,-6877.1,-4972.7,-3543.6,-1237.5,-1074.0,70.6,870.8,1367.4,1387.3,1737.1,1982.1,2279.4,2292.0,2472.2,2587.3,2637.2,2666.8,2725.5,2810.3,2824.9,2891.6,2924.0,2942.3,2983.6,3016.1,3097.5,3172.2,3242.4,3375.1,3502.0,3625.8,3748.1,3870.0,4114.5,4362.0,4613.8,4870.3,5131.7,5398.0]
        H27_Lista = [-1267638.3,-1148022.5,-532513.4,-331791.5,-328390.1,-189942.6,-130363.3,-97068.5,-80149.2,-75815.6,-61095.6,-42212.9,-30767.3,-23203.4,-17912.1,-14823.5,-14049.7,-11140.2,-8890.4,-5092.7,-4813.1,-2802.7,-1325.6,-367.0,-327.6,375.1,883.3,1520.9,1548.5,1945.3,2198.5,2306.2,2369.0,2489.4,2649.0,2674.3,2780.3,2826.6,2851.5,2904.8,2944.7,3040.0,3124.2,3201.5,3343.6,3476.5,3604.6,3730.2,3854.6,4102.8,4352.9,4606.5,4864.5,5127.0,5394.1]
        H28_Lista = [-6517185.0,-5899865.5,-2727839.0,-1696371.1,-1678916.0,-969509.2,-665209.9,-495625.1,-409641.9,-387646.6,-313038.0,-217644.8,-160083.4,-122214.2,-95842.2,-80512.1,-76680.1,-62313.8,-51258.6,-32754.4,-31402.7,-21748.8,-14756.8,-10292.6,-10111.1,-6900.1,-4624.8,-1859.8,-1743.8,-115.8,858.0,1248.0,1466.7,1861.5,2317.9,2380.8,2610.8,2693.1,2733.1,2810.1,2862.0,2975.7,3071.8,3157.9,3310.8,3450.4,3583.1,3712.1,3839.1,4091.1,4343.7,4599.2,4858.6,5122.3,5390.3]
        H29_Lista = [-2245729.2,-2059609.0,-1055576.2,-700849.8,-694640.4,-433570.0,-314197.5,-244492.8,-207915.0,-198391.1,-165477.9,-121655.1,-93872.8,-74790.3,-60975.8,-52683.5,-50574.2,-42512.9,-36112.6,-24870.3,-24015.0,-17716.7,-12879.8,-9609.7,-9472.7,-6983.4,-5123.1,-2697.4,-2590.0,-1012.9,20.9,465.4,725.3,1220.6,1855.5,1950.7,2320.4,2460.7,2529.5,2660.0,2743.2,2902.4,3016.1,3111.4,3276.7,3423.6,3561.3,3693.8,3823.5,4079.3,4334.6,4592.0,4852.8,5117.6,5386.5]
        H30_Lista = [-6521911.7,-5985482.7,-3084281.4,-2054940.3,-2036891.5,-1276795.5,-928207.2,-724234.6,-617043.0,-589113.0,-492518.8,-363708.7,-281906.2,-225643.4,-184869.0,-160374.4,-154141.6,-130311.2,-111380.8,-78109.7,-75577.5,-56931.7,-42616.7,-32946.5,-32541.7,-25191.1,-19708.5,-12585.3,-12271.0,-7673.4,-4688.2,-3416.6,-2678.3,-1286.1,450.5,703.2,1647.0,1980.9,2136.8,2412.1,2569.2,2816.9,2955.6,3061.7,3241.2,3396.2,3539.0,3675.3,3807.8,4067.5,4325.4,4584.7,4847.0,5112.9,5382.7]
        H31_Lista = [-223414992.7,-202701840.0,-95454207.9,-60101853.8,-59500144.8,-34901471.8,-24228937.3,-18229959.4,-15168692.5,-14382959.8,-11708234.5,-8261487.0,-6161365.0,-4767776.9,-3789658.0,-3217351.8,-3073784.0,-2533424.4,-2114930.9,-1407508.0,-1355399.4,-980918.7,-706485.2,-529294.5,-522048.0,-393234.3,-301089.0,-187836.0,-183044.2,-115486.3,-74768.8,-58431.9,-49289.1,-32876.4,-14442.5,-12019.3,-3849.4,-1415.9,-399.0,1150.4,1849.4,2578.7,2805.0,2950.6,3165.9,3339.2,3493.5,3637.7,3776.0,4043.8,4307.1,4570.2,4835.4,5103.5,5375.1]
        H32_Lista = [756960744.1,685826811.6,319213054.0,199374892.5,197342570.9,114569750.2,78921939.3,58998242.3,48875405.5,46283144.1,37480505.9,26199419.7,19373737.0,14873180.4,11733153.1,9905246.7,9447998.9,7732496.9,6410914.3,4195830.6,4033885.7,2876801.0,2038674.7,1504028.8,1482305.8,1098532.4,827454.7,500226.4,486581.9,296797.1,185757.2,142359.2,118488.3,76681.9,32407.0,26962.8,9980.7,5690.8,4125.5,2240.0,1791.9,2152.8,2611.8,2821.0,3084.8,3279.7,3446.8,3599.4,3743.9,4020.0,4288.8,4555.8,4823.9,5094.2,5367.6]
        H33_Lista = [-94142782.2,-84678770.5,-37041259.4,-22136736.7,-21888787.0,-11991170.2,-7897371.3,-5680889.5,-4582239.1,-4304580.6,-3375062.5,-2221685.5,-1552550.8,-1128343.8,-843305.0,-682752.2,-643331.0,-498531.3,-390916.2,-220939.4,-209172.6,-128682.1,-75498.8,-44868.1,-43694.6,-24123.2,-11951.1,7.9,416.6,4992.5,6302.7,6368.6,6250.6,5678.2,4232.4,3948.3,2744.3,2298.7,2104.4,1830.1,1762.4,1988.6,2373.5,2671.0,2997.9,3218.0,3399.0,3560.7,3711.6,3996.3,4270.6,4541.5,4812.4,5085.0,5360.2]
        H34_Lista = [-472303290.8,-427519410.2,-197433017.2,-122650273.7,-121385155.5,-69990079.9,-47966479.3,-35704783.8,-29493187.7,-27904984.9,-22520824.4,-15646263.7,-11506294.2,-8788213.9,-6899348.6,-5803508.4,-5529901.0,-4505545.2,-3719161.6,-2408444.0,-2313085.2,-1634308.2,-1146311.9,-837396.7,-824896.8,-604912.3,-450736.0,-266639.2,-259029.5,-154008.8,-93583.2,-70300.8,-57609.6,-35655.7,-13025.1,-10319.0,-2092.8,-98.3,617.1,1487.1,1742.6,1931.4,2199.0,2511.8,2906.5,3154.4,3350.4,3521.6,3679.2,3972.6,4252.5,4527.3,4801.1,5075.9,5352.8]
        H35_Lista = [100643853.2,90800399.0,40801295.9,24881932.3,24614981.8,13867471.7,9342743.1,6857284.4,5610987.2,5294032.3,4225644.0,2878699.5,2080404.0,1563774.5,1209504.2,1006280.1,955855.0,768378.7,626102.9,393236.5,376562.9,259306.1,177012.6,126181.0,124151.0,88856.6,64725.2,36883.2,35763.8,20691.7,12472.8,9450.4,7852.0,5202.0,2730.7,2468.9,1781.6,1672.6,1651.6,1669.4,1716.6,1874.4,2060.7,2284.7,2722.6,3025.4,3252.6,3443.5,3614.6,3925.8,4216.8,4499.4,4778.9,5058.1,5338.5]
        H36_Lista = [56488441.0,51120675.0,23556680.7,14608202.4,14456909.3,8314952.2,5686997.0,4225772.3,3486322.8,3297367.8,2657204.3,1841058.3,1350546.0,1029119.3,806167.5,677032.8,644820.7,524350.4,432033.1,278616.3,267484.6,188413.9,131812.3,96145.7,94706.1,69431.7,51806.2,30911.4,30052.9,18270.5,11576.7,9027.3,7648.7,5291.8,2935.4,2664.8,1889.1,1732.0,1687.8,1668.2,1699.9,1843.2,2001.8,2180.2,2570.3,2901.9,3156.8,3366.8,3551.3,3880.0,4182.1,4472.2,4757.3,5040.8,5324.5]
        H_Lista = [H1_Lista, H2_Lista, H3_Lista ,H4_Lista, H5_Lista, H6_Lista, H7_Lista, H8_Lista, H9_Lista ,H10_Lista, H11_Lista, H12_Lista, H13_Lista, H14_Lista, H15_Lista ,H16_Lista, H17_Lista, H18_Lista, H19_Lista, H20_Lista, H21_Lista ,H22_Lista, H23_Lista, H24_Lista, H25_Lista, H26_Lista, H27_Lista ,H28_Lista, H29_Lista, H30_Lista, H31_Lista, H32_Lista, H33_Lista ,H34_Lista, H35_Lista, H36_Lista]
        S1_Lista = [8.1488,8.1741,8.3511,8.4469,8.4489,8.5495,8.6132,8.6601,8.6893,8.6976,8.7290,8.7799,8.8207,8.8549,8.8844,8.9049,8.9105,8.9339,8.9552,9.0012,9.0053,9.0398,9.0733,9.1015,9.1028,9.1294,9.1534,9.1938,9.1960,9.2327,9.2652,9.2827,9.2944,9.3208,9.3684,9.3779,9.4256,9.4513,9.4664,9.5021,9.5315,9.6094,9.6850,9.7586,9.8998,10.0343,10.1631,10.2868,10.4056,10.6312,10.8429,11.0429,11.2326,11.4132,11.5857]
        S2_Lista = [7.3711,7.4001,7.5931,7.6932,7.6953,7.7989,7.8639,7.9116,7.9413,7.9497,7.9815,8.0331,8.0743,8.1088,8.1386,8.1592,8.1649,8.1884,8.2098,8.2560,8.2602,8.2949,8.3285,8.3568,8.3581,8.3848,8.4089,8.4495,8.4517,8.4886,8.5212,8.5387,8.5504,8.5769,8.6247,8.6341,8.6820,8.7077,8.7229,8.7586,8.7880,8.8659,8.9415,9.0151,9.1566,9.2914,9.4201,9.5436,9.6626,9.8883,10.1000,10.3000,10.4897,10.6704,10.8429]
        S3_Lista = [6.9506,6.9958,7.2485,7.3589,7.3611,7.4693,7.5359,7.5846,7.6148,7.6233,7.6557,7.7080,7.7497,7.7847,7.8148,7.8356,7.8413,7.8651,7.8867,7.9333,7.9374,7.9723,8.0061,8.0346,8.0359,8.0627,8.0870,8.1277,8.1298,8.1669,8.1996,8.2172,8.2289,8.2555,8.3034,8.3130,8.3609,8.3867,8.4019,8.4377,8.4672,8.5452,8.6209,8.6945,8.8362,8.9711,9.0999,9.2234,9.3424,9.5682,9.7800,9.9800,10.1698,10.3504,10.5229]
        S4_Lista = [6.5942,6.6346,6.8876,7.0074,7.0097,7.1270,7.1981,7.2494,7.2810,7.2899,7.3235,7.3775,7.4204,7.4561,7.4869,7.5081,7.5139,7.5381,7.5601,7.6074,7.6116,7.6470,7.6812,7.7100,7.7113,7.7384,7.7629,7.8040,7.8061,7.8435,7.8764,7.8941,7.9059,7.9326,7.9808,7.9903,8.0385,8.0644,8.0797,8.1157,8.1453,8.2236,8.2996,8.3734,8.5153,8.6503,8.7793,8.9031,9.0221,9.2479,9.4598,9.6599,9.8497,10.0304,10.2029]
        S5_Lista = [6.2799,6.3322,6.6446,6.7828,6.7856,6.9153,6.9917,7.0461,7.0792,7.0885,7.1235,7.1794,7.2235,7.2601,7.2915,7.3132,7.3191,7.3438,7.3661,7.4141,7.4184,7.4542,7.4889,7.5180,7.5194,7.5467,7.5714,7.6129,7.6151,7.6527,7.6859,7.7037,7.7156,7.7425,7.7909,7.8005,7.8489,7.8750,7.8903,7.9264,7.9561,8.0347,8.1109,8.1849,8.3271,8.4623,8.5915,8.7154,8.8345,9.0605,9.2725,9.4726,9.6624,9.8431,10.0157]
        S6_Lista = [5.7761,5.8787,6.4052,6.5929,6.5963,6.7518,6.8369,6.8955,6.9306,6.9404,6.9770,7.0350,7.0805,7.1180,7.1502,7.1723,7.1784,7.2035,7.2262,7.2751,7.2794,7.3158,7.3509,7.3804,7.3818,7.4094,7.4344,7.4762,7.4784,7.5164,7.5498,7.5677,7.5797,7.6067,7.6554,7.6651,7.7137,7.7399,7.7553,7.7916,7.8214,7.9003,7.9768,8.0510,8.1933,8.3286,8.4580,8.5820,8.7012,8.9274,9.1394,9.3396,9.5295,9.7102,9.8828]
        S7_Lista = [5.8838,5.9450,6.3126,6.4745,6.4776,6.6270,6.7134,6.7740,6.8105,6.8207,6.8589,6.9193,6.9664,7.0052,7.0383,7.0610,7.0672,7.0929,7.1161,7.1658,7.1703,7.2072,7.2427,7.2725,7.2739,7.3018,7.3270,7.3692,7.3714,7.4097,7.4433,7.4614,7.4734,7.5007,7.5497,7.5594,7.6083,7.6346,7.6501,7.6865,7.7165,7.7956,7.8722,7.9466,8.0893,8.2249,8.3544,8.4785,8.5978,8.8240,9.0362,9.2364,9.4263,9.6071,9.7797]
        S8_Lista = [5.3126,5.4363,6.0809,6.3113,6.3154,6.5023,6.6016,6.6684,6.7078,6.7188,6.7593,6.8225,6.8713,6.9112,6.9451,6.9683,6.9746,7.0009,7.0245,7.0751,7.0796,7.1171,7.1531,7.1833,7.1847,7.2130,7.2385,7.2811,7.2833,7.3219,7.3558,7.3740,7.3861,7.4135,7.4628,7.4726,7.5217,7.5481,7.5637,7.6002,7.6303,7.7097,7.7866,7.8612,8.0041,8.1399,8.2695,8.3938,8.5132,8.7395,8.9518,9.1521,9.3420,9.5229,9.6955]
        S9_Lista = [4.6752,4.8482,5.7390,6.0457,6.0512,6.2889,6.4096,6.4882,6.5335,6.5460,6.5917,6.6616,6.7145,6.7573,6.7932,6.8177,6.8244,6.8518,6.8765,6.9289,6.9336,6.9722,7.0093,7.0402,7.0416,7.0705,7.0966,7.1400,7.1423,7.1816,7.2160,7.2345,7.2468,7.2746,7.3245,7.3344,7.3840,7.4107,7.4264,7.4633,7.4936,7.5735,7.6508,7.7257,7.8692,8.0054,8.1354,8.2599,8.3794,8.6061,8.8185,9.0189,9.2090,9.3898,9.5625]
        S10_Lista = [3.5202,3.8133,5.2681,5.7312,5.7391,6.0714,6.2282,6.3254,6.3798,6.3945,6.4477,6.5267,6.5850,6.6313,6.6697,6.6956,6.7026,6.7315,6.7573,6.8119,6.8167,6.8566,6.8947,6.9265,6.9280,6.9576,6.9842,7.0285,7.0309,7.0708,7.1058,7.1246,7.1371,7.1653,7.2158,7.2258,7.2760,7.3029,7.3188,7.3559,7.3865,7.4670,7.5448,7.6201,7.7642,7.9008,8.0311,8.1558,8.2755,8.5024,8.7150,8.9155,9.1057,9.2866,9.4593]
        S11_Lista = [1.1290,1.7098,4.4694,5.2692,5.2823,5.8050,6.0294,6.1595,6.2289,6.2473,6.3123,6.4051,6.4708,6.5217,6.5632,6.5909,6.5984,6.6289,6.6561,6.7130,6.7180,6.7593,6.7986,6.8313,6.8328,6.8632,6.8905,6.9357,6.9381,6.9788,7.0144,7.0335,7.0462,7.0748,7.1259,7.1360,7.1867,7.2139,7.2299,7.2674,7.2982,7.3793,7.4576,7.5333,7.6779,7.8149,7.9456,8.0706,8.1904,8.4176,8.6303,8.8310,9.0212,9.2022,9.3750]            
        S12_Lista = [-18.9182,-15.7583,-1.3775,2.3600,2.4175,4.5494,5.3168,5.6967,5.8749,5.9189,6.0635,6.2393,6.3431,6.4132,6.4651,6.4975,6.5060,6.5399,6.5691,6.6283,6.6335,6.6757,6.7156,6.7488,6.7503,6.7813,6.8091,6.8554,6.8579,6.8995,6.9359,6.9553,6.9682,6.9973,7.0491,7.0593,7.1105,7.1379,7.1540,7.1918,7.2228,7.3046,7.3836,7.4598,7.6047,7.7416,7.8730,7.9988,8.1183,8.3458,8.5587,8.7595,8.9497,9.1308,9.3036]
        S13_Lista = [-3.3281,-2.2394,2.8878,4.3330,4.3563,5.2627,5.6304,5.8329,5.9367,5.9635,6.0564,6.1824,6.2669,6.3296,6.3791,6.4114,6.4200,6.4549,6.4854,6.5482,6.5537,6.5985,6.6406,6.6753,6.6769,6.7090,6.7376,6.7850,6.7875,6.8298,6.8667,6.8864,6.8995,6.9289,6.9814,6.9917,7.0436,7.0713,7.0876,7.1258,7.1571,7.2394,7.3187,7.3952,7.5410,7.6788,7.8101,7.9357,8.0558,8.2834,8.4965,8.6974,8.8878,9.0689,9.2418]
        S14_Lista = [-5.3992,-4.1047,2.0526,3.8150,3.8434,4.9563,5.4075,5.6546,5.7801,5.8124,5.9234,6.0718,6.1691,6.2399,6.2949,6.3303,6.3397,6.3775,6.4102,6.4768,6.4825,6.5293,6.5730,6.6088,6.6105,6.6434,6.6728,6.7213,6.7238,6.7670,6.8046,6.8246,6.8379,6.8678,6.9210,6.9315,6.9840,7.0120,7.0285,7.0670,7.0985,7.1814,7.2611,7.3380,7.4845,7.6227,7.7543,7.8801,8.0005,8.2284,8.4417,8.6427,8.8331,9.0143,9.1872]
        S15_Lista = [-12.6796,-10.4939,-0.2491,2.5886,2.6337,4.3624,5.0335,5.3871,5.5613,5.6054,5.7543,5.9454,6.0650,6.1486,6.2117,6.2515,6.2620,6.3035,6.3390,6.4099,6.4160,6.4651,6.5105,6.5475,6.5492,6.5832,6.6134,6.6630,6.6656,6.7097,6.7480,6.7684,6.7819,6.8123,6.8663,6.8769,6.9300,6.9583,6.9749,7.0138,7.0457,7.1292,7.2095,7.2868,7.4337,7.5722,7.7043,7.8305,7.9509,8.1791,8.3925,8.5936,8.7842,8.9654,9.1384]
        S16_Lista = [-58.2452,-49.9990,-13.1158,-3.7918,-3.6497,1.5700,3.4151,4.3137,4.7288,4.8303,5.1598,5.5474,5.7641,5.9018,5.9974,6.0541,6.0686,6.1243,6.1697,6.2558,6.2629,6.3193,6.3701,6.4107,6.4126,6.4494,6.4819,6.5349,6.5376,6.5843,6.6246,6.6459,6.6600,6.6917,6.7476,6.7586,6.8133,6.8424,6.8595,6.8993,6.9318,7.0170,7.0985,7.1768,7.3254,7.4654,7.5979,7.7240,7.8455,8.0744,8.2882,8.4897,8.6804,8.8618,9.0349]
        S17_Lista = [-19.2359,-16.6202,-3.7409,0.1619,0.2262,2.7809,3.8375,4.4164,4.7081,4.7827,5.0363,5.3646,5.5691,5.7097,5.8131,5.8766,5.8931,5.9572,6.0104,6.1116,6.1199,6.1856,6.2437,6.2893,6.2914,6.3320,6.3674,6.4242,6.4271,6.4766,6.5189,6.5412,6.5559,6.5889,6.6471,6.6585,6.7150,6.7450,6.7626,6.8034,6.8367,6.9235,7.0062,7.0856,7.2359,7.3769,7.5103,7.6374,7.7590,7.9885,8.2028,8.4045,8.5955,8.7771,8.9502]
        S18_Lista = [-42.5308,-37.3491,-12.0990,-4.6120,-4.4899,0.3002,2.2282,3.2594,3.7686,3.8974,4.3293,4.8720,5.1964,5.4111,5.5632,5.6539,5.6769,5.7653,5.8364,5.9662,5.9766,6.0563,6.1244,6.1764,6.1787,6.2241,6.2629,6.3244,6.3275,6.3802,6.4249,6.4484,6.4639,6.4984,6.5589,6.5707,6.6292,6.6601,6.6782,6.7201,6.7542,6.8428,6.9269,7.0074,7.1593,7.3014,7.4357,7.5635,7.6855,7.9156,8.1304,8.3324,8.5236,8.7053,8.8786]
        S19_Lista = [-51.4715,-45.4401,-15.8573,-6.9787,-6.8332,-1.0939,1.2388,2.4949,3.1181,3.2759,3.8068,4.4761,4.8773,5.1427,5.3306,5.4422,5.4705,5.5788,5.6653,5.8218,5.8341,5.9284,6.0075,6.0670,6.0696,6.1207,6.1639,6.2312,6.2346,6.2914,6.3391,6.3639,6.3802,6.4164,6.4796,6.4919,6.5524,6.5843,6.6029,6.6460,6.6809,6.7714,6.8570,6.9386,7.0922,7.2355,7.3706,7.4990,7.6214,7.8523,8.0675,8.2698,8.4612,8.6430,8.8164]
        S20_Lista = [-80.8648,-71.7075,-26.8225,-13.3809,-13.1609,-4.5028,-1.0028,0.8711,1.7959,2.0294,2.8116,3.7886,4.3658,4.7420,5.0041,5.1575,5.1961,5.3423,5.4573,5.6598,5.6754,5.7927,5.8882,5.9581,5.9612,6.0198,6.0685,6.1429,6.1466,6.2081,6.2590,6.2854,6.3026,6.3408,6.4068,6.4196,6.4824,6.5153,6.5345,6.5788,6.6146,6.7071,6.7942,6.8770,7.0323,7.1767,7.3127,7.4418,7.5647,7.7962,8.0118,8.2144,8.4060,8.5880,8.7616]
        S21_Lista = [-153.5891,-136.4222,-52.8267,-28.1254,-27.7237,-12.0268,-5.7797,-2.4801,-0.8704,-0.4665,0.8768,2.5259,3.4771,4.0824,4.4940,4.7298,4.7884,5.0073,5.1754,5.4604,5.4816,5.6377,5.7591,5.8446,5.8483,5.9176,5.9737,6.0571,6.0612,6.1283,6.1830,6.2111,6.2294,6.2697,6.3389,6.3522,6.4175,6.4516,6.4714,6.5170,6.5538,6.6483,6.7369,6.8210,6.9781,7.1236,7.2605,7.3905,7.5136,7.7458,7.9619,8.1648,8.3566,8.5388,8.7124]
        S22_Lista = [-62.4174,-56.4312,-24.8444,-14.0973,-13.9120,-6.2365,-2.8192,-0.8587,0.1581,0.4213,1.3263,2.5195,3.2696,3.7831,4.1551,4.3791,4.4363,4.6558,4.8318,5.1477,5.1723,5.3577,5.5076,5.6156,5.6202,5.7087,5.7801,5.8851,5.8902,5.9724,6.0376,6.0703,6.0914,6.1371,6.2140,6.2286,6.2992,6.3357,6.3568,6.4052,6.4441,6.5432,6.6353,6.7219,6.8826,7.0308,7.1693,7.3001,7.4247,7.6582,7.8751,8.0786,8.2709,8.4534,8.6273]
        S23_Lista = [-266.2441,-238.9485,-102.1157,-59.4878,-58.7789,-30.4506,-18.6758,-12.2557,-9.0499,-8.2360,-5.4960,-2.0455,0.0035,1.3368,2.2589,2.7930,2.9265,3.4267,3.8126,4.4651,4.5134,4.8640,5.1283,5.3065,5.3139,5.4513,5.5566,5.7019,5.7087,5.8148,5.8947,5.9337,5.9584,6.0112,6.0976,6.1137,6.1911,6.2305,6.2532,6.3049,6.3461,6.4502,6.5459,6.6353,6.8000,6.9507,7.0910,7.2233,7.3487,7.5836,7.8014,8.0055,8.1982,8.3810,8.5551]
        S24_Lista = [-537.9652,-483.5991,-210.3174,-124.8344,-123.4109,-66.4774,-42.7903,-29.8786,-23.4367,-21.8023,-16.3049,-9.4013,-5.3219,-2.6833,-0.8711,0.1715,0.4308,1.3980,2.1369,3.3648,3.4542,4.0934,4.5601,4.8637,4.8762,5.1012,5.2671,5.4841,5.4939,5.6409,5.7450,5.7937,5.8239,5.8869,5.9860,6.0041,6.0893,6.1321,6.1566,6.2120,6.2559,6.3658,6.4656,6.5579,6.7266,6.8800,7.0221,7.1557,7.2822,7.5185,7.7372,7.9419,8.1350,8.3181,8.4925]
        S25_Lista = [-1382.0259,-1233.2302,-508.1237,-293.0504,-289.5445,-152.1464,-97.1439,-67.9755,-53.7102,-50.1275,-38.2037,-23.5666,-15.1525,-9.8378,-6.2643,-4.2441,-3.7465,-1.9094,-0.5293,1.7046,1.8637,2.9817,3.7718,4.2692,4.2894,4.6462,4.9013,5.2214,5.2354,5.4403,5.5786,5.6411,5.6791,5.7565,5.8738,5.8946,5.9908,6.0380,6.0647,6.1247,6.1716,6.2876,6.3917,6.4872,6.6603,6.8164,6.9605,7.0954,7.2229,7.4606,7.6802,7.8855,8.0791,8.2625,8.4371]
        S26_Lista = [-2628.1513,-2348.0453,-977.3934,-567.9810,-561.2888,-298.3648,-192.6382,-136.4098,-108.8601,-101.9351,-78.8704,-50.5194,-34.2069,-23.9033,-16.9807,-13.0720,-12.1100,-8.5636,-5.9066,-1.6301,-1.3276,0.7865,2.2592,3.1697,3.2062,3.8448,4.2901,4.8274,4.8500,5.1723,5.3758,5.4631,5.5147,5.6159,5.7596,5.7840,5.8937,5.9460,5.9753,6.0404,6.0909,6.2141,6.3230,6.4219,6.5995,6.7585,6.9045,7.0408,7.1693,7.4085,7.6290,7.8349,8.0289,8.2126,8.3874]
        S27_Lista = [-1936.9953,-1755.6822,-819.7022,-512.7393,-507.5253,-294.7833,-202.8059,-151.2271,-124.9479,-118.2080,-95.2811,-65.7778,-47.8244,-35.9187,-27.5637,-22.6740,-21.4470,-16.8268,-13.2448,-7.1738,-6.7253,-3.4921,-1.1048,0.4519,0.5160,1.6623,2.4949,3.5450,3.5905,4.2482,4.6698,4.8496,4.9546,5.1558,5.4219,5.4638,5.6381,5.7130,5.7529,5.8372,5.8992,6.0433,6.1660,6.2749,6.4651,6.6317,6.7828,6.9227,7.0540,7.2967,7.5195,7.7269,7.9220,8.1065,8.2819]
        S28_Lista = [-10618.9745,-9614.7336,-4451.2058,-2770.2423,-2741.7827,-1584.5873,-1087.7616,-810.6984,-670.1519,-634.1896,-512.1720,-356.0711,-261.8099,-199.7574,-156.5195,-131.3734,-125.0861,-101.5083,-83.3563,-52.9523,-50.7301,-34.8515,-23.3416,-15.9871,-15.6879,-10.3940,-6.6401,-2.0746,-1.8828,0.8078,2.4183,3.0636,3.4252,4.0779,4.8311,4.9347,5.3108,5.4438,5.5078,5.6296,5.7102,5.8819,6.0220,6.1434,6.3480,6.5230,6.6796,6.8233,6.9573,7.2037,7.4288,7.6378,7.8339,8.0192,8.1952]
        S29_Lista = [-3440.2261,-3155.9915,-1621.0058,-1077.6660,-1068.1473,-667.6160,-484.1897,-376.9567,-320.6364,-305.9655,-255.2400,-187.6286,-144.7087,-115.1942,-93.8051,-80.9546,-77.6844,-65.1791,-55.2418,-37.7627,-36.4313,-26.6192,-19.0711,-13.9597,-13.7454,-9.8481,-6.9313,-3.1202,-2.9513,-0.4669,1.1655,1.8687,2.2801,3.0652,4.0733,4.2247,4.8121,5.0346,5.1435,5.3489,5.4786,5.7211,5.8872,6.0212,6.2424,6.4266,6.5890,6.7366,6.8735,7.1237,7.3511,7.5616,7.7588,7.9449,8.1215]
        S30_Lista = [-10542.3960,-9673.8276,-4978.7470,-3314.4143,-3285.2420,-2057.1460,-1494.3152,-1165.1465,-992.2260,-947.1781,-791.4142,-583.7908,-452.0066,-361.4086,-295.7781,-256.3651,-246.3380,-208.0084,-177.5702,-124.1005,-120.0328,-90.0897,-67.1152,-51.6046,-50.9555,-39.1723,-30.3884,-18.9845,-18.4816,-11.1291,-6.3600,-4.3304,-3.1527,-0.9333,1.8299,2.2314,3.7272,4.2544,4.4997,4.9310,5.1751,5.5526,5.7553,5.9043,6.1446,6.3390,6.5075,6.6593,6.7991,7.0531,7.2829,7.4950,7.6933,7.8802,8.0574]
        S31_Lista = [-342706.5706,-310937.5298,-146437.5304,-92208.5184,-91285.4916,-53549.6559,-37176.3140,-27972.5148,-23275.6734,-22070.1180,-17966.1920,-12677.5131,-9454.9349,-7316.4227,-5815.4063,-4937.1207,-4716.7916,-3887.5033,-3245.2234,-2159.4613,-2079.4812,-1504.6852,-1083.4305,-811.4294,-800.3052,-602.5567,-461.0935,-287.2155,-279.8584,-176.1287,-113.6067,-88.5203,-74.4805,-49.2767,-20.9690,-17.2480,-4.7041,-0.9693,0.5908,2.9656,4.0345,5.1400,5.4708,5.6759,5.9643,6.1816,6.3637,6.5243,6.6702,6.9322,7.1668,7.3821,7.5825,7.7710,7.9494]
        S32_Lista = [1118118.9615,1013046.9064,471517.2098,294501.0563,291499.0512,169232.5452,116575.8974,87145.9298,72193.1755,68364.0719,55361.4680,38697.9756,28615.7287,21968.0031,17329.9524,14630.0291,13954.6521,11420.7918,9468.7911,6197.1514,5957.9670,4249.0444,3011.2493,2221.6889,2189.6095,1622.8867,1222.6057,739.4537,719.3091,439.1341,275.2366,211.1907,175.9664,114.2864,48.9922,40.9676,15.9521,9.6424,7.3432,4.5811,3.9313,4.4758,5.1473,5.4422,5.7956,6.0403,6.2373,6.4074,6.5599,6.8301,7.0695,7.2880,7.4906,7.6807,7.8602]
        S33_Lista = [-110575.5479,-99295.0255,-42798.4015,-25292.5377,-25002.5961,-13483.3259,-8765.5275,-6231.8037,-4984.0729,-4669.8588,-3622.0739,-2333.7727,-1595.6194,-1133.3630,-826.5710,-655.7121,-614.0372,-462.1407,-350.7808,-179.0728,-167.4679,-89.6977,-40.7166,-14.2010,-13.2256,2.3422,10.9698,17.4664,17.6084,17.9981,16.2716,14.9595,14.0179,11.8476,8.3549,7.7746,5.5161,4.7472,4.4228,3.9780,3.8724,4.2144,4.7751,5.1946,5.6331,5.9093,6.1229,6.3030,6.4623,6.7409,6.9853,7.2069,7.4118,7.6034,7.7841]
        S34_Lista = [-676392.4295,-612218.2484,-282582.7798,-175486.6597,-173675.1893,-100097.1697,-68578.2085,-51034.3023,-42148.4765,-39876.7389,-32176.1277,-22346.1444,-16428.0636,-12543.5619,-9844.7511,-8279.3228,-7888.5117,-6425.5344,-5302.6490,-3431.6405,-3295.5553,-2327.0775,-1631.0810,-1190.6707,-1172.8538,-859.3549,-639.7235,-377.6054,-366.7751,-217.3599,-131.4544,-98.3742,-80.3489,-49.1829,-17.0878,-13.2537,-1.6061,1.2159,2.2284,3.4623,3.8290,4.1145,4.5044,4.9449,5.4744,5.7857,6.0170,6.2078,6.3740,6.6613,6.9107,7.1355,7.3425,7.5357,7.7175]
        S35_Lista = [126894.8486,114445.7879,51283.6735,31215.0356,30878.8075,17354.6077,11671.2509,8553.7197,6992.1516,6595.2418,5258.1496,3574.7132,2578.6986,1935.1180,1494.4369,1241.9597,1179.3572,946.7875,770.5194,482.6151,462.0388,317.5414,216.4206,154.1461,151.6632,108.5601,79.1832,45.4430,44.0915,25.9595,16.1511,12.5709,10.6872,7.5879,4.7554,4.4638,3.7320,3.6375,3.6302,3.6854,3.7642,4.0029,4.2746,4.5896,5.1762,5.5563,5.8245,6.0373,6.2179,6.5225,6.7819,7.0131,7.2244,7.4207,7.6048]
        S36_Lista = [80667.5104,72980.9789,33552.0971,20775.6907,20559.8458,11804.1139,8063.3683,5985.6761,4935.1186,4666.7773,3758.0619,2600.6555,1905.8659,1451.0513,1135.8733,953.4629,907.9807,737.9610,607.7729,391.6754,376.0114,264.8307,185.3592,135.3535,133.3367,97.9522,73.3100,44.1514,42.9551,26.5582,17.2684,13.7389,11.8332,8.5824,5.3503,4.9818,3.9356,3.7306,3.6760,3.6620,3.7149,3.9317,4.1630,4.4140,4.9356,5.3517,5.6527,5.8867,6.0814,6.4033,6.6725,6.9099,7.1255,7.3248,7.5111]
        S_Lista = [S1_Lista, S2_Lista, S3_Lista ,S4_Lista, S5_Lista, S6_Lista, S7_Lista, S8_Lista, S9_Lista ,S10_Lista, S11_Lista, S12_Lista, S13_Lista, S14_Lista, S15_Lista ,S16_Lista, S17_Lista, S18_Lista, S19_Lista, S20_Lista, S21_Lista ,S22_Lista, S23_Lista, S24_Lista, S25_Lista, S26_Lista, S27_Lista ,S28_Lista, S29_Lista, S30_Lista, S31_Lista, S32_Lista, S33_Lista ,S34_Lista, S35_Lista, S36_Lista]
            
        RP = None
        while True:
            RP = input("¿Conoce la Presion? (si/no):\n")
            if RP == "si":
                break
            elif RP == "no":
                break
            else:
                print("Respuesta no aceptable (si/no)")
        if RP == "si":
            while True:
                try: 
                    P= float(input("¿Cual es su valor en MPa?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            print("Alertas por presion:")
            if P < 0.01:
                print("La presion es menor a la tabulada en las tablas")
            elif P >60:
                print("La presion es mayor a la tabulada en las tablas")
            else:
                print("NINGUNA")        
            PVector, P1Vector = Vectores(P_Lista,P_Lista,P)
            j = 0
            for p in P_Lista:
                if p == PVector[0]:
                    P1 =j
                if p == PVector[1]:
                    P2 =j
                if p == PVector[2]:
                    P3 =j
                if p == PVector[3]:
                    P4 =j
                j = j+1
            print("Lista de propiedades:")
            print("[1] TEMPERATURA [°C]")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg]")
            print("[4] ENTALPIA  [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg*K]")
            PropiedadConocida = None
            while True:
                PropiedadConocida = input("¿Qué propiedad conoce?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if PropiedadConocida == "1":
                    PRO_Lista = T_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = "°C"
                    break
                elif PropiedadConocida == "2":
                    PRO_Lista = V_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = "m3/kg"
                    break
                elif PropiedadConocida == "3":
                    PRO_Lista = U_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = "kJ/kg"
                    break
                elif PropiedadConocida == "4":
                    PRO_Lista = H_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = "kJ/kg"
                    break
                elif PropiedadConocida == "5":
                    PRO_Lista = S_Lista
                    PROa_Lista = PRO_Lista[P1]
                    PROb_Lista = PRO_Lista[P2]
                    PROc_Lista = PRO_Lista[P3]
                    PROd_Lista = PRO_Lista[P4]
                    u = "kJ/kg*K"
                    break
                    
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")
            PRO= None
            while True:
                try: 
                    PRO= float(input("¿Cual es su valor en " + u+ " ?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            
            print("Lista de propiedades:")
            print("[1] TEMPERATURA [°C]")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg]")
            print("[4] ENTALPIA [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg*K]")
            Propiedad = None
            while True:
                Propiedad = input("¿Qué propiedad quiere conocer?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if Propiedad == "1":
                    T1 = T_Lista[P1]
                    T2 = T_Lista[P2]
                    T3 = T_Lista[P3]
                    T4 = T_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,T1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,T2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,T3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,T4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 1300
                    if P <= 1:
                        LI = 186.46*P**0.2912
                    else:
                        LI = 180.83*P**0.2339
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.2f}".format(Resultado)
                    u = " °C"
                    break
                elif Propiedad == "2":
                    V1 = V_Lista[P1]
                    V2 = V_Lista[P2]
                    V3 = V_Lista[P3]
                    V4 = V_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,V1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,V2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,V3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,V4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                     
                    if P <= 5:
                        LI = 0.1906*P**(-0.951)
                        LS = 0.7261*P**(-1)
                    else:
                        LS = 0.7215*P**(-0.997)
                        LI = (5e-7)*P**4-(4e-5)*P**3+0.0011*P**2-0.0148*P+0.0889
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.7f}".format(Resultado)
                    u = " m3/kg"
                    break
                elif Propiedad == "3":
                    U1 = U_Lista[P1]
                    U2 = U_Lista[P2]
                    U3 = U_Lista[P3]
                    U4 = U_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,U1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,U2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,U3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,U4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 0.0004*P**2 -1.6181*P+4687.4 
                    if P<=2.5:
                        LI = 31.205*(math.log10(P))+2580.1
                    else:
                        LI = -0.1375*P**3 + 3.4229*P**2-35.121*P+2696.1
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.1f}".format(Resultado)
                    u = " kJ/kg"
                    break
                elif Propiedad == "4":
                    H1 = H_Lista[P1]
                    H2 = H_Lista[P2]
                    H3 = H_Lista[P3]
                    H4 = H_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,H1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,H2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,H3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,H4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    LS = 0.0014*P**2-1.5688*P+5413.15
                    if P<=2:
                        LI = 41.803*(math.log10(P))+2774.5
                    else:
                        LI = -0.1377*P**3 + 3.0947*P**2-32.22*P+2883.7 
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.1f}".format(Resultado)
                    u = " kJ/kg"
                    break
                elif Propiedad == "5":
                    S1 = S_Lista[P1]
                    S2 = S_Lista[P2]
                    S3 = S_Lista[P3]
                    S4 = S_Lista[P4]
                    PRO1Vector, V1Vector = Vectores(PROa_Lista,S1,PRO)
                    PRO2Vector, V2Vector = Vectores(PROb_Lista,S2,PRO)
                    PRO3Vector, V3Vector = Vectores(PROc_Lista,S3,PRO)
                    PRO4Vector, V4Vector = Vectores(PROd_Lista,S4,PRO)
                    a = InterNewton(PRO1Vector, V1Vector, PRO)
                    b = InterNewton(PRO2Vector, V2Vector, PRO)
                    c = InterNewton(PRO3Vector, V3Vector, PRO)
                    d = InterNewton(PRO4Vector, V4Vector, PRO)
                    R = [a,b,c,d]
                    Resultado = InterNewton(PVector, R, P)
                    if P<=10:
                        LS = -0.463*(math.log10(P))+9.4577
                    else:
                        LS = -0.491*(math.log10(P))+9.5255 
                    if P<=5:
                        LI = -0.347*(math.log10(P))+6.5693
                    else:
                        LI = -0.0004*P**3 + 0.0138*P**2-0.2218*P+6.8188
                    if Resultado < LI:
                        n = True
                    elif Resultado >LS:
                        n = True
                    else:
                        n = False
                    Resultado = "{:.4f}".format(Resultado)
                    u = " kJ/kg*K"
                    break
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")

            print("El resultado es: "+ Resultado + u)
            
            
            print("Alertas:")
            if P<0.01:
                print("La presión esta fuera de los datos de las tablas")
            elif P>60:
                print("La presión esta fuera de los datos de las tablas")
            else:
                print("NINGUNA POR LA PRESION")
            if n == True:
                print("Los valores calculados estan fuera del rango de la tabla")
            elif n==False:
                print("NINGUNA POR LOS LIMITES")            
        elif RP == "no":
            T= None
            while True:
                try: 
                    T= float(input("¿Cual es su Temperatura en °C?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            print("Alerta:")
            if T <45.81:
                print("La temperatura es menor a la tabulada")
            elif T >1300:
                print("La temperatura es menor a la tabulada")
            else:
                print("NINGUNA")
            TVector, T1vector = Vectores(T1_Lista, T1_Lista, T)
            print("Lista de propiedades:")
            print("[2] VOLUMEN ESPECIFICO [m3/kg]")
            print("[3] ENERGIA INTERNA [kJ/kg]")
            print("[4] ENTALPIA [kJ/kg]")
            print("[5] ENTROPIA [kJ/kg*K]")
            Propiedad1 = None
            while True:
                Propiedad1 = input("¿Qué propiedad conoce?:\n") #Esto es para definir cual sera nuestro eje y en la interpolación
                if Propiedad1 == "2":
                    PRO_Lista = V_Lista
                    u = "m3/kg"
                    break
                elif Propiedad1 == "3":
                    PRO_Lista = U_Lista
                    u = "kJ/kg"
                    break
                elif Propiedad1 == "4":
                    PRO_Lista = H_Lista
                    u = "kJ/kg"
                    break
                elif Propiedad1 == "5":
                    PRO_Lista = S_Lista
                    u = "kJ/kg*K"
                    break
                else:
                    print("Propiedad no contemplada. Intentelo de nuevo. Solo se aceptan valores como: 1 2 3 4")
            PRO= None
            while True:
                try: 
                    PRO= float(input("¿Cual es su valor en " +u +"?:\n"))
                    break
                except ValueError:
                    print("El valor no es aceptable")
            i = 0
            for t in T1_Lista:
                if t == TVector[0]:
                    T1 =i
                if t == TVector[1]:
                    T2 =i
                if t == TVector[2]:
                    T3 =i
                if t == TVector[3]:
                    T4 =i    
                i = i+1
            Lista1 = PRO_Lista[0]
            Lista2 = PRO_Lista[1]
            Lista3 = PRO_Lista[2]
            Lista4 = PRO_Lista[3]
            Lista5 = PRO_Lista[4]
            Lista6 = PRO_Lista[5]
            Lista7 = PRO_Lista[6]
            Lista8 = PRO_Lista[7]
            Lista9 = PRO_Lista[8]
            Lista10 = PRO_Lista[9]
            Lista11 = PRO_Lista[10]
            Lista12 = PRO_Lista[11]
            Lista13 = PRO_Lista[12]
            Lista14 = PRO_Lista[13]
            Lista15 = PRO_Lista[14]
            Lista16 = PRO_Lista[15]
            Lista17 = PRO_Lista[16]
            Lista18 = PRO_Lista[17]
            Lista19 = PRO_Lista[18]
            Lista20 = PRO_Lista[19]
            Lista21 = PRO_Lista[20]
            Lista22 = PRO_Lista[21]
            Lista23 = PRO_Lista[22]
            Lista24 = PRO_Lista[23]
            Lista25 = PRO_Lista[24]
            Lista26 = PRO_Lista[25]
            Lista27 = PRO_Lista[26]
            Lista28 = PRO_Lista[27]
            Lista29 = PRO_Lista[28]
            Lista30 = PRO_Lista[29]
            Lista31 = PRO_Lista[30]
            Lista32 = PRO_Lista[31]
            Lista33 = PRO_Lista[32]
            Lista34 = PRO_Lista[33]
            Lista35 = PRO_Lista[34]
            Lista36 = PRO_Lista[35]
            VectorLista1 = [Lista1[T1], Lista1[T2], Lista1[T3], Lista1[T4]]
            VectorLista2 = [Lista2[T1], Lista2[T2], Lista2[T3], Lista2[T4]]
            VectorLista3 = [Lista3[T1], Lista3[T2], Lista3[T3], Lista3[T4]]
            VectorLista4 = [Lista4[T1], Lista4[T2], Lista4[T3], Lista4[T4]]
            VectorLista5 = [Lista5[T1], Lista5[T2], Lista5[T3], Lista5[T4]]
            VectorLista6 = [Lista6[T1], Lista6[T2], Lista6[T3], Lista6[T4]]
            VectorLista7 = [Lista7[T1], Lista7[T2], Lista7[T3], Lista7[T4]]
            VectorLista8 = [Lista8[T1], Lista8[T2], Lista8[T3], Lista8[T4]]
            VectorLista9 = [Lista9[T1], Lista9[T2], Lista9[T3], Lista9[T4]]
            VectorLista10 = [Lista10[T1], Lista10[T2], Lista10[T3], Lista10[T4]]
            VectorLista11 = [Lista11[T1], Lista11[T2], Lista11[T3], Lista11[T4]]
            VectorLista12 = [Lista12[T1], Lista12[T2], Lista12[T3], Lista12[T4]]
            VectorLista13 = [Lista13[T1], Lista13[T2], Lista13[T3], Lista13[T4]]
            VectorLista14 = [Lista14[T1], Lista14[T2], Lista14[T3], Lista14[T4]]
            VectorLista15 = [Lista15[T1], Lista15[T2], Lista15[T3], Lista15[T4]]
            VectorLista16 = [Lista16[T1], Lista16[T2], Lista16[T3], Lista16[T4]]
            VectorLista17 = [Lista17[T1], Lista17[T2], Lista17[T3], Lista17[T4]]
            VectorLista18 = [Lista18[T1], Lista18[T2], Lista18[T3], Lista18[T4]]
            VectorLista19 = [Lista19[T1], Lista19[T2], Lista19[T3], Lista19[T4]]
            VectorLista20 = [Lista20[T1], Lista20[T2], Lista20[T3], Lista20[T4]]
            VectorLista21 = [Lista21[T1], Lista21[T2], Lista21[T3], Lista21[T4]]
            VectorLista22 = [Lista22[T1], Lista22[T2], Lista22[T3], Lista22[T4]]
            VectorLista23 = [Lista23[T1], Lista23[T2], Lista23[T3], Lista23[T4]]
            VectorLista24 = [Lista24[T1], Lista24[T2], Lista24[T3], Lista24[T4]]
            VectorLista25 = [Lista25[T1], Lista25[T2], Lista25[T3], Lista25[T4]]
            VectorLista26 = [Lista26[T1], Lista26[T2], Lista26[T3], Lista26[T4]]
            VectorLista27 = [Lista27[T1], Lista27[T2], Lista27[T3], Lista27[T4]]
            VectorLista28 = [Lista28[T1], Lista28[T2], Lista28[T3], Lista28[T4]]
            VectorLista29 = [Lista29[T1], Lista29[T2], Lista29[T3], Lista29[T4]]
            VectorLista30 = [Lista30[T1], Lista30[T2], Lista30[T3], Lista30[T4]]
            VectorLista31 = [Lista31[T1], Lista31[T2], Lista31[T3], Lista31[T4]]
            VectorLista32 = [Lista32[T1], Lista32[T2], Lista32[T3], Lista32[T4]]
            VectorLista33 = [Lista33[T1], Lista33[T2], Lista33[T3], Lista33[T4]]
            VectorLista34 = [Lista34[T1], Lista34[T2], Lista34[T3], Lista34[T4]]
            VectorLista35 = [Lista35[T1], Lista35[T2], Lista35[T3], Lista35[T4]]
            VectorLista36 = [Lista36[T1], Lista36[T2], Lista36[T3], Lista36[T4]]
            
            
            Valor1 = InterNewton(TVector, VectorLista1, T )
            Valor2 = InterNewton(TVector, VectorLista2, T )
            Valor3 = InterNewton(TVector, VectorLista3, T )
            Valor4 = InterNewton(TVector, VectorLista4, T )
            Valor5 = InterNewton(TVector, VectorLista5, T )
            Valor6 = InterNewton(TVector, VectorLista6, T )
            Valor7 = InterNewton(TVector, VectorLista7, T )
            Valor8 = InterNewton(TVector, VectorLista8, T )
            Valor9 = InterNewton(TVector, VectorLista9, T )
            Valor10 = InterNewton(TVector, VectorLista10, T )
            Valor11 = InterNewton(TVector, VectorLista11, T )
            Valor12 = InterNewton(TVector, VectorLista12, T )
            Valor13 = InterNewton(TVector, VectorLista13, T )
            Valor14 = InterNewton(TVector, VectorLista14, T )
            Valor15 = InterNewton(TVector, VectorLista15, T )
            Valor16 = InterNewton(TVector, VectorLista16, T )
            Valor17 = InterNewton(TVector, VectorLista17, T )
            Valor18 = InterNewton(TVector, VectorLista18, T )
            Valor19 = InterNewton(TVector, VectorLista19, T )
            Valor20 = InterNewton(TVector, VectorLista20, T )
            Valor21 = InterNewton(TVector, VectorLista21, T )
            Valor22 = InterNewton(TVector, VectorLista22, T )
            Valor23 = InterNewton(TVector, VectorLista23, T )
            Valor24 = InterNewton(TVector, VectorLista24, T )
            Valor25 = InterNewton(TVector, VectorLista25, T )
            Valor26 = InterNewton(TVector, VectorLista26, T )
            Valor27 = InterNewton(TVector, VectorLista27, T )
            Valor28 = InterNewton(TVector, VectorLista28, T )
            Valor29 = InterNewton(TVector, VectorLista29, T )
            Valor30 = InterNewton(TVector, VectorLista30, T )
            Valor31 = InterNewton(TVector, VectorLista31, T )
            Valor32 = InterNewton(TVector, VectorLista32, T )
            Valor33 = InterNewton(TVector, VectorLista33, T )
            Valor34 = InterNewton(TVector, VectorLista34, T )
            Valor35 = InterNewton(TVector, VectorLista35, T )
            Valor36 = InterNewton(TVector, VectorLista36, T )
            
            
            
            Valores = [Valor1,Valor2,Valor3,Valor4,Valor5,Valor6, Valor7, Valor8, Valor9, Valor10, Valor11, Valor12, Valor13, Valor14, Valor15, Valor16, Valor17, Valor18, Valor19, Valor20, Valor21, Valor22, Valor23, Valor24, Valor25, Valor26, Valor27, Valor28, Valor29, Valor30, Valor31, Valor32, Valor33, Valor34, Valor35, Valor36]
            Valores = Valores[::-1] 
            xVector, Falso = Vectores(Valores,Valores, PRO)
            xVector = xVector[::-1]
            i = 0
            for x in Valores:
                if x == xVector[0]:
                    x1 = i
                if x == xVector[1]:
                    x2 = i
                if x == xVector[2]:
                    x3 = i
                if x == xVector[3]:
                    x4 = i
                i = i+1
            
            P_Lista = P_Lista[::-1]
            yVector = [P_Lista[x1],P_Lista[x2],P_Lista[x3],P_Lista[x4]]


            P =InterNewton(xVector,yVector,PRO)
            Resultado = "{:.2f}".format(P)
            print("La presion es de " +Resultado+ "MPa")         
                        


    elif DATO == "6":
        print("Hasta pronto")
        break





    