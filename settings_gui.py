from tkinter import *
import subprocess

# Function to load the live detection stream
def load():
    confidence = conf_slider.get()/100
    rtsp_url = rtsp_entry.get()
    quit_key = quitkey.get()

    # Display loading message
    load_lbl = Label(window, text='Loading stream...', font=('IMPACT', 12), fg='green', bg='white').place(x=20, y=320)
    window.update_idletasks()

    # Start the live detection subprocess(Change python.exe path based on your venv name)
    process = subprocess.Popen([".venv\Scripts\python.exe", "livedetection.py", str(confidence), rtsp_url, quit_key])

    # Close the main window after loading
    window.destroy()

# Main Tkinter window setup
window = Tk()
window.title('')
window.geometry('350x400+700+275')
window.resizable(False, False)
window['background'] = 'gray14'

# Confidence Slider
lbl_conf = Label(window, text='Confidence', font=('IMPACT', 15), fg='White', bg='gray14').place(x=20, y=20)
conf_slider = Scale(window, from_=0, to_=100, font=('IMPACT', 10), orient=HORIZONTAL, length=300, bg='#E7E6E6')
conf_slider.place(x=20, y=60)

# RTSP URL Entry
lbl_rtsp = Label(window, text='RTSP URL', font=('IMPACT', 15), fg='White', bg='gray14').place(x=20, y=120)
rtsp_entry = Entry(window, font=('IMPACT', 10), bg='#E7E6E6')
rtsp_entry.place(x=20, y=155)

# Quit Key OptionMenu
quitkey=StringVar()
quitkey.set('q')
stream_quit = OptionMenu(window, quitkey, 'q', 'w', 'e', 'r', 't', 'y')
lbl_stream_quit = Label(window, text='Quit Key', font=('IMPACT', 15), fg='White', bg='gray14').place(x=20, y=190)
stream_quit.place(x=20, y=230)

# Load Button
load_button = Button(window, text="LOAD", command=load, font=('IMPACt', 12), bg='#6162FF', fg='white', padx=10, pady=5, cursor='hand2', borderwidth=2,  relief=FLAT )
load_button.place(x=20, y=330, width=140, height=40)

# Start the Tkinter event loop
window.mainloop()