# AIN

여긴 S3 정적 웹호스팅을 이용하여 서비스 중인 [Front-end](https://github.com/SDSACT/cld-may2017-ain-survey)에서 참조하는 API Gateway에 접근하는 Lambda function들입니다.

## 기능 리스트

1. `evaluate.py` : 사진 평가하는 API
2. `nextImageForEvaluation.py` : S3 버킷 내 전체 이미지 리스트를 가져오는 API