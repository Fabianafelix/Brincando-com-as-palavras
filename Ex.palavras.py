filename = "palavras.txt"

# 1 - Quantas palavras há no arquivo?

with open (filename, "r", encoding="utf-8") as f:  
    contador=0
    for linha in f:
        contador += 1
print("Há",contador,"palavras no português brasileiro")

                               
# 2 - Quantas vezes cada letra do alfabeto aparece no arquivo?

alfabeto= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","y","z"]

with open (filename, "r", encoding="utf-8") as f:
    for line in f:
        # Aqui faltou a lógica de contar as letras da palavra.
        # Note que o count está sendo realizado sobre a variável alfabeto, ou seja, ele vai contar a quantidade de ocorrências de uma letra no alfabeto, o que sempre será 1
        # Outro detalhe é que você precisa passar para o método o elemento que se deseja procurar.
        # Talvez você quisesse fazer algo como
        for letra in alfabeto:
            contagem_letra = line.count(letra)
        # Mas ainda falta a lógica de onde salvar a contagem geral de cada letra. Essa eu deixo pra você pensar ;)

# 3 - Quantas palavras começam com cada letra do alfabeto?


    
# 4 - Quantas palavras começam com as mesmas 3 letras do meu nome?


with open (filename, "r", encoding = "utf-8")as f:
    
    for line in f:
        # Vc implementou a lógica para verificar se a string "fab" está em algum lugar da variável line
        # Desse jeito ele contaria palavras como fabuloso, alfabeto e confabular, quando na verdade deveria pegar apenas fabuloso (por exemplo)
        # A lógica correta seria:
        if "fab" == line[:3]:  # Isso faz uma comparação apenas das três primeiras letras da palavra
            print (line)
            # No caso, o exercício pedia para você salvar em outro arquivo as palavras que atendessem ao critério.
            # A lógica para isso é parecida com a que você usou para ler o arquivo original, então acho que você logo consegue

# 5 - Quais palavras possuem todas as letras do meu nome.

name = ["f","a","b","i","n"]
cont=0
with open (filename, "r", encoding = "utf-8") as f:
    for linha in f:
        # A lógica deste é muito parecida com a do item anterior
        # Mas ao invés de comparar se as letras são iguais, você precisa verificar se todas existem na palavra
        # Então ficaria algo como
        contem_todas_letras = True
        for letra in name:
            if letra not in linha:
                # Note que a variável só vai ficar falsa se alguma letra do nome não estiver na linha
                contem_todas_letras = False
                break
        if contem_todas_letras:
            print (rep)
       
       
# Faltou o item do palindromo