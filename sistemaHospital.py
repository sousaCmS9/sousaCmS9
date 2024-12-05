from AssistenteVirtual import AssistenteVirtual
from PlanoDeSaúde import PlanoDeSaude
from usuario import Usuario
from consulta import Consulta

class HospitalSistema:
    def __init__(self):
        self.assistente = AssistenteVirtual()  
        self.plano_de_saude = PlanoDeSaude() 
        self.usuario_atual = None  

    def criar_conta(self):
        print(self.assistente.cumprimentar())  
        nome = input("Por favor, me diga seu nome completo: ")  
        idade = input(f"Quantos anos você tem, {nome}? ")  
        email = input("Qual é o seu e-mail? ")  
        self.usuario_atual = Usuario(nome, idade, email)  
        self.usuario_atual.salvar_em_arquivo()  
        print(f"Parabéns, {nome}! Sua conta foi criada com sucesso. Agora você pode aproveitar todos os recursos do hospital.")
        self.finalizar_opcao()

    def acessar_conta(self):
        nome = input("Digite seu nome para acessar sua conta: ")  
        usuario = Usuario.carregar_usuario(nome)
        if usuario:
            self.usuario_atual = usuario  
            print(f"Bem-vindo de volta, {self.usuario_atual.nome}! Estamos felizes em ter você novamente.") 
        else:
            print(self.assistente.informar_erro("Usuário não encontrado. Parece que você ainda não tem uma conta. Vamos criar uma agora mesmo?"))
        self.finalizar_opcao()

    def acessar_planos(self):
        print("\nAqui estão os planos de saúde que oferecemos. Escolha o que melhor se adapta a você:")
        for i, plano in enumerate(self.plano_de_saude.listar_planos(), 1): 
            print(f"{i}. {plano['nome']} - {plano['preco']}")
        self.finalizar_opcao()

    def marcar_consulta(self):
        if not self.usuario_atual:
            print(self.assistente.informar_erro("Você precisa acessar sua conta primeiro para marcar uma consulta."))  
            return

        especialidade = input("Qual especialidade você deseja consultar? (ex: Cardiologia): ") 
        data = input("Qual data seria conveniente para você? (ex: 10/12/2024): ") 

        consulta = Consulta(especialidade, data)
        self.usuario_atual.adicionar_consulta(consulta)  
        self.usuario_atual.salvar_em_arquivo()  

        print(self.assistente.mensagem_sucesso(f"Sua consulta foi marcada para {data} na especialidade de {especialidade}."))
        self.finalizar_opcao()

    def listar_consultas(self):
        if not self.usuario_atual:
            print(self.assistente.informar_erro("Você precisa acessar sua conta para ver suas consultas."))  
            return

        if self.usuario_atual.consultas:
            print(f"\nAqui estão as consultas agendadas para {self.usuario_atual.nome}:")  
            for consulta in self.usuario_atual.consultas:
                print(f"- Especialidade: {consulta.especialidade} | Data: {consulta.data}")  
        else:
            print("Você ainda não tem consultas agendadas. Que tal agendar uma agora?")
        self.finalizar_opcao()

    def editar_dados_usuario(self):
        if not self.usuario_atual:
            print(self.assistente.informar_erro("Você precisa acessar sua conta para editar seus dados."))  
            return

        print(f"Vamos atualizar seus dados, {self.usuario_atual.nome}. Se algo estiver correto, basta pressionar Enter para manter.")  
        novo_nome = input(f"Seu nome atual é {self.usuario_atual.nome}. Digite o novo nome (ou pressione Enter para manter): ") or self.usuario_atual.nome
        nova_idade = input(f"Sua idade atual é {self.usuario_atual.idade}. Digite a nova idade (ou pressione Enter para manter): ") or self.usuario_atual.idade
        novo_email = input(f"Seu e-mail atual é {self.usuario_atual.email}. Digite o novo e-mail (ou pressione Enter para manter): ") or self.usuario_atual.email

        self.usuario_atual.nome = novo_nome
        self.usuario_atual.idade = nova_idade
        self.usuario_atual.email = novo_email
        self.usuario_atual.salvar_em_arquivo()  

        print(self.assistente.mensagem_sucesso("Seus dados foram atualizados com sucesso!"))
        self.finalizar_opcao()

    def finalizar_opcao(self):
        opcao = input("\nDeseja realizar outra ação? (s) Sim / (n) Não: ").strip().lower()
        if opcao == 's':
            print("\nÓtimo! Vamos continuar.")
        elif opcao == 'n':
            print(self.assistente.despedir())  
            exit()
        else:
            print("Opção inválida. Vamos voltar ao menu principal.")
            self.iniciar()

    def iniciar(self):
        while True:
            print("\n=== Sistema Hospitalar ===")
            print("1. Criar Conta")
            print("2. Acessar Conta")
            print("3. Acessar Planos de Saúde")
            print("4. Marcar Consulta")
            print("5. Listar Consultas")
            print("6. Editar Dados do Usuário")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")  

            if opcao == "1":
                self.criar_conta()  
            elif opcao == "2":
                self.acessar_conta()  
            elif opcao == "3":
                self.acessar_planos()  
            elif opcao == "4":
                self.marcar_consulta() 
            elif opcao == "5":
                self.listar_consultas() 
            elif opcao == "6":
                self.editar_dados_usuario()  
            elif opcao == "7":
                print
