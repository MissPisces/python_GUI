# 制作软件界面(过程化编程)

import tkinter
import tkinter.filedialog
import tkinter.messagebox
# 导入压缩模块库
import zipfile
# 导入os模块库
import os

# 创建主窗口
root = tkinter.Tk()
root.geometry('300x500')
root.title('压缩软件1.0')

# 设置文件路径保存的变量（全局变量）
filelists = []


# 创建添加文件函数
def addfile():
    # 全局化操作
    global filelists
    paths = tkinter.filedialog.askopenfilenames(title='选择需要压缩的文件')
    # 遍历添加文件路径
    for path in paths:
        filelists.append(path)
    # 显示选择的文件路径,将filelists中内容转换成字符串
    lable_info['text'] = '\n'.join(filelists)


# 创建压缩函数
def compress():
    # 全局化变量
    global filelists
    # 设置压缩文件保存路径及名称
    zippath = tkinter.filedialog.asksaveasfilename(filetypes=(('zip文件', '*.zip'),))
    # 创建并打开压缩文件,得到文件指针
    zp = zipfile.ZipFile(zippath, 'a')
    # 压缩
    for filename in filelists:
        zp.write(filename, os.path.basename(filename))
    # 关闭压缩文件
    zp.close()
    # 信息提示
    tkinter.messagebox.showinfo(title='操作结果', message='压缩成功！' + zippath)


# 创建解压函数
def uncompress():
    # 获取压缩文件的位置
    zippath = tkinter.filedialog.askopenfilename()
    # 打开压缩文件
    zp = zipfile.ZipFile(zippath, 'r')
    # 解压
    dirpath = tkinter.filedialog.askdirectory()
    zp.extractall(dirpath)
    # 关闭压缩文件
    zp.close()
    # 信息提示
    tkinter.messagebox.showinfo(title='解压提示', message='解压成功'+dirpath)


# 添加按钮组件
btn_addfile = tkinter.Button(root, text='添加文件', command=addfile)
btn_addfile.place(x=10, y=20, width=80, height=30)

btn_compress = tkinter.Button(root, text='压缩文件', command=compress)
btn_compress.place(x=110, y=20, width=80, height=30)

btn_uncompress = tkinter.Button(root, text='解压文件', command=uncompress)
btn_uncompress.place(x=210, y=20, width=80, height=30)

# 创建信息显示区
lable_info = tkinter.Label(root, bg='white', anchor='nw', justify='left')
lable_info.place(x=10, y=70, width=280, height=300)

root.mainloop()
