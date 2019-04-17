import re

str1 = '123?45yy7890 hi 999 heLLo'

pattern = re.compile('(\d{1,2})') # compile은 기계어로 변환하겠다. 많이 사용 할 경우 속도가 빠름

print(re.findall(pattern,str1)) # findall 모든 것, findone 하나를 찾음
print(re.findall('[A-z]',str1)) # [A-z] 알파벳 대문자 부터 소문자까지 전체 찾기

for i in re.finditer(pattern,str1): # finditer은 루프를 돌면서 찾음, 튜플 형태
	print(i.groups())