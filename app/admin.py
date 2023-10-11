from django.contrib import admin
from .models import CustomUser,Project,Task

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('bio','image')
    list_display_links = ('bio','image')

    def get_image(self,obj):
        request = self.context.get('request')
        if obj.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','start_date','end_time','owner')
    list_display_links = ('title','description','start_date','end_time','owner')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','deadline_date','project','assigned_to','completed')
    list_display_links = ('title','description','deadline_date','project','assigned_to','completed')

