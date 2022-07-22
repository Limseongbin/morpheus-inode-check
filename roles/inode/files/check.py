#!/usr/bin/python3

import sys
import os.path
import urllib3
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

inventoryHostname = sys.argv[1]
logFile = '/tmp/inode_check/'+inventoryHostname+'.log'

if os.path.isfile(logFile):
   with open(logFile) as f:
      lines = [line.strip() for line in f.readlines()]
      
   if len(lines) > 0:
      content = '<h2>'+inventoryHostname+' Server i-node Warning</h2>'
      content += '<table>'
      content += '<tr><th style="border-bottom: 1px black solid;width: 200px;">Filesystem</th><th style="border-bottom: 1px black solid;width: 200px;">Mount on</th><th style="border-bottom: 1px black solid;width: 200px;">Usage</th></tr>'
      
      for line in lines:
         filesystem, mount, percent = line.split(sep=',') 
         content += '<tr><td style="border-bottom: 1px black solid;text-align: center;">' + filesystem + '</td><td style="border-bottom: 1px black solid;text-align: center">' + mount + '</td><td style="border-bottom: 1px black solid;text-align: center">' + percent +'%</td></tr>'
      content += '</table>'
      
      smtp = smtplib.SMTP('smtp.naver.com', 587)
      smtp.starttls()
      smtp.login('lim900309', '442SJG91YJLS')
      
      msg = MIMEMultipart('Multipart')
      msg['From'] = "morpheus alert<lim900309@naver.com>"
      msg['Subject'] = 'Morpheus - '+inventoryHostname+' Server i-node Warning !'
      msg['To'] = "lim900309@gmail.com"
      part = MIMEText(content, 'html') 
      msg.attach(part)
      
      smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
   
      smtp.quit()
      
   print(str(len(lines))+'EA Filesystem i-node Warning')
