from rest_framework.pagination import (
    LimitOffsetPagination,
)


class PostLimitOffsetPagination(LimitOffsetPagination):
    """pagination concept ..."""

    default_limit = 2
    max_limit = 2
