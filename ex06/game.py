import tkinter
import random

root = tkinter.Tk()
root.title("ブロックゲーム")

fnt = ("Times New Roman", 25)

key = ""
keyoff = False
index = 0
tmr = 0 #ゲームが自動で開始する時間
stage = 0 #難易度の値
score = 0 #スコア
bar_x = 0 #パドルの横移動の値
bar_y = 540 #パドルの縦移動の値
ball_x = 0 #ボールの横移動の値
ball_y = 0 #ボールの縦移動の値
ball_xp = 0 #ボールの横反射の値
ball_yp = 0 #ぼーりの縦反射の値
clr = True

block = [] #ブロックの個数
for i in range(5):
    block.append([1]*10)
for i in range(10):
    block.append([0]*10)

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global keyoff
    keyoff = True

def draw_block(): #ブロックのデザイン
    global clr
    clr = True
    cv.delete("back")
    for y in range(15):
        for x in range(10):
            gx = x*80
            gy = y*30

            if block[y][x] == 1:
                cv.create_rectangle(gx+1, gy+4, gx+79, gy+32, fill=block_color(x,y), width=0, tag="back")
                clr = False

    cv.create_text(200, 20, text="STAGE "+str(stage), fill="white", font=fnt, tag="back")
    cv.create_text(600, 20, text="SCORE "+str(score), fill="white", font=fnt, tag="back")

def block_color(x, y):#ブロックの色
    col = "orange"
    return col

def draw_pdl(): #パドルのデザイン
    cv.delete("pdl")
    cv.create_rectangle(bar_x-108, bar_y-12, bar_x+100, bar_y+12, fill="silver", width=0, tag="pdl")

def move_pdl():#バドルの動き
    global bar_x
    if key == "Left" and bar_x > 85:
        bar_x = bar_x - 40
    if key == "Right" and bar_x < 700:
        bar_x = bar_x + 30

def draw_ball():#ボールのデザイン
    cv.delete("ball")
    cv.create_oval(ball_x-20, ball_y-20, ball_x+20, ball_y+20, fill="white", outline="red", width=2, tag="ball")

def move_ball():#ボールの動き
    global index, tmr, score, ball_x, ball_y, ball_xp, ball_yp
    ball_x = ball_x + ball_xp
    if ball_x < 20:
        ball_x = 20
        ball_xp = -ball_xp
    if ball_x > 780:
        ball_x = 780
        ball_xp = -ball_xp


    ball_y = ball_y + ball_yp
    if ball_y >= 600:
        index = 1
        tmr = 4
        return
    if ball_y < 20:
        ball_y = 20
        ball_yp = -ball_yp
    x = int(ball_x/80)
    y = int(ball_y/40)
    if block[y][x] == 1:
        block[y][x] =  0
        ball_yp == ball_yp
        score = score + 10


def main():
    global key, keyoff
    global index, tmr, stage, score
    global bar_x, ball_x, ball_y, ball_xp, ball_yp
    if index == 0:
        tmr = tmr + 1
        if tmr == 1:
            stage = 1
            score = 0
        if tmr == 2:
            ball_x = 160
            ball_y = 240
            ball_xp = 10
            ball_yp = 10
            bar_x = 400
            draw_block()
            draw_ball()
            draw_pdl()
        if tmr == 1:
            index = 1
    elif index == 1:
        move_ball()
        move_pdl()
        draw_block()
        draw_ball()
        draw_pdl()
        
    root.after(30, main)


root.resizable(False, False)
root.bind("<Key>", key_down)
root.bind("<KeyRelease>", key_up)
cv = tkinter.Canvas(root, width=800, height=600, bg="black")
cv.pack()
main()
root.mainloop()
