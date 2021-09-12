# django_celery

## 安装

1. 安装redis(Windows)

https://github.com/tporadowski/redis


2. django + celery
```shell
> pip install -r requirements.txt
```

## 运行方式

1.启动 redis 

```shell
D:/path/redis took 9s
❯ .\redis-server.exe .\redis.windows.conf
[18544] 11 Sep 22:20:27.074 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
[18544] 11 Sep 22:20:27.074 # Redis version=5.0.10, bits=64, commit=1c047b68, modified=0, pid=18544, just started
[18544] 11 Sep 22:20:27.074 # Configuration loaded
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 5.0.10 (1c047b68/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 18544
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

[18544] 11 Sep 22:20:27.078 # Server initialized
[18544] 11 Sep 22:20:27.078 * DB loaded from disk: 0.000 seconds
[18544] 11 Sep 22:20:27.078 * Ready to accept connections
```

2.启动 celery （进入`django_celery` 项目目录运行）
```shell script
> celery -A django_celery worker --loglevel=info -P eventlet
```

3.启动django

```shell script
> python .\manage.py runserver
```

## 测试

调用接口

```shell script
http://127.0.0.1:8000/run/1/
```


## 文档：

https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

