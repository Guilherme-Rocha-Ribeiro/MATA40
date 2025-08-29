# Relatório de Complexidade - Árvore Binária de Busca

## Análise Detalhada por Exercício

### Exercício 1: Contagem de Nós Específicos
| Tipo de Nó | Método | Complexidade | Explicação |
|------------|--------|--------------|------------|
| Folhas | `count_leaves()` | O(n) | Percorre todos os nós uma vez |
| Completos | `count_full_nodes()` | O(n) | Visita cada nó para verificar dois filhos |
| Semi-cheios | `count_half_nodes()` | O(n) | Checa todos os nós com exatamente um filho |

**Observação**: As três operações têm complexidade linear pois exigem percorrer toda a árvore.

### Exercício 2: Manutenção da Altura
| Operação | Complexidade | Detalhes |
|----------|-------------|----------|
| Inserção | O(log n) (médio)<br>O(n) (pior caso) | Atualiza altura no caminho de inserção |
| Atualização | O(n) | Necessária após operações de remoção |

**Justificativa**: A altura é armazenada em cada nó e atualizada durante as operações.

### Exercício 3: Comparação Estrutural
- **Método**: `is_structurally_identical()`
- **Complexidade**: O(n)
- **Análise**: Compara a topologia das árvores visitando todos os nós uma vez

### Exercício 4: Comparação Completa
- **Método**: `is_identical()`
- **Complexidade**: O(n)
- **Análise**: Compara tanto a estrutura quanto os valores dos nós

### Exercício 5: Árvore Espelhada
| Aspecto | Complexidade | Observação |
|---------|-------------|------------|
| Tempo | O(n) | Visita cada nó uma vez |
| Espaço | O(n) | Aloca nova árvore de mesmo tamanho |

### Exercício 6: Listagem por Intervalo
| Cenário | Complexidade | Explicação |
|---------|-------------|------------|
| Pior caso | O(n) | Quando todos os valores estão no intervalo |
| Caso médio | O(k + log n) | k = número de elementos no intervalo |

### Exercício 7: Remoção por Intervalo
| Operação | Complexidade | Detalhes |
|----------|-------------|----------|
| Localização | O(n) | Encontrar todos os nós no intervalo |
| Remoção | O(log n) por nó | Custo de rebalanceamento |
| Total | O(n log n) | Pior caso com muitos nós no intervalo |
