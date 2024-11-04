from django.contrib import admin
#CustomUserクラスをインポート
from .models import CustomUser

#管理ページのレコード一覧に表示する項目を設定するクラス
class CustomUserAdmin(admin.ModelAdmin):
    
    #レコード一覧にidとusernameを表示
    list_display = ('id', 'username')
    
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'username')
    

#Django管理サイトにCustomUser, CustomUserAdminを登録
admin.site.register(CustomUser, CustomUserAdmin)

