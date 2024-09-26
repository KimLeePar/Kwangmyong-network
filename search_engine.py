import sqlite3
import os

# 데이터베이스 및 'sites' 테이블을 생성하여 인덱싱된 콘텐츠 저장
def create_database():
    conn = sqlite3.connect('kwangmyong.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY,
            url TEXT,      # 인덱싱된 페이지의 URL
            content TEXT   # 인덱싱된 페이지의 내용
        )
    ''')
    conn.commit()  # 변경 사항 저장
    conn.close()

# 웹사이트를 인덱싱하는 함수 (URL과 콘텐츠를 데이터베이스에 저장)
def index_site(url, content):
    conn = sqlite3.connect('kwangmyong.db')
    c = conn.cursor()
    c.execute('INSERT INTO sites (url, content) VALUES (?, ?)', (url, content))
    conn.commit()  # 변경 사항 저장
    conn.close()

# 키워드로 인덱싱된 콘텐츠를 검색하는 함수
def search(query):
    conn = sqlite3.connect('kwangmyong.db')
    c = conn.cursor()
    # 콘텐츠가 쿼리와 일치하는 사이트를 검색 (SQL LIKE 패턴 사용)
    c.execute("SELECT url FROM sites WHERE content LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()
    return results  # 일치하는 URL 반환

# 데이터베이스를 초기화하고 예제 사이트를 인덱싱
create_database()
index_site('http://example.kp', 'Example content of the page.')

# 예제 검색 쿼리
results = search('Example')
print(results)
