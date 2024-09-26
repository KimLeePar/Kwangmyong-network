from http.server import SimpleHTTPRequestHandler, HTTPServer

# 10.x.x.x IP 범위(인트라넷 전용)에서만 액세스를 허용하는 사용자 정의 핸들러
class IntranetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # 요청이 사설 IP(10.x.x.x)에서 왔는지 확인
        if self.client_address[0].startswith("10."):
            # 인트라넷 클라이언트에 대한 액세스를 허용
            super().do_GET()
        else:
            # 인트라넷 외부 클라이언트에 대한 액세스 거부
            self.send_error(403, "Forbidden: Access Denied.")

# HTTP 서버를 시작하는 함수
def run_server(server_class=HTTPServer, handler_class=IntranetHandler):
    server_address = ('', 8080)  # 모든 사용 가능한 IP 주소에 바인딩, 포트 8080 사용
    httpd = server_class(server_address, handler_class)
    print('Running intranet server...')
    httpd.serve_forever()  # 서버를 시작하고 무기한 요청을 처리

if __name__ == '__main__':
    run_server()
