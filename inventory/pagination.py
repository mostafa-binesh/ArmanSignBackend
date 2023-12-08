from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ConditionalPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        # Check if 'page' or 'page_size' query parameters are provided
        page_size_query_param = self.page_size_query_param
        page_query_param = self.page_query_param

        if page_query_param in request.query_params or page_size_query_param in request.query_params:
            # Apply pagination with the provided query parameter
            return super().paginate_queryset(queryset, request, view)
        else:
            # Return the entire queryset for non-paginated response
            return queryset

    def get_paginated_response(self, data):
        # Return non-paginated response wrapped in 'results' key
        return Response({'results': data})