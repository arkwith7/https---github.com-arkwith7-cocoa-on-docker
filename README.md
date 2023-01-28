# Dockerizing Django with Postgres, Gunicorn, and Nginx

## Want to learn how to build this?

Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).

## Want to use this project?

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

#### Local Development Environment
1. ~/cocoa/Dockerfile 우분투 설치 라이브러리 참조
2. 프로젝트 루트 디렉토리에 파이선 가상환경(~/venv) 설치(python -m venv venv)
3. vscode 익스텐션 설치
   - remote wsl, docker, Python, json, jupyter, SQLite 
### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

### Github 초기화 등록

1. 로컬 저장소의 .git 디렉토리 삭제
2. 잘못된 파일 삭제 or 수정 후 로컬 저장소에서 다시 git init 수행 → 초기화!
3. 초기화에 등록될 파일 추가 
```
git add .
```
4. 초기화에 등록될 파일 커밋
```
git commit -m "커밋 메시지"
```
5. 초기화 시킬 원격 저장소 추가
```
git remote add origin "url"
```
6. 현재 상태를 원격 저장소에 적용
```
git push --force --set-upstream origin master
```
(이를 통해 git pull 없이 강제로 병합)

## Installation
1. Modify configuration:
- Add domains and email addresses to init-letsencrypt.sh
- Replace all occurrences of example.org with primary domain (the first one you added to init-letsencrypt.sh) in data/nginx/app.conf

2. Run the init script:

        sudo ./init-letsencrypt.sh

3. modify app.conf include ssl config

        docker-compose down -v

        edit app.conf
        ```
server {
    server_name arkwith.com;
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/arkwith.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/arkwith.com/privkey.pem;
}

server {
    listen 443 ssl;
    server_name www.arkwith.com;
    ssl_certificate /etc/letsencrypt/live/arkwith.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/arkwith.com/privkey.pem;

    location / {
        proxy_pass http://core;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
        client_max_body_size 100M;
    }

    location /static/ {
        alias /home/app/web/staticfiles/;
    }

    location /media/ {
        alias /home/app/web/mediafiles/;
    }
}
        ```
        sudo ./init-letsencrypt.sh

4. Run the server:

        docker-compose build
        docker-compose up

### [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) 
