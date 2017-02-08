import codecs
import re
import urllib
from textblob import TextBlob

swapPointsList=[u"और",u"भी",u"था",u"थी",u"मे",u"स",u"पर",u"की",u"है",u"जो" ,u"कोई" ,u"तक",u"की"]
conjunctions=[u"और",u"लेकिन",u"मगर",u"पर",u"चाहे",u"या",u"तो",u"जबकि",u"एंव",u"इसलिए",u"या",u"फिर",u"नहीं",u"तो",u"जैसे",u"कि"]
auxVerb=[]
ChunkList=[]
ChunkListSecond=[]

def findChunks(tempLine,Pos,Pod):
    Chunks=["Determiner|Noun","Determiner|Adjective|Noun","Noun|Preposition","Verb|AuxVerb","Verb|Pronoun","Pronoun|Verb","Adverb|Verb",
            "Noun|Noun","Adverb|Noun","Adjective|Noun","Adjective|Noun|Verb","Pronoun|Adjective|Noun","Pronoun|Noun|Adjective","Adverb|Adverb|Verb"]


    chunkParts=tempLine.split(pod)
    for i in range((0,chunkParts[0].__len__())):
        if pos(i) in Chunks:
            ChunkList.append(chunkParts[i])
            #storePos=pos(i)

        else:
            if (pos(i)|pos(i+1)) in Chunks:
                ChunkList.append(chunkParts[i]+chunkParts[i+1])

            else:
                if (pos(i)|pos(i+1)|pos(i+2)) in chunks:
                    ChunkList.append(chunkParts[i]+chunkParts[i+1]+chunkParts[i+2])

    for j in range(pod,chunkParts[1].__len__()):
        if pos(j) in Chunks:
            ChunkListSecond.append(chunkParts[j])
        else:
            if (pos(j)|pos(j+1)):
                ChunkListSecond.append(chunkParts[j]+chunkParts[j+1])
            else:
                if(pos(j)+pos(j+1)+pos(j+2)) in Chunks:
                    ChunkListSecond.append(chunkParts[j]+chunkParts[j+1]+chunkParts[j+2])


def matchRhyme(word1,word2):
    #str1 = "tekst"
    #word1+="टेक्स्ट"
    str1 = u""
    str2 = u""

    word1 += u"टेक्स्ट"
    word2+= u"टेक्स्ट"

    str1 += " " + word1
    str2 += " " + word2

    hindi_blob1 = TextBlob(str1)
    hindi_blob2 = TextBlob(str2)

    transliteratedtxt1 = hindi_blob1.translate(from_lang="hi", to='en')
    transliteratedtxt1=transliteratedtxt1.substring[:-5]
    transliteratedtxt2 = hindi_blob2.translate(from_lang="hi", to='en')
    transliteratedtxt2= transliteratedtxt2.substring[:-5]

    word1Index= len(transliteratedtxt1)
    word2Index= len(transliteratedtxt2)

    if (word1Index>word2Index):
        shorterWord=word2Index
    else:
        shorterWord=word1Index
    ##Matcing last charater if they are same!!
    while(shorterWord>0):
        if (transliteratedtxt1[word1Index-1] == transliteratedtxt2[word2Index-1]):
            shorterWord=shorterWord-1


        #rhymeMeter=3;
        ##Matching if second Last character is any of the Matras!!
            if ( ((transliteratedtxt1[word1Index-2]=='a') and (transliteratedtxt2[word2Index-2]=='a')) or ((transliteratedtxt1[word1Index-2]=='e') and (transliteratedtxt2[word2Index-2]=='e'))or ((transliteratedtxt1[word1Index-2]=='o') and (transliteratedtxt2[word2Index-2]=='o')) or ((transliteratedtxt1[word1Index-2]=='i') and (transliteratedtxt2[word2Index-2]=='i')) or ((transliteratedtxt1[word1Index-2]=='u') and (transliteratedtxt2[word2Index-2]=='u')) ):
                maxScore=2/shorterWord
                shorterWord=shorterWord-1
                if ((transliteratedtxt1[word1Index - 3]) == (transliteratedtxt2[word2Index - 3])):
                    maxScore = 3 / shorterWord
                    shorterWord=shorterWord-1
                    if ((transliteratedtxt1[word1Index - 4]) == (transliteratedtxt2[word2Index - 4])):
                        maxScore=4/shorterWord
                        shorterWord=shorterWord-1
                        if ((transliteratedtxt1[word1Index - 5]) == (transliteratedtxt2[word2Index - 5])):
                            maxScore=5/shorterWord
                            shorterWord=shorterWord-1

                if(maxScore>=0.5):
                    rhymeMeter=5
                else:
                    rhymeMeter=4








            else:

                if(transliteratedtxt1[word1Index-2]!=transliteratedtxt1[word1Index-2]):
                    maxScore=1/shorterWord
                    shorterWord=shorterWord-1
                    if(transliteratedtxt1[word1Index-3]==transliteratedtxt2[word2Index-3]):
                        maxScore=2/shorterWord
                        shorterWord=shorterWord-1
                        if(transliteratedtxt1[word1Index-4]==transliteratedtxt2[word2Index-4]):
                            maxScore=3/shorterWord
                            shorterWord=shorterWord-1
                            if(transliteratedtxt1[word1Index-5]==transliteratedtxt2[word2Index-5]):
                                maxScore=4/shorterWord
                                shorterWord=shorterWord-1
                    if(maxScore>0.5):
                        rhymeMeter=3
                    else:
                        rhymeMeter=2

        else:
            rhymeMeter=1



    return rhymeMeter







def findPos():
    







with open("readHindi.txt","r")as f:
    for line in f:
        words=line.split()
        for word in words:
            pos=findPos(word)
        pod=findDel(line)
        chunks=findChunks(line,pos,pod)





