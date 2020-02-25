# 导入tkinter库 text
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入组件
text = tkinter.Text(root, width=50, height=10)

# 摆放组件
text.pack()

# 设置值
text.insert(0.0, '你好呀，小朋友！')

# 将主窗口对象加入消息循环中
root.mainloop()
