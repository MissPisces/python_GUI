# 导入dkinter库 panedwindow
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入panedwindow组件
panedwindow = tkinter.PanedWindow(root, orient='horizontal')

# 添加其它组件

but1 = tkinter.Button(panedwindow, text='按钮一')
but2 = tkinter.Button(panedwindow, text='按钮二')

panedwindow.add(but1)
panedwindow.add(but2)
# 摆放panedwindow组件
panedwindow.pack(fill='both', expand='yes')

# 将主窗口对象加入消息循环中
root.mainloop()
