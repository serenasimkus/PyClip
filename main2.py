from Tkinter import Tk, Frame, BOTH, Entry, StringVar
import threading, subprocess, sys, os
from subprocess import Popen, PIPE, STDOUT
from Queue import Queue, Empty
from threading import Thread

class Login(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.name = "None"

        self.proc = Popen(["python", os.path.dirname(os.path.abspath(sys.argv[0]))+ "/" + "discovery.py", self.name], stdout=PIPE, stderr=STDOUT)

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
            self.name = name

            q = Queue()
            t = Thread(target=self.reader_thread, args=[q]).start()
            # Start network discovery
            # subprocess.call([os.path.dirname(os.path.abspath(sys.argv[0]))+ "/" + "discovery.sh", name])
            # process = Popen("python discovery.py", stdout=PIPE)
            # stdout, stderr = process.communicate()
            # # Starts network broadcast
            # process1 = Popen("python server.py " + name, stdout=PIPE)
            # stdout, stderr = process1.communicate()
            self.parent.destroy()

    def reader_thread(self, q):
        """Read subprocess output and put it into the queue."""
        for line in iter(self.proc.stdout.readline, b''):
            print(line)
        print('done reading')

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
