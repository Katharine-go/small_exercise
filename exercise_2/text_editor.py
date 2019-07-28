import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
import tkinter.scrolledtext as tst

class Application(tk.Frame):
    def __init__(self,master = None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.textEdit = tst.ScrolledText(self, width = 80, height = 20) #滚动栏
        self.textEdit.grid(row = 0, column = 0, rowspan = 6)
        self.btnOpen = tk.Button(self, text = 'open', command = self.funcOpen)
        self.btnOpen.grid(row = 1, column = 1)
        self.btnSave = tk.Button(self, text = 'save', command = self.funcSave)
        self.btnSave.grid(row = 2, column = 1)
        self.btnColor = tk.Button(self, text = 'color', command = self.funcColor)
        self.btnColor.grid(row = 3, column = 1)
        self.btnQuit = tk.Button(self, text = 'quit', command = self.funcQuit)
        self.btnQuit.grid(row = 4, column = 1)
    def funcOpen(self):
     	self.textEdit.delete(1.0,tk.END) #清空text组件内容
     	fname = filedialog.askopenfilename(filetypes=[("Python源文件", ".py")])
     	with open(fname, 'r', encoding = 'utf-8') as f1:  #打开文件
     		str1 = f1.read()  #将文件中的内容读到str1中
     	self.textEdit.insert(0.0, str1)  #插入内容到文本框中
    def funcSave(self):
     	str1 = self.textEdit.get(1.0, tk.END)
     	fname = filedialog.asksaveasfilename(filetypes=[("Python源文件", ".py")])
     	with open(fname, 'w', encoding = 'utf-8') as f1:  #打开文件
     	    f1.write(str1)
    def funcColor(self):
     	t, c = colorchooser.askcolor(title = "set color")
     	self.textEdit.config(bg = c)
    def funcQuit(self):
     	root.destroy()

root = tk.Tk()
root.title("Text Editor")
app = Application(master = root)
app.mainloop()
