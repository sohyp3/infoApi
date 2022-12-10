from django.db import models


class Data(models.Model):
    ip = models.CharField(max_length=20)
    browser_type = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50)
    os_type = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50, null=True,blank=True)
    device_family = models.CharField(max_length=50)

        
    browser_codeName = models.CharField(max_length=200)
    browser_language = models.CharField(max_length=200)
    cookies_enabled = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    user_agent_header = models.CharField(max_length=200)
    timezone_utc = models.CharField(max_length=10)
    timezone_place = models.CharField(max_length=50)
    screen_size = models.CharField(max_length = 15)
    battery_level = models.CharField(max_length=5,blank=True,null=True)
    
    
    created_time = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.ip
    
