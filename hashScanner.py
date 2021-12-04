import requests
from time import sleep
from bs4 import BeautifulSoup

print("[MD5-SHA1]")
print("[+]Enter a Format")
format = input(">>>[+]Choose a Format | [MD5]-[SHA1]: ")
if format == "md5" or format == "MD5":
    print("[+]Enter a HASH")
    md5 = input(">>>[+]HASH: ")
    query = "https://md5.gromweb.com/?md5={}".format(md5)
    send_req = requests.get(query)
    sleep(3)
    soup = BeautifulSoup(send_req.content,"lxml")
    hash_info = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_info:
        print("[+]Search HASH: {}".format(md5),"\n")
        print("[%]HASH: {}".format(hash.text))

elif format == "sha1" or format == "SHA1":
    print("[+]Enter a HASH")
    sha1 = input(">>>[+]HASH: ")
    query = "https://sha1.gromweb.com/?hash={}".format(sha1)
    send_req = requests.get(query)
    sleep(3)
    soup = BeautifulSoup(send_req.content,"lxml")
    hash_info = soup.find_all("em",attrs={"class":"long-content string"})

    for hash in hash_info:

        print("[+]Search HASH: {}".format(sha1),"\n")
        print("[%]HASH: {}".format(hash.text))

else:

    print("[Please Make a Valid Selection!]")

input()