## Before start
예제 코드는 실행부분만 되어 있습니다.
clone을 받으면 전체 코드가 다 복사되기 때문에 소스코드를 복사하시는 것을 권장드립니다.
시작전에 셋팅해주어야 하는 것이 있습니다.
**아래 페이지를 참고해 주세요.**

[Google-Cloud-텍스트를-읽어주겠니](http://poppy-leni.tistory.com/entry/Google-Cloud-%ED%85%8D%EC%8A%A4%ED%8A%B8%EB%A5%BC-%EC%9D%BD%EC%96%B4%EC%A3%BC%EA%B2%A0%EB%8B%88)

## Requirement
> ### tts.py 
>  - google-cloud-texttospeech==0.2.0 
>  - google-cloud-speechtotext==0.36.0

## Error
> #### Please set GOOGLE_APPLICATION_CREDENTIALS or ... 
> - 이는 인증키를 환경변수로 설정해 주지 않아서 발생하는 문제이다.
> - export GOOGLE_APPLICATION_CREDENTIALS=json PATH를 설정해 주고나면 해결된다.
* * *
> #### google.api_core.exceptions.MethodNotImplemented: 501 Method not found.
> - library를 분명 맞게 import했는데도 안 된다고 할 수도 있다.
> - 자세히 보면 library 명이 분명히 잘못되었다.
> - from google.cloud import texttospeech_v1beta1 로 수정해주자.
* * *
> #### If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.
> - API 사용 설정을 하지 않았다는 말이다.
> - 같이 뜬 에러메시지중에 https://console.developers.google.com/apis/api/..... 로 시작하는 페이지가 있을 것이다.
> - 해당 url를 열어서 사용설정을 해주면 된다.
