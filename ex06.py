lista = ['BMW X6', 'Supra MK5', 'Audi Q7', 'Mercedes AMG GT', 'Nissan GTR R34']
enc = input("Digite qual carro vôce quer e mostraremos sua posição na lista: ")
if (enc) in lista:
    print("Este item está na posição: ", lista.index(enc))
else:
    print("Não temos este carro na lista!")