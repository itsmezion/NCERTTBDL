## Made by itsmezion and revantTNK

import tkinter
import tkinter.ttk as ttk
from urllib.request import urlretrieve

root = tkinter.Tk()
root.title('NCERT Textbook Downloader')
root.geometry('500x200')
root.configure(bg="beige")

def download(url, filename):
    urlretrieve(url, filename)
    downloadedMessage = tkinter.Message(root, text="Successfully downloaded chapter")
    downloadedMessage.pack(pady=5)

def selected(e):
    if subjectSelector.get() == "Maths":
        chapterSelector.config(value=gr1MathChap)
        chapterSelector.current(0)
    if subjectSelector.get() == "English":
        chapterSelector.config(value=gr1EngChap)
        chapterSelector.current(0)
        
def chosen():
    baseUrl = "https://ncert.nic.in/textbook/pdf/"
    match subjectSelector.get():
        case "Maths":
            match chapterSelector.get():
                case "Chapter 1":
                    download(baseUrl + "aejm101.pdf", "JM CH-1.pdf")
                case "Chapter 2":
                    download(baseUrl + "aejm102.pdf", "JM CH-2.pdf")
                case "Chapter 3":
                    download(baseUrl + "aejm103.pdf", "JM CH-3.pdf")
                case "Chapter 4":
                    download(baseUrl + "aejm104.pdf", "JM CH-4.pdf")
                case "Chapter 5":
                    download(baseUrl + "aejm105.pdf", "JM CH-5.pdf")
                case "Chapter 6":
                    download(baseUrl + "aejm106.pdf", "JM CH-6.pdf")
                case "Chapter 7":
                    download(baseUrl + "aejm107.pdf", "JM CH-7.pdf")
                case "Chapter 8":
                    download(baseUrl + "aejm108.pdf", "JM CH-8.pdf")
                case "Chapter 9":
                    download(baseUrl + "aejm109.pdf", "JM CH-9.pdf")
                case "Chapter 10":
                    download(baseUrl + "aejm110.pdf", "JM CH-10.pdf")
                case "Chapter 11":
                    download(baseUrl + "aejm111.pdf", "JM CH-11.pdf")
                case "Chapter 12":
                    download(baseUrl + "aejm112.pdf", "JM CH-12.pdf")
                case "Chapter 13":
                    download(baseUrl + "aejm113.pdf", "JM CH-13.pdf")
        case "English":
            match chapterSelector.get():
                case "Chapter 1":
                    download(baseUrl + "aemr101.pdf", "Mridang CH-1.pdf")
                case "Chapter 2":
                    download(baseUrl + "aemr102.pdf", "Mridang CH-2.pdf")
                case "Chapter 3":
                    download(baseUrl + "aemr103.pdf", "Mridang CH-3.pdf")
                case "Chapter 4":
                    download(baseUrl + "aemr104.pdf", "Mridang CH-4.pdf")
                case "Chapter 5":
                    download(baseUrl + "aemr105.pdf", "Mridang CH-5.pdf")
                case "Chapter 6":
                    download(baseUrl + "aemr106.pdf", "Mridang CH-6.pdf")
                case "Chapter 7":
                    download(baseUrl + "aemr107.pdf", "Mridang CH-7.pdf")
                case "Chapter 8":
                    download(baseUrl + "aemr108.pdf", "Mridang CH-8.pdf")
                case "Chapter 9":
                    download(baseUrl + "aemr109.pdf", "Mridang CH-9.pdf")
            

subjects = ["English", "Maths"]
gr1EngChap = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7", "Chapter 8", "Chapter 9"]
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