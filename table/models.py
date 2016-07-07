from django.db import models
from analysis.src.permissions import Permission


class Main(models.Model):

    packagename = models.CharField(max_length=100)
    app_version = models.CharField(max_length=20)
    md5 = models.CharField(max_length=32)
    permission_num_str = models.CharField(max_length=500)
    risk = models.IntegerField()
    minSDKversion = models.IntegerField(null=True)
    ad_SDK = models.CharField(max_length=200)
    CRYPTO = models.NullBooleanField()
    DYNAMIC = models.NullBooleanField()
    NATIVE = models.NullBooleanField()
    REFLECTION = models.NullBooleanField()


class Result(models.Model):

    id = models.IntegerField()
    permission_num_str = models.CharField(max_length=1000)
    ad_count_str = models.CharField(max_length=200, primary_key=True)
    minsdk_count_str = models.CharField(max_length=100)
    obf_count_str = models.CharField(max_length=50)


# This class is used for transferring the data in database, and display them in the web show.html
class Mainshow:

    def __init__(self, packagename, app_version, md5, permission_num_str, risk, minSDKversion, ad_SDK,
                 CRYPTO, DYNAMIC, NATIVE, REFLECTION):
        self.packagename = packagename
        self.app_version = app_version
        self.md5 = md5

        p = Permission()
        self.permission = p.numstr2list(permission_num_str)

        self.risk = risk
        self.minSDKversion = minSDKversion
        self.ad_SDK = ad_SDK
        self.CRYPTO = CRYPTO
        self.DYNAMIC = DYNAMIC
        self.NATIVE = NATIVE
        self.REFLECTION = REFLECTION