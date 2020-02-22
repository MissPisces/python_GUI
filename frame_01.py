# 导入dkinter库  frame 框架
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(300, 300)

# 加入框架1
frame1 = tkinter.Frame(root, bg='red', width=300, height=100)

# 摆放框架1
frame1.pack()

# 在框架1中摆放组件
bt1 = tkinter.Button(frame1, text='按键一', font=('simhei', 20))
bt1.pack(side='left')
bt2 = tkinter.Button(frame1, text='按键二', font=('simhei', 20))
bt2.pack(side='left')
bt3 = tkinter.Button(frame1, text='按键三', font=('simhei', 20))
bt3.pack(side='left')

# 加入框架2
frame2 = tkinter.Frame(root, bg='green', width=300, height=100)

# 摆放框架2
frame2.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
