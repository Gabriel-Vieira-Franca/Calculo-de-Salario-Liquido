import math
salarioB = float(input("Digite o Salário Bruto: "))
vale = input("Desncontar Vale Transporte? ")
dep  = int (input("Quantos dependetes possui? "))

dep = 189.90

#INSS
if salarioB < 1320.01:
    inss = float(salarioB*0.075)

elif salarioB < 2571.30:
    inss = float((salarioB-1320.00)*0.09 +99.00)

elif salarioB < 3856.95:
    inss = float((salarioB-2571.29)*0.12 + 211.62)

elif salarioB < 7507.49:
    inss = float((salarioB-3856.94)*0.14 + 365.9)

else:
    salarioB > 7507.50
    inss = float( 876.95)

 
#Vale Transporte
if vale == "Sim" or vale == "sim":
    Descvale = salarioB*0.06
else:
    Descvale = 0


#IRRF
bcirrf = salarioB - inss
bcirrf = bcirrf - dep
if bcirrf < 2112.01:
    irrf = float(bcirrf*0)

elif bcirrf < 2826.66:
    irrf = float(bcirrf*0.075 - 158.40)

elif bcirrf < 3751.06:
    irrf = float(bcirrf*0.15 - 370.40)

elif bcirrf <= 4664.68:
    irrf = float(bcirrf*0.2250 - 651.73)

else:
    bcirrf >= 4664.69 
    irrf = float(bcirrf*0.275 - 876.95)


#Saldo
desconto = float(inss + irrf + Descvale)
salarioL = float(salarioB - desconto)

#Impressão
print ("_____________________________________________")
print (f"Desconto de INSS: R${inss}")
print (f"Desconto de IRRF R${irrf}")
print (f"Desconto do Vale Transporte: R${Descvale}")
print (f"Seu salário líquido é de R${salarioL}")