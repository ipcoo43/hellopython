import re

print('re.findall()')
line = 'Beautiful is better than ugly.' # 뽑아내고자하는 데이터

matches = re.findall('Beautiful', line) # 데이터에서 모든것을(findall) 찾고자 한다
print(matches)

matches2 = re.findall('beautiful', line, re.IGNORECASE) # 대소문자 구분 하지 말라
print(matches2)

zen2 = '''
Although never is often ideaXXX better than * right * now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# re.MULTILINE : 한 문장씩 단어를 찾는다.
print(re.findall('^If', zen2, re.MULTILINE))    # ^ : 시작을 나타냄
print(re.findall('idea\.', zen2, re.MULTILINE)) # \. : 점 자체를 찾음
print(re.findall('idea.', zen2, re.MULTILINE))  # . : 한 글자
print(re.findall('idea.$', zen2, re.MULTILINE)) # $ : 끝을 나타냄

str1 = 'Two aa too'
print(re.findall('t[ow]o',str1,re.IGNORECASE)) # [] : 옵션 o,w중 하나만 와도 된다.
print(re.findall('t[^w]o',str1,re.IGNORECASE)) # [^] : []속의 ^은 not을 뜻함 t다음에 w가 없는 것

str2 = '123?45yy7890 hi 999 hello'
print(re.findall('\d{1,3}',str2))     # \d 숫자 중에서 {1,3} 한글자나 세글자
print(re.findall('[0-9]{1,2}',str2))  # [0-9] 0부터 9까지의 숫자 중에서 {1,2} 한글자나 두글자
print(re.findall('[1-5]{1,2}',str2))  # [1-5] 1에서 5까지의 숫자 중에서 {1,2} 한글자나 두글자