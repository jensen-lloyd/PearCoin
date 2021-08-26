import hashlib
import networking
import json
from time import sleep


import datetime
from datetime import timezone
import time




#List of transactions that have been verified and are waiting to be added to block
pending_transactions = []

#Maximum amount of time (in minutes) that the oldest block will have to wait before being added to a block
max_transaction_time = 0.1

#Time oldest transaction has been waiting to be added to block
transaction_countdown = 0

#Mining difficulty
difficulty = 3

#Blockchain object/list
blockchain = []




#Function for easy hashing of any object or string
def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())




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
        #return


    #If everything at the end if fine:
    transaction['new_balances'] = new_balances
    # print(transaction = json.dumps(transaction, indent=4))
    transaction = json.dumps(transaction)


    pending_transactions.append(transaction)


    global transaction_countdown
    if transaction_countdown == 0:
        transaction_countdown = time.time()








class Block():

    def __init__(self):
        pass


    def create_and_mine(self, data=pending_transactions):

        self.block = {}
        self.block_data = {}
        self.transactions = {}
        self.block_hash = {}

        try:
            self.block_data['index'] = int((blockchain[-1])['index']) + 1
        except:
            self.block_data['index'] = 0

        try:
            self.block_data['previous_hash'] = (blockchain[-1])['hash']
        except:
            self.block_data['previous_hash'] = "0" * 64


        self.transactions = data


        self.block['block_data'] = self.block_data
        self.block['transactions'] = self.transactions

        self.block_hash['nonce'] = 0
        self.block_hash['hash'] = hash(str(self.block['block_data']) + str(self.block['transactions']))
        while self.block_hash['hash'][:difficulty] != difficulty * "0":
                
                self.block_hash['hash'] = hash(str(self.block['block_data']) + str(self.block['transactions']) + str(self.block_hash['nonce']))

                print("hash: " + self.block_hash['hash'])

                self.block_hash['nonce'] +=1
                print("nonce: " + str(self.block_hash['nonce']))



        self.block['hash'] = self.block_hash 

        return(json.dumps(self.block, indent=4))







'''All the code needed to run (just runs other functions in a loop;
taking in, validating and adding transactions from half_nodes or blocks from full_nodes)'''
def main():

    while 2+2 == 4:

        verify_transaction(networking.listen_half_node())
        sleep(10)


        if (transaction_countdown) + int(max_transaction_time * 60) <= time.time():
            #create block
            block = Block()

            print(Block().create_and_mine())

            #mine block


            #print block

            #add block to blockchain


        sleep(5)




#Apparently this is a good thing to do???
if __name__ == '__main__':
    main()