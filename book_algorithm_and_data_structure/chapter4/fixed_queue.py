# 固定長キュークラス
from typing import Any

class FixedQueue:
    """"固定長キュークラス"""
    class Empty(Exception):
        """空のFixedStackに対してdequeあるいはpeekが呼び出されたときに送出する例外"""
        pass

    class Full(Exception):
        """満杯のFixedQueueに対してenqueが呼び出されたときに送出する例外"""
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0 # 現在のデータ数
        self.front = 0 # 先頭要素カーソル
        self.rear = 0 # 末尾要素カーソル
        self.capacity = capacity # キューの容量
        self.que = [None] * capacity # キューの本体

    def __len__(self) -> int:
        """キューに押し込まれているデータ数を返す"""
        return self.no

    def is_empty(self) -> bool:
        """スタックが空かどうか"""
        return self.no <= 0

    def is_full(self) -> bool:
        """スタックが満杯かどうか"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """データxをエンキュー"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        """データをデキュー"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """データをピーク（先頭データを覗き見）"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.que[self.front]


    def find(self, value: Any) -> Any:
        """キューからvalueを探して添字（見つからなければ-1）を返す"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        """キューに含まれるvalueの個数を返す"""
        counter = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                counter += 1
        return counter

    def __contains__(self, value: Any) -> bool:
        """キューにvalueが含まれているか"""
        return self.count(value)

    def clear(self) -> None:
        """キューを空にする"""
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """全データを先頭 -> 末尾の順に表示"""
        if self.is_empty():
            print('キューは空です')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()