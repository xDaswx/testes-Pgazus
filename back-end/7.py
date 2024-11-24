#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra 


"""

Aqui eu decidi criar uma lista que tem 9 items aleatorios,
a variavel i é uma variavel usada para auto increment que aumenta em 1 a cada repetição, o foco dela é armazenar um valor inteiro;
quando esse valor inteiro é menor ou igual a 5 o while deve parar.


para realizar o auto increment em questão utilizamos o operador += (mais igual) onde é basicamente uma soma do valor atual da variavel,  i + 1 = ???
posso dizer que na minha opinião não é uma boa prática, geralmente utilizamos for n in range(value), onde "value" representa quantas vezes tal ação deve
ser feita

"""

lista = [3,4,2,3,6,3,5,1,2]
i = 0
while i <= 5:
    print(lista[i])
    i += 1 # o numero 1 representa o quanto o valor deve aumentar em cada loop, nesse caso a cada loop a variavel aumenta + 1.