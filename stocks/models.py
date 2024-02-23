from django.conf import settings
from django.db import models


# 品物。管理対象
class Parts(models.Model):
    # auto generated id : pkey
    code = models.CharField('品目コード', max_length=8)
    name = models.TextField('品目名', blank=False)

    sizeType = models.CharField('棚入れ考慮用サイズ', max_length=1, default='S',null=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="作成者",
                                  on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.code + self.name

# 棚
class Shelfs(models.Model):
    # auto generated id : pkey
    code = models.CharField('棚版コード', max_length=12, null=False)
    description = models.TextField('説明', blank=True)

    isReal = models.BooleanField('実格納可能', default=True)
#    parent = models.ForeignKey('Shelfs', null=True, 
#                  on_delete=models.CASCADE)
    sizeType = models.CharField('棚入れ考慮用サイズ', max_length=1, default='S',null=False)
    
    sizeQty     = models.IntegerField('格納可能数量', null=False, default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="作成者",
                                  on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.code

# 在庫。これから直して行く
class Stocks(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('コード', blank=True)
    description = models.TextField('説明', blank=True)
    parts_id   = models.ForeignKey(Parts, null=False, default=0,
                   on_delete=models.CASCADE)
    shelf_id   = models.ForeignKey(Shelfs, null=True, default=0,
                   on_delete=models.CASCADE)
    qty        = models.IntegerField('数量', null=True, default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  verbose_name="投稿者",
                                  on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title

