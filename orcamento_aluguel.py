"""
Projeto: Orçamento de Aluguel - Imobiliária R.M
Disciplina: Algorithmic Thinking & Introduction to Object-Oriented Programming
Autor: Eduardo Souza Mattos (R.A. 35984)
Centro Universitário UniFECAF - 2026

Aplicação que gera o orçamento mensal de aluguel (Apartamento, Casa ou
Estúdio), aplica os acréscimos/descontos definidos pela imobiliária,
calcula a parcela do contrato imobiliário e exporta as 12 parcelas do
orçamento para um arquivo .csv.
"""

import csv
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Classe abstrata (base) - representa o conceito geral de Imóvel
# ---------------------------------------------------------------------------
class Imovel(ABC):
    """Classe base abstrata para qualquer tipo de imóvel administrado pela R.M."""

    VALOR_CONTRATO = 2000.00
    MAX_PARCELAS_CONTRATO = 5

    def __init__(self, quartos: int = 1, garagem: bool = False):
        self.quartos = quartos
        self.garagem = garagem

    @abstractmethod
    def calcular_valor_mensal(self) -> float:
        """Cada subclasse implementa sua própria regra de cálculo."""
        raise NotImplementedError

    def calcular_parcela_contrato(self, num_parcelas: int = 5) -> float:
        """Calcula o valor de cada parcela do contrato (até 5 vezes)."""
        num_parcelas = max(1, min(num_parcelas, self.MAX_PARCELAS_CONTRATO))
        return round(self.VALOR_CONTRATO / num_parcelas, 2)


# ---------------------------------------------------------------------------
# Apartamento
# ---------------------------------------------------------------------------
class Apartamento(Imovel):
    VALOR_BASE = 700.00
    ACRESCIMO_2_QUARTOS = 200.00
    ACRESCIMO_GARAGEM = 300.00
    DESCONTO_SEM_CRIANCAS = 0.05  # 5%

    def __init__(self, quartos: int = 1, garagem: bool = False, tem_criancas: bool = True):
        super().__init__(quartos, garagem)
        self.tem_criancas = tem_criancas

    def calcular_valor_mensal(self) -> float:
        valor = self.VALOR_BASE
        if self.quartos >= 2:
            valor += self.ACRESCIMO_2_QUARTOS
        if self.garagem:
            valor += self.ACRESCIMO_GARAGEM
        if not self.tem_criancas:
            valor -= valor * self.DESCONTO_SEM_CRIANCAS
        return round(valor, 2)


# ---------------------------------------------------------------------------
# Casa
# ---------------------------------------------------------------------------
class Casa(Imovel):
    VALOR_BASE = 900.00
    ACRESCIMO_2_QUARTOS = 250.00
    ACRESCIMO_GARAGEM = 300.00

    def calcular_valor_mensal(self) -> float:
        valor = self.VALOR_BASE
        if self.quartos >= 2:
            valor += self.ACRESCIMO_2_QUARTOS
        if self.garagem:
            valor += self.ACRESCIMO_GARAGEM
        return round(valor, 2)


# ---------------------------------------------------------------------------
# Estúdio
# ---------------------------------------------------------------------------
class Estudio(Imovel):
    VALOR_BASE = 1200.00
    VAGAS_INCLUSAS = 2
    VALOR_VAGAS_INCLUSAS = 250.00
    VALOR_VAGA_EXTRA = 60.00

    def __init__(self, vagas_estacionamento: int = 0):
        # Estúdio não segue o conceito de "quartos"/"garagem" tradicional
        super().__init__(quartos=0, garagem=False)
        self.vagas_estacionamento = vagas_estacionamento

    def calcular_valor_mensal(self) -> float:
        valor = self.VALOR_BASE
        if self.vagas_estacionamento > 0:
            valor += self.VALOR_VAGAS_INCLUSAS
            vagas_extras = max(0, self.vagas_estacionamento - self.VAGAS_INCLUSAS)
            valor += vagas_extras * self.VALOR_VAGA_EXTRA
        return round(valor, 2)


