# Welcome!

### This project Was Created For A Couple of Reasons 
    1. I need to delete thousands of unread emails from over the years
    2. In order to test my methods, I also needed a way to send a ton of mass emails

This project accomplished just that.

## How to use program
Overall Instructions:
1. Determine if you want to send or delete emails, files are named appropriately
2. Next, this project only works if you have an "App Password" setup with Google
    * You can set one up at https://myaccount.google.com/security
    * If that still doesn't make sense here is another link with instrucitons: https://support.google.com/mail/answer/185833?hl=en-GB
    * Make sure to select "Mail" when generating this password with Google
    * Save this password once it is created!
3. In these programs, wherever you see 'password' don't use your normal Google password, instead use the app password you just created

## Instructions For Sending Emails
1. There are three variables that need to be filled in the main function, they should be named:
    * email
    * password
    * to
2. Fill the 'email' variable with the email address of the account you want to login to
    * This will also be the email address that all messages are sent from
3. Fill in the 'password' variable with the password of that account
    * Remember to use the app password you should have created above instead of the Google account password
4. Finally, the 'to' variable is the email address that will be receiving these emails. Use whoevers email you would like 

5. Next, change the number in the loop on line 18 to your own liking. 
    * This will change the number of emails sent. By default it is 20

4. Next run the program with the following command
    * python3 sendEmails.py

## Instructions For Deleting Emails
1. There are three variables that need to be filled in the program, they should be named:
    * email
    * password
    * searchCriteria
2. Fill the 'email' variable with the email address of the account you want to login to
    * This will also be the email address that all messages are deleted from
3. Fill in the 'password' variable with the password of that account
    * Remember to use the app password you should have created above instead of the Google account password
4. Next, fill in the 'searchCriteria' varaible in the mainMenu function
    * This is the criteria the program will use to delete emails. Anything that matches that criteria will be deleted.
    * Here is a website the lists all the different keywords the cirteria could use:
        * https://gist.github.com/martinrusev/6121028
    * By default, this program will delete any emails from the: 'no-reply@accounts.google.com' account

* Here is another example of filters for the criteria: https://www.thepythoncode.com/article/deleting-emails-in-python