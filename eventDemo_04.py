# 事件绑定 .bind_all
import tkinter

root = tkinter.Tk()
root.geometry('500x500')

# 创建组件
entry = tkinter.Entry(root)
entry.pack()

button = tkinter.Button(root, text='按钮')
button.pack()

text = tkinter.Text(root, width=20, height=10)
text.pack()


# 定义变色函数
def changeEntry(obj):
    entry['bg'] = 'red'


# 绑定点击鼠标左键事件
button.bind_all('<Button-1>', changeEntry)

root.mainloop()
