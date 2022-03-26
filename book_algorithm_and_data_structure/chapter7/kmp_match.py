# KMP法による文字列探索

def kmp_match(txt: str, pat: str) -> int:
    """KMP法による文字列探索"""
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    # スキップテーブルの作成
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    # 探索
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
            # print(f'if pt:{pt} pp:{pp}')
        elif pp == 0:
            pt += 1
            # print(f'elif pt:{pt} pp:{pp}')
        else:
            pp = skip[pp]
            # print(f'else pt:{pt} pp:{pp}')

    return pt - pp if pp == len(pat) else -1


if __name__ == '__main__':
    s1 = input('テキスト：')
    s2 = input('パターン：')
    idx = kmp_match(s1, s2)

    if idx == -1:
        print('テキスト中にパターンは存在しません')
    else:
        print(f'{idx + 1}文字目にマッチします')
