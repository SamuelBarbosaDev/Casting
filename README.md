# Casting
### Índice

- [Casting](#casting)
    - [Índice](#índice)
    - [Contextualização:](#contextualização)
    - [Metodologia Aplicada:](#metodologia-aplicada)
  - [Entendimento do Negócio:](#entendimento-do-negócio)
  - [Entendimento dos Dados:](#entendimento-dos-dados)
    - [Variáveis:](#variáveis)
  - [Preparação dos Dados:](#preparação-dos-dados)
    - [Segmentando o DataFrame por clientes:](#segmentando-o-dataframe-por-clientes)
  - [Modelagem:](#modelagem)
  - [Avaliação:](#avaliação)
  - [Implantação:](#implantação)
  - [Pré-requisitos para executar o projeto:](#pré-requisitos-para-executar-o-projeto)
    - [Ambiente virtual e Dependências:](#ambiente-virtual-e-dependências)


### Contextualização:
A Solução Casting é uma empresa que presta serviços para outras empresas, e hoje a predição do faturamento para os clientes é realizada de forma manual e simplificada, mas estão em busca de automatizar para gerar mais valor aos clientes, reduzir custos e otimizar o tempo da equipe.

### Metodologia Aplicada:
A análise foi realizada utilizando o modelo CRISP-DM, o CRISP-DM (Cross Industry Standard Process for Data Mining) é um modelo padrão de processo para projetos de mineração de dados que define um conjunto de fases e tarefas que devem ser executadas para desenvolver soluções de mineração de dados efetivas.

![CRISP-DM](/img/CRISP-DM.png)

O modelo CRISP-DM é uma abordagem sistemática e estruturada para a mineração de dados que ajuda as empresas a desenvolver soluções de mineração de dados de maneira eficiente e eficaz, reduzindo o tempo e os custos do projeto.

## Entendimento do Negócio:


## Entendimento dos Dados:
### Variáveis:
| Coluna           | Descrição                                             |
| ---------------- | ----------------------------------------------------- |
| VUF_CODIGO | Código da Venda |
| VUF_CODIGO_BOLETO | Código do Boleto |
| UND_CODIGO | Código da Unidade, ou seja, o local onde foi vendido. |
| FUN_CODIGO | Código do Funcionário |
| VUF_DT | Data da Transação |
| PRO_CODIGO | Código do Produto, ou seja, código do produto vendido. |
| CAT_CODIGO | Código da Categoria, ou seja, código da categoria do produto vendido. |
| VUF_QTBOLETO | Quantidade de Boletos |
| VUF_QTPRODUTO | Quantidade de Produtos |
| VUF_VLRBRUTOVENDA | Valor Bruto da Venda |
| VUF_VLRDESCONTO | Valor do Desconto |
| VUF_VLRLIQFINAL | Valor Líquido da Venda |
| VUF_VLRTROCA | O Valor da Troca, refere-se à situação em que, caso uma pessoa devolva um produto, ela recebe um desconto no valor bruto. |
| CLV_BANCO | Código do Cliente |

***OBS:*** *Na base de dados, podem existir diversas `Vendas` distintas no `mesmo Boleto`. Além disso, internamente, eles possuem uma métrica que representa o `número de produtos` por `Boleto`, e essa métrica é obtida por meio da agregação da coluna `VUF_CODIGO_BOLETO` com base no `VUF_QTBOLETO`.*

*Exemplo:*

```python
  (
    df
    .groupby('VUF_CODIGO_BOLETO')
    .agg({'VUF_QTBOLETO':'sum'})
  )
```

*Output:*

| VUF_QTBOLETO                                       | VUF_CODIGO_BOLETO |
|---------------------------------------------------|-------------------|
| 1                                                 | 4                 |
| 10                                                | 5                 |
| 11                                                | 4                 |
| 12                                                | 4                 |
| 13                                                | 5                 |
| ...                                               | ...               |
| 152461-22-f8ec40f8-a41d-4361-beda-abfcdb8aec73    | 1                 |
| 152461-82-61b1a049-5a8a-4666-8fd4-f54ce0a1d595    | 1                 |
| 152462-22-264a21e3-4c9d-4d55-9509-5f38b27c715a    | 1                 |
| 152462-82-4dcf1591-5378-45a0-991a-d29b3e6209a3    | 1                 |
| 152463-22-df7662df-b21d-4edb-ae0b-a227c2c53943    | 1                 |



## Preparação dos Dados:
### Segmentando o DataFrame por clientes:
```python
for cliente in set(df['CLV_BANCO']):
    temp = df[df.CLV_BANCO == cliente]
    temp.to_csv(f'../data/dataset_{cliente}.csv', index=False)
```

## Modelagem:


## Avaliação:


## Implantação:
Iniciando a etapa de implementação do modelo em produção.

## Pré-requisitos para executar o projeto:
Abaixo, listarei os requisitos necessários para que o projeto funcione corretamente.

### Ambiente virtual e Dependências:
Criando ambiente virtual:
```
python3.10 -m venv .venv
```

Entrando no ambiente virtual:
```
source .venv/bin/activate
```

Instale as dependências:
```
pip install -r requirements.txt
```
