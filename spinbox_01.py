# 导入tkinter库 spinbox
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入组件
spinbox = tkinter.Spinbox(root, from_=0, to=100, increment=0.5)

# 摆放组件
spinbox.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
