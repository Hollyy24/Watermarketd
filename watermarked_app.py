from tkinter import Tk, filedialog, Label, Button, Entry
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageColor
import os


def add():
    global FILE_NAME
    file = filedialog.askopenfilename()
    FILE_NAME = os.path.abspath(file)
    prev = Image.open(FILE_NAME)
    prev.thumbnail((300, 300))
    prev_img = ImageTk.PhotoImage(prev)
    prev_img_label = Label(window, image=prev_img)
    prev_img_label.image = prev_img
    prev_img_label.grid(row=4, column=0, columnspan=2)


def watermarked():
    global FILE_NAME, TEXT
    TEXT = type_text.get()
    base = Image.open(FILE_NAME).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype("Bradley Hand Bold.ttf", FONTSIZE)
    draw = ImageDraw.Draw(txt)
    draw.text((POSITION_X, POSITION_Y), TEXT, font=fnt, fill=COLOR)

    output = Image.alpha_composite(base, txt)
    output2 = output.copy()
    output2.thumbnail((200, 200))
    output_img = ImageTk.PhotoImage(output2)
    watered_img_label.config(image=output_img)
    watered_img_label.image = output_img
    return output


def save_picture():
    output = watermarked()
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        output.save(save_path, quality=95)
        save_text = Label(window, text=f"照片已儲存在 {save_path}!")
        save_text.grid(row=10, column=0, columnspan=2)


def move_up():
    global POSITION_Y
    POSITION_Y -= 10
    watermarked()


def move_down():
    global POSITION_Y
    POSITION_Y += 10
    watermarked()


def move_left():
    global POSITION_X
    POSITION_X -= 10
    watermarked()


def move_right():
    global POSITION_X
    POSITION_X += 10
    watermarked()


def plus_text():
    global FONTSIZE
    FONTSIZE += 5
    watermarked()


def minus_text():
    global FONTSIZE
    FONTSIZE -= 5
    watermarked()


def change_color_white():
    global COLOR
    rgb = ImageColor.getcolor('white', "RGB")
    r, g, b, = rgb
    COLOR = (r, g, b, 255)
    watermarked()

def change_color_black():
    global COLOR
    rgb = ImageColor.getcolor('black', "RGB")
    r, g, b, = rgb
    COLOR = (r, g, b, 255)
    watermarked()


def change_color_red():
    global COLOR
    rgb = ImageColor.getcolor('red', "RGB")
    r, g, b, = rgb
    COLOR = (r, g, b, 255)
    watermarked()


def change_color_green():
    global COLOR
    rgb = ImageColor.getcolor('green', "RGB")
    r, g, b, = rgb
    COLOR = (r, g, b, 255)
    watermarked()




if __name__ == '__main__':
    FILE_NAME = "test.png"
    TEXT = "HELLO"
    POSITION_X = 50
    POSITION_Y = 50
    FONTSIZE = 50
    COLOR = (255, 255, 255, 255)

    window = Tk()
    window.title("Picture Add Watermark")
    window.minsize(800, 600)


    # input
    add_fill = Button(text="選擇檔案", command=add)
    add_fill.grid(row=0, column=2, pady=5)


    prevtiyle = Label(window, text="原始圖檔")
    prevtiyle.grid(row=3, column=1)
    prev = Image.open(FILE_NAME)
    prev.thumbnail((200, 200))
    prev_img = ImageTk.PhotoImage(prev)
    prev_img_label = Label(window, image=prev_img)
    prev_img_label.image = prev_img
    prev_img_label.grid(row=4, column=1)

    ## 浮水印圖片

    watered = Label(window, text='浮水印結果')
    watered.grid(row=3, column=3)

    watered_img_label = Label(window, image=prev_img)
    watered_img_label.grid(row=4, column=3)

    ##填上想要輸入的文字

    type_title = Label(text="填上想要的浮水印文字")
    type_text = Entry(text="填上想要的浮水印文字", width=30, foreground="WHITE")
    type_title.grid(row=1, column=2, pady=10)
    type_text.grid(row=2, column=2, pady=10)

    ##浮水印位置移動

    position_title = Label(text="移動浮水印位置")
    position_up = Button(text="往上", command=move_up)
    position_down = Button(text="往下", command=move_down)
    position_left = Button(text="往左", command=move_left)
    position_right = Button(text="往右", command=move_right)
    position_title.grid(row=6, column=0)
    position_up.grid(row=6, column=1)
    position_down.grid(row=6, column=2)
    position_left.grid(row=6, column=3)
    position_right.grid(row=6, column=4)

    ##浮水印放大縮小

    font_size = Label(text="改變浮水印大小")
    font_size_plus = Button(text="增大", command=plus_text)
    font_size_minus = Button(text="縮小", command=minus_text)
    font_size.grid(row=7, column=0)
    font_size_plus.grid(row=7, column=1)
    font_size_minus.grid(row=7, column=2)

    ##改變浮水印顏色

    font_color = Label(text="選擇浮水印顏色")
    white_color_button = Button(text="白色", command=change_color_white)
    black_color_button = Button(text="黑色", command=change_color_black)
    red_color_button = Button(text="紅色", command=change_color_red)
    green_color_button = Button(text="綠色", command=change_color_green)
    font_color.grid(row=8,column=0)
    white_color_button.grid(row=8, column=1)
    black_color_button.grid(row=8, column=2)
    red_color_button.grid(row=8, column=3)
    green_color_button.grid(row=8, column=4)

    # 貼上檔案按鈕 浮水印按鈕

    motion_text = Label(text="動作")
    output = Button(text="貼上浮水印", command=watermarked)
    save_button = Button(text="儲存檔案", command=save_picture)
    motion_text.grid(row=9, column=0)
    output.grid(row=9, column=1)
    save_button.grid(row=9, column=2)

    window.mainloop()
