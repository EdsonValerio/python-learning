class Amigo:
def __init__(self, nome) :
self.nome = nome

def lembrete(self):
return f"Olá, {self.nome}! Só um lembrete amigável: você não é especial!"

amigo = Amigo("Nome do seu amigo")
print(amigo.lembrete())