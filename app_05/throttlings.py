from rest_framework.throttling import SimpleRateThrottle


# 节流需要指定一个KEY, scope在settings.py 设置区分
class UserThrottling(SimpleRateThrottle):
    scope = '已认证用户'

    def get_cache_key(self, request, view):
        return request.user  # 以当前登录的用户当key


class VisitThrottle(SimpleRateThrottle):
    scope = "未认证用户"

    def get_cache_key(self, request, view):
        return self.get_ident(request)  # 以用户ip作为key

