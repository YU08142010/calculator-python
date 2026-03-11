def calculate():
    """
    ユーザーからの入力を受け取り、四則演算を行うシンプルな計算機プログラム。
    eval()を避け、例外処理とバリデーションを組み込んでいます。
    """
    print("--- 簡易計算機 (安全版) ---")
    
    while True:
        try:
            # 入力の取得
            line1 = input("1つ目の数値を入力してください (終了するには 'q') >> ").strip().lower()
            if line1 == 'q':
                break
            num1 = float(line1)

            num2 = float(input("2つ目の数値を入力してください >> "))
            operator = input("演算子を選択してください [+ - * /] >> ").strip()

            # 計算処理
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("エラー: 0で割ることはできません。")
                    continue
                result = num1 / num2
            else:
                print(f"エラー: '{operator}' は無効な演算子です。")
                continue

            # 結果の表示 (整数の場合は整数として表示)
            if result.is_integer():
                result = int(result)
            print(f"結果: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("エラー: 有効な数値を入力してください。")
            continue

        # 継続確認
        cont = input("計算を続けますか？ (y/n) >> ").lower()
        if cont != 'y':
            print("終了します。")
            break

if __name__ == "__main__":
    calculate()
