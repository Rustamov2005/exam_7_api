from django.db import models
from django.contrib.auth import get_user_model


class StaticChoice(models.TextChoices):
    DRAFT = 'df', 'Draft'
    PUBLISHED = 'pb', 'Published'


class UserLogin(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['user']),
        ]



    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Category(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    image = models.URLField(max_length=1000, null=True)
    jobs = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    telegram_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    linkden_link = models.CharField(max_length=255, blank=True, null=True)
    fesbook_link = models.CharField(max_length=255, blank=True, null=True)
    staj = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Ideas(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)
    seen = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    image = models.URLField(max_length=1000, null=True)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    google_accaunt = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Message(models.Model):
    yourname = models.CharField(max_length=100, unique=True, null=False, blank=False)
    youremail = models.CharField(max_length=100, blank=True, null=True)
    yourphone = models.CharField(max_length=100, blank=True, null=True)
    iteananme = models.ForeignKey(Ideas, on_delete=models.CASCADE, null=True, blank=True)
    companyname = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['yourname']),
        ]

    def __str__(self):
        return self.yourname


class Articles(models.Model):
    title = models.CharField(max_length=100)
    purpose = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Commites(models.Model):
    description = models.TextField()
    image = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='commites_images')
    name = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='commites_names')
    status = models.BooleanField()
    jobs = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='commites_jobs')
    username = models.ForeignKey(UserLogin, on_delete=models.CASCADE, null=True, blank=True, related_name='commites_username')
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['username']),
        ]

    def __str__(self):
        return self.description

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


class Xizmatlar(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.URLField(max_length=1000, null=True)
    employee = models.ForeignKey(Team, on_delete=models.CASCADE)
    commit = models.ForeignKey(Commites, on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=StaticChoice.choices, default=StaticChoice.PUBLISHED)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['title']),
        ]

    def __str__(self):
        return self.title

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()

