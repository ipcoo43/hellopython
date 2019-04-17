import re

zen = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print(re.findall(' is better than', zen)) # is better than 만 출력
print(re.findall('.* is better than .*', zen)) # .* is better than .* 문장까지 출력
print(re.findall('(.*) is better than .*', zen)) # (.*) is better than .* 찾고자하는 앞 단어 출력
print(re.findall('(.*) is better than (.*)', zen)) # (.*) is better than (.*) 찾고자하는 앞 단어 뒷 단어 출력

# \.로 마침표 제거
pattern = re.findall('(.*) is.* better than (.*)\.', zen) 
for i in pattern:
	print('{} > {}'.format(i[0].lower(), i[1]))