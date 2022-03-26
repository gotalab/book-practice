# Boyer-Moore法による文字絵rつ探索（対象は0~255の文字）

def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256 # スキップテーブル

    # スキップテーブルの作成
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1
        print(ord(pat[pt]))

    # 探索
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1
