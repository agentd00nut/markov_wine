
 
import urllib2
from lxml.html import fromstring
import sys
import time
 
urlprefix = "http://www.winespectator.com/dailypicks/category/catid/1/page/"
 
#709
for page in xrange(1, 710):
    try:
        out = "-> On page {} of {}....      {}%"
        print >> sys.stderr, out.format(page, "709", str(round(float(page)/709*100, 2)))
        response = urllib2.urlopen(urlprefix + str(page))
        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "daily-wine-items", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "paragraph", " " ))]')
        for review in sels:
            if review.text:
                print review.text.strip()
        sys.stdout.flush()
        
    except:
        continue
        