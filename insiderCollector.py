import requests

def downloadFiles():
    url = "https://kilthub.cmu.edu/articles/dataset/Insider_Threat_Test_Dataset/12841247"

    data = requests.get(url)


    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text, "html.parser")

    link_tag = soup.find('a', {'id': 'a11y-1-tab-tab-download'})

    # Get the href attribute (the URL)
    if link_tag:
        download_url = link_tag.get('href')
        print("Download URL:", download_url)
    else:
        print("Download link not found")

    response = requests.get(download_url, stream=True)

    # Save the content to a file
    with open("insiderThreatDataset.zip", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("Download completed!")

downloadFiles()

#so can you explain how to icnrease the file speed and update every 30 seconds the progress