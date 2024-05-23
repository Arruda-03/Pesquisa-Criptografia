listaBin = [2**i for i in range(29)] + [' ']
listaAlf = list('abcdefghijklmnopqrstuvwxyz')

listaFatiados = []

def conversao(char):
    if char in listaAlf:
        return listaBin[listaAlf.index(char)]
    else:
        return None

def fatiarInput(palavra):
    segmentos = []
    segmento = ''
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    for char in palavra:
        if char not in alfabeto:
            continue
        if segmento and char <= segmento[-1]:
            segmentos.append(segmento)
            segmento = ''
        segmento += char

    if segmento:
        segmentos.append(segmento)

    return segmentos

def addListaBin(segmento):
    return [conversao(char) for char in segmento]

def somarCrip(lista_bin):
    return sum(lista_bin)

def somarChave(valor_crip, chave):
    chave_int = int(chave)
    return valor_crip + chave_int

def dividirChave(valor_crip, chave):
    chave_int = int(chave)
    return valor_crip - chave_int

def descrip(valor_int):
    resultado = []
    while valor_int > 0:
        potencia = valor_int.bit_length() - 1
        resultado.append(listaAlf[potencia])
        valor_int -= 2**potencia
    return ''.join(resultado[::-1])

def main():
    while True:
        print("\n0.Para sair do programa.\n1.Para criptografar\n2.Para descriptografar.")
        try:
            crip_descrip = int(input(": "))
        except ValueError:
            print("Entrada inválida. Por favor, digite 0, 1 ou 2.")
            continue

        if crip_descrip == 1:
            regras = int(input("Para usar o programa corretamente, o usuário precisa seguir algumas regras.\n1.Para ler as regras: "))
            if regras == 1:
                print("[O usuário só poderá utilizar letras minúsculas, sem caractere especial e sem acentos.]")
            else:
                print("Continuar sem ler as regras.")

            palavra = input("Digite a palavra completa a ser criptografada: ").strip()
            if not palavra.islower() or not palavra.isalpha():
                print("Entrada inválida. Por favor, insira uma palavra válida.")
                continue

            segmentos = fatiarInput(palavra)
            w = float(input("Digite a sua chave: "))

            listaPalavra = []
            for segmento in segmentos:
                y = addListaBin(segmento)
                z = somarCrip(y)
                listaPalavra.append(somarChave(z, w))

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
            chaved = int(input("Digite a chave para descriptografar: "))
            for i in range(cont2):
                while True:
                    try:
                        decimal_binario = int(input(f"Digite em decimal o número do segmento {i + 1}: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número seguindo as regras do programa.")
                valor_chave = dividirChave(decimal_binario, chaved)
                lista_binarios.append(descrip(valor_chave))

            print("Sua palavra descriptografada é: ", ''.join(lista_binarios))

        elif crip_descrip == 0:
            print("Programa encerrado.")
            break
        else:
            print("Resposta incorreta. Por favor, digite 0, 1 ou 2.")

main()
