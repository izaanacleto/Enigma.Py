mapa = {



    "6": "F",

    "5": "E",

    "50": "L",

    "1": "I",

    "26": "Z",

    "MM": "2000",

    "R": "18"

}



mensagem = "6550126MMR"





mensagem_final = ""

i = 0



while i < len(mensagem):

    if mensagem[i:i+2] in mapa:

        mensagem_final+= mapa[mensagem[i:i+2]]

        i += 2

    elif mensagem[i] in mapa:

        mensagem_final += mapa[mensagem[i]]

        i += 1



mensagem_final = mensagem_final.replace("200018", "2018") 



print(mensagem_final)