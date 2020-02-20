# 导入dkinter库
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('300x300')

img1 = tkinter.PhotoImage(file="~/文档/123.png")

# 加入按钮组件1
btu1 = tkinter.Button(root, text='按钮1', bg='red', fg='yellow', font=('simhei', 20))

# 摆放组件1
btu1.pack()

# 加入按钮组件2 设置文本对齐方式 justify (默认中间）
btu2 = tkinter.Button(root, text='按钮2\n第二行', justify='left', font=('simhei', 20))

# 摆放组件2
btu2.pack()

# 加入按钮组件3 state 按钮状态
btu3 = tkinter.Button(root, text='按钮3', state='disable', font=('simhei', 20))

# 摆放组件3
btu3.pack()

# 加入按钮组件4 image compound 图片及文字位置,默认只支持gif和png格式
btu4 = tkinter.Button(root, text='按钮4', image=img1, compound='left', font=('simhei', 20))

# 摆放组件4
btu4.pack()

# 将主窗口对象加入消息循环中
root.mainloop()
