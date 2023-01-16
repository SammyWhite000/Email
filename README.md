# Welcome!

### This project Was Created For A Couple of Reasons 
    1. I need to delete thousands of unread emails from over the years
    2. In order to test my methods, I also needed a way to send a ton of mass emails

This project accomplished just that.

## How to use program
Overall Instructions:
1. Find if you want to send or delete emails, files are named appropriately
2. Next, this project only works if you have an "App Password" setup with Google
    * You can set one up at https://myaccount.google.com/security
    * If that still doesn't make sense here is another link with instrucitons: https://support.google.com/mail/answer/185833?hl=en-GB
    * Save this password once it is created!
3. In these programs, wherever you see 'password' don't use your normal Google password, instead use the app password you just created

Instructions For Sending Emails
1. There are three variables that need to be filled in the main function, they should be named:
    * email
    * password
    * to
2. Fill the 'email' variable with the email address of the account you want to login
    * This will also be the email address that all messages are sent from
3. Fill in the 'password' variable with the password of that account
    * Rememebr to use the app password you should have created above instead of the Google account password
4. Finally, the 'to' variable is the email address that will be receiving these emails. Use whoevers email you would like 

4. Next run the program with the following command
    * python3 sendEmails.py
