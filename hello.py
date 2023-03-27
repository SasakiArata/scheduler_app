import tkinter
from turtle import up

display = tkinter.Tk()

#画面サイズ
display.geometry("400x200")
#画面タイトル
display.title("スケジューラー")

#登録ボタン作成
store_button = tkinter.Button(display, text = "登録")
#表示ボタン作成
show_button = tkinter.Button(display, text = "表示")
#削除ボタン作成
destroy_button = tkinter.Button(display, text = "削除")
#更新ボタン作成
update_button = tkinter.Button(display, text = "更新")

#各種ボタン表示
store_button.pack()
show_button.pack()
destroy_button.pack()
update_button.pack()

display.mainloop()
