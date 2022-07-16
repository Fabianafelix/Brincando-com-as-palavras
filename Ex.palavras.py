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
        repeticao=alfabeto.count("")
    print (line)

# 3 - Quantas palavras começam com cada letra do alfabeto?


    
# 4 - Quantas palavras começam com as mesmas 3 letras do meu nome?


with open (filename, "r", encoding = "utf-8")as f:
    
    for line in f:
        if "fab" in line:
            print (line)

# 5 - Quais palavras possuem todas as letras do meu nome.

name = ["f","a","b","i","n"]
cont=0
with open (filename, "r", encoding = "utf-8") as f:
    for linha in f:
        rep = name.count ("a")
        print (rep)
       
