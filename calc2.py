from tkinter import *
from functools import partial

win = Tk()
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/", ]
row_num = 0
col_num = 0
res = Label(win, text="", font=('cascadia code', 20))
res.grid(row=row_num, column=col_num)
def solve_for(input):
    if input == "=":
        ans = str(eval(res.cget("text")))
        res.config(text=ans)
    elif input == "C":
        res.config(text=" ")
    else:
        res.config(text=res.cget("text") + input)
for i in range(len(btn_txt)):
    Button(win, width=10, height=5, text=btn_txt[i], command=partial(solve_for, btn_txt[i])).grid(row=row_num+2, column=col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.title("Medyo Calculator")
win.geometry("320x470+800+200")
win.mainloop()