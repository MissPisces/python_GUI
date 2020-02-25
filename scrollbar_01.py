# 导入tkinter库 scrollbar
import tkinter

# 创建主窗口对象
root = tkinter.Tk()

# 设置窗口大小
root.geometry('500x500')

# 加入组件
scrollbar = tkinter.Scrollbar(root)

# 摆放组件
scrollbar.pack(fill='y', side='right')

# 将主窗口对象加入消息循环中
root.mainloop()
