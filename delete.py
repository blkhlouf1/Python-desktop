import imaplib
imaplib._MAXLINE = 400000000
box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
box.login("mohamedfianng5689@gmail.com","2F1t2y5G4h")
box.select('Inbox')
typ, data = box.search(None, '(SINCE "01-OCT-2021" BEFORE "01-NOV-2021")')
for num in data[0].split():
   box.store(num, '+FLAGS', '\\Deleted')
box.expunge()
box.close()
box.logout()