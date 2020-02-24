# 导入dkinter库 Menubutton
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(300, 300)

# 加入menubutton组件
menubutton = tkinter.Menubutton(root, text='性别')

# 摆放组件
menubutton.pack()

# 添加选项

sex = tkinter.StringVar()
menu = tkinter.Menu(menubutton)
menu.add_radiobutton(label='男', variable=sex)
menu.add_radiobutton(label='女', variable=sex)

# 将菜单配置到组件
menubutton.config(menu=menu)

# 将主窗口对象加入消息循环中
root.mainloop()
