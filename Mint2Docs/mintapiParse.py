import mintapinew as mintapi
import gspread
import json
from oauth2client.client import SignedJwtAssertionCredentials
#http://gspread.readthedocs.org/en/latest/oauth2.html
#http://urllib3.readthedocs.org/en/latest/security.html

def outputPrint(n,b,l):
    print "{0:<50} -  {1:<20} -  {2:<30}".format(n,b,str(l))

    
def login(i):
    with open("login"+str(i)+".txt",'r') as f:
        login = f.readlines()
    return mintapi.Mint(str(login[0].strip()),str(login[1].strip()))

def getAccount(i):
    with open("login"+str(i)+".txt",'r') as f:
        login = f.readlines()
    return mintapi.get_accounts(str(login[0].strip()),str(login[1].strip()))

json_key = json.load(open('googlekey.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)

gc = gspread.authorize(credentials)
sh = gc.open("spreadsheet name")

wks = sh.get_worksheet(1)
print wks
#cell_list = wks.range("A1:C8")

#mint
#https://github.com/mcronce/mintapi
#mainline doesnt work, needs to merge changes, 
#Don't pip install, just copy mintapi directory from this project

#mintaccount = login(1)
#for i in mintaccount.get_transactions()['date']:
    #print i

mintaccount = login(1)
accounts = mintaccount.get_accounts()
tempCitiSpark = 0
for i in accounts:
    if int(i["accountStatus"]) == 1:
        if i["accountName"] == "Checking":
            wks.update_acell("D6", "$"+str(i["currentBalance"]))
        elif i["accountName"] == "Chase":
            wks.update_acell("D8", "$"+str(i["currentBalance"]))
        #...
                
        outputPrint(i["accountName"],i["currentBalance"],i["fiLastUpdatedInDate"])
wks.update_acell("D11","$"+str(tempCitiSpark))

print 
mintaccount = login(2)
accounts = mintaccount.get_accounts() 

wks = sh.get_worksheet(3)
print wks
for i in accounts:
    if int(i["accountStatus"]) == 1:
        if i["accountName"] == "Discover":
            wks.update_acell("D11", "$"+str(i["currentBalance"]))
        outputPrint(i["accountName"],i["currentBalance"],i["fiLastUpdatedInDate"])

    #....
    outputPrint(i["accountName"],i["currentBalance"],i["fiLastUpdatedInDate"])
wks.update_acell("D11","$"+str(tempCitiSpark))
