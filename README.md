# Casting
### Índice

- [Casting](#casting)
    - [Índice](#índice)
    - [Contextualização:](#contextualização)
    - [Metodologia Aplicada:](#metodologia-aplicada)
  - [Entendimento do Negócio:](#entendimento-do-negócio)
  - [Entendimento dos Dados:](#entendimento-dos-dados)
    - [Variáveis:](#variáveis)
    - [DataFrame:](#dataframe)
    - [Verificando as dimensões do dataframe:](#verificando-as-dimensões-do-dataframe)
    - [Verificando os tipos:](#verificando-os-tipos)
    - [Descrição das colunas do tipo `numérico`:](#descrição-das-colunas-do-tipo-numérico)
    - [Descrição das colunas do tipo `object`:](#descrição-das-colunas-do-tipo-object)
    - [Verificando os valores nulos:](#verificando-os-valores-nulos)
  - [Preparação dos Dados:](#preparação-dos-dados)
    - [Segmentando o DataFrame por clientes:](#segmentando-o-dataframe-por-clientes)
  - [Modelagem:](#modelagem)
  - [Avaliação:](#avaliação)
  - [Implantação:](#implantação)
  - [Pré-requisitos para executar o projeto:](#pré-requisitos-para-executar-o-projeto)
    - [Ambiente virtual e Dependências:](#ambiente-virtual-e-dependências)


### Contextualização:
A Solução Casting é uma empresa com mais de 30 anos de experiência no mercado. O portfólio da Solução Casting abrange produtos como a solução de Gestão de Talentos e a Gestão de Performance para Vendas.

Seu principal produto é o aplicativo `Casting`, que combina uma eficaz Gestão de Performance de Vendas com uma metodologia que tem auxiliado grandes empresas do varejo a aprimorar a administração de seus vendedores e, consequentemente, a aumentar suas vendas.

### Metodologia Aplicada:
A análise foi realizada utilizando o modelo CRISP-DM, o CRISP-DM (Cross Industry Standard Process for Data Mining) é um modelo padrão de processo para projetos de mineração de dados que define um conjunto de fases e tarefas que devem ser executadas para desenvolver soluções de mineração de dados efetivas.

![CRISP-DM](/img/CRISP-DM.png)

O modelo CRISP-DM é uma abordagem sistemática e estruturada para a mineração de dados que ajuda as empresas a desenvolver soluções de mineração de dados de maneira eficiente e eficaz, reduzindo o tempo e os custos do projeto.

## Entendimento do Negócio:
A Solução Casting é uma empresa que presta serviços para outras empresas, e hoje a predição do faturamento para os clientes é realizada de forma manual e simplificada, mas estão em busca de automatizar para gerar mais valor aos clientes, reduzir custos e otimizar o tempo da equipe.

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

### DataFrame:
```python
df.head(3)
```

*Output:*
| VUF_CODIGO                            | VUF_CODIGO_BOLETO                     | UND_CODIGO | FUN_CODIGO                            | VUF_DT     | PRO_CODIGO                            | CAT_CODIGO                            | VUF_QTBOLETO | VUF_QTPRODUTO | VUF_VLRBRUTOVENDA | VUF_VLRDESCONTO | VUF_VLRLIQFINAL | VUF_VLRTROCA | CLV_BANCO    |
|---------------------------------------|---------------------------------------|------------|---------------------------------------|------------|---------------------------------------|---------------------------------------|--------------|---------------|-------------------|-----------------|-----------------|-------------|--------------|
| B28DDB4B-8A49-4658-8539-5DA3F20AA39F | 1000                                  | 1000       | D4758B39-E7EA-4D97-B6B1-6236CE2C05A2 | 2022-06-18 | BBEF56E1-66E0-47A6-95AC-5479DE79577B | 6768760F-758A-4B31-AE33-CEB127A956CB | 1            | 1.0           | 15.0              | 0.0             | 15.0            | 0.0         | CASTING_DB108 |
| 8E22E8FC-65DC-44BA-AFFA-4D661108F0B4 | 1001                                  | 1001       | D4758B39-E7EA-4D97-B6B1-6236CE2C05A2 | 2022-06-18 | AF858E1C-9C72-4B63-AC51-A8185ECCCC35 | 0136ECF4-9F4D-4DBE-A78D-B2ED565CE60C | 1            | 1.0           | 32.0              | 0.0             | 32.0            | 0.0         | CASTING_DB108 |
| E36DEDC5-78CB-4452-9E04-AD174E32747C | 1002                                  | 1002       | D4758B39-E7EA-4D97-B6B1-6236CE2C05A2 | 2022-06-20 | B0974005-D231-438C-A0C1-F6A211B00697 | 7B6AD9C1-F745-4137-B62D-4A67E865E781 | 1            | 1.0           | 15.0              | 0.0             | 15.0            | 0.0         | CASTING_DB108 |


### Verificando as dimensões do dataframe:
```python
casting.verificando_as_dimensões_do_dataframe(
    dataframe=df
)
```

*Output:*
```output
Linhas: 65535 
Colunas: 14
```

### Verificando os tipos:
```python
casting.verificando_tipos(
    dataframe=df
)
```

*Output:*
| Campo            | Tipos    |
|------------------|----------|
| VUF_CODIGO       | object   |
| VUF_CODIGO_BOLETO | object   |
| UND_CODIGO       | object   |
| FUN_CODIGO       | object   |
| VUF_DT           | object   |
| PRO_CODIGO       | object   |
| CAT_CODIGO       | object   |
| VUF_QTBOLETO     | int64    |
| VUF_QTPRODUTO    | float64  |
| VUF_VLRBRUTOVENDA | float64  |
| VUF_VLRDESCONTO  | float64  |
| VUF_VLRLIQFINAL  | float64  |
| VUF_VLRTROCA     | float64  |
| CLV_BANCO        | object   |


### Descrição das colunas do tipo `numérico`:
```python
casting.descrição(
    dataframe=df,
    vertical=True
)
```

*Output:*
|           | count  |   mean |    std |    min |   10% |   15% |   25% |   50% |   75% |   85% |   95% |   99% |    max |
|-----------|-------|--------|--------|--------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| VUF_QTBOLETO      | 65535 |   0.47 |   0.50 |   0.00 |  0.00 |  0.00 |  0.00 |  0.00 |  0.00 |  1.00 |  1.0 |  1.00 |   1.0  |
| VUF_QTPRODUTO     | 65535 |   1.00 |   3.39 |  -4.00 |  1.00 |  1.00 |  1.00 |  1.00 |  1.00 |  1.00 |  1.0 |  3.00 | 850.0  |
| VUF_VLRBRUTOVENDA | 65535 | 355.83 | 782.00 | -15250.00 |  5.98 |  7.98 | 15.00 | 170.00 | 440.00 | 759.00 | 1499.0 | 3290.00 | 45900.0 |
| VUF_VLRDESCONTO   | 65535 |  60.21 | 253.92 |  -8627.99 |  0.00 |  0.00 |  0.00 |  0.00 |  0.00 | 112.00 | 312.0 | 840.00 | 12450.0 |
| VUF_VLRLIQFINAL   | 65535 | 295.62 | 619.81 |  -7326.00 |  5.00 |  6.98 | 13.98 | 144.00 | 359.98 | 640.00 | 1281.0 | 2719.66 | 45900.0 |
| VUF_VLRTROCA      | 65535 |   0.00 |   0.00 |   0.00 |  0.00 |  0.00 |  0.00 |  0.00 |  0.00 |   0.00 |   0.0 |  0.00 |   0.0  |


### Descrição das colunas do tipo `object`:
```python
casting.descrição_object(
    dataframe=df,
    vertical=True
)
```

*Output:*
| Campo             | Contagem | Único   | Top                                    | Frequência |
|-------------------|----------|---------|----------------------------------------|------------|
| VUF_CODIGO        | 65535    | 65535   | B28DDB4B-8A49-4658-8539-5DA3F20AA39F | 1          |
| VUF_CODIGO_BOLETO | 65535    | 25693   | 1574                                   | 150        |
| UND_CODIGO        | 65535    | 30      | FADCA1CC-2E3A-4278-BF58-F44F8D8940C9 | 13920      |
| FUN_CODIGO        | 65535    | 184     | 1F7A8D46-D0A3-45A6-B4FF-510CDB4E460B | 3475       |
| VUF_DT            | 65535    | 632     | 2022-04-30                            | 1286       |
| PRO_CODIGO        | 62788    | 10126   | 08962C5F-8C97-4B24-91BB-F1C564558ABB | 1886       |
| CAT_CODIGO        | 65535    | 37      | 12FDE7ED-AF3D-4EA5-8250-BBF2D0A5BB90 | 14289      |
| CLV_BANCO         | 65535    | 2       | CASTING_DB108                          | 37780      |

### Verificando os valores nulos:
```python
casting.verificando_valores_nulos(
    dataframe=df
)
```

*Output:*
| Campo             | Quantidade | Porcentagem |
|-------------------|------------|-------------|
| VUF_CODIGO        | 0          | 0.00%       |
| VUF_CODIGO_BOLETO | 0          | 0.00%       |
| UND_CODIGO        | 0          | 0.00%       |
| FUN_CODIGO        | 0          | 0.00%       |
| VUF_DT            | 0          | 0.00%       |
| PRO_CODIGO        | 2747       | 4.19%       |
| CAT_CODIGO        | 0          | 0.00%       |
| VUF_QTBOLETO      | 0          | 0.00%       |
| VUF_QTPRODUTO     | 0          | 0.00%       |
| VUF_VLRBRUTOVENDA | 0          | 0.00%       |
| VUF_VLRDESCONTO   | 0          | 0.00%       |
| VUF_VLRLIQFINAL   | 0          | 0.00%       |
| VUF_VLRTROCA      | 0          | 0.00%       |
| CLV_BANCO         | 0          | 0.00%       |


## Preparação dos Dados:
### Segmentando o DataFrame por clientes:
```python
for cliente in set(df['CLV_BANCO']):
    temp = df[df.CLV_BANCO == cliente]
    temp.to_csv(f'../data/dataset_{cliente}.csv', index=False)
```

## Modelagem:
Utilizamos o modelo **ARIMA** para realizar a previsão do faturamento líquido dos clientes das soluções Casting. Para uma melhor organização, separamos os notebooks por cliente e por etapa do CRISP-DM (Data Understanding, Data Preparation e Model). Os modelos foram convertidos para o formato pickle e estão armazenados na pasta **models/**. Eles podem ser facilmente utilizados através do seguinte comando em Python:

```python
import pickle


path = r'models/DB069.pkl'

with open(path, 'rb') as file:
    model = pickle.load(file)
```

Para realizar uma previsão, basta executar o seguinte comando:

```python
model.forecast(1)
```

Caso deseje aumentar a quantidade de previsões, basta ajustar o número dentro do método **forecast**. No entanto, é importante observar que a primeira previsão é feita com base nos dados reais fornecidos. A partir da segunda previsão, o modelo utiliza dados previamente previstos, o que torna as previsões menos precisas à medida que o número de previsões aumenta.

Lembre-se, o modelo deve ser re-treinado com dados atualizados. Recomendo que, a cada fechamento de mês, você o re-treine utilizando os novos dados.

Algumas observações: inicialmente, recebemos uma quantidade desnecessariamente grande de dados. Uma vez que o objetivo do projeto é prever o faturamento líquido por mês, seria suficiente fornecer os dados já agrupados mensalmente. Tivemos dataframes com mais de 2 milhões de linhas, porém, ao considerarmos os dados realmente relevantes (faturamento líquido agrupado por mês), essas mais de 2 milhões de linhas resultaram em cerca de 20 linhas em média. Apesar de termos dados correspondentes a aproximadamente 1 ano e 9 meses, acredito que seria necessário uma janela temporal maior, de no mínimo 32 meses ou mais, para obtermos um modelo de melhor qualidade.

## Avaliação:
Através da criação de modelos de séries temporais, conseguimos alcançar o objetivo de desenvolver um modelo para prever o faturamento líquido mensal. Caso as sugestões levantadas anteriormente sejam implementadas na próxima versão do projeto, poderemos criar um modelo ainda mais aprimorado.

Inicialmente, tínhamos a intenção de utilizar uma rede neural como modelo, mas devido a alguns fatores, optamos por empregar o ARIMA. Contudo, em uma futura versão do projeto, consideramos a possibilidade de utilizar um modelo de redes neurais, como evidenciado na amostra presente no arquivo `DB063_rnn.ipynb` dentro da pasta `notebooks/models/`.


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
