# Written by Riceblades11

import smtplib

# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login('<ursogay1029@gmail.com>', 'nzyxochshdilyvfs')

server.sendmail('<ursogay1029@gmail.com>',
                '<3142087405>@<mms.att.net>', '<hi>')
