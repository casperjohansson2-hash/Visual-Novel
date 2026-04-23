import random
from PIL import Image, ImageTk
import tkinter as tk

scen = 1
valde_1 = False
valde_2 = False

bra_väg = False
okej_väg = False
dålig_väg = False
tärning = False
gåtor = False
skadad = False 

root = tk.Tk()
root.title("Visual Novel")
root.geometry("1408x768")

canvas = tk.Canvas(root, width=1408, height=768)
canvas.pack()

bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Öppen grind.jpg"))
bg_id = canvas.create_image(0, 0, anchor="nw", image=bg_img)

canvas.create_rectangle(0, 640, 1408, 768, fill="black", outline="#FFFFFF", width=0)
dialog_text = canvas.create_text(
    20, 660,
    text="(Du har precis avslutat ditt arbetspass på den lokala kyrkogården och ska gå hem) Vad snabbt det blir mörkt nu för tiden!",
    fill="white",
    font=("Arial", 16),
    anchor="nw"
)

def klick_nästa():
    global scen, valde_1, valde_2
    scen += 1
    valde_1 = False
    valde_2 = False
    uppdatera_scen()

def klick_val_1():
    global scen, valde_1, valde_2
    scen += 1
    valde_1 = True
    valde_2 = False
    uppdatera_scen()

def klick_val_2():
    global scen, valde_1, valde_2
    scen += 1
    valde_1 = False
    valde_2 = True
    uppdatera_scen()

nästa_knapp = tk.Button(root, text="Nästa", font=("Arial", 12), command=klick_nästa)
knapp_1 = tk.Button(root, font=("Arial", 12), command=klick_val_1)
knapp_2 = tk.Button(root, font=("Arial", 12), command=klick_val_2)

def visa_nästa():
    nästa_knapp.place(x=1300, y=680)
    knapp_1.place_forget()
    knapp_2.place_forget()

def visa_val(text1, text2):
    nästa_knapp.place_forget()
    knapp_1.config(text=text1)
    knapp_2.config(text=text2)
    knapp_1.place(x=1100, y=660) 
    knapp_2.place(x=1100, y=710)

def dölj_alla_knappar():
    nästa_knapp.place_forget()
    knapp_1.place_forget()
    knapp_2.place_forget()

