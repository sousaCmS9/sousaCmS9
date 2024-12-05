from consulta import Consulta

class Usuario:
    def __init__(self, nome, idade, email): #O construtor da classe, que inicializa as propriedades do usuário (nome, idade, e-mail) e cria uma lista vazia de consultas.
        self.nome = nome
        self.idade = idade
        self.email = email
        self.consultas = []  # Lista de consultas

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def salvar_em_arquivo(self):
        # Lógica de salvar os dados do usuário em um arquivo
        with open(f"{self.nome}_dados.txt", "w") as arquivo:
            arquivo.write(f"Nome: {self.nome}\nIdade: {self.idade}\nEmail: {self.email}\n")
            for consulta in self.consultas:
                arquivo.write(f"Consulta: {consulta.especialidade} - {consulta.data}\n")

    @staticmethod #@staticmethod decorador utilizado para definir métodos dentro de uma classe que não dependem do estado da instância (ou seja, não precisam acessar ou modificar os atributos da instância).
    def carregar_usuario(nome):
        try: # tentar executar um bloco de código que pode gerar um erro (uma exceção). fazendo que o código não seja interrompido durante a execulção 
            with open(f"{nome}_dados.txt", "r") as arquivo: #  with usado para abrir arquivos e garantir que, após o uso, o arquivo será fechado corretamente
                dados = arquivo.readlines() #as cria um alias (ou referência) para o objeto que está sendo manipulado dentro do bloco de código
                nome = dados[0].strip().split(": ")[1] #strip remover espaços em branco ou outros caracteres indesejados do início e do final de uma string
                idade = dados[1].strip().split(": ")[1] # split dividir uma string em uma lista, usando um separador específico
                email = dados[2].strip().split(": ")[1]
                usuario = Usuario(nome, idade, email)
                for linha in dados[3:]:
                    especialidade, data = linha.strip().split(" - ")
                    usuario.adicionar_consulta(Consulta(especialidade.split(": ")[1], data))
                return usuario
        except FileNotFoundError: #except é usada em conjunto com a palavra-chave try para lidar com exceções (erros) que podem ocorrer durante a execução do código
            return None

    def excluir_conta(self):
        # Lógica para excluir a conta do usuário
        pass
