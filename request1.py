import requests

# 로그인이 필요 없는 페이지
# timeout=(커넥션하는데 5, 처리하는데 14) : 19초를 기다림
# 사용자가 기다리는초 7초
r = requests.get('http://google.com', timeout=(5,14))
r.text  # html이 들어 있음
r.status_code # 상태 확인

# 로그인이 필요한 페이지
# 로그인 정보 : cookie
custom_cookie = {'cookie_name': 'cookie_value'}
r = requests.get('http://example.com/cookies', cookies=custom_cookie)

# 막아놓은 모바일을 강제로 바꿈
custom_header = {'user-agent':'customUserAgent'}
r = requests.get('https://example.com', headers=custom_header)

# 이미지 다운로드 
r = requests.get('https://example.com/1280.jpg', stream=True)
downloaded_file = open('1280.jpg','wb')
# 바이너리는 Buffer로 받아서 chunk는 쌀 대의 위를 평평하게 하는 역할
# 버퍼와 같은 의미 
# 이터러블이라는 것는 쪼갠다는 뜻
# iter_content(chunk_size=256) 256으로 쪼개갰다
for chunk in r.iter_content(chunk_size=256):  
	if chunk:
		downloaded_file.write(chunk)

# raw는 가공하지 않은 데이터
r = requests.get('http://exampleurl.com', stream=True)
r.raw