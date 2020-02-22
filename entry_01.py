# 导入dkinter库 entry组件
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入单行文本输入框;长度代表字符数
username = tkinter.Entry(root, width=50, bg='red', fg='yellow', font=('simhei', 20))

# 摆放组件
username.pack()

# 加入单行文本输入框（密码形式）
password = tkinter.Entry(root, show='*')

# 摆放组件
password.pack()

# 加入单行文本输入框（state属性）
password1 = tkinter.Entry(root, state='disabled')

# 摆放组件
password1.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
