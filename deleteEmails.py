import imaplib
import threading

set = {'info@seekdiscomfort.com', 'venmo@venmo.com', 'oldnavy@email.oldnavy.com', '1800usbanks@notifications.usbank.com', 
'security@mail.instagram.com', 'noreply@steampowered.com', 
'TurboTax@em1.turbotax.intuit.com', 'no-reply@accounts.google.com', 'BestBuy@email.bestbuy.com', 'learn@itr.mail.codecademy.com', 'jobalerts-noreply@linkedin.com', 
'notifications@github.com', 'vailresorts@express.medallia.com', 'whitesammyt@gmail.com'}

def delEmail(who):
    inbox = imaplib.IMAP4_SSL('imap.gmail.com')

    #inbox.login('whitesammyt@gmail.com', '')
    inbox.login('sammytwhite9@gmail.com', '')
    inbox.select("Inbox")
    #whoFrom = 'NOT BODY "Lockheed"'
    whoFrom = 'BEFORE "29-NOV-2022"'
    #whoFrom = 'ALL'
    typ, data = inbox.search(None, whoFrom)
    for x in data[0].split():
        inbox.store(x, '+FLAGS', '\\Deleted')
    print("Done")
    inbox.expunge()
    inbox.close()
    inbox.logout()

def main():

    # creating thread
    arg = set.pop()
    t1 = threading.Thread(target=delEmail, args=(arg,))

    arg1 = set.pop()
    t2 = threading.Thread(target=delEmail, args=(arg1,))

    arg2 = set.pop()
    t3 = threading.Thread(target=delEmail, args=(arg2,))

    arg3 = set.pop()
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

main()