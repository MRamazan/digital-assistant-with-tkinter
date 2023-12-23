import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from pygame import mixer

from itertools import count, cycle


import time
import psutil
import datetime


# Bilgisayarın açılış zamanını al
boot_time_timestamp = psutil.boot_time()

# Açılış zamanını datetime nesnesine çevir
boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)

start = time.strftime("%H:%M")

int_start = time.strftime("%H%M")

print(start)



for x, y in enumerate(int_start):
    if x == 0:
        ilk = y
    elif x == 1:
        ikinci = y
    elif x == 2:
        üçüncü = y
    elif x == 3:
        dördüncü = y

hour = ilk + ikinci
min = üçüncü + dördüncü
hour2 = int(hour) + 2
hour3 = (str(hour2) + ":" + time.strftime("%M"))
hour4 = int(hour) + 3
hour5 = int(min) + 30
if hour5 >= 60:
    hour6 = hour5 - 60
    hour7 = hour4 + 1
    if hour6 < 10:
     hour8 = (str(hour7) + ":0" + str(hour6))
    else:
     hour8 = (str(hour7) + ":" + str(hour6))
else:
    hour8 = str(hour4) + ":" + str(hour5)

hour9 = int(hour) + 5
hour10 = str(hour9) +  ":" + str(min)

hour11 = int(hour) + 7
hour12 = str(hour11) + ":" + str(min)

# Pencere oluşturun
window = tk.Tk()
window.title("DigitalAssistant")
window.geometry("700x600")
window.config(bg="white")
window.wm_attributes("-topmost", True)
window.wm_overrideredirect(True)
window['bg'] = 'grey'
window.attributes('-transparentcolor', 'grey')






# Buton ekleyin ve bir fonksiyonu bağlayın


def resized(img1, width, height):
    img = Image.open((img1))
    resized_img = img.resize((width, height))
    return ImageTk.PhotoImage(resized_img)







