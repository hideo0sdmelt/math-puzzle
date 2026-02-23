# ある数字の各桁に対して四則演算の演算子を入れる場合を考える
# 計算後に「元の数の桁を逆から並べた数字」と同じになるものを考えたい
# 1000～9999の範囲で上記条件を満たすものはいくつあるか
import itertools
import re

from tqdm import tqdm


def solve():
    # 使用する想定の演算子。空もありうる
    operators = ["+", "-", "*", "/", ""]

    # 対象の範囲を探索
    for num in tqdm(range(1000, 10000)):

        # 末尾が0のものは、逆順にすると桁が変わるのでスキップ
        if num % 10 == 0:
            continue

        s_num = str(num)

        # 「元の数の桁を逆から並べた数字」がこれ。ここと一致するかを見たい
        target = int(s_num[::-1])

        # 各演算子をそれぞれの数字の間に挟み込むパターンを考える
        for op1, op2, op3 in itertools.product(operators, repeat=3):

            # 少なくとも1つは演算子が入っていないと意味がないので、両方空はスキップ
            if op1 == "" and op2 == "" and op3 == "":
                continue

            # 各演算子をそれぞれの数字の間に挟み込んだ計算式
            expr = f"{s_num[0]}{op1}{s_num[1]}{op2}{s_num[2]}{op3}{s_num[3]}"
            # 2数字の先頭にある 0 を削除
            clean_expr = re.sub(r"\b0+(?=\d)", "", expr)

            # 0での割り算エラーを防ぐ
            try:
                # evalで文字列を計算。割り算を考慮してfloatで比較
                if eval(clean_expr) == target:
                    print(f"発見！: {expr} = {target} (元の数: {num})")
            except ZeroDivisionError:
                continue

    return None


if __name__ == "__main__":
    solve()
