import imapclient

# server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# server.login('joakimfkk@gmail.com', 'vuvc bvzf ocev ywgo')

# select_info = server.select_folder('INBOX')
# print(f"{select_info[b'EXISTS']} messages in inbox.") # 14 messages in inbox. [TRUE FOR THE MOMENT] 

# print()

# server.logout()
def retrieving_mails():
    import email
    from imapclient import IMAPClient

    host = 'imap.gmail.com'
    username = 'joakimfkk@gmail.com'
    password = 'vuvc bvzf ocev ywgo'

    with IMAPClient(host) as server:
        server.login(username, password)
        server.select_folder('INBOX', readonly=True)

        messages = server.search('UNSEEN')
        for uid, message_data in server.fetch(messages, 'RFC822').items():
            email_message = email.message_from_bytes(message_data[b'RFC822'])
            print(f"{uid} - {email_message.get('From')} - {email_message.get('Subject')}")

def using_pyzmail_and_imapclient():
    import email
    from imapclient import IMAPClient
    import pyzmail

    host = 'imap.gmail.com'
    username = 'joakimfkk@gmail.com'
    password = 'vuvc bvzf ocev ywgo'

    with IMAPClient(host) as server:
        server.login(username, password)
        server.select_folder('INBOX', readonly=True)
        messages = server.search('UNSEEN')
        uid_list = []
        for uid, message_data in server.fetch(messages, 'RFC822').items():
            uid_list.append(uid)
        
        message = pyzmail.PyzMessage.factory()




using_pyzmail_and_imapclient()