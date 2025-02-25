import requests
from bs4 import BeautifulSoup
import time
import os

def downloadFiles():
    url = "https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, "html.parser")
    link_tag = soup.find('a', {'id': 'a11y-1-tab-tab-download'})

    # Get the href attribute (the URL)
    if link_tag:
        download_url = link_tag.get('href')
        print("Download URL:", download_url)
    else:
        print("Download link not found")
        return

    response = requests.get(download_url, stream=True)
    
    total_size = int(response.headers.get('Content-Length', 0))
    downloaded = 0
    
    # Define progress update interval (in seconds)
    progress_interval = 10

    # Save the content to a file
    with open("insiderThreatDataset.zip", "wb") as file:
        start_time = time.time()
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                downloaded += len(chunk)
                
                # Update progress every 30 seconds
                if time.time() - start_time >= progress_interval:
                    start_time = time.time()
                    progress = (downloaded / total_size) * 100
                    print(f"Download progress: {progress:.2f}%")
    
    print("Download completed!")

#This should be max speed so download time will depend on wifi speed

downloadFiles()
