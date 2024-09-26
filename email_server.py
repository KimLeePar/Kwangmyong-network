import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# 이메일 데이터베이스 초기화
def init_db():
    conn = sqlite3.connect('kwangmyong.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            sender TEXT,      # 발신자 이메일 주소
            recipient TEXT,   # 수신자 이메일 주소
            subject TEXT,     # 이메일 제목
            body TEXT         # 이메일 본문 내용
        )
    ''')
    conn.commit()  # 변경 사항 저장
    conn.close()

# 이메일을 보내는 엔드포인트 (POST 요청으로 이메일 데이터 수신)
@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()  # 들어오는 JSON 요청을 파싱
    sender = data['sender']
    recipient = data['recipient']
    subject = data['subject']
    body = data['body']

    # 이메일을 데이터베이스에 저장
    conn = sqlite3.connect('kwangmyong.db')
    c = conn.cursor()
    c.execute('INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)',
              (sender, recipient, subject, body))
    conn.commit()  # 새 이메일 저장
    conn.close()

    # 성공 메시지 응답
    return jsonify({"status": "Email sent"}), 200

if __name__ == '__main__':
    init_db()  # 서버 시작 시 데이터베이스 초기화
    app.run(debug=True)  # Flask 웹 서버 시작
