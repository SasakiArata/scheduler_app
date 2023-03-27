import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('テキストボックス')
# テキストボックス
txt = tkinter.Entry(width=20)
txt.place(x=90, y=70)
# ラベル
lbl = tkinter.Label(text='数値')
lbl.place(x=30, y=70)
# ボタン作成
btn = tkinter.Button(root, text='計算')
btn.place(x=230, y=70)
# 表示
root.mainloop()



#　ボタン作成 btn = tkinter.Button(tki, text=' 計算', command=btn_ckick)
# btn.place(x=140, y=170)


