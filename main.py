import tkinter
import libs.component.button.part as btn
import libs.component.Label.part as label
import libs.const.font as font
import libs.const.num as num

display = tkinter.Tk()

#画面サイズ
display.geometry(font.DISPLAY_SIZE)
#画面タイトル
display.title(font.DISPLAY_TITLE)

#登録ボタン
btn.store(display)
#表示ボタン
btn.shwo(display)
#削除ボタン
btn.destroy(display)
#更新ボタン
btn.update(display)

#ラベル表示
label.create(display)

display.mainloop()
