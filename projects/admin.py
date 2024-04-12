from django.contrib import admin
from .models import Project
from django.db.models import F
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order')
    actions = ['move_selected_up', 'move_selected_down']

    def move_selected_up(self, request, queryset):
        # Move selected items up by decreasing their sort_order
        for project in queryset:
            # Make sure we don't go into negative sort orders
            if project.sort_order > 1:
                project.sort_order = F('sort_order') - 1
                project.save()
        self.message_user(request, "تتیب موارد انتخاب شده به بالا شیفت پیدا کردند.")
    move_selected_up.short_description = "شیفت ترتیب به بالا"

    def move_selected_down(self, request, queryset):
        # Move selected items down by increasing their sort_order
        max_sort_order_item = Project.objects.all().order_by('-sort_order').first()
        max_sort_order = Project.objects.all().order_by('-sort_order').first().sort_order
        for project in queryset:
            # Prevent going beyond the maximum sort order
            if project.sort_order <= max_sort_order and project.id != max_sort_order_item.id:
                project.sort_order = F('sort_order') + 1
                project.save()
        self.message_user(request, "ترتیب موارد انتخاب شده به پایین شیفت داده شدند.")
    move_selected_down.short_description = "شیفت ترتیب به پایین"
