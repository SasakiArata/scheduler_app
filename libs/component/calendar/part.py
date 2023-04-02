import datetime
import calendar
import tkinter
import libs.const.let as let
 
WEEK = ["日", "月", "火", "水", "木", "金", "土"]
 
# 現在年月取得
year  = datetime.date.today().year
month = datetime.date.today().month

def func(arg, calendar_frame, head_frame):
 
    # グローバル変数定義
    global year
    global month
 
    # 月を変更
    month += arg
 
    # 月が1未満の場合は前年にする
    if   month < 1:
        month = 12
        year -= 1
 
    # 月が12より大きい場合は翌年にする
    elif month > 12:
        month = 1
        year += 1

    ### ラベルウィジェットを初期化
    for widget in head_frame.winfo_children():
        if isinstance(widget, tkinter.Label):
            widget.destroy()
 
    ### ラベルに年月を設定
    label = tkinter.Label(master=head_frame, text=str(year) + "年" + str(month) + "月",  font=("游ゴシック",20))
 
    ### 年月表示
    label.grid(column=1,row=0)

    # カレンダーオブジェクト作成
    cl = calendar.Calendar(firstweekday=6)
 
    # 該当年月のカレンダーを取得
    cal = cl.monthdayscalendar(year, month)
 
    # ウィジェット初期化
    for widget in calendar_frame.winfo_children():
        widget.destroy()
 
    # 曜日配列を取得
    for i,x in enumerate(WEEK):
 
        # 日曜日は赤、土曜日は青にする
        if   i == 0:
            label_day = tkinter.Label(master=calendar_frame, text=x, font=("游ゴシック",18), width=3, fg="red")
        elif i == 6:
            label_day = tkinter.Label(master=calendar_frame, text=x, font=("游ゴシック",18), width=3, fg="blue")
        else:
            label_day = tkinter.Label(master=calendar_frame, text=x, font=("游ゴシック",18), width=3)
 
        # 曜日を表示
        label_day.grid(row=0, column=i, pady=2)
 
    # 行カウンター
    row_cnt = 1
 
    # カレンダー配列を取得
    for week in cal:
        for i,day in enumerate(week):
 
            # 0だったら空白を設定
            if day == 0:
                day = " "
            else:
                if len(str(day)) == 1:
                    #1桁日付の幅埋め
                    day = " " + str(day) + " "
 
            # 日曜日は赤、土曜日は青にする
            if day != " ":
                if   i == 0:
                    label_day = tkinter.Button(master=calendar_frame, text="{:>2}".format(day), font=("游ゴシック",18), height=1, fg="red", relief=tkinter.FLAT)
                elif i == 6:
                    label_day = tkinter.Button(master=calendar_frame, text="{:>2}".format(day), font=("游ゴシック",18), height=1, fg="blue", relief=tkinter.FLAT)
                else:
                    label_day = tkinter.Button(master=calendar_frame, text="{:>2}".format(day), font=("游ゴシック",18), height=1, relief=tkinter.FLAT)
            else:
                label_day = tkinter.Label(master=calendar_frame, text="{:>2}".format(day), font=("游ゴシック",18), height=1, relief=tkinter.FLAT, bg=let.CALENDAR_BG)

 
            # 日にちを表示
            label_day.grid(row=row_cnt, column=i, padx=2, pady=2)
 
        # カウントアップ
        row_cnt = row_cnt + 1