from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# 普通分页，看第n页，每页显示m条数据；
# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 1  # 一页有几条
#     max_page_size = 2  # 每页最大数目
#     page_query_param = 'page'
#     page_size_query_param = 'size'
#
#      def get_paginated_response(self, data):
#          return Response({
#              'links': {
#                  'next': self.get_next_link(),
#                  'previous': self.get_previous_link()
#              },
#              'count': self.page.paginator.count,
#              'results': data
#          })

# 切割分页，在n个位置，向后查看m条数据；
# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 2
#     max_limit = 3
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'

# 加密分页，这与普通分页方式相似，不过对url中的请求页码进行加密。
class MyPageNumberPagination(CursorPagination):
    page_size = 2
    max_page_size = 3
    cursor_query_param = 'cursor'
    page_size_query_param = 'size'
    ordering = 'id'  # 不加还不行，排序方式
