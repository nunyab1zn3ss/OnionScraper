import requests
from bs4 import BeautifulSoup
import socket

# Set the keywords to search for
keywords = ["hacking", "malware", "phishing"]

# Set the URL of the darknet search engine
url = "http://darksearchengine.onion"

# Set the search query
query = "example"

# Send a request to the darknet search engine and retrieve the HTML response
response = requests.get(url, params={"q": query})

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all of the .onion domain links in the HTML response
links = soup.find_all("a", href=lambda href: href and href.endswith(".onion"))

# Open the results file
with open("results.txt", "w") as f:
    # Iterate through the links
    for link in links:
        # Get the domain name from the link
        domain = link["href"]

        # Attempt to resolve the domain name using the Tor network
        try:
            # Set the Tor proxy
            socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
            socket.socket = socks.socksocket

            # Resolve the domain name
            addr = socket.gethostbyname(domain)

            # Print the resolved IP address
            print(f"Resolved '{domain}' to {addr}.", file=f)

            # Set the URL of the darknet site
            url = f"http://{domain}"

            # Send a request to the darknet site and retrieve the HTML response
            response = requests.get(url)

            # Parse the HTML response using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Iterate through the keywords
            for keyword in keywords:
                # Search the HTML response for the keyword
                results = soup.find_all(string=keyword)

                # Print the number of results found
                print(f"Found {len(results)} occurrences of '{keyword}'.", file=f)

                # Print the results
                for result in results:
                    print(result, file=f)

        # Handle any exceptions
        except Exception as e:
            # Print the error message
            print(f"Error: {e}", file=f)
