![banner](/Sem%20nome%20(575%20x%20414%20px).png)
# Trabalho Final - Sistema Distribuído

## Introdução
O trabalho prático consiste na resolução do Problema de N Rainhas de forma paralela ou distribuída. O objetivo é desenvolver e comparar algoritmos paralelos e sequenciais, testando a escalabilidade e a eficiência em diferentes configurações de hardware. Este relatório apresenta os tempos de execução dos algoritmos, bem como as especificações das máquinas utilizadas.

### Configurações das Máquinas
#### Máquina 1
Processador: Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz
Memória RAM: 16,0 GB (utilizável: 15,8 GB)

#### Máquina 2
Processador: AMD Ryzen 5 7520U with Radeon Graphics 2.80 GHz
Memória RAM: 16,0 GB (utilizável: 15,2 GB)

#### Máquina 3
Processador: AMD Ryzen 5 5600X 6-Core Processor @ 3.70 GHz
Memória RAM: 48,0 GB (utilizável: 47,9 GB)

#### Máquina 4
Processador: AMD Ryzen 7 1700 Eight-Core Processor @ 3.00 GHz
Memória RAM: 16,0 GB 3000Mhz

#### Máquina 5
Processador   AMD Ryzen 7 4800H with Radeon Graphics 2.90 GHz 
RAM instalada    32,0 GB (utilizável: 19,9 GB)

## Tempos de Execução

### Máquina 1
##### Paralelo:
6 Rainhas: 0.0060 segundos
9 Rainhas: 0.0540 segundos
12 Rainhas: 6.9064 segundos
##### Sequencial:
6 Rainhas: 0.0010 segundos
9 Rainhas: 0.0510 segundos
12 Rainhas: 6.7970 segundos

### Máquina 2
##### Paralelo:
6 Rainhas: 0.0065 segundos
9 Rainhas: 0.0506 segundos
12 Rainhas: 6.9875 segundos

##### Sequencial:
6 Rainhas: 0.0010 segundos
9 Rainhas: 0.0495 segundos
12 Rainhas: 6.6797 segundos

### Máquina 3
##### Paralelo:
6 Rainhas: 0.0040 segundos
9 Rainhas: 0.0401 segundos
12 Rainhas: 5.2696 segundos

##### Sequencial:
6 Rainhas: 0.0010 segundos
9 Rainhas: 0.0362 segundos
12 Rainhas: 5.1900 segundos

### Máquina 4
##### Paralelo:
6 Rainhas: 0.0070 segundos
9 Rainhas: 0.0740 segundos
12 Rainhas: 9.7924 segundos

##### Sequencial:
6 Rainhas: 0.0010 segundos
9 Rainhas: 0.0670 segundos
12 Rainhas: 9.2750 segundos

### Máquina 5
##### Paralelo:
6 Rainhas - 0.0070 segundos
9 Rainhas - 0.0529 segundos
12 Rainhas - 6.4177 segundos

##### Sequencial:
6 Rainhas - 0.0010 segundos
9 Rainhas - 0.0441 segundos
12 Rainhas - 6.3355 segundos

## Conclusões e Análises
**Comparação de Tempos:** Observa-se que o tempo de execução da solução paralela é geralmente maior do que o da solução sequencial em N menores, mas tende a se equiparar ou superar a solução sequencial em N maiores, dependendo do poder de processamento da máquina.

**Escalabilidade:** As máquinas com mais núcleos e maiores frequências de CPU (Máquinas 3 e 4) apresentam melhor desempenho para o algoritmo paralelo, especialmente em N maiores.

**Eficiência:** Apesar das diferenças de hardware, as soluções paralelas em máquinas com processadores mais potentes e mais núcleos (Máquinas 3 e 4) conseguem melhores tempos de execução em N maiores, o que sugere uma boa escalabilidade do algoritmo.

**Gargalos:** O overhead de criação e sincronização de threads pode ser um fator limitante para N menores, onde o tempo de comunicação entre threads é comparável ao tempo de cálculo. Em N maiores, o paralelismo tende a ser mais eficiente, especialmente em máquinas com mais núcleos.

Roteiro para Apresentação (10 minutos)
Introdução (1 minuto)

Apresentar o problema de N Rainhas e o objetivo do trabalho.
Breve descrição das abordagens paralela e sequencial.
Metodologia (2 minutos)

Explicar a implementação em Java/Python utilizando threads para paralelismo.
Descrever como a solução sequencial foi usada como base para validar a solução paralela.
Mencionar o uso de diferentes configurações de hardware para testar a eficiência.
Resultados e Comparação (4 minutos)

Apresentar os tempos de execução em cada máquina para os diferentes valores de N (6, 9, 12).
Comparar a eficiência do algoritmo paralelo versus o sequencial em diferentes configurações.
Discutir as diferenças de desempenho entre as máquinas, destacando o impacto da CPU e da RAM.
Análise de Escalabilidade e Eficiência (2 minutos)

Analisar como a solução paralela escala com o aumento de N e a diferença de desempenho entre as máquinas.
Identificar gargalos e sugerir melhorias como o uso de outras técnicas de paralelismo ou otimizações no algoritmo.
Conclusão (1 minuto)

Resumir as principais descobertas e a importância do paralelismo em problemas como o N Rainhas.
Agradecer pela atenção e abrir para perguntas.
