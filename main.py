import importlib

def run():
    print("=== 数学パズル・セレクター ===")
    default_num = "12"  # 今集中している番号
    num = input(f"パズル番号を入力 (デフォルト {default_num}): ") or default_num

    # ファイル名を作成 (例: "src.puzzle1")
    module_name = f"src.puzzle{num}"

    try:
        # 指定された番号のファイルを動的に読み込む
        puzzle_module = importlib.import_module(module_name)

        print(f"--- パズル {num} 開始 ---")

        # 読み込んだファイルの中にある solve() 関数を実行
        # データのパスが必要なら引数で渡す
        data_path = f"data/numbers{num}.txt"
        result = puzzle_module.solve(data_path)

        print(f"結果: {result}")
        print(f"--- パズル {num} 終了 ---")

    except ModuleNotFoundError:
        print(f"エラー: src/puzzle{num}.py が見つかりません！")
    except AttributeError:
        print(f"エラー: puzzle{num}.py の中に 'solve' 関数が見当たりません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    run()