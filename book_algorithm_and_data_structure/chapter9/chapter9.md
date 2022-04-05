# 第 9 章 木構造と二分探索木

## 9-1 木構造

前章で学習したリストは、順序付けられたデータの並びを表現するデータ構造でした。本章では、データ間の階層的な関係を表現するデータ構造である木構造を学習する。

### 木とは

#### 気に関する用語

木に関する用語は、階層的なデータ構造を表す木は、節・ノードと枝とで攻勢されます。各ノードは枝を通じて他のノードと結びつきます。もとも上流のノードが根、最下流のノードは葉です。

- 根
- 葉
- 非終端節
- 子
- 親
- 兄弟
- 先祖
- 子孫
- レベル
- 度数
- 高さ
- 部分木
- 空木

### 順序木と無順序木

### 順序木の探索

#### 幅優先探索、横型探索

レベルの低い点から始めて、左側から右側へとなぞり、それが終わると次のレベルに下る方法です。

#### 深さ優先探索・縦型探索

走査順が複数あり

- 行きがけ順
- 通りがけ順
- 帰りがけ順

## 9-2 二分木と二分探索木

### 二分木

- 各ノードが左の子と右の子を持つ木を二分木と呼ぶ。２つの子の一方あるいは、療法が存在しないノードがあっても大丈夫。

### 完全二分木

根から下方のレベルへとノードが空くことなく詰まっている二分木のことを完全二分木と呼びます。