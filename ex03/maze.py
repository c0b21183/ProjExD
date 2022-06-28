import tkinter
import tkinter.messagebox

key = ""
def key_down(e):
    global key
    key = e.keysym
def key_up(e):
    global key 
    key = ""

cx = 1
cy = 1
yuka = 0
def main_proc():
    global cx, cy, yuka
    if key == "Up" and maze[cy-1][cx] == 0:
        cy +=  1
    if key == "Down" and maze[cy+1][cx] == 0:
        cy = cy + 1
    if key == "Left" and maze[cy][cx-1] == 0:
        cx = cx - 1
    if key == "Right" and maze[cy][cx+1] == 0:
        cx = cx + 1
    if maze[cy][cx] == 0:
       maze[cy][cx] == 2
       yuka = yuka + 1
       canvas.create_rectangle(cx*80, cy*80, cx*80+79, cy*80+79, fill="blue", width=0)
       canvas.delete("MYCHR")
       canvas.create_image(cx*80+40, cy*80+40, image=tori)
       if yuka == 1000:
        canvas.update()
        tkinter.messagebox.showinfo("おめでとう！")
       else:
        root.after(100, main_proc)
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("迷えるこうかとん")
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas = tkinter.Canvas(width = 1500, height = 900, bg = "White")
    canvas.pack()

    maze = [
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
       [1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1],
       [1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1],
       [1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1],
       [1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
       [1,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1],
       [1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
       ] 
for y in range(9):
    for x in range(17):
        if maze[y][x] == 1:
             canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79, fill="gray", width = 0)
tori = tkinter.PhotoImage(file="fig/1.png")
canvas.create_image(cx*80+40, cy*80+40, image= tori)
main_proc()
root.mainloop()

