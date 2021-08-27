'''import tkinter
from tkinter import messagebox'''
import json
import hashlib

'''
#Current balance is for demonstration purposes
currentBalance = 0

def makeTransaction():
    fetchedReciever = recieverEntry.get()
    fetchedAmount = amountEntry.get()
    if int(fetchedAmount) <= currentBalance:
        messagebox.showinfo("TRANSACTION SUCCESSFUL", 
            "Transaction made to",
            fetchedReciever,
            "of amount "+str(fetchedAmount))
    else:
        messagebox.showinfo("TRANSACTION FAILED", 
            "The user has attempted to transact an amount more than they have!")

    output1 = tkinter.Label(root, text="The intended reciever is: "+ fetchedReciever)
    canvas.create_window(200, 230, window = output1)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 500, height = 400)
canvas.pack()
#Creating entry boxes
recieverEntry = tkinter.Entry(root)
amountEntry = tkinter.Entry(root)
#Creating labels
title = tkinter.Label(root, text="Enter the desired reciever and transaction amount below")
transactionLabel = tkinter.Label(root, text="Transaction reciever: ")
currentBalanceLabel = tkinter.Label(root, text="Balance: "+str(currentBalance))
transactionAmountLabel =  tkinter.Label(root, text="Transaction Amount: ")
title.pack()
#Creating buttons
createTransButt = tkinter.Button(root, text="Create Transaction", command=makeTransaction)

#Positioning the labels and entry boxes and button
canvas.create_window(200, 50, window = recieverEntry)
canvas.create_window(180, 25, window = title)
canvas.create_window(80, 50, window = transactionLabel)
canvas.create_window(80, 100, window = transactionAmountLabel)
canvas.create_window(200, 100, window = amountEntry)
canvas.create_window(80, 150, window = createTransButt)
canvas.create_window(400, 25, window = currentBalanceLabel)


#Transaction gui
root.mainloop()




'''

#Function for easy hashing of any object or string
def hash(*args):
    hash = ""
    for arg in args:
        hash += str(arg)

    return str(hashlib.sha256(hash.encode('utf-8')).hexdigest())



def create_transaction(sender, receiver, amount):

    transaction_details = {}
    transaction_signature = {}
    transaction = {}

    transaction_details['sender'] = 'sender'
    transaction_details['receiver'] = 'receiver'
    transaction_details['amount'] = 1
    transaction_details['sender_new_balance'] = 'sender_new_balance'
    transaction_details['receiver_new_balance'] = 'receiver_new_balance'
    
    transaction_signature['signature'] = hash(transaction_details)

    transaction['transaction'] = transaction_details
    transaction['signature'] = transaction_signature

    return(json.dumps(transaction, indent=4))

print(create_transaction('sender', 'receiver', 1))