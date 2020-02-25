# 导入dkinter库  scale
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入组件
scale = tkinter.Scale(root, orient='vertical', from_=50, to=80, resolution='0.5')

# 摆放组件
scale.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
