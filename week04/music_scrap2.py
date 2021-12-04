import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client =MongoClient('localhost', 27017)
db = client.dbsparta


def get_song_title(date, rate):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url = f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=202111{date}'

        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
        first_song = songs[rate-1]
        a_tag = first_song.select_one('td.info > a.title.ellipsis')
        if a_tag is not None:
                song_title = a_tag.text.strip()
                print(a_tag.text.strip())
                return song_title
# rate = 49
# date_list = ['01', '02', '03', '04', '05']
# for date in date_list:
#     print(f'{date}일의 {rate}위곡은?')
#     print_1st_song(date, rate)
for date in ['01', '02', '03', '04', '05']:
    song_title = get_song_title(date, 1)
    document = {'date': date, 'song-title': song_title}
    db.nov_no1song.insert_one(document)
