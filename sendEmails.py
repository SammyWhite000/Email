import smtplib
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' Lockheed']
numbers = ['1','2','3','4','5','6','7','8','9','0']
subjects = ['one', 'two', 'three', 'four', 'five', 'six']
# Make body of the paragraph
def randMessage():
    returnMessage = ''
    for x in range(50):
        returnMessage += random.choice(numbers)
        for x in range(7):
            returnMessage += random.choice(alphabet)
    return 'Subject: {}\n\n{}'.format(random.choice(subjects), returnMessage) 

def main():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('whitesammyt@gmail.com', '')
    count = 0
    for x in range(20):
        count +=1
        print(count)
        message = randMessage()
        s.sendmail("whitesammyt@gmail.com", "whitesammyt@gmail.com", message)
    s.quit()

main()