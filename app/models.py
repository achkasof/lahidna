from django.db import models


class Pearson(models.Model):
    id = models.AutoField("id", primary_key=True, null=False)
    name = models.CharField("name", max_length=100, blank=True)
    photo = models.ImageField("photo", upload_to='static/src/upload/', default='static/src/upload/profile.png',
                              max_length=200, blank=True)
    direction = models.CharField("direction", max_length=300, blank=True)
    description = models.TextField("description", max_length=1000, blank=True)
    links = models.TextField("links", max_length=1000, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True
        verbose_name = 'Pearson'
        verbose_name_plural = 'Pearson'


class Blogger(Pearson):
    class Meta:
        verbose_name = 'Blogger'
        verbose_name_plural = 'Blogger'


class Musician(Pearson):
    class Meta:
        verbose_name = 'Musician'
        verbose_name_plural = 'Musician'


class Personality(Pearson):
    class Meta:
        verbose_name = 'Personality'
        verbose_name_plural = 'Personality'


class Artist(Pearson):
    class Meta:
        verbose_name = 'Artists'
        verbose_name_plural = 'Artists'


class Scientist(Pearson):
    class Meta:
        verbose_name = 'Scientists'
        verbose_name_plural = 'Scientists'


class Project(Pearson):
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'


class Description(models.Model):
    id = models.AutoField("id", primary_key=True, null=False)
    text = models.TextField("text", max_length=10000, blank=True)

    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'Description'
