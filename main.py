import tkinter as tk
dic = {1:'+',2:'-',3:'*',4:'/'}

def solve():
    secondn = n2.get()
    sign = var.get()
    if secondn == '0' and dic[sign]=='/':
        ans.config(text=' 0으로 나눌 수 없습니다')
    else:
        answer = eval(n1.get()+dic[sign]+secondn)
    ans.config(text='%.2f'%answer)

root = tk.Tk()
var = tk.IntVar()
var.set(1)
n1 = tk.Entry(root)
n1.pack()
n2 = tk.Entry(root)
n2.pack()
add = tk.Radiobutton(root, text='Button +', variable = var, value=1)
add.pack()
sub = tk.Radiobutton(root, text='Button -', variable = var, value=2)
sub.pack()
mul = tk.Radiobutton(root, text='Button *', variable = var, value=3)
mul.pack()
div = tk.Radiobutton(root, text='Button /', variable = var, value=4)
div.pack()
result = tk.Button(root,text='Result',command = solve)
result.pack()
ans = tk.Label(root,text='결과 표시창')
ans.pack()
root.mainloop()