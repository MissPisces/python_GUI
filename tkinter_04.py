# 组件布局place
# 导入dkinter库
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(500, 500)

# 加入按钮组件1
btu1 = tkinter.Button(root, text='button1')

# 摆放组件1
btu1.place(x=100, y=20)

# 加入按钮组件2
btu2 = tkinter.Button(root, text='button2')

# 摆放组件2
btu2.place(x=200, y=120, width=50, height=50)

# 加入按钮组件3
btu2 = tkinter.Button(root, text='button3')

# 摆放组件3
btu2.place(relx=0.5, rely=0.5, relwidth=0.1, relheight=0.1)

# 将主窗口对象加入消息循环中
root.mainloop()
