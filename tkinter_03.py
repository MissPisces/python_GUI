# 组件布局grid
# 导入dkinter库
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(500, 500)

# 加入按钮组件1
btu1 = tkinter.Button(root, text='button1')

# 摆放组件1
btu1.grid()

# 加入按钮组件2
btu2 = tkinter.Button(root, text='button2')

# 摆放组件2
btu2.grid(row=1, column=0)

# 加入按钮组件3
btu3 = tkinter.Button(root, text='button3')

# 摆放组件3
btu3.grid(row=0, column=1)

# 加入按钮组件4
btu4 = tkinter.Button(root, text='button4')

# 摆放组件4
btu4.grid(row=2, column=0, columnspan=2, ipadx=40)

# 加入按钮组件5
btu5 = tkinter.Button(root, text='button5')

# 摆放组件5
btu5.grid(row=0, column=2, rowspan=2, ipady=20)

# 将主窗口对象加入消息循环中
root.mainloop()
