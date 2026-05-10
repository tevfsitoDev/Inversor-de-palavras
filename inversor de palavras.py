frase = input("Introduzca Uma Frase: ")
#aqui o usuário escreve a frase que será invertida
invertido= ""
#aqui serão almacenadas as letras a invertir
for almacen in frase:
    #aqui com "for" criamos a variável temporal "almacen", a qual vai pegar temporalmente as letras da variável "frase".
    invertido=almacen + invertido
    #Aqui estamos indicando que a letra a seguir este no primeiro lugar do índice fazendo que a palavra esteja invertida.

#basicamente é como escrever de frente pra atrás.
print(invertido)    