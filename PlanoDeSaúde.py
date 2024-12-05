class PlanoDeSaude:
    def __init__(self):  #O construtor da classe que inicializa a lista de planos de saúde oferecidos (Plano Básico, Plano Avançado e Plano Premium).
        self.planos = [
            {"nome": "Plano Básico", "preco": "R$ 200/mês"},
            {"nome": "Plano Avançado", "preco": "R$ 400/mês"},
            {"nome": "Plano Premium", "preco": "R$ 600/mês"},
        ]

    def listar_planos(self):
        return self.planos
