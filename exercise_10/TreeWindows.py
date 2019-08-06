import tkinter
import tkinter.ttk
import os

class TreeWindows:
    def __init__(self):
        self.win = tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win,height = 500) #树状
        self.ysb = tkinter.ttk.Scrollbar(self.win, orient="vertical", command=self.tree.yview())  # y滚动条
        self.xsb = tkinter.ttk.Scrollbar(self.win, orient="horizontal", command=self.tree.xview())  # x滚动条
        self.tree.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)  # y滚动条关联
        self.tree.grid(row=0, column=0)
        self.tree.heading("#0", text="Path", anchor="w")  # 初始化头部,表头 west靠近西方
        self.tree.bind("<<TreeviewSelect>>", self.gosel)  # 事件(选中)绑定

        filepath = "/Users/macintoshhd/Desktop"  # 路径
        root = self.tree.insert("", "end", text=filepath, open=True)  # 插入一个节点
        self.loadtree(root, filepath)  # 递归

        self.e = tkinter.StringVar()
        self.entry = tkinter.Entry(self.win, textvariable=self.e)
        self.e.set("请选择文件")
        self.entry.grid(row=0, column=2)

        self.ysb.grid(row=0, column=1, sticky="ns")
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.win.grid()  # 表格展示

    def loadtree(self, parent, rootpath):
        for path in os.listdir(rootpath):  # 遍历当前目录
            abspath = os.path.join(rootpath, path)  # 连接成绝对路径
            oid = self.tree.insert(parent, 'end', text=abspath, open=False)  # 插入树枝
            if os.path.isdir(abspath):
                self.loadtree(oid, abspath)  # 递归回去

    def gosel(self, event):
        self.select = event.widget.selection()  # 获取所选的项(可能是多项，所以要for循环)
        for idx in self.select:
            print(self.tree.item(idx)["text"])
            self.e.set(self.tree.item(idx)["text"])

    def show(self):
        self.win.mainloop()

mytree = TreeWindows()
mytree.show()
