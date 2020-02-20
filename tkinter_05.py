# 测试中文支持

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()  # must be here

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

f1 = tkFont.Font(family='microsoft yahei', size=30, weight='bold')
f2 = tkFont.Font(family='microsoft yahei', size=30, slant='italic')
f3 = tkFont.Font(family='lisu', size=30, underline=1, overstrike=1)
f4 = tkFont.Font(family='TkMenuFont', size=30)
tk.Label(root, text='汉字字体', font=f1).pack()
tk.Label(root, text='汉字字体', font=f2).pack()
tk.Label(root, text='汉字字体', font=f3).pack()
tk.Label(root, text='默认汉字字体', font=f4).pack()

print(tkFont.BOLD)
root.mainloop()
