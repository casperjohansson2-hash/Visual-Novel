from PIL import Image, ImageTk
import tkinter as tk

scen = 1
valde_1 = False
valde_2 = False
valde_3 = False

root = tk. Tk()
root.title("Visual Novel")
root.geometry("1408x768")

canvas = tk. Canvas(root, width=1408, height=768)
canvas.pack()


bg_img = ImageTk. PhotoImage(Image.open("assets/backgrounds/Öppen grind.jpg"))
bg_id = canvas.create_image(0, 0, anchor="nw", image=bg_img)

canvas.create_rectangle(
0, 640, 1408, 768,
fill="black",
outline= "#FFFFFF",
width=0
)

dialog_text = canvas.create_text(
20 , 660,
text="(Du har precis avslutat ditt arbetspass på den lokala kyrkogården och ska gå hem) Vad snabbt det blir mörkt nu för tiden!",
fill="white",
font=("Arial", 16),
anchor="nw"
)

def nasta_scen(event):
    global bg_img, scen
    # Ladda in den nya bilden
    bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Stängd grind.jpg"))
    
    
    canvas.itemconfig(bg_id, image=bg_img)
    
    scen += 1
    change_text()
    

def change_text():
    if scen == 2:
        canvas.itemconfig(dialog_text, text="(Grind slängs igen) O jävlar! Vad fan slog grinden igen för?! " \
        "-Det var jag. (Du vänder dig om..)")
    elif scen == 3:
        if valde_1:
            canvas.itemconfig(dialog_text, text="")
root.bind("<Button-1>", nasta_scen)

def val_1():
    global valde_1, valde_2, valde_3
    valde_1 = True
    valde_2 = False
    valde_3 = False
    change_text()
    valde_1 = False
    valde_2 = False
    valde_3 = False
    knapp_1.place_forget()
    knapp_2.place_forget()

def val_2():
    global valde_1, valde_2, valde_3
    valde_1 = False
    valde_2 = True
    valde_3 = False
    change_text()
    valde_1 = False
    valde_2 = False
    valde_3 = False
    knapp_1.place_forget()
    knapp_2.place_forget()

knapp_1 = tk.Button(root, text="Dö", font=("Arial", 12), command=val_1)
knapp_1.place(x=600, y=400) 

knapp_2 = tk.Button(root, text="Ayoooo  ", font=("Arial", 12), command=val_2)
knapp_2.place(x=600, y=450)

root.mainloop()