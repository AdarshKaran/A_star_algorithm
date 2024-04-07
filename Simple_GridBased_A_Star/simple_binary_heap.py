class BinaryHeap:
    """A simple binary heap implementation."""

    def __init__(self):
        """Initialize an empty binary heap."""
        self.heap = []

    def push(self, value):
        """Push a value onto the heap, maintaining the heap property."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Pop and return the smallest value from the heap, maintaining the heap property.
        If the heap is empty, return None.
        """
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            value = self.heap.pop()
            self._heapify_down(0)
            return value
        return None

    def _heapify_up(self, index):
        """Restore the heap property by swapping the element at index with its parent, if necessary."""
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Restore the heap property by swapping the element at index with its smallest child, if necessary."""
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)