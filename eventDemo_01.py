# 事件绑定 鼠标事件
import tkinter

root = tkinter.Tk()
root.geometry('500x500')

# 创建单行文本框
entry = tkinter.Entry(root)

entry.pack()


# 定义变色函数
def changered(eventobj):
    eventobj.widget['bg'] = 'red'


def changeyellow(eventobj):
    eventobj.widget['bg'] = 'yellow'


# 鼠标事件绑定
entry.bind('<Enter>', changered)
entry.bind('<Leave>', changeyellow)

root.mainloop()
