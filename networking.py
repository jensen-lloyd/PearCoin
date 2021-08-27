import sockets


#Only here for testing, will remove later
import hashlib
import json


host = []
port = "1234"





#Function for easy hashing of any object or string
def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())






#Listens to all traffic
def listen():
    pass



#send through all transmissions that are coming from half_nodes (only send one at a time, and remove from queue when forwarded to main program)
def listen_half_node():

    transaction_details = {}
    transaction_signature = {}
    transaction = {}

    transaction_details['sender'] = 'sender'
    transaction_details['receiver'] = 'receiver'
    transaction_details['amount'] = 1
    transaction_signature['signature'] = hash(transaction_details)

    transaction['transaction'] = transaction_details
    transaction['signature'] = transaction_signature

    return(transaction)




#send through all transmissions that are coming from full_nodes (only send one at a time, and remove from queue when forwarded to main program)
def listen_full_node():
    pass



#send out a transmission to all known full_nodes
def send_network():
    pass