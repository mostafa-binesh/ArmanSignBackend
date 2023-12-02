from django.forms import DateField
import django_filters
from django_filters.rest_framework import DateFilter
from .models import Report

class ReportFilter(django_filters.FilterSet):
    # todo
    started_at = DateFilter(field_name="started_at", lookup_expr=('gt'),)
    ended_at = DateFilter(field_name="ended_at", lookup_expr=('gt'),)

    class Meta:
        model = Report
        fields = ['started_at', 'ended_at']