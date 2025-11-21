from typing import Any, Iterable, Optional, Iterator

class Node:
    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"

class LinkedList: 
    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        self.head: Optional[Node] = None
        self._length = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value: Any) -> None:
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self._length += 1

    def prepend(self, value: Any) -> None:
        self.head = Node(value, next=self.head)
        self._length += 1

    def insert_after(self, prev_node: Node, value: Any) -> None:
        if prev_node is None:
            raise ValueError("prev_node must be a Node in the list")
        prev_node.next = Node(value, next=prev_node.next)
        self._length += 1

    def remove(self, value: Any) -> bool:
        """Remove first occurrence of value. Returns True if removed."""
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._length -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def pop(self, index: int = -1) -> Any:
        """Remove and return element at index (default last)."""
        if self.head is None:
            raise IndexError("pop from empty list")
        if index < 0:
            index = self._length + index
        if not (0 <= index < self._length):
            raise IndexError("index out of range")
        prev = None
        cur = self.head
        for _ in range(index):
            prev, cur = cur, cur.next
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next
        self._length -= 1
        return cur.value

    def find(self, predicate) -> Optional[Node]:
        """Return first node for which predicate(node.value) is True."""
        cur = self.head
        while cur:
            if predicate(cur.value):
                return cur
            cur = cur.next
        return None

    def reverse(self) -> None:
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def clear(self) -> None:
        self.head = None
        self._length = 0

    def to_list(self) -> list:
        return [x for x in self]

    @classmethod
    def from_iter(cls, iterable: Iterable[Any]) -> "LinkedList":
        return cls(iterable)

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"


# Example usage:
# ll = LinkedList([1, 2, 3])
# ll.append(4)
# ll.prepend(0)
# print(ll)           # LinkedList([0, 1, 2, 3, 4])
# ll.remove(2)
# print(ll.to_list()) # [0, 1, 3, 4]
# ll.reverse()
# print(ll)           # LinkedList([4, 3, 1, 0])