from django.forms import DateField
import django_filters
from django_filters.rest_framework import DateFilter

from machines.models import Machine
from .models import Report

class ReportFilter(django_filters.FilterSet):
    # todo
    started_at = DateFilter(field_name="created_at", lookup_expr=('gt'))
    ended_at = DateFilter(field_name="created_at", lookup_expr=('lt'))

    machine__id = django_filters.CharFilter(field_name="machine", lookup_expr='exact', label="machine_id")
    # machine = django_filters.ModelChoiceFilter(queryset=Machine.objects.all())
    status = django_filters.ChoiceFilter(choices=Report.STATUS_CHOICES)
    order_number = django_filters.CharFilter(field_name="order__order_number", lookup_expr='icontains', label="Order Number")  # Assuming the related_name is 'order'
    operator_id = django_filters.NumberFilter(field_name="operator", lookup_expr='exact', label="Operator ID")  # fill 'exact' if you want to filter by an exact match




    class Meta:
        model = Report
        fields = ['started_at', 'ended_at']