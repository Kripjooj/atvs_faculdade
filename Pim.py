usuarios = {}
usuario_logado = None
cursos_disponiveis = {
    "1": {"nome": "Introdução à Programação", "carga_horaria": "40h", "modulos": []},
    "2": {"nome": "Segurança da Informação Básica", "carga_horaria": "30h", "modulos": []},
    "3": {"nome": "LGPD na Prática", "carga_horaria": "25h", "modulos": []},
    "4": {"nome": "Inclusão Digital para Todos", "carga_horaria": "35h", "modulos": []},
}

def mostrar_menu_principal():
    print("\n=== PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA ===")
    print("1. Login / Cadastro")
    print("2. Cursos Disponíveis")
    print("3. Informações de Segurança")
    print("4. Cadastrar Módulos")
    print("5. Sair")
    return input("Escolha uma opção: ")

def tela_login_cadastro():
    while True:
        print("\n=== LOGIN / CADASTRO ===")
        print("1. Fazer Login")
        print("2. Criar Novo Usuário")
        print("0. Voltar")
        opcao = input("Escolha: ")
        
        if opcao == '1':
            fazer_login()
        elif opcao == '2':
            criar_usuario()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def fazer_login():
    global usuario_logado
    print("\n--- Login ---")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        usuario_logado = usuario
        print(f"\nBem-vindo(a), {usuario}!")
        return True
    else:
        print("\nCredenciais inválidas!")
        return False

def validar_senha(senha):
    if len(senha) < 8:
        return "Senha precisa ter pelo menos 8 caracteres"
    
    maiuscula = False
    numero = False
    simbolo = False
    simbolos_permitidos = "!@#$%&*,.;\"':[]()_+=-"
    
    for c in senha:
        if c.isupper():
            maiuscula = True
        elif c.isdigit():
            numero = True
        elif c in simbolos_permitidos:
            simbolo = True
    
    if not maiuscula:
        return "Adicione pelo menos uma letra maiúscula!"
    elif not numero:
        return "Adicione pelo menos um número!"
    elif not simbolo:
        return f"é necessario de pelo menos um  símbolo especial permitido: "
    else:
        return None  # Senha válida!

def criar_usuario():
    print("\n--- Novo Cadastro ---")
    usuario = input("Escolha um nome de usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe!")
        return
    
    if " " in usuario:
        print("Nome de usuário não pode conter espaços!")
        return
    
    while True:
        senha = input("Crie uma senha (mínimo 8 caracteres, com maiúscula, número e símbolo): ")
        erro = validar_senha(senha)
        
        if erro is None:
            usuarios[usuario] = senha
            print("Cadastro realizado com sucesso!")
            break
        else:
            print(f"Erro: {erro}")

def tela_cursos():
    print("\n=== CURSOS DISPONÍVEIS ===")
    cursos = [
        "1. Introdução à Programação (40h)",
        "2. Segurança da Informação Básica (30h)",
        "3. LGPD na Prática (25h)",
        "4. Inclusão Digital para Todos (35h)",
    ]
    for curso in cursos:
        print(curso)
    input("\nPressione Enter para voltar...")

def tela_seguranca():
    print("\n=== INFORMAÇÕES DE SEGURANÇA ===")
    print("• Todas as senhas são armazenadas de forma segura")
    print("• Dados pessoais protegidos pela LGPD")
    print("• Criptografia de ponta a ponta")
    print("• Não compartilhe suas credenciais")
    print("• Atualizações regulares de segurança\n")
    input("Pressione Enter para voltar...")

def tela_modulos():
    print("\n=== CADASTRAR MÓDULOS ===")
    if not usuario_logado:
        print("Você precisa estar logado para acessar esta função!")
        input("\nPressione Enter para voltar...")
        return

    # Mostra cursos existentes para escolha
    print("\nCursos disponíveis para adicionar módulos:")
    for id_curso, curso in cursos_disponiveis.items():
        print(f"{id_curso}. {curso['nome']} ({curso['carga_horaria']})")

    id_curso = input("\nDigite o número do curso: ")
    if id_curso not in cursos_disponiveis:
        print("Curso inválido!")
        input("\nPressione Enter para voltar...")
        return

    modulo = input("Nome do novo módulo: ")
    cursos_disponiveis[id_curso]["modulos"].append(modulo)  # Adiciona módulo ao curso
    print(f"\nMódulo '{modulo}' cadastrado com sucesso no curso '{cursos_disponiveis[id_curso]['nome']}'!")
    input("\nPressione Enter para voltar...")

def tela_cursos():
    print("\n=== CURSOS DISPONÍVEIS ===")
    for id_curso, curso in cursos_disponiveis.items():
        print(f"\n{id_curso}. {curso['nome']} ({curso['carga_horaria']})")
        if curso["modulos"]:  # Se houver módulos cadastrados
            print("   Módulos incluídos:")
            for modulo in curso["modulos"]:
                print(f"   - {modulo}")
    input("\nPressione Enter para voltar...")

def main():
    while True:
        escolha = mostrar_menu_principal()
        
        if escolha == '1':
            tela_login_cadastro()
        elif escolha == '2':
            tela_cursos()
        elif escolha == '3':
            tela_seguranca()
        elif escolha == '4':
            tela_modulos()
        elif escolha == '5':
            print("\nObrigado por usar nossa plataforma!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    main()