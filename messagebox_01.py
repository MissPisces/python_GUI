# 导入tkinter库
import tkinter
# 导入messagebox库
import tkinter.messagebox

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')


# 创建函数
def okcancel():
    result = tkinter.messagebox.askokcancel(title='okcancel', message='Are you OK?')
    print(result)


# 加入组件
btu = tkinter.Button(root, text='按钮一', command=okcancel)

# 摆放组件
btu.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
