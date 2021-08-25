import hashlib
import networking



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


#Check that the fields are filled, sender has sufficient funds, a suitable fee is attached
def verify_transaction(transaction):
    pass



'''All the code needed to run (just runs other functions in a loop;
taking in, validating and adding transactions from half_nodes or blocks from full_nodes)'''
def main():
    while 2+2 == 4:
        verify_transaction(networking.listen_half_node())




#Apparently this is a good thing to do???
if __name__ == '__main__':
    main()