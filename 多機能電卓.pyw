# 電卓 Level3

import tkinter as tk  # tkinterモジュールをインポート
import math  # 数学関数をインポート

# メイン関数
def main():
    root = tk.Tk()  # メインウィンドウを作成
    root.title("電卓L3")  # ウィンドウタイトルを設定
    den = Dentaku(root)  # Dentakuクラスのインスタンスを作成
    root.mainloop()  # イベントループを開始してウィンドウを表示

# 電卓クラス
class Dentaku():
    # 作成（初期化）
    def __init__(self, root):
        self.tf = tk.Frame(root)  # トップレベルのフレーム（ウィンドウ内のエリア）を作成
        self.tf.grid(column=0, row=0, padx=15, pady=15)  # グリッドレイアウトで配置
        self.first_operand = None  # 最初の数値（演算のため）
        self.current_operation = None  # 現在選択されている演算子
        self.decimal = False  # 小数点モード
        self.memory = 0  # メモリの初期化

        # ボタンを配置（ラベル、関数を定義したリスト）
        ButtonDef = (
            # 行 列 ラベル 関数
            (4, 0, "0", self.numinput),  # ボタン位置、ラベル、関数のマッピング
            (3, 0, "1", self.numinput),
            (3, 1, "2", self.numinput),
            (3, 2, "3", self.numinput),
            (2, 0, "4", self.numinput),
            (2, 1, "5", self.numinput),
            (2, 2, "6", self.numinput),
            (1, 0, "7", self.numinput),
            (1, 1, "8", self.numinput),
            (1, 2, "9", self.numinput),
            (4, 1, "*", self.mul),  # 乗算ボタン
            (4, 2, "/", self.div),  # 除算ボタン
            (1, 3, "-", self.sub),  # 減算ボタン
            (2, 3, "+", self.add),  # 加算ボタン
            (3, 3, "=", self.equal),  # イコールボタン
            (4, 3, "C", self.clear),  # クリアボタン
            (5, 0, ".", self.decimal_mode),  # 小数点ボタン
            (5, 1, "M+", self.memory_add),  # メモリ追加ボタン
            (5, 2, "M-", self.memory_sub),  # メモリ減算ボタン
            (5, 3, "MC", self.memory_clear),  # メモリクリアボタン
            (6, 0, "MR", self.memory_recall),  # メモリ呼び出しボタン
            (6, 1, "MS", self.memory_store),  # メモリ保存ボタン
            (6, 2, "√", self.square_root),  # 平方根ボタン
            (6, 3, "±", self.toggle_sign),  # ±ボタン
        )

        root.option_add('*Button.font', 'ＭＳゴシック 28')  # ボタンのフォント設定
        for r, c, label, func in ButtonDef:  # 定義されたボタンを配置
            Button = tk.Button(self.tf, text=label)  # ボタンを作成
            Button.bind("<Button-1>", func)  # ボタンがクリックされたときの処理をバインド
            Button.grid(column=c, row=r, sticky=tk.N + tk.E + tk.S + tk.W)  # ボタンの位置とサイズを設定

        # 数字が表示される「エントリー」
        root.option_add('*Entry.font', 'ＭＳゴシック 32')  # エントリーのフォント設定
        self.NumBox = tk.Entry(self.tf, width=10, justify=tk.RIGHT)  # 入力された数字を表示するエントリー
        self.NumBox.insert(tk.END, "0")  # 初期値として"0"を表示
        self.NumBox.grid(column=0, columnspan=4, row=0)  # エントリーの配置

    # ボタン毎の動作を定義（イベントドライバ群）
    def numinput(self, e):  # 数字入力の処理
        button_label = e.widget['text']  # 数字ボタンのラベル
        current_value = self.NumBox.get()  # 現在表示されている値
        if current_value == "0" or current_value == "Undefined":  # 初期状態やエラー状態のチェック
            self.NumBox.delete(0, tk.END)  # 既存の値を削除
            self.NumBox.insert(0, button_label)  # ボタンのラベルを表示
        else:
            if self.decimal == True and button_label != ".":  # 小数点モード
                if "." in current_value:
                    self.NumBox.insert(tk.END, button_label)  # 小数点があればそのまま表示
                else:
                    self.NumBox.insert(tk.END, "." + button_label)  # 小数点を挿入して表示
            else:
                self.NumBox.insert(tk.END, button_label)  # 数字を入力する

    def mul(self, e):  # 乗算
        self.first_operand = float(self.NumBox.get())  # 最初の数値を取得
        self.current_operation = "mul"  # 現在の演算を乗算に設定
        self.NumBox.delete(0, tk.END)  # 数値入力欄をクリア

    def div(self, e):  # 除算
        self.first_operand = float(self.NumBox.get())  # 最初の数値を取得
        self.current_operation = "div"  # 現在の演算を除算に設定
        self.NumBox.delete(0, tk.END)  # 数値入力欄をクリア

    def sub(self, e):  # 減算
        self.first_operand = float(self.NumBox.get())  # 最初の数値を取得
        self.current_operation = "sub"  # 現在の演算を減算に設定
        self.NumBox.delete(0, tk.END)  # 数値入力欄をクリア

    def add(self, e):  # 加算
        self.first_operand = float(self.NumBox.get())  # 最初の数値を取得
        self.current_operation = "add"  # 現在の演算を加算に設定
        self.NumBox.delete(0, tk.END)  # 数値入力欄をクリア

    def equal(self, e):  # イコールボタンの処理
        second_operand = float(self.NumBox.get())  # 2番目の数値を取得
        if self.current_operation == "mul":  # 乗算
            result = self.first_operand * second_operand
        elif self.current_operation == "add":  # 加算
            result = self.first_operand + second_operand
        elif self.current_operation == "sub":  # 減算
            result = self.first_operand - second_operand
        elif self.current_operation == "div":  # 除算
            if second_operand == 0:  # ゼロで割り算の場合
                self.NumBox.delete(0, tk.END)
                self.NumBox.insert(0, "Undefined")  # "Undefined"を表示
                return
            else:
                result = self.first_operand / second_operand
        else:
            return
        self.NumBox.delete(0, tk.END)  # 結果表示欄をクリア
        self.NumBox.insert(0, str(result))  # 結果を表示
        self.current_operation = None  # 演算のリセット
        self.decimal = False  # 小数モードのリセット

    def clear(self, e):  # クリアボタンの処理
        self.NumBox.delete(0, tk.END)  # 数値表示欄をクリア
        self.NumBox.insert(0, "0")  # 初期状態に戻す
        self.first_operand = None  # 最初の数値をリセット
        self.current_operation = None  # 演算をリセット
        self.decimal = False  # 小数モードをリセット

    def decimal_mode(self, e):  # 小数点モードの切替
        current_value = self.NumBox.get()  # 現在表示されている値
        if not self.decimal:  # 小数点がまだない場合
            self.decimal = True  # 小数点モードを有効に
            if "." not in current_value:  # すでに小数点が含まれていないか確認
                self.NumBox.insert(tk.END, ".")  # 小数点を挿入
        else:
            return

    def memory_add(self, e):  # メモリ追加
        self.memory += float(self.NumBox.get())  # 現在の値をメモリに加算
        self.clear(e)  # 数値入力欄をクリア

    def memory_sub(self, e):  # メモリ減算
        self.memory -= float(self.NumBox.get())  # 現在の値をメモリから減算
        self.clear(e)  # 数値入力欄をクリア

    def memory_clear(self, e):  # メモリクリア
        self.memory = 0  # メモリのリセット

    def memory_recall(self, e):  # メモリ呼び出し
        self.NumBox.delete(0, tk.END)  # 数値表示欄をクリア
        self.NumBox.insert(0, str(self.memory))  # メモリの値を表示

    def memory_store(self, e):  # メモリ保存
        self.memory = float(self.NumBox.get())  # 現在の値をメモリに保存

    def square_root(self, e):  # 平方根
        current_value = float(self.NumBox.get())  # 現在表示されている値
        result = math.sqrt(current_value)  # 平方根を計算
        self.NumBox.delete(0, tk.END)  # 数値表示欄をクリア
        self.NumBox.insert(0, str(result))  # 結果を表示

    def toggle_sign(self, e):  # ±ボタン
        current_value = float(self.NumBox.get())  # 現在表示されている値
        result = current_value * -1  # 符号を反転
        self.NumBox.delete(0, tk.END)  # 数値表示欄をクリア
        self.NumBox.insert(0, str(result))  # 結果を表示

# メイン関数を実行
main()
