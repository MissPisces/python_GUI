# 组件布局pack
# 导入dkinter库
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.minsize(500, 500)

# 加入按钮组件
btu1 = tkinter.Button(root, text='button1')

# 摆放组件
btu1.pack(side='bottom')

# 将主窗口对象加入消息循环中
root.mainloop()
