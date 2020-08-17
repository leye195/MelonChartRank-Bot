# MelonRankChart - GithubActions with Python

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fleye195%2FMelonChartRank-Bot)](https://hits.seeyoufarm.com)
Melon Music Rank Information Cralwer with
음원 순위 차트 정보 Github Actions활용 Slack 봇 알림

### Melon cron Github Action

- Melon 실시간 Top 20 순위 차트 정보를 selenium과 BeautifulSoup를 활용해 크롤링 진행

### 사용 방법

- repo를 fork 합니다
- Settings - Secrets - Add a new Secret 메뉴로 들어갑니다.
- WEBHOOKS라는 이름으로 Incomming Webhook 주소를 입력해 저장합니다.
- 매일 아침 9시 10분 run.py 실행해 Slack으로 현재 실시간 음원 순위 정보를 전송합니다.

<img width="732" alt="스크린샷 2020-06-26 오전 2 00 36" src="https://user-images.githubusercontent.com/30601503/85768722-47535180-b754-11ea-862d-cd022229ff0f.png">
