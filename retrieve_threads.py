import json
import time
import csv
import datetime

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

def request_until_succeed(url):
    req = Request(url)
    success = False
    while success is False:
        try:
            response = urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL {}: {}".format(url, datetime.datetime.now()))
            print("Retrying.")

    return response.read()

def writeFile(path, name, text):
    write_file = open(path + name,"w+")
    write_file.write(text)
    write_file.close()



filename = "my_csv.csv" # csv filename
count = 0 # csv row counter

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        url = url[:len(url)-1] + ".json"
        name_file = url[url.rfind('/')+1:]

        json_downloaded = request_until_succeed(url)
        data = json.dumps(json_downloaded)
        writeFile("./threads/", name_file, data)
        print("\n" + str(count) + " writing: "+ name_file)

        count +=1
