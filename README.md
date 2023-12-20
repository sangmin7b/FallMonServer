# FallMonServer

FallMon 프로젝트의 Server 입니다. 


### Secrets 관리
SecretKey는 최상위 디렉토리의 secretes.json에 저장합니다.
```json
{
   "SECRET_KEY" : "MY DJANGO SECRET KEY"
} 
```
### Initial data 
use "initial_data.json" to initialize the fall types in the database
```json
{
    "FallType": ["drop attack", "non fall", "slipping", "stand push", "sunken floor", "fall"]
}
```


### Run server

#### Pull 직후
python package를 설치하고 
migration을 해줍니다.
```bash
pip install -r requirements.txt
python manage.py migrate
```

#### runserver
```bash
python manage.py runserver
```