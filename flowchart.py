from graphviz import Digraph

dot = Digraph('Orcamento', format='png')
dot.attr(rankdir='TB', bgcolor='white', dpi='150')
dot.attr('node', fontname='Helvetica', fontsize='11')
dot.attr('edge', fontname='Helvetica', fontsize='10')

# Início/Fim
dot.node('inicio', 'Início', shape='oval', style='filled', fillcolor='#2E7D32', fontcolor='white')
dot.node('fim', 'Fim', shape='oval', style='filled', fillcolor='#C62828', fontcolor='white')

# Entrada
dot.node('sel_tipo', 'Selecionar tipo de imóvel\n(Apartamento / Casa / Estúdio)', shape='parallelogram', style='filled', fillcolor='#BBDEFB')

# Decisão tipo
dot.node('dec_tipo', 'Tipo de imóvel?', shape='diamond', style='filled', fillcolor='#FFF9C4')

# Apartamento
dot.node('apto_dados', 'Informar: nº de quartos,\ngaragem (S/N), tem filhos (S/N)', shape='parallelogram', style='filled', fillcolor='#BBDEFB')
dot.node('apto_calc', 'Calcular valor base R$700\n+ R$200 (2 quartos)\n+ R$300 (garagem)\n- 5% se não tem filhos', shape='box', style='filled', fillcolor='#E1BEE7')

# Casa
dot.node('casa_dados', 'Informar: nº de quartos,\ngaragem (S/N)', shape='parallelogram', style='filled', fillcolor='#BBDEFB')
dot.node('casa_calc', 'Calcular valor base R$900\n+ R$250 (2 quartos)\n+ R$300 (garagem)', shape='box', style='filled', fillcolor='#E1BEE7')

# Estúdio
dot.node('estudio_dados', 'Informar: quantidade de\nvagas de estacionamento', shape='parallelogram', style='filled', fillcolor='#BBDEFB')
dot.node('estudio_calc', 'Calcular valor base R$1200\n+ R$250 (2 vagas inclusas)\n+ R$60 por vaga extra', shape='box', style='filled', fillcolor='#E1BEE7')

# Comum
dot.node('parcela_contrato', 'Calcular parcela do contrato\nR$2.000,00 / até 5x', shape='box', style='filled', fillcolor='#FFCCBC')
dot.node('gerar_12', 'Gerar as 12 parcelas mensais\n(mensalidade + parcela do\ncontrato nos 5 primeiros meses)', shape='box', style='filled', fillcolor='#FFCCBC')
dot.node('exibir', 'Exibir orçamento mensal\nna tela', shape='parallelogram', style='filled', fillcolor='#BBDEFB')
dot.node('exportar', 'Exportar orçamento\npara arquivo .csv', shape='parallelogram', style='filled', fillcolor='#BBDEFB')

dot.edge('inicio', 'sel_tipo')
dot.edge('sel_tipo', 'dec_tipo')

dot.edge('dec_tipo', 'apto_dados', label='Apartamento')
dot.edge('dec_tipo', 'casa_dados', label='Casa')
dot.edge('dec_tipo', 'estudio_dados', label='Estúdio')

dot.edge('apto_dados', 'apto_calc')
dot.edge('casa_dados', 'casa_calc')
dot.edge('estudio_dados', 'estudio_calc')

dot.edge('apto_calc', 'parcela_contrato')
dot.edge('casa_calc', 'parcela_contrato')
dot.edge('estudio_calc', 'parcela_contrato')

dot.edge('parcela_contrato', 'gerar_12')
dot.edge('gerar_12', 'exibir')
dot.edge('exibir', 'exportar')
dot.edge('exportar', 'fim')

dot.render('fluxograma_orcamento', cleanup=True)
print("Fluxograma gerado com sucesso!")