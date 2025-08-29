from LinkedList import SLS

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Altura inicial é 1 para novos nós

class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):
        """Imprime a árvore de forma hierárquica"""
        print("\nESTRUTURA DA ÁRVORE BINÁRIA:")
        self._print_tree(self.root, 0, "Raiz:")

    def _print_tree(self, node, level, prefix):
        if node is not None:
            print("   " * level + prefix, node.value, f"(altura: {node.height})")
            if node.left is not None or node.right is not None:
                self._print_tree(node.left, level + 1, "ESQ:")
                self._print_tree(node.right, level + 1, "DIR:")

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        
        # Atualiza a altura corretamente
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node
    
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    
    # Contagem
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def count_full_nodes(self):
        return self._count_full_nodes(self.root)

    def _count_full_nodes(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is not None and node.right is not None:
            count = 1
        return count + self._count_full_nodes(node.left) + self._count_full_nodes(node.right)

    def count_half_nodes(self):
        return self._count_half_nodes(self.root)

    def _count_half_nodes(self, node):
        if node is None:
            return 0
        count = 0
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            count = 1
        return count + self._count_half_nodes(node.left) + self._count_half_nodes(node.right)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def is_structurally_identical(self, other_bst):
        return self._is_structurally_identical(self.root, other_bst.root)

    def _is_structurally_identical(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (self._is_structurally_identical(node1.left, node2.left) and 
                self._is_structurally_identical(node1.right, node2.right))

    def is_identical(self, other_bst):
        return self._is_identical(self.root, other_bst.root)

    def _is_identical(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.value == node2.value and 
                self._is_identical(node1.left, node2.left) and 
                self._is_identical(node1.right, node2.right))

    def mirror(self):
        new_tree = BST()
        new_tree.root = self._mirror(self.root)
        return new_tree

    def _mirror(self, node):
        if node is None:
            return None
        new_node = TreeNode(node.value)
        # Corrigindo a inversão - agora está correto
        new_node.left = self._mirror(node.right)
        new_node.right = self._mirror(node.left)
        # Atualizando a altura após espelhamento
        new_node.height = 1 + max(self._get_height(new_node.left), self._get_height(new_node.right))
        return new_node

    def list_range(self, min_val, max_val):
        """Returns a LinkedList of values in the range [min_val, max_val]"""
        result = SLS()
        self._list_range(self.root, min_val, max_val, result)
        return result
    
    def _list_range(self, node, min_val, max_val, result):
        if node is None:
            return
        
        if node.value > min_val:
            self._list_range(node.left, min_val, max_val, result)
        
        if min_val <= node.value <= max_val:
            result.add(node.value)
        
        if node.value < max_val:
            self._list_range(node.right, min_val, max_val, result)
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def _remove(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)
        return node
    
    def remove_range(self, min_val, max_val):
        self.root = self._remove_range(self.root, min_val, max_val)
        # Atualiza alturas após remoção
        self._update_heights(self.root)
        
        
    def _remove_range(self, node, min_val, max_val):
        if node is None:
            return None
        
        node.left = self._remove_range(node.left, min_val, max_val)
        node.right = self._remove_range(node.right, min_val, max_val)
        
        if min_val <= node.value <= max_val:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = self._remove(node.right, temp.value)
        return node

    def _update_heights(self, node):
        if node is None:
            return 0
        left_height = self._update_heights(node.left)
        right_height = self._update_heights(node.right)
        node.height = 1 + max(left_height, right_height)
        return node.height



if __name__ == "__main__":
    def print_ll(ll):
        current = ll.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("LinkedList:", "->".join(values) if values else "empty")

    bst = BST()
    valores = [50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45]
    for val in valores:
        bst.insert(val)

    bst.print_tree()
    print("\nConteúdo da árvore em ordem (travessia in-order) em LinkedList:")
    print_ll(bst.list_range(0, 100))
    print("\n")

    # Contagem de Nós
    print("Contagem de nos")
    print(f"Nós Folha (sem filhos): {bst.count_leaves()}")
    print(f"Nós Completos (com 2 filhos): {bst.count_full_nodes()}")
    print(f"Nós Semi-Cheios (com 1 filho): {bst.count_half_nodes()}")

    # Altura dos Nós 
    print("\nValidacao de alturas")
    print(f"Altura da raiz (nó 50): {bst.root.height}")
    print(f"Altura da sub-árvore esquerda (nó 30): {bst.root.left.height}")
    print(f"Altura da sub-árvore direita (nó 70): {bst.root.right.height}")

    # Comparação de Árvores
    print("\nComparacao de Arvores")
    bst_identica = BST()
    for val in valores: bst_identica.insert(val)
    bst_diferente = BST()
    for val in [60, 30, 80, 20, 50]: bst_diferente.insert(val)
    
    print(f"A árvore principal é ESTRITAMENTE IDÊNTICA à 'bst_identica")
    print(f"Resultado: {bst.is_identical(bst_identica)}")

    print(f"\nA árvore principal é ESTRUTURALMENTE IDÊNTICA à 'bst_diferente'?")
    print(f"Resultado: {bst.is_structurally_identical(bst_diferente)}")

    # Árvore Espelhada 
    bst_espelhada = bst.mirror()
    print(f"Pricipal" )
    bst.print_tree()
    
    print("\nEspelhada")
    bst_espelhada.print_tree()

    # Listar Chaves em um Intervalo
    print("valores no intervalo [25, 60]:")
    print_ll(bst.list_range(25, 60))

    #Remover Chaves em um Intervalo 
    print("árvore ANTES da remoção era:")
    print_ll(bst.list_range(0, 100))
    
    print("\nRemovendo os nós com chaves no intervalo [30, 70]")
    bst.remove_range(30, 70)
    
    print("\nO estado da árvore DEPOIS da remoção é:")
    print_ll(bst.list_range(0, 100))
    
    print("\nÁrvore após remoção do intervalo [30,70]:")
    bst.print_tree()