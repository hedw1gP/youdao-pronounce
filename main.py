#coding:utf-8
import urllib2
import json
word = raw_input("Type the world you want the pronunciation: ")
html = urllib2.urlopen(r'http://fanyi.youdao.com/openapi.do?keyfrom=WrongPronounce&key=602608676&type=data&doctype=json&version=1.1&q=%s'%word)
jsonfetch = json.loads(html.read())
print(jsonfetch)
print("us:"+jsonfetch['us-phonetic'])
# 然而现实很骨感……