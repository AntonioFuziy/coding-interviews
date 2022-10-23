# Final Interview - Antonio Fuziy

## Descrição

Um aluno de administração do Insper é muito interessado em mercado financeiro, verificando um histórico de fechamento de uma ação ele tem a dúvida de como identificar o melhor retorno que alguém poderia ter comprando e vendendo-a.

## Problem - Best Time to Buy and Sell Stock ||

Escreva um algoritmo que encontre e retorne o retorno máximo possível em um histórico de um ação.

## Limitações

Em cada dia, você pode decidir comprar e/ou vender as ações. Você só pode deter no máximo uma ação de cada vez. Porém, você pode comprar e vender a ação imediatamente no mesmo dia.

## Dicas

- 1. Utilize um gráfico para representar o histórico de ações baseado na entrada do algoritmo. Consegue pensar em qual seria o retorno máximo?

- 2. Observe o gráfico ou a entrada e tente identificar máximos e mínimos locais em sequência.

- 3. Identifique a diferença entre cada valor da ação sequencialmente.

## Solução

### Solução 1

Para essa solução devemos olhar para a entrada do algoritmo como um gráfico e através dele identificar a diferença de retorno de um pico após um vale, verificando um retorno máximo.

Um exemplo para essa solução pode ser verificado através do gráfico a seguir:

Para a entrada [7, 1, 5, 3, 6, 4]

![Graph 1](/images/solution1_maxprofit.png)

Dessa forma, observando os picos e vales do gráfico o algoritmo tende a priorizar os retornos com maior diferença entre picos e vales. Portanto, o resultado do algoritmo será 7, somando-se a diferença entre o pico **i** e o vale **i** com resultado 4, junto da diferença do pico **j** e vale **j** com resultado 3, logo 4 + 3 = 7.

### Solução 2

Para a segunda solução o algoritmo é bem similar, porém mais simples. Nesse caso, ao invés de precisar identificar picos e vales, identifica-se apenas a diferença dos valores em sequência, caso o segundo valor seja maior que o primeiro. Pode-se verificar esse comportamento no gráfico abaixo:

Para a entrada [1, 7, 2, 3, 6, 7, 6, 7]

![Graph 2](/images/solution2_graph.png)

Portanto, identificando a soma dos valores de A, B, C, D e E, temos um resultado de 12 como maior retorno.

### Pre interview assignment

Implemente qualquer solução em Python e envie-a aqui. Sua função deve usar a seguinte declaração:

```python
def max_profit(prices: list[int]) -> int:
```

O valor de retorno é um inteiro, como a da solução acima.

## Referência

[Best Time to Buy and Sell Stock || - Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)