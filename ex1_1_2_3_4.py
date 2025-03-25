class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def show_heap_lst(self):
        print(self.heap)

    def search(self, target):
        for i in self.heap:
            if i == target:
                return True
        return False

def turn_into_heap(intLst):
    heap = MinHeap()
    for i in intLst:
        heap.insert(i)
    return heap

intLst = [5, 2, 3, 7, 1]

heap = turn_into_heap(intLst)

heap.insert(0)

heap.show_heap_lst()

to_find = 7

result_search = heap.search(to_find)

if result_search:
    print(f"Valor {to_find} encontrado!")
else:
    print(f"Valor {to_find} não encontrado.")

heap.pop()

heap.show_heap_lst()