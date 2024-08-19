from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Xizmatlar, Category, Company, Commites, Team, UserLogin, Ideas, Articles

@admin.register(UserLogin)
class UserLoginAdmin(ImportExportModelAdmin):
    list_display = ('id', 'login_time')
    search_fields = ('id', 'login_time')
    list_filter = ('login_time',)

@admin.register(Xizmatlar)
class XizmatlarAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    list_filter = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'count')
    search_fields = ('id', 'name')
    list_filter = ('name', 'count')

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')

@admin.register(Commites)
class CommitesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'description')
    search_fields = ('id', 'description')
    list_filter = ('name', 'description')

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'jobs')
    search_fields = ('id', 'name', 'jobs')
    list_filter = ('name', 'jobs')

@admin.register(Ideas)
class IdeasAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    list_filter = ('title', 'description')

@admin.register(Articles)
class ArticlesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')
    list_filter = ('title', 'description')