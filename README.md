# Autify Test
## Function
Fetches metadata and html source code of url given as an argument. 
## Run Code
### Without Docker
Run on command line ```python3 fetch.py --metadata https://www.facebook.com``` for example. 
Or if you want to run it without metadata ```python3 fetch.py https://www.facebook.com```. 

### With Docker
Build the Dockerfile using ```docker build --tag [tag] . ```
then run the image using the tag you gave above.
