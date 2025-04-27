

def test_lista_vazia():
    frutas = ['banana', 'limao', 'laranja']
    frutas.append('manga')
    print("Lista de frutas disponíveis:", frutas)

    try:
        frutas_comprar = input('Digite o nome da fruta que deseja comprar: ')
        if frutas_comprar in frutas:
            print('A fruta está na lista.')
        else:
            add = input('Fruta não encontrada. Deseja adicionar? (s/n): ').strip().lower()
            if add == 's':
                frutas.append(frutas_comprar)
                print('Fruta adicionada com sucesso.')
            else:
                print('Fruta não adicionada.')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executando o teste
test_lista_vazia()


