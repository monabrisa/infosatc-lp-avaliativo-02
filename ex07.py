filmes = []
jogos = []
livros = []
esporte = []

#inserir os valores e os itens nas variaveis
filmes.insert(0, "Jogos vorazes")
filmes.insert(1, "Viuva negra")

jogos.insert(0, "Valorant")
jogos.insert(1, "Apex legends")

livros.insert(0, "Diario de Anne Frank")
livros.insert(1, "Diario de um banana")

esporte.insert(0, "Basquete")
esporte.insert(1, "Futebol")

tudo = [filmes, jogos, livros, esporte]#agrupar tudo em uma variavel

print("O item 1 dentro da lista de livros é: ", (livros[1]))#printar os livros dentro da lista

del esporte[1]#deletei o item de valor 1 da lista esportes

disciplinas = ['História', 'Português']#criar a lista de disciplinas

tudo_novo = [tudo + disciplinas]#agrupar as disciplinas junto com as outras listas

print("A lista de filmes: ", (filmes))
print("A lista de jogos: ", (jogos))
print("A lista de livros: ", (livros))
print("A lista de esportes: ", (esporte))
print("A lista de disciplinas: ", (disciplinas))
