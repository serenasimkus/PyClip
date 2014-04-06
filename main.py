from Tkinter import Tk, Frame, BOTH, Entry, StringVar
import threading, subprocess, sys, os
from subprocess import Popen, PIPE

class Login(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Centered window")
        self.entrythingy = Entry()
        self.entrythingy.pack()
        self.contents = StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def print_contents(self, event):
        name = self.contents.get()
        if(name):
            # Start network discovery
            subprocess.call([os.path.dirname(os.path.abspath(sys.argv[0]))+ "/" + "discovery.sh", name])
            # process = Popen("python discovery.py", stdout=PIPE)
            # stdout, stderr = process.communicate()
            # # Starts network broadcast
            # process1 = Popen("python server.py " + name, stdout=PIPE)
            # stdout, stderr = process1.communicate()
            root.destroy()

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
    ex = Login(root)
    root.mainloop()

if __name__ == '__main__':
    main()
