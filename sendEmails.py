import smtplib
import random

possibleCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                    'r','s','t','u','v','w','x','y','z',' ', '1','2','3','4','5','6','7','8','9','0']
possibleSubjects = ['one', 'two', 'three', 'four', 'five', 'six']

def main():
    email = ''             # Email address from where mail will be sent from
    password = ''                               # Email password where mail will be sent from
    to = ''                # Who the generated email will be sent to
    sendMessage(email, password, to)

def sendMessage(email, password, receiver):
    s = smtplib.SMTP('smtp.gmail.com', 587)     # This changes based on provider, but this is how to do it with gmail
    s.starttls()
    s.login(email,password)                     # Login to senders email 
    for x in range(20):                         # Number of Emails to send
        message = randMessage()                 # Generate random body paragraph with subject
        s.sendmail(email, receiver, message)    # Send the mail
    s.quit()

# Generate Random Body Paragraph With Random Subject
def randMessage():
    returnMessage = ''
    subject =random.choice(possibleSubjects)    # Chose random subject 
    for x in range(700):                        # Number of characters in message body 
        returnMessage += random.choice(possibleCharacters)  # Add each random character to string
    return 'Subject: {}\n\n{}'.format(subject , returnMessage)  # Return Message with Subect

main()