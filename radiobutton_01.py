# 导入dkinter库  radiobutton
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

sex = tkinter.StringVar()

# 加入组件
radiobutton1 = tkinter.Radiobutton(root, text='男', variable=sex, value='man')

# 摆放组件
radiobutton1.pack()

# 加入组件
radiobutton2 = tkinter.Radiobutton(root, text='女', variable=sex, value='woman')

# 摆放组件
radiobutton2.pack()
# 将主窗口对象加入消息循环中
root.mainloop()
