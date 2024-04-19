#Interface inicial
def primeiratela():
    print('====================== MEU CARRO PORTO ======================')
    print('Seja bem vindo ao app Meu Carro Porto!')


#Funções
def menuprincipal ():
    print('====================== MENU PRINCIPAL ======================')
    print('[1] - Onde posso acessar o site da Porto?')
    print('[2] - Meu carro está com um problema')
    print('[3] - Chamar um mecânico')
    print('[4] - O que é o aplicativo Meu Carro Porto?')
    print('[5] - Sair do aplicativo')
    
def tela1():
    print('|----------------------------------------------------------------------------|')
    print('|Você pode acessar o site da Porto pelo link: https://encurtador.com.br/cekIQ|')
    print('|----------------------------------------------------------------------------|')
def tela2():
    print('|-------------------------------------------------------------------------------------------|')
    print('|Use o link de acesso do aplicativo para entrar em contato com a Porto e resolver o problema|')
    print('|-------------------------------------------------------------------------------------------|')
def tela3():
    print('|--------------------------------------------|')
    print('|Um guincho será enviado para sua localização|')
    print('|--------------------------------------------|')
def tela4():
    print('|-----------------------------------------------------------------------------------------|')
    print('|É um aplicativo desenvolvido em Python para te ajudar a entrar em contato com um mecânico|')
    print('|-----------------------------------------------------------------------------------------|')

#Navegando pelo menu
def main():
    while True:
        primeiratela()
        menuprincipal()

        escolha = input('Para navegar pelo aplicativo, por favor digite um número: ')

        if escolha == "1":
            tela1()
        elif escolha == "2":
            tela2()
        elif escolha == "3":
            tela3()
        elif escolha == "4":
            tela4()
        elif escolha == "5":
            break
        else:
            print('|-------------------------------------------|')
            print('|Opção inválida! Por favor, digite novamente|')
            print('|-------------------------------------------|')
if __name__ == "__main__":
    main()
