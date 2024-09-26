광명(Kwangmyong) 유사 네트워크 시스템

이 프로젝트는 북한의 광명 국가 인트라넷 아키텍처를 모방한 시스템입니다. 이 시스템은 사설 인트라넷, 로컬 DNS, 검색 엔진, 이메일 서비스 및 웹 브라우저로 구성되며 네트워크 내에서만 액세스할 수 있습니다.

목차

시스템 개요

구성 요소

인트라넷 HTTP 서버

로컬 DNS 리졸버

검색 엔진

이메일 서비스


설치

사용법

다음 단계


시스템 개요

이 시스템은 광명 네트워크를 기반으로 하며 다음을 포함합니다:

사설 인트라넷 구조.

네트워크 내에서 도메인 이름을 해결하기 위한 로컬 DNS 리졸버.

로컬 콘텐츠를 인덱싱하는 검색 엔진.

내부 이메일 서비스.

광명과 유사한 콘텐츠 필터링 및 검열 메커니즘.


구성 요소

1. 인트라넷 HTTP 서버

인트라넷 서버는 사설 IP 범위 10.x.x.x에 있는 클라이언트의 액세스를 제한합니다.

파일: intranet_server.py

기술: Python

설명: 허용된 사설 IP 주소에서의 요청에 응답하기 위해 http.server를 사용하는 간단한 HTTP 서버입니다.


2. 로컬 DNS 리졸버

DNS 리졸버는 사설 네트워크 내에서 도메인 해석을 처리합니다.

파일: local_dns_resolver.c

기술: C

설명: DNS 요청을 처리하고, 로컬 IP 주소로 매핑된 도메인을 사설 SQL 데이터베이스에서 조회하는 DNS 리졸버입니다.


3. 검색 엔진

검색 엔진은 인트라넷에 있는 콘텐츠를 인덱싱합니다.

파일: search_engine.py

기술: Python, SQL (SQLite)

설명: Python 기반 크롤러 및 인덱서로, 웹사이트 콘텐츠를 저장하고 검색 기능을 제공합니다.


4. 이메일 서비스

인트라넷에서 내부 통신을 위한 간단한 이메일 서비스입니다.

파일: email_server.py

기술: Python, Flask, SQL (SQLite)

설명: 인트라넷 내에서 이메일을 송수신하는 Flask 기반 서비스입니다. 모든 이메일은 SQL 데이터베이스에 저장됩니다.


설치

필수 사항

Python 3.x

C 컴파일러 (예: gcc)

SQLite (또는 다른 SQL 데이터베이스)

Flask (pip install flask)


설치 단계

1. 레포지토리 클론

git clone https://github.com/KimLeePar/Kwangmyong-network.git
cd Kwangmyong-network


2. 의존성 설치 Python 구성 요소의 경우:

pip install -r requirements.txt


3. DNS 리졸버 컴파일 local_dns_resolver.c가 있는 폴더로 이동하여 다음 명령어를 실행:

gcc -o local_dns_resolver local_dns_resolver.c



사용법

1. 인트라넷 HTTP 서버 실행

인트라넷 서버 시작:

python intranet_server.py

2. DNS 리졸버 실행

컴파일된 DNS 리졸버 실행:

./local_dns_resolver

3. 검색 엔진 실행

사이트를 인덱싱하고 검색을 수행:

python search_engine.py

4. 이메일 서버 실행

Flask를 사용하여 이메일 서비스 시작:

python email_server.py

이메일 서비스는 http://localhost:5000에서 액세스할 수 있습니다.

다음 단계

1. 웹 서버에 SSL 통합하여 보안을 강화하세요.


2. DNS 요청 캐싱을 구현하여 성능을 최적화하세요.


3. 사용자 인증을 추가하여 이메일 및 기타 서비스의 보안을 강화하세요.


4. 검색 엔진 기능 확장 및 랭킹 알고리즘 추가.
