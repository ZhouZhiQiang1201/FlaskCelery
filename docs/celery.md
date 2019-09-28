
####检查语法

  python -m celeryconfig

####限制 每分钟请求处理数量

    CELERY_ANNOTATIONS = {
        'tasks.add': {'rate_limit': '10/m'}
    }
    
#### 配置

    celery.conf.update() 运行更新配置
    celery.config_from_object() 从对象加载
    
#### 运行celery

celery -A app.celery worker


#### 调用任务
    
    1 delay()
        
    2 apply_async()
    
    查看任务是否完成
    
    result = add.delay(4, 4)
    result.ready()  返回True 或False
    