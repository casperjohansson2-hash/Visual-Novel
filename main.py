from PIL import Image, ImageTk
import tkinter as tk

scen = 1
valde_1 = False
valde_2 = False

bra_väg = False
okej_väg = False
dålig_väg = False
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
def nästa():
    nästa_scen()
def val_1():
    global valde_1, valde_2
    valde_1 = False
    valde_2 = False
    change_text()
    valde_1 = True
    dölj_val()
    nästa_scen()

def val_2():
    global valde_1, valde_2
    valde_1 = False
    valde_2 = False
    change_text()
    valde_2 = True
    dölj_val()
    nästa_scen()

nästa_knapp = tk.Button(root, text="Nästa", font=("Arial", 12), command=nästa)
knapp_1 = tk.Button(root, text="", font=("Arial", 12), command=val_1)
knapp_2 = tk.Button(root, text="", font=("Arial", 12), command=val_2)

def visa_val():
    knapp_1.place(x=600, y=400) 
    knapp_2.place(x=600, y=450)

def dölj_val():
    knapp_1.place(x=600, y=11100) 
    knapp_2.place(x=600, y=41150)



dölj_val()
nästa_knapp.place(x=1300, y=680)
def nästa_scen():
    global bg_img, scen, knapp_1, knapp_2
    dölj_val()
    if scen == 1:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Stängd grind.jpg"))
    elif scen == 2:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Spök kvinna.jpg"))
        nästa_knapp.place(x=1300, y=1680)
        knapp_1 = tk.Button(root, text="Vem är du?", font=("Arial", 12), command=val_1)
        knapp_2 = tk.Button(root, text="Gå och dö.", font=("Arial", 12), command=val_2)
        visa_val()
    elif scen == 3 and valde_1:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Spök kvinna.jpg"))
        knapp_1 = tk.Button(root, text="Visst!", font=("Arial", 12), command=val_1)
        knapp_2 = tk.Button(root, text="Nej, jag vill hem.", font=("Arial", 12), command=val_2)
        visa_val()
    elif scen == 3 and valde_2:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Spök kvinna.jpg"))
    elif scen == 4:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Spök kvinna.jpg"))
        nästa_knapp.place(x=1300, y=680)
    elif scen == 5:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Stig.jpg"))
        knapp_1 = tk.Button(root, text="Gå höger", font=("Arial", 12), command=val_1)
        knapp_2 = tk.Button(root, text="Gå vänster", font=("Arial", 12), command=val_2)
        visa_val()
    
    
    canvas.itemconfig(bg_id, image=bg_img)
    
    scen += 1
    change_text()
    

def change_text():
    global bra_väg, okej_väg, dålig_väg
    if scen == 2:
        canvas.itemconfig(dialog_text, text="(Grind slängs igen) O jävlar! Vad fan slog grinden igen för?! \n" 
        "-Det var jag. (Du vänder dig om..)")
    elif scen == 3:
        canvas.itemconfig(dialog_text, text="Jag behöver din hjälp. En ond ande här har väckt och hållt oss andra andar från att gå in i vår sömn. \n" 
        "Vi behöver din hjälp att befria oss från hans makt!")
    elif scen == 4 and valde_1:
        canvas.itemconfig(dialog_text, text="-Jag kommer inte ihåg... Jag har varit här så länge jag kommer ihåg, men vi behöver din hjälp!\n Kan du hjälpa oss?")
    elif scen == 4 and valde_2:
        canvas.itemconfig(dialog_text, text="-Men jag är redan död...   Du: Men gå och dö igen eller något!   -Jag kommer aldrig öppna grinden igen. Hejdå!")
    elif scen == 5 and valde_1:
        canvas.itemconfig(dialog_text, text="-Tack! Jag tror att jag såg honom borta i den östra delen av kyrkogården. Lycka till!")
        bra_väg = True
    elif scen == 5 and valde_2:
        canvas.itemconfig(dialog_text, text="-Okej, jag förstår... Tyvärr så kan jag inte släppa ut dig, jag använde all min kraft på att stänga och låsa grinden. \nGå och fråga någon av mina vänner här i kyrkogården att öppna grinden åt dig. Hej då!")
        okej_väg = True
    elif scen == 6 and bra_väg:
        canvas.itemconfig(dialog_text, text="Vilket håll är öst? Jag får gissa antar jag")
    elif scen == 6 and okej_väg:
        canvas.itemconfig(dialog_text, text="Undrar vart de andra andarna är då. Jag får ta och välja en väg.")






root.mainloop()