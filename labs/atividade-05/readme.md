# Troca de figurinhas

Maria e João estão colecionando figurinhas da Copa. Cada figura tem um identificador único, um número inteiro. Assim, como a maioria das pessoas, para completar o album de figurinhas, elas gostam de trocar figurinhas. Eles obviamente não se importam com cartas idênticas que ambos têm e não querem receber cartas repetidas na troca. Além disso, as cartas são trocadas em uma única operação: Maria dá a João $N$ figurinhas distintas e recebe de volta outras $N$ figurinhas distintas.

Eles querem maximizar o número de figurinhas que podem trocar. Por exemplo, se Maria tem `{1, 1, 2, 3, 5, 7, 8, 8, 9, 15}` e João tem `{2, 2, 2, 3, 4, 6, 10, 11, 11}`, eles conseguem trocar no máximo quatro figurinhas.

Escreva um programa que dado o conjunto de cartas de Maria e João, determina o número máximo de cartas que podem ser trocadas.


## Input (Entrada)

A primeira linha contém dois inteiros $A$ e $B$, separados por um espaço em branco, indicando o número de cartas de Maria e João $(1 ≤ A ≤ 104$ and $1 ≤ B ≤ 104)$. A segunda linha contem $A$ inteiros separados por espaço, indicando a carta de Maria $(1 ≤ X_i ≤ 105)$. A terceira linha também contém $B$ inteiros separados por espaço, sendo as cartas de João $(1 ≤ Y_i ≤ 105)$.

## Output

Para cada caso de teste, seu programa deve imprimir uma única linha, contendo um número inteiro, indicando o número máximo de cartas que Maria e João podem trocar.


---


### Exemplo teste 01


Entrada (Input):
```
1 1
1000
1000
```

Saída (Output):
```
0
```

### Exemplo teste 02

Entrada (Input):
```
3 4
1 3 5
2 4 6 8
```

Saída (Output):
```
3
```

### Exemplo teste 03

Entrada (Input):
```
10 9
1 1 2 3 5 7 8 8 9 15
2 2 2 3 4 6 10 11 11
```

Saída (Output):
```
4
```
