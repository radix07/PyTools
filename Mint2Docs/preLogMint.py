import mintapi

#mint only, used to kick mint to update all accounts

#https://github.com/mcronce/mintapi
#mainline doesnt work, needs to merge changes, 
#Don't pip install, just copy mintapi directory from this project

def outputPrint(n,b,l):
    print "{0:<50} -  {1:<20} -  {2:<30}".format(n,b,str(l))

def getMintAccount(i):
    with open("login"+str(i)+".txt",'r') as f:
        login = f.readlines()
    return mintapi.get_accounts(str(login[0].strip()),str(login[1].strip()))

accounts = getMintAccount(1) 

for i in accounts:
    outputPrint( i["accountName"],i["currentBalance"],i["fiLastUpdatedInDate"])

print 
accounts = getMintAccount(2) 

for i in accounts:
    outputPrint( i["accountName"],i["currentBalance"],i["fiLastUpdatedInDate"])
    #print i