class ImageButton(tk.Button):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """


    def load(self, im, width, height):
        if isinstance(im, str):
          im = Image.open(im)

        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.resize((width, height))))  # görüntünün karesini alır
                im.seek(i)  # istenen kareyi arar. seek = aramak

        except EOFError:
            pass


        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None


    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)



def sleep(süre):
    window.withdraw()
    time.sleep(süre)
    window.deiconify()
    remove_buttons()
    button10 = ImageButton(window,command=window.destroy)
    button10.grid(row=2, column=0)
    button10.load(r"C:\Users\PC\Downloads\nami-gif-5.gif", 400, 300)
    slow_print("Uyku vakti, İYİ GECELER!")

def play():
    mixer.init()
    mixer.music.load(r"C:\Users\PC\Downloads\konnichiwa.mp3")
    mixer.music.play()

def slow_print(text, current_text="", word_delay=300, letter_delay=30):
    new_font = font.Font(family="ComicSans MS", size=15, weight="bold", slant="roman", underline=False)
    label = tk.Label(window, text="", wraplength=500, bg="white")
    label.grid(row=6, column=0, ipadx=7, ipady=10)
    label.config(font=new_font)
    for char in text:
        current_text += char
        label.config(text=current_text)
        window.update()
        window.after(letter_delay)


def remove_buttons():
    for widget in window.winfo_children():
        widget.destroy()

def ikinci_sayfa(süre):
    play()
    remove_buttons()
    window.update()
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    button2 = ImageButton(window,command=lambda: üçüncü_sayfa(" 2 ", " 1.5 "))
    button2.grid(row=2, column=0)
    button2.load(r"C:\Users\PC\Downloads\nami-gif-5.gif", 500, 400)

    slow_print("Eğlenmen için" + süre + " saat zamanın var," + süre + " saat geçince tekrar görüşücez. İYİ EĞLENCELER!")

def üçüncü_sayfa(süre,süre2):
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    window.withdraw()
    if zaman >= hour3 and day != "Saturday" and day != "Sunday":
     remove_buttons()
     window.deiconify()
     play()
     button3 = ImageButton(window, command=lambda: dördüncü_sayfa(" 1.5 "))
     button3.grid(row=2, column=0)
     button3.load(r"C:\Users\PC\Downloads\1fa731928210a896bf23c52b2f5b8801.gif", 500, 400)
     slow_print(süre + " saat geçti. Artık çalışma vakti." + süre2 + "saat sonra tekrar mola vericeksin. İYİ ÇALIŞMALAR!")
    else:
        time.sleep(15)
        üçüncü_sayfa(" 2 ", " 1.5 ")

def dördüncü_sayfa(süre):
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    window.withdraw()
    if zaman >= str(hour8) and day != "Saturday" and day != "Sunday":
      remove_buttons()
      window.deiconify()
      play()
      button4 = ImageButton(window,command=lambda: beşinci_sayfa(" 2 "))
      button4.grid(row=2, column=0)
      button4.load(r"C:\Users\PC\Downloads\6gGAXzl.gif", 500, 400)
      slow_print("Artık mola verebilirsin." + süre + "saat sonra yeniden çalışma vakti olucak. İYİ EĞLENCELER!")
    else:
        time.sleep(15)
        dördüncü_sayfa(" 1.5 ")


def beşinci_sayfa(süre):
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    window.withdraw()
    if zaman >= str(hour10) and day != "Saturday" and day != "Sunday":
      remove_buttons()
      window.deiconify()
      play()
      button5 = ImageButton(window,command=lambda: altıncı_sayfa(" 01:00"))
      button5.grid(row=2, column=0)
      button5.load(r"C:\Users\PC\Downloads\6ddbb48575a137d23f41076d40c6bbcf.gif",500, 400)
      slow_print("Şimdi çalışma vakti!" + süre + " saat sonra mola vericeksin ve gün bitmiş olucak")
    else:
         time.sleep(15)
         beşinci_sayfa(" 2 ")

def altıncı_sayfa(süre):
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    window.withdraw()
    if zaman >= str(hour12) and day != "Saturday" and day != "Sunday":
      remove_buttons()
      window.deiconify()
      play()
      button6 = ImageButton(window, command=window.destroy)
      button6.grid(row=2, column=0)
      button6.load(r"C:\Users\PC\Downloads\nami-robin-hand-wake-aj0rsh91nu1m7nun.gif", 500, 400)
      if zaman >= "23:00":
       slow_print("Artık saat geç oldu. Bilgisayarı kapat ve \nyatağına git. gece" + süre + "'a kadar dizi izleyebilirsin. \nİYİ İŞ ÇIKARDIN!!")
      elif zaman <= "23:00" and zaman >= "21:30":
       slow_print("Saat hala erken. 1 saat daha çalışıp zamanı değerlendirebilirsin. 1 saat sonra dönücem. İYİ ÇALIŞMALAR!")
       window.withdraw()
       time.sleep(3600)
       window.deiconify()
       play()
       button8 = ImageButton(window, command=window.destroy)
       button8.grid(row=2, column=0)
       slow_print("Uyku vakti! İYİ GECELER!")


    else:
      time.sleep(15)
      altıncı_sayfa(" 01:00")

def  alternatif1():
    remove_buttons()
    window.deiconify()
    button7 = ImageButton(window,command=lambda: alternatif2(" 1.5 ", " 1.5 ", " 1 ", " 1 "))
    button7.grid(row=2, column=0)
    button7.load(r"C:\Users\PC\Downloads\animesher.com_manga-ami-one-piece-1851980.gif", 500, 400)
    slow_print("Bugün Bilgisayarı geç açtın. Hastaysan dinlenebilirsin. Mazeretin yoksa çalışmaya başlamalısın!")

def alternatif2(süre, süre2, süre3, süre4):
    zaman = time.strftime("%H:%M")
    day = time.strftime("%A")
    window.withdraw()
    if zaman >= "18:00" and zaman <= "18:30" and day != "Saturday" and day != "Sunday":
        remove_buttons()
        window.deiconify()
        button6 = ImageButton(window, command=lambda: alternatif3(" 2 "))
        button6.grid(row=2, column=0)
        button6.load(r"C:\Users\PC\Downloads\6jZp.gif",  500, 400)
        slow_print("Bugün Bilgisayarı geç açtığın için çalışma saatleri değişicek, Eğlenmen için"+ süre +" saat süren var. İYİ EĞLENCELER!!")
    elif zaman >= "18:30" and zaman <= "20:00" and day != "Saturday" and day != "Sunday":
        remove_buttons()
        window.deiconify()
        button6 = ImageButton(window, command=alternatif4)
        button6.grid(row=2, column=0)
        button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 500, 400)
        slow_print("Bugün Bilgisayarı geç açtığın için çalışma saatleri değişicek, Eğlenmen için"+ süre2 +" saat süren var. İYİ EĞLENCELER!!")
    elif zaman >= "20:00" and zaman <= "21:00" and day != "Saturday" and day != "Sunday":
        remove_buttons()
        window.deiconify()
        button6 = ImageButton(window, command=alternatif5)
        button6.grid(row=2, column=0)
        button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
        slow_print(
            "Bugün Bilgisayarı geç açtığın için çalışma saatleri değişicek, Eğlenmen için"+ süre3 +" saat süren var. İYİ EĞLENCELER!!!!")
    elif zaman >= "21:00" and zaman <= "22:30" and day != "Saturday" and day != "Sunday":
        remove_buttons()
        window.deiconify()
        button6 = ImageButton(window, command=alternatif6)
        button6.grid(row=2, column=0)
        button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
        slow_print("Bugün Bilgisayarı geç açtığın için çalışma saatleri değişicek, Eğlenmen için"+ süre4 +" saat süren var. İYİ EĞLENCELER!!")
    elif zaman >= "22:30" and zaman <= "23:59" and day != "Saturday" and day != "Sunday":
        remove_buttons()
        window.deiconify()
        button6 = ImageButton(window, command=window.destroy)
        button6.grid(row=2, column=0)
        button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
        slow_print("Bugün Bilgisayarı geç açtı. saaat geç oldu. Uyku vakti. İYİ GECELER!")


def alternatif3(süre):
    window.withdraw()
    time.sleep(5400)
    window.deiconify()
    remove_buttons()
    button6 = ImageButton(window, command=alternatif7)
    button6.grid(row=2, column=0)
    button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
    slow_print("Eğlence vakti bitti. Çalışma zamanı! Merak etme" + süre + "saat sonra geri dönücem ve eğlenmen için zaman ayırıcam!")

def alternatif4(süre):
     window.withdraw()
     time.sleep(5400)
     window.deiconify()
     remove_buttons()
     button6 = ImageButton(window, command=alternatif4)
     button6.grid(row=2, column=0)
     button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
     slow_print(
            "Çalışma zamanı!" + süre + "saat sonra mola vericeksin!")

def alternatif5(süre):
    window.withdraw()
    time.sleep(3600)
    window.deiconify()
    remove_buttons()
    button6 = ImageButton(window, command=alternatif4)
    button6.grid(row=2, column=0)
    button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
    slow_print("Eğlence vakti bitti. Çalışma zamanı!" + süre + "saat sonra mola vericeksin!")

def alternatif6():
    zaman = time.strftime("%H:%M")
    window.withdraw()
    time.sleep(3600)
    window.deiconify()
    remove_buttons()
    button6 = ImageButton(window, command=lambda: sleep(5400))
    button6.grid(row=2, column=0)
    button6.load(r"C:\Users\PC\Downloads\6jZp.gif", 400, 300)
    slow_print("Eğlence vakti bitti. Çalışma zamanı! günün son çalışması bu. İyi çalışmalar!!")



def alternatif7():
    pass


im = Image.open(r"C:\Users\PC\Downloads\ai-generated-anime-girl-sticker-the-dark-ones-png.png")
resized_img = im.resize((150, 200))
img2 = ImageTk.PhotoImage(resized_img)
def png1():

    btn = tk.Button(text='Button', font='Helvetica 36', bg='grey', fg='blue', image=img2, command=ilk_sayfa)
    btn.grid(row=2, column=0)
    lbl = tk.Label(window, text="T I K L A", bg="pink")
    lbl.grid(row=3, column=0)
    play()


def ilk_sayfa():
    remove_buttons()
    play()
    button1 = ImageButton(window, command=lambda: ikinci_sayfa(" 2 "))
    button1.grid(row=2, column=0)
    button1.load(r'C:\Users\PC\Downloads\indir.gif', 500, 400)
    slow_print("Bilgisayarı açtın. Hoşgeldin!, okuldan geldiğin için dinlenebilirsin.")


def zaman_update():
    day = time.strftime("%A")
    saat = time.strftime("%H:%M")
    if start <= "23:59" and start >= "14:00":
        png1()



    else:
     time.sleep(15)
     zaman_update()


zaman_update()

window.mainloop()