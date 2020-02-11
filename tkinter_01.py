# 导入dkinter库
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(300, 300)

# 加入按钮组件
btu = tkinter.Button(root, text='button')

# 摆放组件
btu.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
