class AssistenteVirtual:
    def __init__(self, nome="Maya"): #construtor da classe para iniciar a assistente virtual 
        self.nome = nome

    def cumprimentar(self):
        return f"Olá! Eu sou {self.nome}, sua assistente virtual. Como posso ajudar você hoje no hospital? 😊"

    def despedir(self):
        return f"Foi um prazer ajudar você! Tenha um ótimo dia e cuide-se bem! 🌸"

    def informar_erro(self, mensagem):
        return f"Desculpe, algo deu errado... {mensagem}. Não se preocupe, vou tentar ajudar de outra forma! 😊"

    def mensagem_sucesso(self, acao):
        return f"Ótimo! {acao} está concluído. Se precisar de algo mais, estou aqui! 🏥"
    
    def pedir_confirmacao(self, acao):
        return f"Você tem certeza que deseja {acao}? Responda 'sim' ou 'não' para confirmar. 🤔"
