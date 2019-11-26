import imapclient

server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
server.login('joakimfkk@gmail.com', 'vuvc bvzf ocev ywgo')

select_info = server.select_folder('INBOX')
print(f"{select_info[b'EXISTS']} messages in inbox.") # 14 messages in inbox. [TRUE FOR THE MOMENT] 

print()

server.logout()