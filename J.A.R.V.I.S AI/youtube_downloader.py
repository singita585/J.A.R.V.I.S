#imports that needed to downloaded youtube videos
from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file_size = 0

# Progress of the video being download
def progress(stream=None, chunk=None, remaining=None):
    file_download = (file_size-remaining)
    per = round((file_download/file_size)*100, 1)
    dBtn.config(text=f'{per}% downloaded')

# Codes to start downloading the video
def startDownload():
    global file_size
    try:
        URL = urlField.get()
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)
        path_save = askdirectory()
        if path_save is None:
            return
        ob = Youtube(URL, on_progress_callback=progress)
        strm = ob.streams[0]
        x = ob.description.split("|")
        file_size = strm.filesize
        dfile_size = file_size
        dfile_size /= 1000000
        dfile_size = riund(dfile_size, 2)
        label.config(text="Size: " + str(dfile_size) + " MB")
        label.pack(side=TOP, pady=10)
        desc.config(text=ob.title + "\n\n" + "Label: " + ob.author + "\n\n" + "length: " + str(round(ob.length/60, 1)) + "mins\n\n"
                    "Views: " + str(round(ob.views/1000000, 2)) + "M")
        desc.pack(side=TOP, pady=10)
        strm.download(path_save, strm.title)
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0, END)
        label.pack_forget()
        desc.pack_forget()
        dBtn.config(text="Start Download")

    except Exception as e:
        print(e)
        print("Error!!")

def startDownloadthread():
    thread = Thread(target=startDownload)
    thread.start()

main = Tk()
main.title("My Youtube Downloader")
main.config(bg = "#3498DB")
main.iconbitmap("images\\youtube-ios-app.ico")
main.geometry("500x600")

file = PhotoImage(
    file="images\\photo.png")
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("Calibri", 16), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=15)

dBtn = Button(main, text="Start Download", font=(
    "Calibri", 16), relief="ridge", activeforeground="red", command=startDownloadthread)
dBtn.pack(side=TOP)
label = Label(main, text="")
desc = Label(main, text="")
author = Label(main, text="@G.S.")
author.config(font=("Courier", 44))
author.pack(side=BOTTOM)
main.mainloop()