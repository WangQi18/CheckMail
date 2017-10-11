#!/usr/bin/env python
# -*- coding: utf-8 -*-
#test for  tread

import poplib,time,os
from email import parser

username = 'xxxxx'
password = 'xxxxx'

def mail_get():
	pop_conn = poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user(username)
	pop_conn.pass_(password)
	#Get messages from server:
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	# Concat message pieces:
	messages = ["\n".join(mssg[1]) for mssg in messages]
	#Parse message intom an email object:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	#print messages
	for message in messages:
	    print message['subject']
	    title = message['subject']
	pop_conn.quit()
