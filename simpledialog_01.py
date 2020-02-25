# 导入tkinter库
import tkinter
# 导入messagebox库
import tkinter.simpledialog

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')


# 创建函数
def askname():
    result = tkinter.simpledialog.askstring(title='输入名字', prompt='请输入名字', initialvalue='xiaoyang')
    print(result)


# 加入组件
btu = tkinter.Button(root, text='获取用户名', command=askname)

# 摆放组件
btu.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
