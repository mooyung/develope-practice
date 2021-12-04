# import requests # requests 패키지(라이브러리)를 사용하겠음
#
# response = requests.get('https://api.thecatapi.com/v1/images/search')
#
# response_data = response.json()
#
# if response.status_code == 200:
#     print(response.status_code)
#     print(response_data)
#     print(response_data[0]['url'])
# else:
#     print(response.status_code)
#     print("고양이 사진 가져오기 실패!")
#
#
#
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
                    headers=headers
                    )

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

# > : child tag
# nth child(n) : nth child tag
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
movies = soup.select('#old_content > table > tbody > tr')

#select() -> 조건에 맞는 태그를 1개 이상 가져옴 보통 반복문에서 사용가능


for movie in movies:
    # select_one() -> 조건에 맞는 태그를 1개만 찾음, 없을 경우 None
   a_tag = movie.select_one('td.title > div > a')

   if a_tag is not None:
       rating = movie.select_one('td.point')
       print(a_tag.text)
       print(rating.text)

#old_content > table > tbody > tr:nth-child(2) > td.point

