"""Uses brand new features of Python 3"""
import argparse
import os
import socket
import sys
import time
import requests
from googlesearch import search 

try:
    from __version__ import __version__
except ModuleNotFoundError:
    from plunder.__version__ import __version__


def getLinks(query, proxy):
    """
    Get user input ip address or use default.
    """
    currentnum = 1
    userinput = input(
        f'What query do you want to run? (default {query}): ') or query
    start_time = time.time()
    print(f'\nGetting results from google for: {userinput}...')

    links = []
    for j in search(query, tld="co.in", num=100, stop=100, pause=2): 
        links.append(j) 
    # always print the time it took to complete
    print("--- %s seconds ---" % (time.time() - start_time))


def prep():
    """
    Get the args and set them.

    args
    ----
    q or query for the search parameters you want to send
    v or version for the current version
    j or json to output to a json file
    """
    parser = argparse.ArgumentParser(description='How to run plunder.')
    parser.add_argument('-q', '--query', help='Your query to search', dest="query", default=".php?id=1")
    parser.add_argument('-v', '--version', action='version',
                        version=__version__)
    parser.add_argument('-j','--json', help='Output in JSON file, otherwise output to screen only.', dest="json_out", action='store_true', default=False)
    args = parser.parse_args()
    return args


def load_proxies(url):
    """
    Get's list of ip addresses from free proxy servers.
    Accepts: url as string
    Returns: list of ip addresses and ports
    Prints: ip address and port used only in verbose mdoe
    """
    listofproxies = requests.get(url).text
    lists = [x for x in listofproxies.split('\n') if "+" in x]
    filtered = set(x.split()[0] for x in lists if x[0].isdigit())
    return filtered


logo = """                                     
 ____ ____ ____ ____ ____ ____ ____      
||P |||L |||U |||N |||D |||E |||R ||     
||__|||__|||__|||__|||__|||__|||__||     
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|                                                                                                                  
"""


def main():
    """
    Main function that runs everything.
    """
    args = prep()
    proxyurl = 'http://spys.me/proxy.txt'
    proxySet = load_proxies(proxyurl)
    getInput(args.query, proxySet.pop())


if __name__ == "__main__":
    print(logo)
    main()
