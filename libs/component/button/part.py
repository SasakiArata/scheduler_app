import tkinter
#import script as process
import libs.const.font as font
import libs.const.num as num

'''
ボタンに関する作成・表示
'''
#登録ボタン作成・表示
def store(display):
    store_button = tkinter.Button(display, text = font.STORE)
    #store_button = tkinter.Button(display, text = font.STORE, command=process.store_btn_click)
    store_button.pack()

#表示ボタン作成・表示
def shwo(display):
    show_button = tkinter.Button(display, text = font.SHWO)
    show_button.pack()

#削除ボタン作成
def destroy(display):
    destroy_button = tkinter.Button(display, text = font.DESTROY)
    destroy_button.pack()

#更新ボタン作成・表示
def update(display):
    update_button = tkinter.Button(display, text = font.UPDATE)
    update_button.pack()