#!/usr/bin/python

__description__ = 'Get the MDL list and put it in a parsable list'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2010/11/26'

import optparse
import urllib
import simplejson
import random
import os

global mdl
mdl = "http://www.malwaredomainlist.com/hostslist/hosts.txt"

def get_list():
	print "== Downloading MDL =="
	os.system('wget -t 1 -P /tmp ' + mdl)
	print "== Downloaded List =="
	
def parse_list(filename):
	print "== Parsing File =="
	urls = []
	fd = file(filename,'r')
	lines = fd.readlines()
	for line in lines:
		data = line.split('  ')
		urls.append(data[1].strip())
	fd.close()
	return urls
	print "== File Parsed =="
	
def write_list(filename, parsed):
	print "== Writing List =="
	fd = file(filename, 'w')
	for url in parsed:
		fd.write(url + '\n')
	fd.close()
	print "== List Written =="
	
#do work
#get_list()
parsed = parse_list('/tmp/hosts.txt')
write_list('/root/host_clean.txt',parsed)