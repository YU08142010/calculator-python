import sys

# CLI helper functions (for compatibility)
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('無効な数字です。もう一度入力してください。')

def get_operator(prompt):
    ops = ['+', '-', '*', '/']
    while True:
        op = input(prompt)
        if op in ops:
            return op
        print('演算子は + - * / のいずれかでなければなりません。')

# CLI main loop

def run_cli():
    while True:
        a = get_number('最初の数字は何ですか >>')
        b = get_number('最後の数字は何ですか >>')
        c = get_operator('記号は何ですか +|-|*|/ >>')

        try:
            if c == '+':
                result = a + b
            elif c == '-':
                result = a - b
            elif c == '*':
                result = a * b
            elif c == '/':
                result = a / b
            print('結果:', result)
        except ZeroDivisionError:
            print('0で割ることはできません。')

        cont = input('続けますか？ (y/n) >> ').strip().lower()
        if cont != 'y':
            print('終了します。')
            break

# GUI implementation using tkinter

def run_gui():
    try:
        import tkinter as tk
        from tkinter import messagebox
    except ImportError:
        print('TkinterがインストールされていないためGUIを起動できません。')
        return

    def calculate():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            op = operator_var.get()
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                res = a / b
            result_var.set(str(res))
        except ValueError:
            messagebox.showerror('エラー', '数値を正しく入力してください。')
        except ZeroDivisionError:
            messagebox.showerror('エラー', '0で割ることはできません。')

    root = tk.Tk()
    root.title('電卓')

    tk.Label(root, text='最初の数字').grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text='次の数字').grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text='演算子').grid(row=2, column=0, padx=5, pady=5)
    operator_var = tk.StringVar(root)
    operator_var.set('+')
    tk.OptionMenu(root, operator_var, '+', '-', '*', '/').grid(row=2, column=1, padx=5, pady=5)

    tk.Button(root, text='計算', command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

    result_var = tk.StringVar()
    tk.Label(root, text='結果').grid(row=4, column=0, padx=5, pady=5)
    tk.Label(root, textvariable=result_var).grid(row=4, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    # コマンドライン引数に "cli" があればコンソール版を起動
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'cli':
        run_cli()
    else:
        run_gui()
