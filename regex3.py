import re

str1 = 'aaaaaaa<hr>This</hr><html>'   
  # 내가 찾고자하는 것이 <로 시작하고 >로 끝남
  # ()는 찾고자하는 것을 묶어서 찾겠다
  # ()인 부분만 나에게 주세요
  # . 한글자
  # * 없어도 되고 있어도 됨
  # .* 아무 문자나 n개가 와라
  # + 하나는 최소한 있어야 함
pattern1 = re.compile('<(.*)>') # ()를 <()> 안에 싼 경우
pattern2 = re.compile('(<.*>)') # ()를 (<>) 밖에 싼 경우
pattern3 = re.compile('<\/(.*)>') # \/  </를 사용하겠다
pattern4 = re.compile('<(.{1,2})>') # 2글자만 찾음

print(re.findall(pattern1,str1))
print(re.findall(pattern2,str1))
print(re.findall(pattern3,str1))
print(re.findall(pattern4,str1))

for i in re.finditer(pattern1, str1):
	print(i.groups(1))