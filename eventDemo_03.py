# 事件绑定 .bind_class
import tkinter

root = tkinter.Tk()
root.geometry('500x500')

# 创建组件
btn1 = tkinter.Button(root, text='按钮一')
btn1.place(x=20, y=20, width=80, height=40)

btn2 = tkinter.Button(root, text='按钮二')
btn2.place(x=20, y=70, width=80, height=40)

btn3 = tkinter.Button(root, text='按钮三')
btn3.place(x=20, y=120, width=80, height=40)

btn4 = tkinter.Button(root, text='按钮四')
btn4.place(x=20, y=170, width=80, height=40)

btn5 = tkinter.Button(root, text='按钮五')
btn5.place(x=20, y=220, width=80, height=40)

btn6 = tkinter.Button(root, text='按钮六')
btn6.place(x=20, y=270, width=80, height=40)


# 定义鼠标进入函数
def changeBg(obj):
    obj.widget['bg'] = 'red'


# 鼠标进入事件绑定
btn1.bind_class('Button', '<Enter>', changeBg)

# 定义鼠标离开函数
def changeBg2(obj):
    obj.widget['bg'] = 'yellow'


# 鼠标离开事件绑定
btn1.bind_class('Button', '<Leave>', changeBg2)
root.mainloop()
