dias = int(input('quantidade de dias pelos quais o carro foi alugado:'))
km = float(input('Por favor, digite a quilometragem do carro:')) 
totaldias = dias * 60
totalkm = km * 0.15
totalvalor = totaldias + totalkm
print(f'O total a se pagar por {dias} dias e {km}Km rodados, é de: R${totalvalor} (R${totaldias} pelos dias, R${totalkm} pela quilometragem)')
