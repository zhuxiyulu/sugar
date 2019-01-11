import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
redisCon = redis.Redis(connection_pool=pool, charset='utf-8')
