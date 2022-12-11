# Trabalho 3 - Unidade 2

**Alunos : Efrain Marcelo Pulgar Pantaleon e Pedro Leandro Batista Marques**

## Como Rodar o Projeto

Para rodar o arquivo ```atividade3U2.ipynb``` temos 2 opções:

1) Rodar o arquivo pelo [Google Colaboratory](https://colab.research.google.com/) via upload.
 - Será necessário tirar as '#' do primeiro script, pois ele instalará dependências necessárias.

2) Rodar Via VsCode
 - Será necessário criar um ambiente virtual com o comando ```python -m  venv venv```
 - Ativar o ambiente virtual com o comando ```./venv/Scripts/activate```
 - Após ativarmos o ambiente, basta rodar o comando ```pip install -r requirements.txt``` para instalar as dependências do projeto automaticamente

## Video Explicativo do Projeto

Para a atividade, produzimos um video para descrever os resultados obtidos em nossos estudos e como ele foi realizado.Para acessar o video, basta clicar [aqui](https://drive.google.com/file/d/1F-gvBDnlAqdj57dAySGQRvHpFpePPI1O/view)

## Breve descrição do projeto e dos resultados

O objetivo deste projeto é gerar uma rede dirigida a partir de links das páginas da wikipedia. A página que escolhemos, foi a página de [carnabauis](https://pt.wikipedia.org/wiki/Carnaubais), que é um município do interior do estado do Rio Grande do Norte. A página escolhida (assim como todas as outras na wikipedia) referenciam/citam outras páginas, e com isso, pode-se gerar um *grafo dirigido* a partir desses links das páginas. 

### Requisito 1
---
A rede que geramos se limita a ```duas camadas``` de profundidade, ou seja, a primeira camada é a própria página de [carnabauis](https://pt.wikipedia.org/wiki/Carnaubais) e a segunda camada são as páginas que a página de [carnabauis](https://pt.wikipedia.org/wiki/Carnaubais) cita. Abaixo estão as páginas que encontramos nessas duas camadas:

```
0 Carnaubais
1 Brazil
1 Flag Of Carnaubais
1 Geographic Coordinate System
1 Municipalities Of Brazil
1 Northeast Region, Brazil
1 Regions Of Brazil
1 Rio Grande Do Norte
1 States Of Brazil
1 Time Zone
```

Apesar da pouca quantidade de páginas presentes nessas camadas quando averiguamos a quantidade de nós e conexões da rede nos deparamos com a seguinte situação:

```
Quantidade de Nós: 2358
Quantidade de Conexões: 3357
```

Então, foi feito um tratamento para *remover autocitações*, *remover citações duplicadas* e dentre outros métodos para limpar a rede. Daí, ficamos apenas com:  

```
Quantidade de Nós: 9
Quantidade de Conexões: 45
```

Quando analisamos a métrica ```in-degree```, que é uma métrica que diz respeito a quantas conexões chegam em um nó, ou seja, no nosso caso seria quantas vezes uma página foi citada, abaixo percebe-se que a página do *Brazil* foi a mais citada dentro da nossa rede.

```
8 Brazil
7 Regions Of Brazil
6 States Of Brazil
6 Northeast Region, Brazil
6 Rio Grande Do Norte
5 Geographic Coordinate System
5 Municipalities Of Brazil
1 Carnaubais
1 Flag Of Carnaubais
```

Foi gerada uma imagem da rede para visualizá-la melhor:

![rede](./output.png)

### Requisito 2
---

Apesar da análise da métrica ```in-degree``` nos permitir visualizar quem foi a página mais citada, apenas essa métrica não é suficiente para uma análise mais detalhada da nossa rede. Logo, geramos uma imagem com outras quatro métricas: ```degree centrality```, ```closeness centrality```, ```betweeness centrality``` e ```eigenvector centrality```.

![métricas](./alltogether.png)

Observando a escala de cores, a página do *Brazil* é a que tem o maior ```degree centrality```, ou seja, ela é a página que mais foi citada. Quando analizamos a métrica ```closeness centrality```, observamos que a página do *Brazil* é a que tem essa maior métrica, ou seja, ela é a página que está mais próxima das outras. Já quando analizamos a métrica ```betweeness centrality```, vemos que as páginas que tem essa maior métrica são as páginas do *Brazil* e a do *Rio Grande do Norte*, ou seja, essas são as páginas que mais participam do fluxo de informação. Por fim, a página que possui o maior ```eigenvector centrality``` é a página do *Brazil*, ou seja, ela contém mais páginas vizinhas *importantes*.

### Requisito 3
---

Com essa rede, também construímos um *histograma*, um de *Função Densidade Probabilidade* (```PDF```) e um Gráfico de *Função Densidade acumulada* (```CDF```) com relação a métrica ```degree``` da rede.

Histograma:

![histograma](./histograma.png)

Função Densidade Probabilidade (```PDF```):

![PDF](./probability_density_function.png)

Função Densidade acumulada (```CDF```):

![PDF](./cumulative_density_function.png)

Ao analizar a ```CDF``` da rede, vemos que cerca de *60% das páginas (nós) da rede possuem 10 ou menos páginas vizinhas*.

### Requisito 4
---
Também geramos uma imagem com vários gráficos das 4 métricas do requisito 2. A diagonal principal da imagem contém a ```PDF``` da rede com relação as métricas da coluna ao lado, as imagens acima da diagonal principal são *scatter plots* de uma métrica em relação a outra (observar a legenda da imagem) e as imagens abaixo da diagonal principal são outra forma de visualizar o scatter plot correspondente (nese caso, quanto mais próximo da cor branca, maior é a métrica).

![ALL](./all.png)

### Requisito 5
---

Por fim, geramos uma imagem com o núcleo (```core```) e casca (```shell```) da rede:

![core-shell](./k-core_sociopatterns.png)

### Referências
Repositório de Algorítmos e Estruturas de dados II do Professor Ivanovitch [![Repository](https://img.shields.io/badge/-Repo-191A1B?style=flat-square&logo=github)](https://github.com/ivanovitchm/datastructure)
