Objetivo:
	Construir um jogo da forca.

Requisitos:

- O usuario deve poder chutar uma letra;
- O usuario deve poder vizualizar a letra formatada na palavra;
- O usuario deve ter um numero limitado de tentativas;
- A palavra da forca só deve aparecer se ou usario acertar a palavra ou chutar certo antes das suas vidas acabarem;
- 

Regras de negocio:

- O sistema deve receber os valores de chute;
- O sistema deve receber 1 valor por vez do usuario, nao mais que isso;
	- Caso o usuario chute dois digitos, deve retornar a informacao 
- O sistema deve verificar se existem espacos na entrada do valor do usuario;
	- caso sim, retirar;
- O sistema deve guardar a palavra chave numa estrutura de multiplos dados, como uma lista;
- O sistema deve comparar o dado de entrada do usuario com os dados que estao na lista da palavra chave;
	- Caso os dados forem iguais, deve retornar um print dos dados acertados na formatacao da palavra;
- A contagem do tamanho da palavra precisa ser dinamica, nao estatica, assim como a formatacao; 

