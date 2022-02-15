
def separa_centena(numero):
    centena = int(numero / 100)
    return centena

def separa_dezena(numero):
    dezena = int((numero % 100) / 10)
    return dezena

def separa_unidade(numero):
    unidade = int(((numero % 100) % 10))
    return unidade

def escreve_centena(centena):
    lista=['cento','duzentos','trezentos','quatrocentos','quinhentos','seissentos','setessentos','oitossentos','novessentos']
    return lista[centena-1]

def escreve_dezena(dezena,unidade):
    if(dezena == 1):
        soma=dezena+unidade
        lista = ['dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove']
        return lista[soma - 1]
    else:
        lista = ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
        return lista[dezena-2]

def escreve_unidade(unidade):
    if(unidade==0):
        return 'zero'
    else:
        lista = ['um','dois','três','quatro','cinco','seis','sete','oito','nove']
        return lista[unidade-1]

def verifica(dezena, unidade):
    if(dezena==0 and unidade==0):
        return 1
    else:
        return 0

def numero_por_extenso(numero):

    centena = separa_centena(numero)
    dezena = separa_dezena(numero)
    unidade = separa_unidade(numero)

    ver = verifica(dezena,unidade)
    print("Numero: ",centena, dezena, unidade)

    if (centena==1 and ver == 1):
        print("cem")

    if (centena!=1 and centena!= 0 and ver == 1):
        escrita_centena = escreve_centena(centena)
        print(escrita_centena)

    if(centena==0 and dezena>=2 and unidade!=0):
        escrita_dezena=escreve_dezena(dezena,unidade)
        escrita_unidade=escreve_unidade(unidade)
        print("{} e {}".format(escrita_dezena,escrita_unidade))

    if (centena == 0 and dezena == 1 and unidade != 0):
        escrita_dezena = escreve_dezena(dezena,unidade)

        print("{}".format(escrita_dezena))

    if (centena == 0 and dezena != 0 and unidade == 0):
        escrita_dezena = escreve_dezena(dezena,unidade)
        escrita_unidade = escreve_unidade(unidade)
        print("{}".format(escrita_dezena))

    if(centena>=1 and dezena !=0 and unidade!=0):
        escrita_centena = escreve_centena(centena)
        escrita_dezena=escreve_dezena(dezena,unidade)
        escrita_unidade=escreve_unidade(unidade)
        print("{} e {} e {}".format(escrita_centena,escrita_dezena,escrita_unidade))

    if (centena==0 and dezena==0):
        print(escreve_unidade(unidade))

    if(centena>=1 and dezena==0 and unidade!=0):
        print("{} e {}".format(escreve_centena(centena),escreve_unidade(unidade)))

if(__name__=="__main__"):
    numero = input('Digite um numero entre 1 e 999: ')
    numero = int(numero)
    numero_por_extenso(numero)







