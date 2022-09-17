# 写了一个自己的jwt 工具方法
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }