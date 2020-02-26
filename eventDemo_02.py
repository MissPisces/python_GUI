# 事件绑定 键盘事件
import tkinter

root = tkinter.Tk()
root.geometry('500x500')


# 定义变色函数
def changeR(eventobj):
    eventobj.widget['bg'] = 'red'


def changeY(eventobj):
    eventobj.widget['bg'] = 'yellow'


# 键盘事件绑定:按下r键 按下y键 ，注意区分大小写
root.bind('<Control-KeyPress-r>', changeR)
root.bind('<Control-KeyPress-R>', changeR)
root.bind('<Control-KeyPress-y>', changeY)

root.mainloop()
