from urllib.request import urlretrieve
import requests as r
from tqdm import tqdm

baseUrl = "https://ncert.nic.in/textbook/pdf/"

def dl(url, filename):
    try:
        urlretrieve(url, filename)
        print(f"Successfully downloaded book/chapter as {filename}!")
    except Exception:
        print(f"Download failed with error: {Exception}")

def dl_with_requests(url, filename): #requests lib supports progress tracking, needed because NCERT servers are slow asf
    try:
        response = r.get(url, stream=True) # This sends a GET request to the NCERT servers to download the .zip or .pdf file
        response.raise_for_status()  # Raises an HTTPError for bad responses or failed downloads
        
        # Open the local file to write the downloaded content
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024


        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
                with open(filename, "wb") as file:
                        for data in response.iter_content(block_size):
                                progress_bar.update(len(data))
                                file.write(data)
        
        print(f"\nBook/Chapter downloaded successfully as {filename}!")
        return True
    except r.exceptions.RequestException as e:
        print(f"Error downloading file with code {e}")
        return False

grade = int(input("Select your grade [1-12]: "))

def g1():
    subject = int(input('''\nSelect the subject:
                    
                    1. English
                    2. Mathematics
                    3. Hindi
                    4. Urdu
                    
                    Select the number corresponding to the subject: '''))
                    
    if subject == 1:
        boc = int(input('''\nDo you want to download all of Mridang or just one chapter?
                        
                        1. Full Book
                        2. One Chapter
                        
                        Select the number corresponding to the option: '''))
                        
        if boc == 2:
            chapter = int(input("\nSelect the chapter you wish to download [1-9]: "))
            match chapter:
                case 1:
                    dl_with_requests(baseUrl + "amer101.pdf", "Mridang CH-1.pdf")
                case 2:
                    dl_with_requests(baseUrl + "aemr102.pdf", "Mridang CH-2.pdf")
                case 3:
                    dl_with_requests(baseUrl + "amer103.pdf", "Mridang CH-3.pdf")
                case 4:
                    dl_with_requests(baseUrl + "amer104.pdf", "Mridang CH-4.pdf")
                case 5:
                    dl_with_requests(baseUrl + "amer105.pdf", "Mridang CH-5.pdf")
                case 6:
                    dl_with_requests(baseUrl + "amer106.pdf", "Mridang CH-6.pdf")
                case 7:
                    dl_with_requests(baseUrl + "amer107.pdf", "Mridang CH-7.pdf")
                case 8:
                    dl_with_requests(baseUrl + "amer108.pdf", "Mridang CH-8.pdf")
                case 9:
                    dl_with_requests(baseUrl + "amer109.pdf", "Mridang CH-9.pdf")
        elif boc == 1:
            dl_with_requests(baseUrl + "aemr1dd.zip", "Mridang, English Grade-1.zip1")
                    
    if subject == 2:
        boc = int(input('''Do you want to download all of Joyful Mathematics or just one chapter?
                        
                        1. Full Book
                        2. One Chapter
                        
                        Select the number corresponding to the option: '''))
        
        if boc == 1:
            dl(baseUrl + "aejm1dd.zip", "Joyful Mathematics Full Book.zip")
        elif boc == 2:
            chapter = int(input("Select the chapter to wish to download [1-13]:"))
            match chapter:
                case 1:
                    dl_with_requests(baseUrl + "aejm101.pdf", "JM CH-1.pdf")
                case 2:
                    dl_with_requests(baseUrl + "aejm102.pdf", "JM CH-2.pdf")
                case 3:
                    dl_with_requests(baseUrl + "aejm103.pdf", "JM CH-3.pdf")
                case 4:
                    dl_with_requests(baseUrl + "aejm104.pdf", "JM CH-4.pdf")
                case 5:
                    dl_with_requests(baseUrl + "aejm105.pdf", "JM CH-5.pdf")
                case 6:
                    dl_with_requests(baseUrl + "aejm106.pdf", "JM CH-6.pdf")
                case 7:
                    dl_with_requests(baseUrl + "aejm107.pdf", "JM CH-7.pdf")
                case 8:
                    dl_with_requests(baseUrl + "aejm108.pdf", "JM CH-8.pdf")
                case 9:
                    dl_with_requests(baseUrl + "aejm109.pdf", "JM CH-9.pdf")
                case 10:
                    dl_with_requests(baseUrl + "aejm110.pdf", "JM CH-10.pdf")
                case 11:
                    dl_with_requests(baseUrl + "aejm111.pdf", "JM CH-11.pdf")
                case 12:
                    dl_with_requests(baseUrl + "aejm112.pdf", "JM CH-12.pdf")
                case 13:
                    dl_with_requests(baseUrl + "aejm113.pdf", "JM CH-13.pdf")
                    
  
                        
g1()