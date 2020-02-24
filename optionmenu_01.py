# 导入dkinter库 OptionMenu
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(300, 300)

# 创建变量
result = tkinter.StringVar()
result.set('请选择：')

# 加入optionmenu组件，选择结果传至result中
optionmenu = tkinter.OptionMenu(root, result, '选择一', '选择二', '选择三')

# 摆放组件
optionmenu.pack()


# 将主窗口对象加入消息循环中
root.mainloop()
