import tkinter
#import script as process
import libs.const.font as font
import libs.const.num as num

'''
ラベルに関する作成・表示
'''

#def label_click(event):
#    tkinter.label["text"] = "ボタンがクリックされた"

#ラベルの作成・表示
def create(display):
#    label_text = tkinter.StringVar(display)
#    label_text.set("クリックしてください")
    # ラベル設定
#    label = tkinter.Label(display, textvariable=label_text)
    
    # ラベルをpackで配置
#    label.pack()
    
    # bind関数でラベルクリック時の動作を設定
#    label.bind("<ButtonPress>", label_click)
    label = tkinter.Label(display, text='YEEEES', bg='blue', width=10, height=3)
    label.pack()
