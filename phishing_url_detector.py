
from urllib.parse import urlparse

url = input("Enter website URL: ")

parsed = urlparse(url)

if (parsed.scheme in ["http", "https"]
    and parsed.netloc
    and ("@" in url or "-" in parsed.netloc
         or len(parsed.netloc) > 30)):
    print("Warning: Suspicious URL")
elif parsed.scheme in ["http", "https"] and parsed.netloc:
    print("URL looks normal based on basic checks")
else:
    print("Invalid URL format")
