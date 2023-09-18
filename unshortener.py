import requests

def unshorten(short):
    try:
        while True:
            response = requests.head(short, allow_redirects=True)
            if response.url == short:
                break
            short = response.url
        return response.url
    except requests.exceptions.RequestException as e:
        print (f"Error: {e}")
        return None

short = input("Enter a short URL: ")
print (f"Unshortening {short}...")
long = unshorten(short)
if long:
    print (f"Long URL: {long}")
else:
    print ("No URL found")
