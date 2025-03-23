import subprocess
import tkinter as tk
import os

# Top level window
frame = tk.Tk()
frame.title("Youtube downloader")

frame.geometry('400x200')

def printInput():
    try:
        Link = inputtxt.get(1.0, "end-1c")
        os.chdir(os.getcwd())

        cmd = r"C:\Users\PC\Desktop\yt-dlp-master\yt-dlp-master\yt-dlp.cmd "+Link
        print(cmd)
        #cmd = 'yt-dlp -f best "'+Link+'"'
        os.system(cmd)
        result = subprocess.check_output(cmd, shell=True)
        lbl.config(text=result)
    except Exception as err:
        lbl.config(text=err)
        #print(f"Unexpected {err=}, {type(err)=}")


# TextBox Creation
lblhead = tk.Label(frame, text = "Place Youtube vedio Link below")
lblhead.pack()
lbl3 = tk.Label(frame, text = "")
lbl3.pack()
inputtxt = tk.Text(frame,
                   height = 1,
                   width = 40)

inputtxt.pack()
lbl4 = tk.Label(frame, text = "Click Download")
lbl4.pack()
# Button Creation
printButton = tk.Button(frame,
                        text = "Download",
                        command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
