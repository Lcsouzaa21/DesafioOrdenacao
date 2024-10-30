def ordenar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            conteudo = file.read()

        numeros = list(map(int, conteudo.split()))

        for i in range(1, len(numeros)):
            chave = numeros[i]
            j = i - 1

            while j >= 0 and numeros[j] > chave:
                numeros[j + 1] = numeros[j]
                j -= 1
            numeros[j + 1] = chave

        print("Números prdenados: ", numeros)

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e o caminho.")
    except ValueError:
        print("Erro ao converter para números. Verifique o conteúdo do arquivo.")

ordenar_arquivo('extra.txt')