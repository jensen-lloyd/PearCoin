import hashlib
import networking
import time
from time import sleep




#Maximum amount of time (in minutes) that the oldest block will have to wait before being added to a block
max_transaction_time = 0.1

#Mining difficulty
difficulty = 1



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
DO NOT CHANGE THESE VARIABLES!!!
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#Time oldest transaction has been waiting to be added to block
#(starts at 0, and a Unix-time replaces it once a transaction is added)
transaction_countdown = 0

#List of transactions that have been verified and are waiting to be added to block
pending_transactions = []

#Blockchain object/list
blockchain = []

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


genesis = {'block_data': {'index': 0,
                                  'previous_hash': "0"*64
                                 }, 
                   'transactions': {"This is the genesis block of PearCoin! This currency has a fixed value of 1 (one) Australian Dollar; no more, and no less."
                                 }, 
                   'block_hash': {'nonce': "",
                                  'hash': "0fcc64eda3ca6a55fd06fb0676540e68af26da8f553afeb9e6acc7392ac85de5"
                                }}


blockchain.append(genesis)



#Function for easy hashing of any object or string
def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())




'''Check that the fields are filled, sender has sufficient funds, 
sender's signature is correct, a suitable fee is attached'''
def verify_transaction(transaction):
    
    # transaction = json.loads(transaction)
    

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


        self.block_data['index'] = int(blockchain[-1]['block_data']['index']) + 1
        self.block_data['previous_hash'] = blockchain[-1]['block_hash']


        self.transactions = data


        self.block['block_data'] = self.block_data
        self.block['transactions'] = self.transactions

        self.block_hash['nonce'] = 0
        self.block_hash['hash'] = hash(str(self.block['block_data']) + str(self.block['transactions']))
        while self.block_hash['hash'][:difficulty] != difficulty * "0":
                
                self.block_hash['hash'] = hash(str(self.block['block_data']) 
                                            + str(self.block['transactions']) 
                                            + str(self.block_hash['nonce']))

                # print("nonce: " + str(self.block_hash['nonce']) + (20 * " ") + "hash: " + self.block_hash['hash'], end='\r')

                self.block_hash['nonce'] +=1



        self.block['hash'] = self.block_hash 

        # return(json.dumps(self.block, indent=4))
        return(self.block)






'''All the code needed to run (just runs other functions in a loop;
taking in, validating and adding transactions from half_nodes or blocks from full_nodes)'''
def main():

    while 2+2 == 4:

        verify_transaction(networking.listen_half_node())
        

        sleep(5)


        if (transaction_countdown) + int(max_transaction_time * 60) <= time.time():
            #create block object
            block = Block()

            #Fill block object with data and calculate hash
            # block.create_and_mine()

            #add block to blockchain and delete block
            blockchain.append(block.create_and_mine())

            del block

            # print((blockchain[0])['block_data'])
            print(str(blockchain[-1]) + "\n\n\n\n\n")
            print(blockchain[0]['block_hash']['hash'])


        sleep(1)




#Apparently this is a good thing to do???
if __name__ == '__main__':
    main()