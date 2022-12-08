import requests
from bs4 import BeautifulSoup
import socket

# TO DO: Set the keywords to search for
keywords = ["hacking", "malware", "phishing"]

# Set the URL of the darknet search engine
url = "http://darksearchengine.onion"

# TO DO: Set the search query
query = "example"

response = requests.get(url, params={"q": query})
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", href=lambda href: href and href.endswith(".onion"))

with open("results.txt", "w") as f:
    for link in links:
        domain = link["href"]

        try:
            socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
            socket.socket = socks.socksocket

            addr = socket.gethostbyname(domain)
            print(f"Resolved '{domain}' to {addr}.", file=f)
            url = f"http://{domain}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            
            for keyword in keywords:
                results = soup.find_all(string=keyword)
                print(f"Found {len(results)} occurrences of '{keyword}'.", file=f)
                
                for result in results:
                    print(result, file=f)

        except Exception as e:
            print(f"Error: {e}", file=f)
