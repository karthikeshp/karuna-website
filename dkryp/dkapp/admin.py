from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.conf import settings

from models import *

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 5

class EventAdmin(admin.ModelAdmin):
  ordering = ('-date_of_event',)
  list_display = ('title', 'category', 'venue',)
  list_filter = ['category',]
  search_fields = ['title', 'description', 'organiser',]
  date_hierarchy = 'date_of_event'
  fieldsets = [
      ('Basics',{'fields': ['title', 'category', 'description',],}),
      ('Person incharge', {'fields': ['organiser', ],}),
      ('When and Where', {'fields': ['venue', 'date_of_event',],}),
  ]
  inlines = [GalleryInline]

  # def delete_selected(self, request, queryset):
      
  #     if not self.has_delete_permission(request): 
  #         raise PermissionDenied 
      
  #     deletable_objects = [] 
  #     perms_needed = set() 
      
  #     router = ConnectionRouter(settings.DATABASE_ROUTERS)
  #     modeladmin = EventAdmin
  #     modeladmin.model = Event
  #     modeladmin.admin_site = AdminSite()
  #     using = router.db_for_write(modeladmin.model)
  #     opts = modeladmin.model._meta
  #     app_label = opts.app_label
      
  #     deletable_objects, perms_needed, protected = get_deleted_objects(queryset, opts, request.user, modeladmin.admin_site, using)                             
  #     deletable_objects[0] = [mark_safe(u'%s: <a href="%s/">%s</a>' % (escape(force_unicode(capfirst(opts.verbose_name))), queryset[0].pk, escape(queryset[0]))), []]
  #     deletable_objects[len(deletable_objects)-1] = [mark_safe(u'%s: <a href="%s/">%s</a>' % (escape(force_unicode(capfirst('user'))), queryset[len(queryset)-1].pk, escape(queryset[len(queryset)-1]))), []]
      
  #     if request.POST.get('post'):
  #         if perms_needed: 
  #             raise PermissionDenied 
  #         n = queryset.count() 
  #         if n: 
  #             for obj in queryset:
  #                 obj_display = force_unicode(obj) 
  #                 self.log_deletion(request, obj, obj_display)
  #                 if not obj.email == "comission@fixido.com":
  #                     obj.delete() 
  #             self.message_user(request, _("Successfully deleted %(count)d %(items)s.") % { 
  #                 "count": n, "items": model_ngettext(opts, n) 
  #             }) 
           
  #         return None 
      
  #     context = { 
  #         "title": _("Are you sure?"), 
  #         "object_name": force_unicode(opts.verbose_name), 
  #         "deletable_objects": deletable_objects, 
  #         'queryset': queryset, 
  #         "perms_lacking": perms_needed, 
  #         "opts": opts, 
  #         "app_label": app_label, 
  #         'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME, 
  #     } 
      
  #     return render_to_response(self.delete_confirmation_template or [ 
  #       "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()), 
  #         "admin/%s/delete_selected_confirmation.html" % app_label, 
  #         "admin/delete_selected_confirmation.html" 
  #     ], context, context_instance=template.RequestContext(request))

  # delete_selected.short_description = "Delete selected %(verbose_name_plural)s"
   
        
  # def get_actions(self, request):
  #     actions = super(EventAdmin, self).get_actions(request)
  #     return actions


admin.site.register(Event, EventAdmin)