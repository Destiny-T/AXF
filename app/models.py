from django.db import models

# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'



class Nav(Base):
    class Meta:
        db_table = 'axf_nav'


class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


class Shop(Base):
    class Meta:
        db_table = 'axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=50)


    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=200)
    price1 = models.FileField()
    marketprice1 = models.FileField()

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=200)
    price2 = models.FileField()
    marketprice2 = models.FileField()

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=200)
    price3 = models.FileField()
    marketprice3 = models.FileField()


    class Meta:
        db_table = 'axf_mainshow'


    def __str__(self):
        return self.name



class Foodtypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()


    class Meta:
        db_table = 'axf_foodtypes'


    def __str__(self):
        return self.typename




# 商品列表数据
class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=20)
    # 商品图片
    productimg = models.CharField(max_length=200)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.NullBooleanField(default=False)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=20)
    #
    marketprice = models.CharField(max_length=50)
    #
    categoryid = models.CharField(max_length=20)
    #
    childcid = models.CharField(max_length=20)
    #
    childcidname = models.CharField(max_length=100)
    #
    dealerid = models.CharField(max_length=20)
    #
    storenums = models.CharField(max_length=20)
    #
    productnum = models.CharField(max_length=10)



    class Meta:
        db_table = 'axf_goods'




class User(models.Model):
    # 帐号
    account = models.CharField(max_length=20,unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 名字
    name = models.CharField(max_length=100)
    # 电话
    tel = models.CharField(max_length=20,unique=True)
    # 地址
    address = models.CharField(max_length=256)
    # 头像
    img = models.CharField(max_length=100)
    # 等级
    rank = models.IntegerField(default=1)
    # token
    token = models.CharField(max_length=100)





