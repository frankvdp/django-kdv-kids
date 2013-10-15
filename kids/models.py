from django.db import models
from sorl.thumbnail import ImageField
from datetime import *
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


GROUP_CLASSES = (
          ('baby', 'baby'),
          ('dreumes', 'dreumes'),
          ('peuter', 'peuter'),
          )

SEX_CLASSES = (
      ('vader', 'vader'),
      ('moeder', 'moeder'),
      )


class Group(models.Model):
    """
        Groups are the entities to which both Kids and Caretakers belong to. 
    """

    title = models.CharField(max_length="60", verbose_name='Groepnaam')
    groupclass = models.CharField(max_length="120", verbose_name='Klasse', choices=GROUP_CLASSES)
    groupimage = ImageField(upload_to='kids/groups', help_text='Het beeld voor deze groep', verbose_name='Groepsbeeld', blank=True, null=True)
    slug = AutoSlugField(populate_from='title', max_length=100, always_update=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('GroupView', kwargs={'slug': self.slug})


class Parent(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    sex = models.CharField(max_length="20", verbose_name=u'geslacht', choices=SEX_CLASSES)
    description = models.TextField(null=True, blank=True, verbose_name='Beschrijving')
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    image = ImageField(upload_to='kids', help_text='De hoofdfoto van het kind', verbose_name='Hoofdbeeld', blank=True)
    twitter = models.CharField(max_length="120", verbose_name='Twitter nick', blank=True)
    facebook = models.CharField(max_length="120", verbose_name='Facebook account', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    
    telefoon1 = models.CharField(max_length="12", verbose_name='Telefoon 1', blank=True)
    telefoon2 = models.CharField(max_length="12", verbose_name='Telefoon 2', blank=True)
    telefoon3 = models.CharField(max_length="12", verbose_name='Telefoon 3', blank=True)

    def __unicode__(self):
        return self.fullname


class Kid(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    slug = AutoSlugField(populate_from='fullname', max_length=100, always_update=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    birth_date = models.DateField('Geboortedatum', blank=True, null=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    image = ImageField(upload_to='kids', help_text='De hoofdfoto van het kind', verbose_name='Hoofdbeeld', blank=True)
    objects = models.Manager()

    parents = models.ManyToManyField('Parent', related_name='kids', blank=True)
    group = models.ForeignKey('Group', related_name='kids', blank=True,)

    def __unicode__(self):
        return self.name

    @property
    def age(self):
        from dateutil.relativedelta import relativedelta
        import datetime
        today = datetime.date.today()
        return u'%s jaar, %s maand(en)' % (relativedelta(today, self.birth_date).years, relativedelta(today, self.birth_date).months)

    def get_absolute_url(self):
        return reverse('KidView', kwargs={'slug': self.slug})


class Caretaker(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    slug = AutoSlugField(populate_from='fullname', max_length=100, always_update=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    birth_date = models.DateField('Geboortedatum', blank=True, null=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    image = ImageField(upload_to='caretakers', help_text='Een foto van de verzorgster', verbose_name='Foto', blank=True)
    objects = models.Manager()

    group = models.ForeignKey('Group', related_name='caretakers', blank=True,)

    def __unicode__(self):
        return self.name

    @property
    def age(self):
        from dateutil.relativedelta import relativedelta
        import datetime
        today = datetime.date.today()
        return u'%s jaar, %s maand(en)' % (relativedelta(today, self.birth_date).years, relativedelta(today, self.birth_date).months)

    def get_absolute_url(self):
        return reverse('CaretakerView', kwargs={'slug': self.slug})