import time
import tkinter as tk
from PIL import Image, ImageTk

H1 = 64
H2 = 24
H3 = 16

class Clock(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#000")
        self.timelbl = tk.Label(self, text="5:45", font=('Helvetica', H1), fg="white", bg="black")
        self.timelbl.pack(anchor=tk.E)
        self.daylbl = tk.Label(self, text="Wednesday", font=('Helvetica', H2), fg="white", bg="black")
        self.daylbl.pack(anchor=tk.E)
        self.datelbl = tk.Label(self, text="1/16/2019", font=('Helvetica', H2), fg="white", bg="black")
        self.datelbl.pack(anchor=tk.E)


class Weather(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#000")
        self.temperature = tk.Label(self, text="22 * C", font=("Helvetica", H1), fg="white", bg="black")
        self.temperature.pack(side=tk.TOP, anchor=tk.W)
        self.condition = tk.Label(self, text="Clear", font=("Helvetica", H3), fg="white", bg="black")
        self.condition.pack(side=tk.TOP, anchor=tk.W)
        self.forecast = tk.Label(self, text="Sunny day but a bit of drizzle may come tomororw", font=("Helvetica", H3), fg="white", bg="black")
        self.forecast.pack(side=tk.TOP, anchor=tk.W)
        self.location = tk.Label(self, text="Lalitpur, Nepal", font=("Helvetica", H3), fg="white", bg="black")
        self.location.pack(side=tk.TOP, anchor=tk.W)


class News(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#000")
        self.headlines = tk.Label(self, text="Hello World Today is Wednesday.\nThis is special but needs more to do.\nNew Headline is github is free.\nToday is the day when she was born.", font=("Helvetica", H3), fg="white", bg="black")
        self.headlines.pack(anchor=tk.CENTER)

class Quote(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#000")
        self.quoteofday = tk.Label(self, text='"  Passion often gets suppressed beneath the responsibilites!  "', font=("Helvetica", H3), fg="white", bg="black")
        self.quoteofday.pack(anchor=tk.CENTER)


class Application(tk.Frame):
    screen_x = 0
    screen_y = 0
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        Application.screen_x = master.winfo_screenwidth()
        Application.screen_y = master.winfo_screenheight()
        self.master.bind('<Return>', self.Home)
        self.pack()
        self.StartUp()

    def StartUp(self):
        try:
            img = Image.open('res/images/logo.png')
        except:
            print("Image couldnot be loaded")
            exit()
        logo = ImageTk.PhotoImage(img)
        label = tk.Label(self.master, image=logo)
        label.image = logo # keep a reference!

        canvas = tk.Canvas(self.master, width=Application.screen_x, height=Application.screen_y, bd=0, highlightthickness=0, bg="#000")
        img = canvas.create_image(Application.screen_x / 2,Application.screen_y / 2,image=logo)
        canvas.pack()

    def Home(self, e):
        self.CleanAll(self.master)
        self.master.unbind('<Return>')

        topframe = tk.Frame(self.master, bg="#000")
        topframe.pack(fill=tk.BOTH, expand=tk.YES)
        midframe = tk.Frame(self.master, bg="#000")
        midframe.pack(fill=tk.BOTH, expand=tk.YES)
        bottomframe = tk.Frame(self.master, bg="#000")
        bottomframe.pack(fill=tk.BOTH, expand=tk.YES)

        weatherframe = Weather(topframe)
        weatherframe.pack(side=tk.LEFT, padx=100, pady=60, anchor=tk.N)

        clockframe = Clock(topframe)
        clockframe.pack(side=tk.RIGHT, padx=100, pady=60, anchor=tk.N)

        newsframe = News(bottomframe)
        newsframe.pack()

        quoteframe = Quote(midframe)
        quoteframe.pack()

    def CleanAll(self, Parent):
        listofchilds = Parent.winfo_children()
        for child in listofchilds:
            descendents = child.winfo_children()
            if descendents:
                listofchilds.extend(descendents)
            else:
                listofchilds.remove(child)
                child.pack_forget()
        return listofchilds


root = tk.Tk()
root.config(background="#000")
root.state('zoomed')
# root.attributes('-fullscreen',False)
app = Application(master=root)
app.mainloop()
