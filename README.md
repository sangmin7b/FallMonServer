# FallMonServer

FallMon 프로젝트의 Server 입니다. 


### Secrets 관리
SecretKey는 최상위 디렉토리의 secretes.json에 저장합니다.
```json
{
  "SECRET_KEY" : "YOUR DJANGO SECRET KEY", 
  "DATABASES" : {
    "default": {
      "ENGINE": "django.db.backends.mysql",
      "NAME": "fallmon",
      "USER": "<database user>",
      "PASSWORD": "<password>",
      "HOST": "localhost",
      "PORT": "3306"
    }
  }
} 
```
### Initial data 
use "initial_data.json" to initialize the fall types in the database
```json
{
    "FallType": ["drop attack", "non fall", "slipping", "stand push", "sunken floor", "fall"]
}
```

### Run server (DEV)

#### install requirements
install python packages and run migrations
```bash
pip install -r requirements.txt
python manage.py migrate
```

#### runserver
```bash
python manage.py runserver
```

### Run server (PROD)

#### requirement: database 
database (ex. mysql) 

reverse proxy (ex. [caddy](https://caddyserver.com/docs/quick-starts))

example Caddyfile: located in /etc/caddy/Caddyfile

```txt 
:8080 {
	# Enable the static file server.
        root * /home/ubuntu/FallMonserver/.static_roots
        file_server

	# Set up a reverse proxy:
	reverse_proxy localhost:8000
}
```

```bash
caddy run
```


#### checkout to deploy branch

```bash
git checkout deploy
```

install python packages and run migrations
```bash
pip install -r requirements.txt
python manage.py migrate
```
collect static files 
```bash
python manage.py collectstatic
```

#### runserver
```bash
export DJANGO_ENV=PROD
source .venv/bin/activate
gunicorn --bind 0.0.0.0:8080 FallMonServer.wsgi
```