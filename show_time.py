import tkinter as tk
import time
import pyperclip
import os


os.environ['LC_ALL'] = 'UTF-8'

def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    label.config(text="北京时间：" + current_time,fg="red")
    label.after(1000, update_time)

def copy_time():
    current_time = time.strftime("%Y-%m-%d", time.localtime())
    time_split=current_time.split("-")
    res="{}年{}月{}日".format(time_split[0],time_split[1],time_split[2])
    pyperclip.copy(res)


def on_checkbox_changed():
    if var.get():
        # 将窗口置顶
        root.lift()
        # 设置窗口属性
        root.attributes('-topmost', True)
    else:
        # 取消窗口置顶
        root.attributes('-topmost', False)





root = tk.Tk()




# 创建一个 BooleanVar 对象
var = tk.BooleanVar()
# 创建一个选择框
checkbutton = tk.Checkbutton(root, text="保持置顶", variable=var)
# 将选择框放置在窗口中
checkbutton.pack()
# 监听选择框状态变化
var.trace_add('write', lambda *args: on_checkbox_changed())




root.title("")
label = tk.Label(root, font=("Verdana", 16))
label.pack()

copy_button = tk.Button(root, text="              复制时间               ", command=copy_time)
copy_button.pack()

update_time()

root.mainloop()
