#!/usr/bin/python

__description__ = 'Grab files from Google of a certain file type'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2010/11/26'

import optparse
import urllib
import simplejson
import random
import os
import time

def grab_files(urls):
    print "== Downloading Files =="
    for url in urls:
        os.system('wget -t 3 -P /root/dirtyhands/files/ ' + url)
    print "== Files Downloaded =="

def get_urls(file_type="pdf", host_list="null", dump=False):
    print "== Making Queries =="
    count = 0
    hit_count = 0
    url_list = []
    if host_list == "null":
    	print "Specify a valid file!"
    fd = file(host_list,'r')
    hosts = fd.readlines()
    if dump == True:
        log = open('/root/dirtyhands/logs/' + str(time.time()), 'a')
    for host in hosts:
        #construct the query
        query = urllib.urlencode({'q' : 'site:%s filetype:%s' % (host, file_type)})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&%s' % (query)
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        results = json['responseData']['results']
        for i in results:
            url_list.append(i['url'])
            count+=1
            hit_count+=1

        print "== Analyzed == %s : %d" % (host.strip(), hit_count)
        if dump == True:
            log.write("%s : %d\n" % (host.strip(), hit_count))

        hit_count = 0
        #time.sleep(5)
    fd.close()
    log.close()
    return url_list
    
def main():
    oParser = optparse.OptionParser(usage='usage: %prog [options]\n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-t', '--type', type='string', help='filetype to download')
    oParser.add_option('-l', '--list', default='null', type='string', help='file of hosts')
    oParser.add_option('-d', '--dump', action='store_true', default=False, help='log to a file')
    #oParser.add_option('-s', '--scan', action='store_true', default=False, help='scan downloaded files')
    (options, args) = oParser.parse_args()

    if options.type:
        urls = get_urls(options.type, options.list, options.dump)
        grab_files(urls)
    else:
        oParser.print_help()
        return

if __name__ == '__main__':
    main()
