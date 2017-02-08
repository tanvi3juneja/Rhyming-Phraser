# coding: utf-8
from bs4 import BeautifulSoup
import codecs
import re
import urllib
from collections import defaultdict

finallist={}
file1=codecs.open("C:/Users/Akanksha/Desktop/output.txt",'w')

with codecs.open("C:/Users/Akanksha/Desktop/hindicleaneddata.txt", 'r', 'utf8') as f:
    for line in f:
        tempV = line.split(" ")[0].encode('utf-8')
        r = urllib.urlopen('http://dict.hinkhoj.com/hindi-dictionary.php?word=' + tempV + '&ie=UTF-8').read()
        soup = BeautifulSoup(r)
        lettersx = soup.find_all("a", {'class': "hin_dict_span"})
        keyslist = []
        for elements in lettersx:
            # print "text:"+elements.text
            keyslist.append(elements.text)

        valuesList = []
        letters = soup.find_all("span", class_="gram_dict_span")
        for elements in letters:
            # print "POS:"+elements.text
            valuesList.append(elements.text.encode('utf-8'))

        cat={}
        for i in range(0,len(keyslist)):
            for j in range(0,valuesList.__len__()):
                cat[keyslist[i],valuesList[j]]=cat.get((keyslist[i],valuesList[j]),0)+1
            #cat[keyslist[i]].append(valuesList[i])

        for key, val in cat.items():
            file1.write(key[0].encode('utf-8')+ ':' + key[1].encode('utf-8')+ ';')
            file1.write("\n")

        file1.write("***********")
        file1.write("\n")

        # m=re.search("\<h2 class\=\"top0\"\>(.*)\<\/h2\>",letters[0])
        # print m.group(1)'''''