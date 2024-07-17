largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede'))
metroquadrado = (largura * altura)
litro = metroquadrado / 2
print('Sua parede tem uma dimensão de {}x{} e a sua área é de {}M².'.format(largura, altura, metroquadrado))
print('Para pintar esta parede, você precisará de {:.2f}Litros de tinta.'.format(litro))