# ---------------------------------------------------------------------------
# Orçamento - orquestra o cálculo mensal e a geração do arquivo .csv
# ---------------------------------------------------------------------------
class Orcamento:
    MESES = 12

    def __init__(self, imovel: Imovel, num_parcelas_contrato: int = 5):
        self.imovel = imovel
        self.num_parcelas_contrato = num_parcelas_contrato
        self.valor_mensal = imovel.calcular_valor_mensal()
        self.parcela_contrato = imovel.calcular_parcela_contrato(num_parcelas_contrato)

    def gerar_parcelas(self) -> list:
        """Retorna uma lista com as 12 parcelas do orçamento anual."""
        parcelas = []
        for mes in range(1, self.MESES + 1):
            contrato_no_mes = self.parcela_contrato if mes <= self.num_parcelas_contrato else 0.00
            total_mes = round(self.valor_mensal + contrato_no_mes, 2)
            parcelas.append({
                "mes": mes,
                "aluguel": self.valor_mensal,
                "parcela_contrato": round(contrato_no_mes, 2),
                "total": total_mes,
            })
        return parcelas

    def exibir_resumo(self):
        print(f"\nTipo de imóvel: {type(self.imovel).__name__}")
        print(f"Valor mensal do aluguel: R$ {self.valor_mensal:.2f}")
        print(f"Parcela do contrato ({self.num_parcelas_contrato}x): R$ {self.parcela_contrato:.2f}")
        print("\nOrçamento das 12 parcelas:")
        for p in self.gerar_parcelas():
            print(f"  Mês {p['mes']:02d}: Aluguel R$ {p['aluguel']:.2f} "
                  f"+ Contrato R$ {p['parcela_contrato']:.2f} "
                  f"= Total R$ {p['total']:.2f}")

    def exportar_csv(self, caminho_arquivo: str = "orcamento_aluguel.csv"):
        parcelas = self.gerar_parcelas()
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(["Mes", "Valor_Aluguel", "Parcela_Contrato", "Total_Mensal"])
            for p in parcelas:
                escritor.writerow([p["mes"], f"{p['aluguel']:.2f}",
                                    f"{p['parcela_contrato']:.2f}", f"{p['total']:.2f}"])
        print(f"\nArquivo '{caminho_arquivo}' gerado com sucesso!")


# ---------------------------------------------------------------------------
# Camada de interação com o usuário (entrada/validação de dados)
# ---------------------------------------------------------------------------
def ler_inteiro(mensagem: str, minimo: int = None, maximo: int = None) -> int:
    """Valida entrada numérica usando laço while, conforme visto na disciplina."""
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            numero = int(valor)
            if (minimo is None or numero >= minimo) and (maximo is None or numero <= maximo):
                return numero
        print("Entrada inválida. Tente novamente.")


def ler_sim_nao(mensagem: str) -> bool:
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print("Responda apenas com S ou N.")


def montar_imovel() -> Imovel:
    print("\nTipos de imóvel disponíveis:")
    print("1 - Apartamento (R$ 700,00)")
    print("2 - Casa (R$ 900,00)")
    print("3 - Estúdio (R$ 1.200,00)")

    opcao = ler_inteiro("Escolha o tipo de imóvel (1/2/3): ", minimo=1, maximo=3)

    if opcao == 1:
        quartos = ler_inteiro("Número de quartos (1 ou 2): ", minimo=1, maximo=2)
        garagem = ler_sim_nao("Deseja incluir garagem? (S/N): ")
        tem_criancas = ler_sim_nao("Possui crianças? (S/N): ")
        return Apartamento(quartos=quartos, garagem=garagem, tem_criancas=tem_criancas)

    elif opcao == 2:
        quartos = ler_inteiro("Número de quartos (1 ou 2): ", minimo=1, maximo=2)
        garagem = ler_sim_nao("Deseja incluir garagem? (S/N): ")
        return Casa(quartos=quartos, garagem=garagem)

    else:
        vagas = ler_inteiro("Quantidade de vagas de estacionamento (0 se nenhuma): ", minimo=0)
        return Estudio(vagas_estacionamento=vagas)


def main():
    print("=== Imobiliária R.M - Gerador de Orçamento de Aluguel ===")
    imovel = montar_imovel()
    num_parcelas = ler_inteiro("Em quantas vezes deseja parcelar o contrato (1 a 5): ", minimo=1, maximo=5)

    orcamento = Orcamento(imovel, num_parcelas_contrato=num_parcelas)
    orcamento.exibir_resumo()
    orcamento.exportar_csv("orcamento_aluguel.csv")


if __name__ == "__main__":
    main()