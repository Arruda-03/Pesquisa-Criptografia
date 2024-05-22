listaBin = [2**0,2**1,2**2,2**3,2**4,2**5,2**6,2**7,2**8,2**9,2**10,2**11,2**12,
            2**13,2**14,2**15,2**16,2**17,2**18,2**19,2**20,2**21,2**22,2**23,2**24,
            2**25,2**26,2**27,2**28,' ']

listaAlf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z','.','-','#',' ']


listaFatiados = []

def conversao(x):
    if x == listaAlf[0]:
        res = listaBin[0]
    elif x == listaAlf[1]:
        res = listaBin[1]
    elif x == listaAlf[2]:
        res = listaBin[2]
    elif x == listaAlf[3]:
        res = listaBin[3]
    elif x == listaAlf[4]:
        res = listaBin[4]
    elif x == listaAlf[5]:
        res = listaBin[5]
    elif x == listaAlf[6]:
        res = listaBin[6]
    elif x == listaAlf[7]:
        res = listaBin[7]
    elif x == listaAlf[8]:
        res = listaBin[8]
    elif x == listaAlf[9]:
        res = listaBin[9]
    elif x == listaAlf[10]:
        res = listaBin[10]
    elif x == listaAlf[11]:
        res = listaBin[11]
    elif x == listaAlf[12]:
        res = listaBin[12]
    elif x == listaAlf[13]:
        res = listaBin[13]
    elif x == listaAlf[14]:
        res = listaBin[14]
    elif x == listaAlf[15]:
        res = listaBin[15]
    elif x == listaAlf[16]:
        res = listaBin[16]
    elif x == listaAlf[17]:
        res = listaBin[17]
    elif x == listaAlf[18]:
        res = listaBin[18]
    elif x == listaAlf[19]:
        res = listaBin[19]
    elif x == listaAlf[20]:
        res = listaBin[20]
    elif x == listaAlf[21]:
        res = listaBin[21]
    elif x == listaAlf[22]:
        res = listaBin[22]
    elif x == listaAlf[23]:
        res = listaBin[23]
    elif x == listaAlf[24]:
        res = listaBin[24]
    elif x == listaAlf[25]:
        res = listaBin[25]
    elif x == listaAlf[26]:
        res = listaBin[26]
    elif x == listaAlf[27]:
        res = listaBin[27]
    elif x == listaAlf[28]:
        res = listaBin[28]
    elif x == listaAlf[29]:
        res == listaBin[29]
    return res


def fatiarInput(x):
    listaFatiar = []
    for i in range(0, len(x),):
        listaFatiar.append(x[0])
        x = x[1:len(x)]
    return listaFatiar

def addListaBin(x,y):
    listaConvertidos = []
    res = listaConvertidos
    cont = len(x)
    while cont > 0:
        conversao(y[0])
        listaConvertidos.append(conversao(y[0]))
        y = y[1:len(y)]
        cont = cont - 1
    return res
  
       
def somarCrip(x):
    soma = 0
    for x in x:
        soma += x
    return soma
    
def somarChave(x,y):
    b = x*y
    return b

def dividirChave(b,y):
    x = b//y
    return x

def separarPalavras(x):
    for i in x():
        x1 = x.split()
    return x1
    

def descrip(x):
    import string
    a = bin(x)
    listaAlfabeto = list(string.ascii_lowercase)[::-1]
    lista_binarios = list(str(a))
    lista_binarios = lista_binarios[2:]
    correspondencias = []
    offset = len(listaAlfabeto) - len(lista_binarios)
    
    for i in range(len(lista_binarios)):
        if lista_binarios[i] == '1':
            correspondencias.append(listaAlfabeto[offset + i])
    return ''.join(correspondencias)[::-1]







def teste():
    x = int(input("input num p bin: "))
    y = int(input("input chave"))
    dividirChave(x,y)
    print(dividirChave(x,y))
    





def main():
    while True:
        listaPalavra = []
        print("\n0.Para sair do programa.\n1.Para criptografar\n2.Para descriptografar.")

        crip_descrip = int(input(": "))
  
        if crip_descrip == 1:
            regras = int(input("Para usar o programa corretamente, o usuário precisa seguir algumas regras.\n1.Para ler as regras: "))
            if regras == 1:
                print("[Para criptografar o usuário precisa separar a palavra em 'segmentos'.\nO usuário só poderá utilizar letras minúsculas e sem acentos.")
                print("Para separar a palavra, o usuário deve separar cada segmento onde o mesmo percorra o alfabeto e não repita nenhuma letra.")
                print("Exemplo: renata, segmento 1: r, segmento 2: en, segmento 3: at, segmento 4: a")
                print("A palavra renata possui 4 segmentos, seguindo a lógica alfabética e sem repetir letra ou voltar o alfabeto em cada segmento.]")
            else:
                print("Continuar sem ler as regras.")

            cont = int(input("Digite quantos segmentos sua palavra possui: "))
            if cont > 0:
                for i in range(1, cont + 1):
                    segmento = i
            w = float(input("Digite a sua chave: "))
            while cont > 0:
                x = input("Digite a palavra do segmento {} a ser criptografada: ".format(segmento))
                if x.strip() == '':
                    print("Entrada inválida. Por favor, insira uma palavra válida.")
                    continue
                fatiarInput(x)
                y = fatiarInput(x)
                addListaBin(x, y)
                z = addListaBin(x, y)
                somarCrip(z)
                v = somarCrip(z)
                listaPalavra.append(somarChave(v, w))
                segmento -= 1
                cont -= 1

            print("Sua palavra criptografada é: ", listaPalavra)
        elif crip_descrip == 2:
            regras = int(input("Para usar o programa corretamente, o usuário precisa seguir algumas regras.\n1.Para ler as regras: "))
            if regras == 1:
                print("[O usuário só poderá utilizar números decimais sem pontos '.' ou vírgulas ','.")
                print("O usuário precisa do acesso a chave para descriptografar, caso contrário a frase/palavra será impressa incorretamente.]")
            else:
                print("Continuar sem ler as regras.")
                
            lista_binarios = []
            cont2 = int(input("Digite quantos segmentos suas cifras criptografadas possuem: "))
            if cont2 > 0:
                for i in range(1, cont2+1):
                    segmento2 = i
                chaved = int(input("Digite a chave para descriptografar: "))
                while cont2 > 0:
                    while True:
                        try:
                            decimal_binario = int(input("Digite em decimal o número do segmento {}: ".format(segmento2)))
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número seguindo as regras do programa.")
                    binario_chave = dividirChave(decimal_binario,chaved)
                    descrip(binario_chave)
                    lista_binarios.append(descrip(binario_chave))
                    cont2 -= 1
                    segmento2 -= 1
                print("Sua palavra descriptografada é: ", ''.join(lista_binarios))
        elif crip_descrip == 0:
            print("Programa encerrado.")
            break
        else:
            print("Resposta incorreta. Por favor, digite 0, 1 ou 2.")

main()
