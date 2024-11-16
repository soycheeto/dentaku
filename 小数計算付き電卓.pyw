# 電卓 Level2

import sys
import tkinter as tk

# メイン関数
def main():
	root = tk.Tk()
	root.title("電卓L2")
	den = Dentaku(root)
	root.mainloop()

# 電卓クラス
class Dentaku():
	# 作成
	def __init__(self, root):
		self.tf = tk.Frame(root)	# トップレベルのフレーム
		self.tf.grid(column = 0, row = 0, padx = 15, pady = 15)
		self.first_operand = None
		self.current_operation = None
		self.decimal = False

		# ボタンを配置
		ButtonDef = (
		#	 行 列 ラベル 関数
			(4, 0, "0", self.numinput),
			(3, 0, "1", self.numinput),
			(3, 1, "2", self.numinput),
			(3, 2, "3", self.numinput),
			(2, 0, "4", self.numinput),
			(2, 1, "5", self.numinput),
			(2, 2, "6", self.numinput),
			(1, 0, "7", self.numinput),
			(1, 1, "8", self.numinput),
			(1, 2, "9", self.numinput),
			(4, 1, "*", self.mul),
			(4, 2, "/", self.div),
			(1, 3, "-", self.sub),
			(2, 3, "+", self.add),
			(3, 3, "=", self.equal),
			(4, 3, "C", self.clear),
		    (5, 0, ".", self.decimal_mode),)
	
		root.option_add('*Button.font', 'ＭＳゴシック 28')
		for r, c, label, func in ButtonDef:
			Button = tk.Button(self.tf, text = label)
			Button.bind("<Button-1>", func)
			Button.grid(column = c, row = r, sticky = tk.N +tk.E + tk.S + tk.W)

		# 数字が表示される「エントリー」
		root.option_add('*Entry.font', 'ＭＳゴシック 32')
		self.NumBox = tk.Entry(self.tf, width = 10, justify = tk.RIGHT)
		self.NumBox.insert(tk.END, "0")
		self.NumBox.grid(column = 0, columnspan = 4, row = 0)

	# ボタン毎の動作を定義（イベントドライバ群）
	def numinput(self, e):	
		button_label=e.widget['text']		# 数字キー
		current_value=self.NumBox.get()
		if current_value=="0":
			self.NumBox.delete(0, tk.END)
			self.NumBox.insert(0, button_label)
		else:
			if self.decimal==True and button_label != ".":
				if "." in current_value:
					self.NumBox.insert(tk.END, button_label)
				else:
					self.NumBox.insert(tk.END, "." + button_label)
			else:
			    self.NumBox.insert(tk.END, button_label)
		
	def mul(self, e):				# ×
		self.first_operand =float(self.NumBox.get())
		self.current_operation = "mul"
		self.NumBox.delete(0,tk.END)

	def div(self, e):				# ／
		self.first_operand =float(self.NumBox.get())
		self.current_operation = "div"
		self.NumBox.delete(0, tk.END)

	def sub(self, e):				# －
		self.first_operand =float(self.NumBox.get())
		self.current_operation = "sub"
		self.NumBox.delete(0, tk.END)

	def add(self, e):				# ＋
		self.first_operand =float(self.NumBox.get())
		self.current_operation = "add"
		self.NumBox.delete(0, tk.END)

	def equal(self, e):				# ＝
		second_operand =float(self.NumBox.get())
		if self.current_operation=="mul":
			result = self.first_operand * second_operand
		elif self.current_operation=="add":
			result = self.first_operand + second_operand
		elif self.current_operation=="sub":
			result = self.first_operand - second_operand
		elif self.current_operation=="div":
			if second_operand==0:
				self.NumBox.delete(0, tk.END)
				self.NumBox.insert(0, "Undefined")
				return
			else:
				result = self.first_operand/second_operand
		else:
			return
		self.NumBox.delete(0,tk.END)
		self.NumBox.insert(0,float(result))
		self.current_operation = None
		self.decimal = False

	def clear(self, e):				# Ｃ
		self.NumBox.delete(0, tk.END)
		self.NumBox.insert(0,"0")
		self.first_operand = None
		self.current_operation = None
		self.decimal = False
	def decimal_mode(self, e):
		current_value = self.NumBox.get()
		if not self.decimal:
			self.decimal=True
			if '.' not in current_value:
				self.NumBox.insert(tk.END, ".")
		else:
			pass
			
	

if __name__ == '__main__':
	main()
