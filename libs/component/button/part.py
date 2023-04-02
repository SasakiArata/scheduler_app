import tkinter
import libs.component.calendar.part as cal
import libs.const.let as let
import libs.const.num as num
import random

'''
登録ボタンに関する作成・表示・処理
'''
#登録ボタン押下時の処理
def store_btn_click(frame):
    x = random.randrange(200)
    y = random.randrange(400)
    label = tkinter.Label(frame, text='登録ラベル', bg='red')
    label.place(x=x, y=y)

#作成・表示
def store(frame):
    #store_button = tkinter.Button(display, text = font.STORE)
    store_button = tkinter.Button(frame, text = let.STORE, command=lambda:store_btn_click(frame))
    store_button.grid(column=0,row=0)

'''
表示ボタンに関する作成・表示・処理
'''
#表示ボタン押下時の処理
def shwo_btn_click(frame):
    x = random.randrange(200)
    y = random.randrange(400)
    label = tkinter.Label(frame, text='表示ラベル', bg='green')
    label.place(x=x, y=y) 
#表示ボタン作成・表示
def shwo(frame):
    show_button = tkinter.Button(frame, text = let.SHWO, command=lambda:shwo_btn_click(frame))
    show_button.grid(column=1,row=0)

'''
削除ボタンに関する作成・表示・処理
'''
#削除ボタン押下時の処理
def destroy_btn_click(frame):
    x = random.randrange(200)
    y = random.randrange(400)
    label = tkinter.Label(frame, text='削除ラベル', bg='purple')
    label.place(x=x, y=y)
#削除ボタン作成
def destroy(frame):
    destroy_button = tkinter.Button(frame, text = let.DESTROY, command=lambda:destroy_btn_click(frame))
    destroy_button.grid(column=2,row=0)

'''
更新ボタンに関する作成・表示・処理
'''
#更新ボタン押下時の処理
def update_btn_click(frame):
    x = random.randrange(200)
    y = random.randrange(400)
    label = tkinter.Label(frame, text='更新ラベル', bg='Yellow')
    label.place(x=x, y=y)
#更新ボタン作成
def update(frame):
    update_button = tkinter.Button(frame, text = let.UPDATE, command=lambda:update_btn_click(frame))
    update_button.grid(column=3,row=0)

'''
カレンダー月を進める
'''
def month_prev(calendar_frame, date_frame):
    month_button = tkinter.Button(date_frame, text="＜", font=(None,12), command=lambda:cal.func(-1, calendar_frame, date_frame))
    month_button.grid(column=0,row=0)

def month_next(calendar_frame, date_frame):
    month_button = tkinter.Button(date_frame, text="＞", font=(None,12), command=lambda:cal.func(1, calendar_frame, date_frame))
    month_button.grid(column=2,row=0)