def uppdatera_scen():
    global bg_img, scen, bra_väg, okej_väg, dålig_väg, tärning, gåtor, skadad

    if dålig_väg:
        try:
            bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Dåligt slut.jpg"))
        except:
            pass 
        canvas.itemconfig(bg_id, image=bg_img)
        canvas.itemconfig(dialog_text, text="Du fastnade för evigt på kyrkogården... (Starta om spelet)")
        dölj_alla_knappar()
        return

    if scen == 2:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Stängd grind.jpg"))
        canvas.itemconfig(dialog_text, text="(Grind slängs igen) O jävlar! Vad fan slog grinden igen för?! \n-Det var jag. (Du vänder dig om..)")
        visa_nästa()

    elif scen == 3:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Spök kvinna.jpg"))
        canvas.itemconfig(dialog_text, text="Jag behöver din hjälp. En ond ande här har väckt och hållt oss andra andar från att gå in i vår sömn. \nVi behöver din hjälp att befria oss från hans makt!")
        visa_val("Vem är du?", "Gå och dö.")

    elif scen == 4:
        if valde_1:
            canvas.itemconfig(dialog_text, text="-Jag kommer inte ihåg... Jag har varit här så länge jag kommer ihåg, men vi behöver din hjälp!\n Kan du hjälpa oss?")
            visa_val("Visst!", "Nej, jag vill hem.")
        elif valde_2:
            canvas.itemconfig(dialog_text, text="-Men jag är redan död... Du: Men gå och dö igen eller något! \n-Jag kommer aldrig öppna grinden igen. Hejdå!")
            dålig_väg = True
            uppdatera_scen()

    elif scen == 5:
        if valde_1:
            bra_väg = True
            canvas.itemconfig(dialog_text, text="-Tack! Jag tror att jag såg honom borta i den östra delen av kyrkogården. Lycka till!")
        elif valde_2:
            okej_väg = True
            canvas.itemconfig(dialog_text, text="-Okej, jag förstår... Tyvärr så kan jag inte släppa ut dig, jag använde all min kraft på att stänga grinden. \nGå och fråga någon av mina vänner här i kyrkogården. Hej då!")
        visa_nästa()

    elif scen == 6:
        bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Stig.jpg"))
        if bra_väg:
            canvas.itemconfig(dialog_text, text="Vilket håll är öst? Jag får gissa antar jag.")
        elif okej_väg:
            canvas.itemconfig(dialog_text, text="Undrar vart de andra andarna är då. Jag får ta och välja en väg.")
        visa_val("Gå höger", "Gå vänster")

    elif scen == 7:
        if valde_1:
            tärning = True
            bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Liemannen.jpg"))
            canvas.itemconfig(dialog_text, text="Okänd: Vem går där?")
            visa_val("Ingen", "Bara en förbipasserande")
        elif valde_2:
            gåtor = True
            bg_img = ImageTk.PhotoImage(Image.open("assets/backgrounds/Ond ande.jpg"))
            canvas.itemconfig(dialog_text, text="Ond ande: Stanna där du är! Ta ett steg till, så blir det ditt sista!")
            visa_val("Prata med den", "Spring för livet")

    elif scen == 8:
        if tärning:
            if valde_1:
                canvas.itemconfig(dialog_text, text="Liemannen: Du är visst någon! Jag är Liemannen, och du ska spela tärningar för ditt liv, Ingen!")
            elif valde_2:
                canvas.itemconfig(dialog_text, text="Liemannen: Antingen är du det, eller inte. Jag är Liemannen, och du ska spela tärningar för ditt liv.")
            visa_val("Spela", "Vägra")
            
        elif gåtor:
            if valde_1:
                canvas.itemconfig(dialog_text, text="Ond ande: Du är modig som stannar. Jag vill spela ett spel gåtor med dig. Svara rätt, så får du överleva.")
                if bra_väg:
                    visa_val("Jag är skickad av ett av spökena", "Jag vill inte")
                elif okej_väg:
                    visa_val("Ok", "Jag vill inte")
            elif valde_2:
                canvas.itemconfig(dialog_text, text="Du vänder dig om och rusar, men skuggorna hinner ikapp dig direkt...")
                dålig_väg = True
                uppdatera_scen()
                
    elif scen == 9:
        if tärning:
            if valde_1: 
                slag = random.randint(1, 6) 
                if slag >= 4:
                    canvas.itemconfig(dialog_text, text=f"(Du skakar tärningen... Den landar på {slag}!)\nLiemannen: Ett avtal är ett avtal. Du har vunnit ditt liv. Har du något sista önskemål?")
                    visa_val("Ta den onda andens själ istället!", "Släpp bara ut mig.")
                else:
                    canvas.itemconfig(dialog_text, text=f"(Den landar på {slag}.)\nLiemannen: Din själ tillhör mig nu!")
                    dålig_väg = True 
                    visa_nästa() 
            elif valde_2: 
                canvas.itemconfig(dialog_text, text="Liemannen: Ingen vägrar Döden!")
                dålig_väg = True
                uppdatera_scen()
        elif gåtor:   
            if valde_2:
                canvas.itemconfig(dialog_text, text="Ond ande: Det var inget val! Nu dör du!")
                dålig_väg = True
                uppdatera_scen()
            else:
                canvas.itemconfig(dialog_text, text="Ond ande: Okej, svarar du rätt på mina gåtor släpper jag ut dig.")
                visa_nästa()

    elif scen == 10:
        if tärning:
            if valde_1:
                canvas.itemconfig(dialog_text, text="Liemannen: En intressant begäran... Det ska bli gjort. Den onde anden ska skördas.\nDu är fri att gå.")
            else:
                canvas.itemconfig(dialog_text, text="Liemannen: Gå då. Och kom inte tillbaka förrän det är din tid på riktigt.")
            visa_nästa()
        elif gåtor:
            canvas.itemconfig(dialog_text, text="Gåta 1: Vad är det som har rötter, aldrig dör, och aldrig växer?")
            visa_val("Ett berg", "Ett träd")

    elif scen == 11:
        if tärning:
            canvas.itemconfig(dialog_text, text="Du går mot grinden... Den är nu öppen. Du sprang hem så fort du bara kunde.\nBra slut! (Vinst via vadslagning)")
            dölj_alla_knappar()
        elif gåtor:
            if valde_1:
                 canvas.itemconfig(dialog_text, text="Rätt! Gåta 2: Vad skapar och förstör, utan fysisk form, ger och tar liv?")
                 visa_val("Tiden", "Elden")
            else:
                 if okej_väg:
                     skadad = True
                     canvas.itemconfig(dialog_text, text="(Fel! Den onde anden attackerar dig och du skadas rejält!)\nOnd ande: Du får EN chans till. Vad skapar och förstör, utan fysisk form?")
                     visa_val("Tiden", "Elden")
                 else:
                     dålig_väg = True
                     uppdatera_scen()

    elif scen == 12: 
        if gåtor:
            if valde_1:
                canvas.itemconfig(dialog_text, text="Imponerande. Sista gåtan: Vad är svaret på livet, universum och allting?")
                visa_val("42", "Kärlek")
            else:
                if okej_väg:
                    skadad = True
                    canvas.itemconfig(dialog_text, text="(Fel! Du träffas av mörk magi och faller till marken...)\nOnd ande: Sista chansen nu! Vad är svaret på livet och allt?")
                    visa_val("42", "Kärlek")
                else:
                    dålig_väg = True
                    uppdatera_scen()

    elif scen == 13:
        if gåtor:
            if valde_1:
                if skadad:
                    canvas.itemconfig(dialog_text, text="Ond ande: Du klarade dig, men inte utan skador... Gå nu innan jag ångrar mig.")
                else:
                    canvas.itemconfig(dialog_text, text="Du är visare än du ser ut. Grinden är öppen. Gå nu.")
                visa_nästa()
            else:
                dålig_väg = True
                uppdatera_scen()
    
    elif scen == 14:
         canvas.itemconfig(dialog_text, text="Du haltar ut genom grinden och ser solen börja gå upp. Du lever.\nOkej slut (Vinst via gåtor)")
         dölj_alla_knappar()

    canvas.itemconfig(bg_id, image=bg_img)

visa_nästa()
root.mainloop()