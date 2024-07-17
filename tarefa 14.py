preço =  float(input('Digite o preço do produto'))
desconto =  preço - (15/100 * preço) 
print('O valor com desconto de 15% é de R${:.2f}'.format(desconto))
