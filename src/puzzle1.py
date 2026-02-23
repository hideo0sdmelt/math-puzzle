def solve(file_path):
    """ファイルから数字を読み込んで合計を出す関数"""
    total = 0
    with open(file_path, "r") as f:
        for line in f:
            total += int(line.strip())
    return total