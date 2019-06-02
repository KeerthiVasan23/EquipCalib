import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import datetime

MY_ADDRESS = 'ksb.valves.notification@gmail.com'
PASSWORD = 'ksbisgreat'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def mail(itemno,serialno,equipment,rangee,lc):
    names, emails = get_contacts('contacts.txt') # read contacts

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = "Equipment needs to be caliberated\nItem number:"+str(itemno)+"\nEquipment name:"+equipment +"\nSerial no.:"+serialno+"\nRange:"+rangee+"\nLeast Count:"+lc

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Equipment Caliberation"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()

def main():
    conn=sqlite3.connect('equipment.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM equipment')
    dbdata=cur.fetchall()
    rows=len(dbdata)
    i=0
    now=str(datetime.date.today())
    while i<rows:
        if(now==dbdata[i][6]):
            mail(dbdata[i][1],dbdata[i][2],dbdata[i][3],dbdata[i][4],dbdata[i][5])
        i+=1 

if __name__ == '__main__':
    main()
