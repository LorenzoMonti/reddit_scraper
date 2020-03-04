import json
import time
import csv
import datetime
import urllib.request

# Config
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'
INPUT_CSV_FILE_NAME = 'URLs.csv'
OUTPUT_FOLDER = './threads/'
INDENT_JSON = True

# Consts
USER_AGENT_KEY = 'User-Agent'
UTF8_ENCODING = 'utf8'
JSON_EXTENSION = '.json'

def request_until_succeed(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            USER_AGENT_KEY: USER_AGENT
        }
    )
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
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

count = 0 # csv row counter
with open(INPUT_CSV_FILE_NAME) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['Links']
        url = url[:len(url)-1] + JSON_EXTENSION
        name_file = url[url.rfind('/')+1:]
        json_downloaded = request_until_succeed(url)
        data = json.loads(json_downloaded.decode(UTF8_ENCODING))
        if INDENT_JSON == True:
            data = json.dumps(data, indent=4, sort_keys=True)
        else:
            data = json.dumps(data)
        writeFile(OUTPUT_FOLDER, name_file, data)
        print("\n" + str(count) + " writing: "+ name_file)
        count +=1
