
import urllib.request
import sys
import datetime
import bs4
def fetch(
    urls: list,
    metadata: bool,
) -> None:
    urls_trunc_fetched = [] 
    num_links = 0
    images = 0
    for url in urls:
        try:
            html = urllib.request.urlopen(url)
        except:
            print(url + " not accessible/valid.")
            continue
        webpage = html.read()
        # Assuming all inputs start with https://www. which should be the case
        #  for valid formatting or else we could implement function to make sure but outside of scope of project
        trunctated_url = url[12:]
        urls_trunc_fetched.append(trunctated_url)
        #BeautifulSoup most efficient way could have done it from scratch by searching using Regular Expressions in HTML text
        soup = bs4.BeautifulSoup(webpage, 'html.parser')
        images_found = soup.findAll('img')
        links_found = soup.findAll('a')
        images += len(images_found)
        num_links += len(links_found)
        f = open("./" +trunctated_url + ".html", 'w+')
        f.write(str(webpage))
        f.close()
    if metadata == True:
        print("Last Fetched: " + str(datetime.date.today()))
        print("Site Fetched: " + trunctated_url)
        print("Images: " + str(images))
        print("Number of Links: " + str(num_links))
if __name__ == "__main__": 
    urls = []
    for url in sys.argv[1:]:
        urls.append(url)
    #Could also have used getopt.getopt to use options and arguments but thought this was faster implementation for this example.
    if urls[0] == '--metadata': 
        urls = urls[1:]
        fetch(urls,True)
    else:
        fetch(urls,False)
    
 
    
# Completed in around 25 minutes could not complete bonus since lack of time during holidays but => use BS4 to download all assets into local file
# and then write script to run html with all files from local folder (pretty easy) needs around 25 mins implementation
