[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HsKbEEuZ)
# Laboratório 01 - TADs, Classes e Objetos

## Objetivos:

1. Reforçar o conceito de Tipos Abstratos de Dados;
2. Aprofundar o uso de Classes e Objetos na linguagem *Python*;
3. Praticar o conceito de modularização na linguagem *Python*.

## Antes de começar...

Analise com cuidado os códigos apresentados na aula. 
Nos exercícios abaixo voce poderá utilizar os TADs/Classes definidos como base para construir seua códigos.  

## Exercícios:

1. Desenvolva um TAD **Setor**, que representa uma área retangular em um plano 2D, como mostra a Figura 1. Um setor possui diversas propriedades, entre elas:

    1. Localização no plano 2D;
    1. Largura e Altura;
    1. Perimetro;
    1. Área.

![](./imgs/setor.png)

Figura 1 - Setor Retangular.
  
   Além dessas propriedades, o TAD **Setor** deve possuir operações básicas como:

   1. Acesso a localização;
   1. Ajuste de sua localização no plano;
   1. Acesso as dimensões;
   1. Ajuste de suas dimensões;
   1. Acesso ao perímetro;
   1. Acesso à área.

   Faça um programa de teste no mõdulo desse TAD para testar suas operações.

2. Desenvolva novos métodos para o TAD **Setor** que permitam identificar se existe sobreposição entre dois setores.

3. Modifique o TAD **Setor** para que além de determinar se houve sobreposição, determinar a região de sobreposição. Reflita sobre essa região de sobreposição: como ela pode ser caracterizada? Leve isso em conta ao desenvolver seu novo TAD.

4. Construa uma aplicação de teste que gere diversos setores de forma aleatória (a quantidade fornecida pela linha de comando como nos exemplos fornecidos no Lab) que estejam contidos em um plano de dimensões 1kmx1km. Setores fora desse plano não devem ser armazenados. Uma vez criados todos os setores, gere estatisticas sobre sua distribuição:

    1. Qual o percentual de setores possuem sobreposição?
    2. Dos que possuem sobreposição, qual o percentual médio da área de sobreposição entre eles?

## Referencias Bibliográficas:

- Canning, J., Broder, A., Lafore, R., **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 
- Karumanchi, N. , **Data Structures And Algorithmic - Thinking With Python**. CareerMonk Publications. 2020.
- Goodrich,M.T., Tamassia, R., Goldwasser, M.H.. **Data Structures and Algorithms in Python**. John Wiley & Sons, Inc. 2012.
- John Sturtz, [**Python Modules and Packages – An Introduction**](https://realpython.com/python-modules-packages/).
