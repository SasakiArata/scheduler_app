import tkinter
import libs.component.button.part as btn
import libs.component.Label.part as label
import libs.component.calendar.part as cal
import libs.const.let as let
import libs.const.num as num

#メインウィンドウ
display = tkinter.Tk()

#画面サイズ
display.geometry(let.DISPLAY_SIZE)
#画面タイトル
display.title(let.DISPLAY_TITLE)

#ヘッダフレーム定義
head_frame = tkinter.Frame(display,height=400, width=500, pady=20, padx=10)
#カレンダー日付フレーム定義
date_frame = tkinter.Frame(display,height=60, width=500, pady=0, padx=0)
#カレンダーフレーム定義
calendar_frame = tkinter.Frame(display,height=400, width=500, pady=0, padx=0, bg=let.CALENDAR_BG)
#フッタフレーム定義
foot_frame = tkinter.Frame(display,height=400, width=500, pady=0, padx=0)



#ラベル表示
label.create(head_frame)

#カレンダー表示
cal.func(0, calendar_frame, date_frame)
btn.month_prev(calendar_frame, date_frame)
btn.month_next(calendar_frame, date_frame)



#登録ボタン
btn.store(foot_frame)
#表示ボタン
btn.shwo(foot_frame)
#削除ボタン
btn.destroy(foot_frame)
#更新ボタン
btn.update(foot_frame)



#ヘッダフレーム配置
head_frame.grid(column=0,row=0)
#カレンダー日付フレーム配置
date_frame.grid(column=0,row=1)
#カレンダーフレーム配置
calendar_frame.grid(column=0,row=3)
#フッタフレーム配置
foot_frame.grid(column=0,row=4)

display.mainloop()
