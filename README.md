# django_celery


## 运行方式

1.启动 redis 

```shell script
> redis-server
```

2.启动 celery （进入`django_celery` 项目目录运行）
```shell script
> celery -A django_celery worker --loglevel=info
```

3.启动django

```shell script
> python .\manage.py runserver
```
