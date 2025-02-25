import subprocess
from bs4 import BeautifulSoup
import time

def downloadFiles():
    url = "https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247"
    
    # Fetch the page content using requests
    import requests
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    
    # Extract the download link from the page
    link_tag = soup.find('a', {'id': 'a11y-1-tab-tab-download'})
    
    if link_tag:
        download_url = link_tag.get('href')
        print("Download URL:", download_url)
    else:
        print("Download link not found")
        return
    
    # Use wget to download the file
    print("Starting download with wget...")
    try:
        # Using subprocess to call wget
        subprocess.run(["wget", download_url, "-O", "insiderThreatDataset.zip", "-c", "--quiet"])
        print("Download completed!")
    except Exception as e:
        print(f"Error downloading the file: {e}")

downloadFiles()
