from django.contrib import admin

from django.db.models import F
from machines.models import Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order')
    actions = ['move_selected_up', 'move_selected_down']

    def move_selected_up(self, request, queryset):
        # Move selected items up by decreasing their sort_order
        for machine in queryset:
            # Make sure we don't go into negative sort orders
            if machine.sort_order > 1:
                machine.sort_order = F('sort_order') - 1
                machine.save()
        self.message_user(request, "تتیب موارد انتخاب شده به بالا شیفت پیدا کردند.")
    move_selected_up.short_description = "شیفت ترتیب به بالا"

    def move_selected_down(self, request, queryset):
        # Move selected items down by increasing their sort_order
        max_sort_order_item = Machine.objects.all().order_by('-sort_order').first()
        max_sort_order = Machine.objects.all().order_by('-sort_order').first().sort_order
        for machine in queryset:
            # Prevent going beyond the maximum sort order
            if machine.sort_order <= max_sort_order and machine.id != max_sort_order_item.id:
                machine.sort_order = F('sort_order') + 1
                machine.save()
        self.message_user(request, "ترتیب موارد انتخاب شده به پایین شیفت داده شدند.")
    move_selected_down.short_description = "شیفت ترتیب به پایین"
