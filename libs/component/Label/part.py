import tkinter
import datetime
#import script as process
import libs.const.let as let
import libs.const.num as num

'''
ラベルに関する作成・表示
'''

#def label_click(event):
#    tkinter.label["text"] = "ボタンがクリックされた"

#ラベルの作成・表示
def create(head_frame):
    #曜日定義
    week_dict = {
        'Sunday': '日',
        'Monday': '月',
        'Tuesday': '火',
        'Wednesday': '水',
        'Thursday': '木',
        'Friday': '金',
        'Saturday': '土'
        }
    #曜日取得
    key = datetime.date.today().strftime('%A')
    #日付取得
    date_label = datetime.date.today().strftime('%Y年%m月%d日') + '（' + week_dict[key] + '）'
    label = tkinter.Label(head_frame, text=str(date_label), fg='#FF4500', font=("MSゴシック", "20", "bold"))
    label.grid(column=0,row=0)
