import imaplib
import threading

# input the exact emails you want to be removed from your inbox in the set
emailsToBeRemoved = {} # All Emails put into this set will be completely removed from your inbox
# To use this set, look at 'Version Two' of the deleteEmails section in the README

def main():
    print("Welcome to email Deleter!")
    email = ''
    password = ''
    mainMenu(email, password)

def mainMenu(email, password):
    # ********************* Change this Variable *********************************
    searchCriteria = 'FROM "no-reply@accounts.google.com"' # Look at README for more search criterias
    # ****************************************************************************
    threadTuple =''
    if searchCriteria == '888':
        threadTuple = createThreadsSet(email, password)
    else:
        threadTuple = createThreads(email,password, searchCriteria)
    startThreads(threadTuple)

# creating threads then return a tuple of them
def createThreads(email, password, searchCriteria):

    t1 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t2 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t3 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t4 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t5 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t6 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))

    return (t1,t2,t3,t4,t5,t6) 

def createThreadsSet(email, password):
# NEED TO UPDATE
    t1 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t2 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t3 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t4 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t5 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))
    t6 = threading.Thread(target=markEmails, args=(email, password, searchCriteria,))

    return (t1,t2,t3,t4,t5,t6)

def startThreads(threads):
    # Start each thread then wait for each thread to be finished executing
    threads[0].start()
    threads[1].start()
    threads[2].start()
    threads[3].start()
    threads[4].start()
    threads[5].start()

    threads[0].join()
    threads[1].join()
    threads[2].join()
    threads[3].join()
    threads[4].join()
    threads[5].join()

# Go through inbox, mark each email that meets searchCriteria, then delete all marked emails
def markEmails(email, password, searchCriteria):
    inbox = imaplib.IMAP4_SSL('imap.gmail.com')
    inbox.login(email, password) 
    inbox.select("Inbox")
    typ, data = inbox.search(None, searchCriteria)
    for x in data[0].split():
        inbox.store(x, '+FLAGS', '\\Deleted')
    inbox.expunge()
    inbox.close()
    inbox.logout()

main()