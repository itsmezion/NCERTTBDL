## Made by itsmezion and revantTNK

import tkinter
import tkinter.ttk as ttk
from urllib.request import urlretrieve

root = tkinter.Tk()
root.title('NCERT Textbook Downloader')
root.geometry('500x250')
root.configure(bg="beige")

def download(url, filename):
    urlretrieve(url, filename)
    downloadedMessage = tkinter.Message(root, text="Successfully downloaded chapter")
    downloadedMessage.pack(pady=5)

def selected(e):
    if subjectSelector.get() == "Maths":
        chapterSelector.config(value=gr1MathChap)
        chapterSelector.current(0)
    if subjectSelector.get() == "Science":
        chapterSelector.config(value=gr1SciChap)
        chapterSelector.current(0)
        
def chosen():
    baseUrl = "https://ncert.nic.in/textbook/pdf/"
    match subjectSelector.get():
        case "Maths":
            match chapterSelector.get():
                case "Chapter 1":
                    download(baseUrl + "hemh101.pdf", "MATH CH-1.pdf")
                case "Chapter 2":
                    download(baseUrl + "hemh102.pdf", "MATH CH-2.pdf")
                case "Chapter 3":
                    download(baseUrl + "hemh103.pdf", "MATH CH-3.pdf")
                case "Chapter 4":
                    download(baseUrl + "hemh104.pdf", "MATH CH-4.pdf")
                case "Chapter 5":
                    download(baseUrl + "hemh105.pdf", "MATH CH-5.pdf")
                case "Chapter 6":
                    download(baseUrl + "hemh106.pdf", "MATH CH-6.pdf")
                case "Chapter 7":
                    download(baseUrl + "hemh107.pdf", "MATH CH-7.pdf")
                case "Chapter 8":
                    download(baseUrl + "hemh108.pdf", "MATH CH-8.pdf")
                case "Chapter 9":
                    download(baseUrl + "hemh109.pdf", "MATH CH-9.pdf")
                case "Chapter 10":
                    download(baseUrl + "hemh110.pdf", "MATH CH-10.pdf")
                case "Chapter 11":
                    download(baseUrl + "hemh111.pdf", "MATH CH-11.pdf")
                case "Chapter 12":
                    download(baseUrl + "hemh112.pdf", "MATH CH-12.pdf")
                case "Chapter 13":
                    download(baseUrl + "hemh113.pdf", "MATH CH-13.pdf")
        case "Science":
            match chapterSelector.get():
                case "Chapter 1":
                    download(baseUrl + "hesc101.pdf", "SCIENCE CH-1.pdf")
                case "Chapter 2":
                    download(baseUrl + "hesc102.pdf", "SCIENCE CH-2.pdf")
                case "Chapter 3":
                    download(baseUrl + "hesc103.pdf", "SCIENCE CH-3.pdf")
                case "Chapter 4":
                    download(baseUrl + "hesc104.pdf", "SCIENCE CH-4.pdf")
                case "Chapter 5":
                    download(baseUrl + "hesc105.pdf", "SCIENCE CH-5.pdf")
                case "Chapter 6":
                    download(baseUrl + "hesc106.pdf", "SCIENCE CH-6.pdf")
                case "Chapter 7":
                    download(baseUrl + "hesc107.pdf", "SCIENCE CH-7.pdf")
                case "Chapter 8":
                    download(baseUrl + "hesc108.pdf", "SCIENCE CH-8.pdf")
                case "Chapter 9":
                    download(baseUrl + "hesc109.pdf", "SCIENCE CH-9.pdf")
                case "Chapter 10":
                    download(baseUrl + "hesc110.pdf", "SCIENCE CH-10.pdf")
                case "Chapter 11":
                    download(baseUrl + "hesc111.pdf", "SCIENCE CH-11.pdf")
                case "Chapter 12":
                    download(baseUrl + "hesc112.pdf", "SCIENCE CH-12.pdf")
                case "Chapter 13":
                    download(baseUrl + "hesc113.pdf", "SCIENCE CH-13.pdf")
            

subjects = ["Science", "Maths"]
gr1SciChap = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7", "Chapter 8", "Chapter 9", "Chapter 10", "Chapter 11", "Chapter 12", "Chapter 13"]
gr1MathChap = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7", "Chapter 8", "Chapter 9", "Chapter 10", "Chapter 11", "Chapter 12", "Chapter 13"]
    
welcome = tkinter.Label(root, text="Download every chapter, every textbook, here.")
welcome.configure(bg="beige")
welcome.pack()

subjectSelector = ttk.Combobox(root, value=subjects)
subjectSelector.pack(pady=5)
subjectSelector.current(0)
subjectSelector.set(subjects[0])
subjectSelector.bind("<<ComboboxSelected>>", selected)

chapterSelector = ttk.Combobox(root, value=[" "])
chapterSelector.pack(pady=5)
chapterSelector.current(0)

downloadButton = tkinter.Button(root, text="Download", command=chosen)
downloadButton.configure(bg="yellow")
downloadButton.pack(pady=20)

root.mainloop()
