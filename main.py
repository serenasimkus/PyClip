from Tkinter import Tk, Frame, BOTH, Entry, StringVar
import threading

# Project Modules
import discovery, server

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Centered window")
        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.contents = StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def print_contents(self, event):
        name = self.contents.get()
        # Start network broadcast
        threading.Thread(server.Discoverable(name))
        print(discovery.main())

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():

    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
