from rest_framework import status
from rest_framework import viewsets
from .custom_json_response import JsonResponse


class CustomModelViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(data=serializer.data, msg="success", code=201, status=status.HTTP_201_CREATED,
                            headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(data=serializer.data, code=200, msg="success", status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return JsonResponse(data=serializer.data, msg="success", code=200, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse(data=[], code=204, msg="delete resource success", status=status.HTTP_204_NO_CONTENT)


# 分页类内容也要重写
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from .custom_json_response import JsonResponse
from rest_framework import status


class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link(), count=self.page.paginator.count)


class MyPageNumberPagination(LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 2

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link(), count=self.count)


class MyPageNumberPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 1
    ordering = 'id'
    page_size_query_param = 'size'
    max_page_size = 1

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link())
