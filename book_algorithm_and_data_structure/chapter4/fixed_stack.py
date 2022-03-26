# 固定長スタッククラス
from typing import Any

class FixedStack:
    """"固定長スタッククラス"""
    class Empty(Exception):
        """空のFixedStackに対してpopあるいはpeekが呼び出されたときに送出する例外"""
        pass

    class Full(Exception):
        """満杯のFixedStackに対してpushが呼び出されたときに送出する例外"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # スタック本体
        self.capacity = capacity # スタックの容量
        self.ptr = 0 # スタックポインタ

    def __len__(self) -> int:
        """スタックに積まれているデータ数を返す"""
        return self.ptr

    def is_empty(self) -> bool:
        """スタックが空かどうか"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """スタックが満杯かどうか"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """スタックにvalueをプッシュする"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """スタックからデータをポップ（頂上のデータを取り出す）"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """スタックからデータをピーク（頂上のデータを覗き見）"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """スタックを空にする（全データの削除）"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """スタックからvalueを探して添字（見つからないときは-1）を返す"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        """スタックに含まれるvalueの個数を返す"""
        counter = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                counter += 1
        return counter

    def __contains__(self, value: Any) -> bool:
        """スタックにvalueが含まれているか"""
        return self.count(value)

    def dump(self) -> None:
        """ダンプ（スタック内の全データを底から頂上の順に表示）"""
        if self.is_empty():
            print('スタックは空です')
        else:
            print(self.stk[:self.ptr])