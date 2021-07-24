
import sys

import requests
import argparse
from email.utils import getaddresses
import json
import json
from requests import ConnectionError


def find_leaks(email):
    url = "http://pwndb2am4tzkvold.onion/"
    username = email
    domain = "%"

    if "@" in email:
        username = email.split("@")[0]
        domain = email.split("@")[1]
        if not username:
            username = '%'

    request_data = {'luser': username, 'domain': domain,
                    'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}

    # Tor proxy
    proxy = '127.0.0.1:9050'
    print(type(proxy))
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://{}'.format(proxy), 'https': 'socks5h://{}'.format(proxy)}

    r = session.post(url, data=request_data)
    return parse_pwndb_response(r.text)


def parse_pwndb_response(text):

    if "Array" not in text:
        return None

    leaks = text.split("Array")[1:]
    emails = []

    for leak in leaks:
        leaked_email = ''
        domain = ''
        password = ''
        try:
            leaked_email = leak.split("[luser] =>")[1].split("[")[0].strip()
            domain = leak.split("[domain] =>")[1].split("[")[0].strip()
            password = leak.split("[password] =>")[1].split(")")[0].strip()
        except:
            pass
        if leaked_email:
            emails.append({'username': leaked_email,
                          'domain': domain, 'password': password})
    return emails


def check_pawn():
    G, B, R, W, M, C, end = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m'
    info = end + W + "[-]" + W
    good = end + G + "[+]" + C
    bad = end + R + "[" + W + "!" + R + "]"
    emails = ['@worldlink.com.np', '@nicasiabank.com']
    print(info + " Searching for leaks...")

    results = []
    for email in emails:

        leaks = find_leaks(email.strip())
        if leaks:
            for leak in leaks:
                results.append(leak)
            print(results)
        with open('data.txt', 'w') as outfile:
            json.dump(results, outfile)

        return "ok"
