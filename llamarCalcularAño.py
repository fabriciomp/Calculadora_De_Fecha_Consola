import calculaDia
import colorama

colorama.init(convert=True)

print(colorama.Fore.GREEN+"Calcular un día de la semana cualquiera")
print(colorama.Fore.GREEN+"CalculaDORA DE FECHAS")
print(colorama.Fore.LIGHTRED_EX+"")
año= input("Ingresa año AAAA: ") 
mes= input("Ingresa mes mm: ") 
dia= input("Ingresa dia dd: ") 

año_Residuo_Año= calculaDia.AñoIngresado(año) #devuelve el año el residuo y el valor a restar
mes_devuelto = calculaDia.Mes_Ingresado(mes)#devuelve  codigo de mes 033615 625035
dia_Devuelto = calculaDia.Dia_Ingresado(dia)
mes_en_Texto= calculaDia.Texto_Mes(mes)



#print (año_Residuo_Año)
#print(mes, dia_Devuelto)
print(colorama.Fore.LIGHTBLUE_EX+"")

dia_Mostra =calculaDia.Calclcular_Dia(año_Residuo_Año[0], mes_devuelto, dia_Devuelto,año_Residuo_Año[1],año,mes )
print(f"El día {dia} de {mes_en_Texto} de {año} cayo un "+dia_Mostra)