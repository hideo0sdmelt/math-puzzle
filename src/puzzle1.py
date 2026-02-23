# 10進数、2進数、8進数いずれで表現しても回文数となる数のうち、
# 10進数、10以上、最小

def solve():
    for num in range(10, 1000):
        s10 = str(num)
        s2 = f"{num:b}"
        s8 = f"{num:o}"

        # 元の文字列と、逆順にした文字列を比較
        if (s10 == s10[::-1] and
                s2 == s2[::-1] and
                s8 == s8[::-1]):
            print(num, "は回文数")
            return num

    return None


if __name__ == "__main__":
    solve()
