import math
salarioB = float(input("Digite o Salário Bruto: "))
#vale = input("Desncontar Vale Transporte? ")

if salarioB < 1302.01:
    salarioL = float(salarioB*0.075)
    print (f"Desconto de INSS R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salário Líquido R${salarioL}")
    
elif salarioB < 2571.30:
    salarioL = float(salarioB*0.09 - 19.53)
    print (f"Desconto de INSS R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salário Líquido R${salarioL}")
elif salarioB < 3856.94:
    salarioL = float(salarioB*0.12 - 96.67)
    print (f"Desconto de INSS R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salário Líquido R${salarioL}")
elif salarioB < 7507.49:
    salarioL = float(salarioB*0.14 - 173.81)
    print (f"Desconto de INSS R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salário Líquido R${salarioL}")
else:
    salarioB > 7507.50
    salarioL = float(salarioB - 876,95)
    print (f"Desconto de INSS R${salarioL}")
    salarioL = salarioB - salarioL
    print (f"Salário Líquido R${salarioL}")
    
    
    
    