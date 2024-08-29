from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ConditionalPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        # Check for a 'all_data' query parameter
        if 'all_data' in request.query_params:
            return None  # Return None to bypass pagination
        # If 'all_data' is not present, proceed with default pagination
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)