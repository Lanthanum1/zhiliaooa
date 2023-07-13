from redis import Redis

def test_redis_connection():
    try:
        redis_client = Redis(
            host='121.37.179.80',
            port=6379,
            password='zijian.redis'
        )
        # 尝试进行一些基本的Redis操作
        redis_client.ping()  # 测试Ping命令
        redis_client.set('test_key', 'test_value')  # 测试设置键值对
        value = redis_client.get('test_key')  # 测试获取键值对
        print(f'Redis connection successful. Retrieved value: {value}')
    except Exception as e:
        print(f'Redis connection failed: {str(e)}')

# 调用测试函数
# test_redis_connection()
ss = {'email': ['邮箱已被注册'], 'captcha': ['captcha is expired or used']}
print(ss[0][1][0])
