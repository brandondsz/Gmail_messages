import imaplib
import email

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
		
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('', '')
mail.list()
mail.select("[Gmail]/Sent Mail")

result, data = mail.search(None, 'all')
 
ids = data[0]
id_list = ids.split() 
 
for i in range(len(id_list)):
	result, data = mail.fetch(id_list[i], "(RFC822)")
 
	raw_email = data[0][1]


	email_message = email.message_from_string(raw_email)
 
	print email_message['To']
 
	print email.utils.parseaddr(email_message['From']) 
 
	print get_first_text_block(email_message)
	
