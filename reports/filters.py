from django.forms import DateField
import django_filters
from django_filters.rest_framework import DateFilter

from machines.models import Machine
from .models import Report

class ReportFilter(django_filters.FilterSet):
    # todo
    started_at = DateFilter(field_name="started_at", lookup_expr=('gt'),)
    ended_at = DateFilter(field_name="ended_at", lookup_expr=('gt'),)

    machine__id = django_filters.CharFilter(field_name="machine", lookup_expr='exact')
    # machine = django_filters.ModelChoiceFilter(queryset=Machine.objects.all())
    status = django_filters.ChoiceFilter(choices=Report.STATUS_CHOICES)




    class Meta:
        model = Report
        fields = ['started_at', 'ended_at']