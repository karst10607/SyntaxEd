# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql.cursors
import en
    
connection = pymysql.connect(host='localhost',
                             user='sunya',
                             password='123456',
                             db='syntaxed')

def getWords():
    with connection.cursor() as cursor:
        #cursor.execute('SELECT string FROM verb')
        cursor.execute('SELECT string FROM noun')
        return cursor.fetchall()
        #for result in resList:
            #print result[0]

def updateVerb(resList):
    for result in resList:
        word = result[0]
        progress = en.verb.present_participle(word)
        past = en.verb.past(word)
        ppt = en.verb.past_participle(word)
        #print word + ' ' + progress + ' ' + past + ' ' + ppt
        sql = "UPDATE verb SET progressive='"+progress+"', pt='"+past+"', ppt='"+ppt+"' WHERE string='"+word+"'"
        try:
            with connection.cursor() as cursor:
                print sql
                cursor.execute(sql)
                connection.commit()
        except:
            print 'error'
    
def updateNoun(resList):
    for result in resList:
        word = result[0]
        plural = en.noun.plural(word)
        sql = "UPDATE noun SET plural='"+plural+"' WHERE string='"+word+"'"
        try:
            with connection.cursor() as cursor:
                print sql
                cursor.execute(sql)
                connection.commit()
        except:
            print 'error'

if __name__ == '__main__':
    resList = getWords()
    #updateVerb(resList)
    updateNoun(resList)