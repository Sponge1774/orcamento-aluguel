# Orçamento de Aluguel — Imobiliária R.M
### Rental Budget Generator — R.M Real Estate

🇧🇷 [Português](#-português) | 🇺🇸 [English](#-english)

---

## 🇧🇷 Português

Aplicação em Python, desenvolvida com Programação Orientada a Objetos, para geração de orçamentos de locação (Apartamento, Casa ou Estúdio) para a empresa fictícia R.M.

**Disciplina:** Algorithmic Thinking & Introduction to Object-Oriented Programming
**Instituição:** Centro Universitário UniFECAF
**Autor:** Eduardo Souza Mattos — R.A. 35984
**Ano:** 2026

### Descrição

O programa solicita ao usuário o tipo de imóvel desejado e os dados específicos de cada tipo, calcula o valor mensal do aluguel aplicando as regras de negócio da R.M., calcula a parcela do contrato imobiliário (parcelável em até 5 vezes) e gera o orçamento das 12 parcelas do ano, exibindo-o na tela e exportando-o para um arquivo `.csv`.

### Regras de negócio

| Tipo de imóvel | Valor base | Acréscimos | Descontos |
|---|---|---|---|
| Apartamento | R$ 700,00 (1 quarto) | + R$ 200,00 (2º quarto) / + R$ 300,00 (garagem) | − 5% se não possui filhos |
| Casa | R$ 900,00 (1 quarto) | + R$ 250,00 (2º quarto) / + R$ 300,00 (garagem) | — |
| Estúdio | R$ 1.200,00 | + R$ 250,00 (2 vagas inclusas) / + R$ 60,00 por vaga extra | — |

Contrato imobiliário: R$ 2.000,00, parcelável em até 5 vezes.

### Estrutura do projeto

```
orcamento_aluguel/
├── orcamento_aluguel.py       # Código-fonte principal (classes e lógica da aplicação)
├── flowchart.py               # Script que gera o fluxograma da aplicação (Graphviz)
├── fluxograma_orcamento.png   # Fluxograma gerado (Parte Teórica)
├── Parte_Teorica_Orcamento_Aluguel.pdf   # Documento da Parte Teórica (fluxograma + lógica do algoritmo)
├── orcamento_aluguel.csv      # Exemplo de saída gerada pela aplicação
└── README.md                  # Este arquivo (PT/EN)
```

### 📂 Arquivos do projeto

- [`orcamento_aluguel.py`](orcamento_aluguel.py) — código-fonte principal (classes e lógica da aplicação)
- [`flowchart.py`](flowchart.py) — script que gera o fluxograma da aplicação (Graphviz)
- [`fluxograma_orcamento.png`](fluxograma_orcamento.png) — fluxograma gerado (Parte Teórica)
- [`Parte_Teorica_Orcamento_Aluguel.pdf`](Parte_Teorica_Orcamento_Aluguel.pdf) — documento completo da Parte Teórica (fluxograma e estrutura lógica)
- [`orcamento_aluguel.csv`](orcamento_aluguel.csv) — exemplo de saída gerada pela aplicação

### Classes principais

- **`Imovel`** (classe abstrata): atributos e comportamentos comuns a todos os imóveis; define o cálculo da parcela do contrato.
- **`Apartamento`**, **`Casa`**, **`Estudio`**: herdam de `Imovel` e sobrescrevem `calcular_valor_mensal()`, cada uma com sua própria regra (polimorfismo).
- **`Orcamento`**: recebe um `Imovel` e gera as 12 parcelas mensais, exibindo-as na tela e exportando-as para `.csv`.

### 🚀 Etapas de Execução do Projeto

O projeto segue três etapas, na seguinte ordem: primeiro o código-fonte, depois a geração do orçamento (.csv) a partir dele e, por fim, a geração do fluxograma que documenta a lógica da aplicação.

**Etapa 1 — Código-fonte: `orcamento_aluguel.py`**

Este é o arquivo principal do projeto, contendo as classes (`Imovel`, `Apartamento`, `Casa`, `Estudio`, `Orcamento`) e toda a lógica de cálculo do orçamento de aluguel.

- **Softwares utilizados:** Python 3 (`sudo apt install python3 python3-pip python3-venv`) e Visual Studio Code como editor de código (`code .`).

**Etapa 2 — Geração do `orcamento_aluguel.csv` a partir do código**

Com o `orcamento_aluguel.py` pronto, ele é executado no terminal:

```bash
python3 orcamento_aluguel.py
```

O programa solicita os dados do imóvel (tipo, quartos, garagem, filhos/vagas de estacionamento, número de parcelas do contrato) e, ao final da execução, **gera automaticamente** o arquivo `orcamento_aluguel.csv` na mesma pasta, contendo as 12 parcelas do orçamento anual.

- **Softwares utilizados:** Python 3 (execução do script) e, opcionalmente, LibreOffice Calc para abrir e conferir o conteúdo do arquivo gerado:
  ```bash
  libreoffice --calc orcamento_aluguel.csv
  ```

**Etapa 3 — Geração do `fluxograma_orcamento.png`**

Por fim, o fluxograma da aplicação (parte teórica do trabalho) é gerado a partir de um script separado, `flowchart.py`, que usa a biblioteca Graphviz para desenhar o diagrama.

```bash
python3 flowchart.py
```

Isso cria o arquivo `fluxograma_orcamento.png` na mesma pasta.

- **Softwares utilizados:** Python 3, o software Graphviz instalado no sistema (`sudo apt install graphviz` no Linux) e a biblioteca Python correspondente (`pip install graphviz --break-system-packages`).

### Licença

Projeto acadêmico, desenvolvido exclusivamente para fins avaliativos da disciplina.

---

## 🇺🇸 English

A Python application, built with Object-Oriented Programming, that generates rental budgets (Apartment, House, or Studio) for the fictional real estate company R.M.

**Course:** Algorithmic Thinking & Introduction to Object-Oriented Programming
**Institution:** Centro Universitário UniFECAF
**Author:** Eduardo Souza Mattos — Student ID: 35984
**Year:** 2026

### Description

The program asks the user for the desired property type and its specific details, calculates the monthly rent by applying R.M's business rules, calculates the real estate contract installment (payable in up to 5 installments), and generates the 12-month annual budget, both displaying it on screen and exporting it to a `.csv` file.

### Business rules

| Property type | Base price | Surcharges | Discounts |
|---|---|---|---|
| Apartment | $700.00 (1 bedroom) | + $200.00 (2nd bedroom) / + $300.00 (garage) | − 5% if no children |
| House | $900.00 (1 bedroom) | + $250.00 (2nd bedroom) / + $300.00 (garage) | — |
| Studio | $1,200.00 | + $250.00 (2 parking spots included) / + $60.00 per extra spot | — |

Real estate contract: $2,000.00, payable in up to 5 installments.

### Project structure

```
orcamento_aluguel/
├── orcamento_aluguel.py       # Main source code (application classes and logic)
├── flowchart.py               # Script that generates the application flowchart (Graphviz)
├── fluxograma_orcamento.png   # Generated flowchart (Theoretical Part)
├── Parte_Teorica_Orcamento_Aluguel.pdf   # Theoretical Part document (flowchart + algorithm logic)
├── orcamento_aluguel.csv      # Sample output generated by the application
└── README.md                  # This file (PT/EN)
```

### 📂 Project files

- [`orcamento_aluguel.py`](orcamento_aluguel.py) — main source code (application classes and logic)
- [`flowchart.py`](flowchart.py) — script that generates the application flowchart (Graphviz)
- [`fluxograma_orcamento.png`](fluxograma_orcamento.png) — generated flowchart (Theoretical Part)
- [`Parte_Teorica_Orcamento_Aluguel.pdf`](Parte_Teorica_Orcamento_Aluguel.pdf) — full Theoretical Part document (flowchart and logical structure)
- [`orcamento_aluguel.csv`](orcamento_aluguel.csv) — sample output generated by the application

### Main classes

- **`Imovel`** (abstract class, "Property" in English): attributes and behaviors common to all properties; defines the contract installment calculation.
- **`Apartamento`**, **`Casa`**, **`Estudio`** ("Apartment", "House", "Studio"): inherit from `Imovel` and override `calcular_valor_mensal()` ("calculate_monthly_value"), each applying its own pricing rule (polymorphism).
- **`Orcamento`** ("Budget"): receives an `Imovel` instance and generates the 12 monthly installments, displaying them on screen and exporting them to `.csv`.

> Note: class and method names remain in Portuguese in the source code, matching the original assignment language. This section simply explains their purpose in English.

### 🚀 Project Execution Steps

The project follows three steps, in this order: first the source code, then generating the budget (.csv) from it, and finally generating the flowchart that documents the application's logic.

**Step 1 — Source code: `orcamento_aluguel.py`**

This is the project's main file, containing the classes (`Imovel`, `Apartamento`, `Casa`, `Estudio`, `Orcamento`) and all the rental budget calculation logic.

- **Software used:** Python 3 (`sudo apt install python3 python3-pip python3-venv`) and Visual Studio Code as the code editor (`code .`).

**Step 2 — Generating `orcamento_aluguel.csv` from the code**

With `orcamento_aluguel.py` ready, it is run in the terminal:

```bash
python3 orcamento_aluguel.py
```

The program asks for the property details (type, bedrooms, garage, children/parking spots, number of contract installments) and, at the end of execution, **automatically generates** the `orcamento_aluguel.csv` file in the same folder, containing the 12 installments of the annual budget.

- **Software used:** Python 3 (running the script) and, optionally, LibreOffice Calc to open and check the generated file's contents:
  ```bash
  libreoffice --calc orcamento_aluguel.csv
  ```

**Step 3 — Generating `fluxograma_orcamento.png`**

Finally, the application's flowchart (the theoretical part of the assignment) is generated from a separate script, `flowchart.py`, which uses the Graphviz library to draw the diagram.

```bash
python3 flowchart.py
```

This creates the `fluxograma_orcamento.png` file in the same folder.

- **Software used:** Python 3, the Graphviz software installed on the system (`sudo apt install graphviz` on Linux), and the corresponding Python library (`pip install graphviz --break-system-packages`).

### License

Academic project, developed exclusively for course evaluation purposes.
