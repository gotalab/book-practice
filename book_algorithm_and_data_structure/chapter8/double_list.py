# 循環・重連結リスト
from __future__ import annotations
from typing import Any, Type

class Node:
    """循環・重連結リスト用ノードクラス"""
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    """循環・重連結リストクラス"""
    def __init__(self) -> None:
        self.head = self.current = Node() # ダミーノード
        self.no = 0

    def __len__(self) -> int:
        """線形リスト上のノード数を返却する"""
        return self.no

    def is_empty(self) -> bool:
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """dataと等価なノードを探索"""
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        """着目ノードを表示"""
        if self.is_empty():
            print('着目ノードはありません')
        else:
            print(self.current.data)

    def print(self) -> None:
        """全ノードを表示"""
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """全ノードを逆順に表示"""
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """着目ノードを一つ後方に進める"""
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """着目ノードを一つ前方に進める"""
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        """着目ノードの直後にノードを挿入"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """先頭にノードを挿入"""
        self.current = self.head
        self.add(data)

    def add_last(self, data: Any) -> None:
        """末尾にノードを挿入"""
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        """着目ノードを削除"""
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.currnt is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """ノードpを削除"""
        ptr = self.head.next
        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """先頭ノードを削除"""
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        """末尾ノードを削除"""
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0

    def __iter__(self) -> DoubleLinkedListIterator:
        """イテレータを返却"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """降順イテレータを返却"""
        return DoubleLinkedListReverseIterator(self.head)


class DoubleLinkedListIterator:
    """DoubleLinkedListのイテレータ用クラス"""
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = data.current.next
            return data

class DoubleLinkedListReverseIterator:
    """DoubleLinkedListの降順イテレータ用クラス"""
    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = data.current.prev
            return data
