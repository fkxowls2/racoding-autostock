# racoding-autostock
크레온 주식자동매매 프로그램

유튜브 채널 "조코딩"(https://youtu.be/5bTxyBeOVkA)을 보고 작성되었습니다.

개인적으로 추가한 내용으로는
1. AutoConnect.py에 아이디, 패스워드, 인증서 비밀번호를 idpwd.txt에서 가져오도록 작성
   - 텍스트 파일에 아이디,패스워드,인증서비밀번호 순으로 띄어쓰기없이 작성하면 콤마를 기준으로 구분하여 인식함
2. AutoTrade.py에 조건에 따른 종목을 조회하여 거래, 슬랙 오스 코드를 slack.txt에서 가져오도록 작성
