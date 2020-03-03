## Parsing URLs for Firewall Squid Proxy Migration
import csv
from urllib.parse import urlparse




## Open log. Should already be in .csv format
with open('****************') as text_file: #Put excel file her_
    print("Below is the raw data, ensure it is the correct list. Large lists may not be listed in entirety\n")
    readURLS = csv.DictReader(text_file)

## Create list from rows of URLs
    URLS = []
    for row in readURLS:
        print(row['URL'])
        URLS.append(row['URL'])

## Confirm you have the right list. Putting this in otherwise I won't
while True:
    if input('Do You Want To Continue? ') != 'n':
        print('\nBeginning Parsing...')
        break

## Begin parsing
print('Below is the parsed URLs\n')

newURLS = ([s.strip('http://') for s in URLS]) # remove http:// from list values
newURLS = list(dict.fromkeys(newURLS))  # remove duplicates

print('this is a test\n')
print(newURLS)

with open("********************","w") as f:    #put your desired path where you want the output .csv to be saved
    wr = csv.writer(f,delimiter="\n")
    wr.writerow(newURLS)
