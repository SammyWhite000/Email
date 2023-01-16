import imaplib
import threading

# input the exact emails you want to be removed from your inbox in the set
emailsToBeRemoved = {} # All Emails put into this set will be completely removed from your inbox

def startThreads():

    whoFrom = 'ALL'
    # creating thread
    arg = emailsToBeRemoved.pop()
    t1 = threading.Thread(target=delEmail, args=(arg,))

    arg1 = emailsToBeRemoved.pop()
    t2 = threading.Thread(target=delEmail, args=(arg1,))

    arg2 = emailsToBeRemoved.pop()
    t3 = threading.Thread(target=delEmail, args=(arg2,))

    arg3 = emailsToBeRemoved.pop()
    t4 = threading.Thread(target=delEmail, args=(arg3,))
    t5 = threading.Thread(target=delEmail, args=(arg3,))
    t6 = threading.Thread(target=delEmail, args=(arg3,))

    t1.start()
    t2.start()
    t3.start()
    t4.start() 
    t5.start() 
    t6.start() 

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

def delEmail(who):
    inbox = imaplib.IMAP4_SSL('imap.gmail.com')

    #inbox.login('whitesammyt@gmail.com', '')
    inbox.login('sammytwhite9@gmail.com', '')
    inbox.select("Inbox")
    #whoFrom = 'NOT BODY "Lockheed"'
    whoFrom = 'BEFORE "29-NOV-2022"'
    
    typ, data = inbox.search(None, whoFrom)
    for x in data[0].split():
        inbox.store(x, '+FLAGS', '\\Deleted')
    print("Done")
    inbox.expunge()
    inbox.close()
    inbox.logout()

def main():
    mainMenu()

main()