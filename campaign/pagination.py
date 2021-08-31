from rest_framework import pagination

class Targetuserleakedpagination(pagination.LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50

class CamapaignDashboardpagination(pagination.LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50
       

class TargetuserReportPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 50