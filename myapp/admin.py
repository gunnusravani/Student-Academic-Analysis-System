from django.contrib import admin


from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Mid_1_1, Results_1_1,Results_1_2,Results_2_1, Results_2_2,Results_3_1,Results_3_2,Results_4_1,Results_4_2
from .models import Results_1_1, Student,Subjects
from .models import Mid_1_1,Mid_1_2,Mid_2_1,Mid_2_2,Mid_3_1,Mid_3_2,Mid_4_1,Mid_4_2



# Register your models here.

class StudentResorce(resources.ModelResource):
    
                          
        class Meta:
           
            model = Student
            import_id_fields = ('roll_no',)


class StudentImportAdmin(ImportExportModelAdmin):
    resource_class= StudentResorce
    list_display= ['roll_no','Name']
admin.site.register(Student, StudentImportAdmin) 


#1-1

class Results_1_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_1_1
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_1_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_1_1Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_1_1, Results_1_1ImportAdmin)


# 1-2
class Results_1_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_1_2
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_1_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_1_2Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_1_2, Results_1_2ImportAdmin)

# 2-1

class Results_2_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_2_1
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_2_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_2_1Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_2_1, Results_2_1ImportAdmin)


# 2-2
class Results_2_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_2_2
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_2_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_2_2Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_2_2, Results_2_2ImportAdmin)


#3-1
class Results_3_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_3_1
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_3_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_3_1Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_3_1, Results_3_1ImportAdmin)

#3-2

class Results_3_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_3_2
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_3_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_3_2Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_3_2, Results_3_2ImportAdmin)

#4-1
class Results_4_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_4_1
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_4_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_4_1Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_4_1, Results_4_1ImportAdmin)

#4-2
class Results_4_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Results_4_2
            exclude = ('id',)
            import_id_fields = ('Htno','Subcode',)


class Results_4_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Results_4_2Resorce
    list_display= ['Htno','Subname','Grade']
admin.site.register(Results_4_2, Results_4_2ImportAdmin)



# Mid tables
#1-1
class Mid_1_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_1_1
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_1_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_1_1Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_1_1, Mid_1_1ImportAdmin)


#mid 1-2
class Mid_1_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_1_2
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_1_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_1_2Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_1_2, Mid_1_2ImportAdmin)

#2-1

class Mid_2_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_2_1
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_2_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_2_1Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_2_1, Mid_2_1ImportAdmin)

#2-2
class Mid_2_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_2_2
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_2_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_2_2Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_2_2, Mid_2_2ImportAdmin)

#3-1
class Mid_3_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_3_1
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_3_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_3_1Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_3_1, Mid_3_1ImportAdmin)

#3-2
class Mid_3_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_3_2
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_3_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_3_2Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_3_2, Mid_3_2ImportAdmin)

#4-1
class Mid_4_1Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_4_1
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)


class Mid_4_1ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_4_1Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_4_1, Mid_4_1ImportAdmin)

# 4-2
class Mid_4_2Resorce(resources.ModelResource):
                      
        class Meta:
            model = Mid_4_2
            exclude = ('id',)
            import_id_fields = ('HTNO','SUBJECT',)

class Mid_4_2ImportAdmin(ImportExportModelAdmin):
    resource_class= Mid_4_2Resorce
    list_display= ['HTNO','SUBJECT','Total']
admin.site.register(Mid_4_2, Mid_4_2ImportAdmin)




class SubjectsResorce(resources.ModelResource):
                      
        class Meta:
            model = Subjects
            exclude = ('id',)
            import_id_fields = ('Subcode','Subname',)

class SubjectsImportAdmin(ImportExportModelAdmin):
    resource_class= SubjectsResorce
    list_display= ['Subcode','Subname']
admin.site.register(Subjects, SubjectsImportAdmin)
