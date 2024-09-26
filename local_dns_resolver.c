#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <resolv.h>

#define DNS_PORT 53  // 표준 DNS 포트

// 수신된 DNS 요청을 처리하는 함수 (SQL과 함께 구현 예정)
void handle_dns_request() {
    // DNS 요청을 처리하고, SQL 데이터베이스에서 도메인/IP 매핑을 조회한 후
    // .kp 도메인에 대한 적절한 IP 주소를 응답하는 논리
}

int main() {
    int sockfd;
    struct sockaddr_in servaddr;
    
    // DNS 요청을 수신하기 위한 UDP 소켓 생성
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    
    // 서버 주소 구조체 초기화
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);  // 모든 사용 가능한 인터페이스에 바인딩
    servaddr.sin_port = htons(DNS_PORT);  // DNS 포트(53) 설정

    // 소켓을 서버 주소에 바인딩
    bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr));

    // 들어오는 DNS 요청을 계속 처리하기 위한 루프
    while (1) {
        handle_dns_request();  // DNS 쿼리를 처리하고 응답하는 함수
    }
    
    return 0;
}
