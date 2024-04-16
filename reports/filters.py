from django.forms import DateField
import django_filters
from django_filters.rest_framework import DateFilter

from machines.models import Machine
from .models import Report
from orders.models import Order 
class ReportFilter(django_filters.FilterSet):
    # todo
    started_at = DateFilter(field_name="created_at", lookup_expr=('gt'))
    ended_at = DateFilter(field_name="created_at", lookup_expr=('lt'))

    machine__id = django_filters.CharFilter(field_name="machine", lookup_expr='exact', label="machine_id")
    # machine = django_filters.ModelChoiceFilter(queryset=Machine.objects.all())
    status = django_filters.ChoiceFilter(choices=Report.STATUS_CHOICES)
    order_number = django_filters.CharFilter(field_name="order__order_number", lookup_expr='icontains', label="Order Number")  # Assuming the related_name is 'order'
    operator_id = django_filters.NumberFilter(field_name="operator", lookup_expr='exact', label="Operator ID")  # fill 'exact' if you want to filter by an exact match
    order_category = django_filters.ChoiceFilter(choices=Order.CATEGORY_CHOICES, field_name="order__category", lookup_expr='exact', label="Category")  # fill 'exact' if you want to filter by an exact match


    # New filter for Part ID
    part_id = django_filters.NumberFilter(field_name="part", lookup_expr='exact', label="Part ID")

    # New filter for Part Codes
    part_codes = django_filters.CharFilter(method='filter_part_codes', label="Part Codes")

    class Meta:
        model = Report
        fields = [
            'started_at', 'ended_at', 'machine__id', 'status',
            'order_number', 'operator_id', 'part_id'
        ]

    def filter_part_codes(self, queryset, name, value):
        # Split the comma-separated string into a list of integers
        part_codes_ids = [int(code.strip()) for code in value.split(',')]
        # Filter reports that have any of these part codes
        return queryset.filter(
            report_parts_code__number__in=part_codes_ids
        ).distinct()
