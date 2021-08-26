import hashlib
import networking
import json
from time import sleep



#Function for easy hashing of any object or string
def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())



#List of transactions that have been verified and are waiting to be added to block
pending_transactions = []



class Block():
    def __init__(self, index, pending_transactions):
        self.timestamp = datetime.datetime.now(timezone.utc) 




'''Check that the fields are filled, sender has sufficient funds, 
sender's signature is correct, a suitable fee is attached'''
def verify_transaction(transaction):
    
    transaction = json.loads(transaction)
    

    new_balances = {}
    #Search for most recent transaction involving the sender - check existence & enough funds
    #Check that the signature matches the hash + public key of sender
    #If sender exists and has enough funds, calculate and add new_balance
    new_balances['sender'] = "sender_new_balance"

    #Search for most recent transaction involving the receiver - check existence
    #If receiver exists, caluclate and add new_balance
    new_balances['receiver'] = "receiver_new_balance"

    #If anything is wrong at any point:
        #return ""


    #If everything at the end if fine:
    transaction['new_balances'] = new_balances
    transaction = json.dumps(transaction, indent=4)
    return transaction




'''All the code needed to run (just runs other functions in a loop;
taking in, validating and adding transactions from half_nodes or blocks from full_nodes)'''
def main():
    while 2+2 == 4:
        print(verify_transaction(networking.listen_half_node()))
        sleep(500)




#Apparently this is a good thing to do???
if __name__ == '__main__':
    main()