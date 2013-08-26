from django.db import models
from sorl.thumbnail import ImageField
from datetime import *
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


class Group(models.Model):
    title = models.CharField(max_length="60", verbose_name='Groepnaam')
    groupclass = models.CharField(max_length="120", verbose_name='Groepnaam')
    groupimage = ImageField(upload_to='kids/groups', help_text='Het beeld voor deze groep', verbose_name='Groepsbeeld', blank=True, null=True)
    slug = AutoSlugField(populate_from='title', max_length=100, always_update=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('GroupView', [self.slug, ])


class Parent(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    description = models.TextField(null=True, blank=True, verbose_name='Beschrijving')
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(help_text='Vanaf wanneer is deze actief', verbose_name='Publicatiedatum', default=datetime.now())
    unpublish_at = models.DateTimeField(help_text='Wanneer stopt deze actie', verbose_name='Depublicatiedatum', default=datetime.now() + timedelta(days=7))
    image = ImageField(upload_to='kids', help_text='De hoofdfoto van het kind', verbose_name='Hoofdbeeld', blank=True)
    twitter = models.CharField(max_length="120", verbose_name='Twitter nick', blank=True)
    facebook = models.CharField(max_length="120", verbose_name='Facebook account', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    telefoon1 = models.CharField(max_length="12", verbose_name='Telefoon 1', blank=True)
    telefoon2 = models.CharField(max_length="12", verbose_name='Telefoon 2', blank=True)
    telefoon3 = models.CharField(max_length="12", verbose_name='Telefoon 3', blank=True)
    objects = models.Manager()

    def __unicode__(self):
        return self.fullname


class PublishableKidManager(models.Manager):
    def get_query_set(self):
        return super(PublishableKidManager, self).get_query_set().filter(publish_at__lt=datetime.now())


class Kid(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    slug = AutoSlugField(populate_from='fullname', max_length=100, always_update=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    birth_date = models.DateField('Geboortedatum', blank=True, null=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(help_text='Vanaf wanneer is deze actief', verbose_name='Publicatiedatum', default=datetime.now())
    unpublish_at = models.DateTimeField(help_text='Wanneer stopt deze actie', verbose_name='Depublicatiedatum', default=datetime.now() + timedelta(days=7))
    image = ImageField(upload_to='kids', help_text='De hoofdfoto van het kind', verbose_name='Hoofdbeeld', blank=True)
    objects = models.Manager()

    parents = models.ManyToManyField('Parent', related_name='kids', blank=True)
    group = models.ForeignKey('Group', related_name='kids', blank=True,)

    def __unicode__(self):
        return self.name

    def is_published(self):
        if self.publish_at < datetime.now() and self.unpublish_at > datetime.now():
            return True
        else:
            return False

    @property
    def age(self):
        from dateutil.relativedelta import relativedelta
        import datetime
        today = datetime.date.today()
        return u'%s jaar, %s maand(en)' % (relativedelta(today, self.birth_date).years, relativedelta(today, self.birth_date).months)

    def _admin_is_published(self):
        if self.is_published() == True:
            return 'Ja'
        else:
            return 'Nee'

    def get_absolute_url(self):
        return reverse('KidView', kwargs={'slug': self.slug})

    _admin_is_published.short_description = 'Actief?'
    _admin_is_published.allow_tags = True


class Caretaker(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    slug = AutoSlugField(populate_from='fullname', max_length=100, always_update=True)
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    birth_date = models.DateField('Geboortedatum', blank=True, null=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(help_text='Vanaf wanneer is deze actief', verbose_name='Publicatiedatum', default=datetime.now())
    unpublish_at = models.DateTimeField(help_text='Wanneer stopt deze actie', verbose_name='Depublicatiedatum', default=datetime.now() + timedelta(days=7))
    image = ImageField(upload_to='caretakers', help_text='Een foto van de verzorgster', verbose_name='Foto', blank=True)
    objects = models.Manager()

    group = models.ForeignKey('Group', related_name='caretakers', blank=True,)

    def __unicode__(self):
        return self.name

    def is_published(self):
        if self.publish_at < datetime.now() and self.unpublish_at > datetime.now():
            return True
        else:
            return False

    @property
    def age(self):
        from dateutil.relativedelta import relativedelta
        import datetime
        today = datetime.date.today()
        return u'%s jaar, %s maand(en)' % (relativedelta(today, self.birth_date).years, relativedelta(today, self.birth_date).months)

    def _admin_is_published(self):
        if self.is_published() == True:
            return 'Ja'
        else:
            return 'Nee'

    def get_absolute_url(self):
        return reverse('CaretakerView', kwargs={'slug': self.slug})

    _admin_is_published.short_description = 'Actief?'
    _admin_is_published.allow_tags = True


class BlogEntry(models.Model):
    name = models.CharField(max_length="60", verbose_name='Naam')
    fullname = models.CharField(max_length="120", verbose_name='Volledige naam')
    description = models.TextField(verbose_name='Beschrijving', null=True, blank=True)
    birth_date = models.DateField('Geboortedatum', blank=True, null=True)

    # Dates
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(help_text='Vanaf wanneer is deze actief', verbose_name='Publicatiedatum', default=datetime.now())
    unpublish_at = models.DateTimeField(help_text='Wanneer stopt deze actie', verbose_name='Depublicatiedatum', default=datetime.now() + timedelta(days=7))
    image = ImageField(upload_to='caretakers', help_text='Een foto van de verzorgster', verbose_name='Foto', blank=True)
    objects = models.Manager()

    group = models.ForeignKey('Group', related_name='blogs', blank=True,)

    def __unicode__(self):
        return self.name

    def is_published(self):
        if self.publish_at < datetime.now() and self.unpublish_at > datetime.now():
            return True
        else:
            return False

    @property
    def age(self):
        from dateutil.relativedelta import relativedelta
        import datetime
        today = datetime.date.today()
        return u'%s jaar, %s maand(en)' % (relativedelta(today, self.birth_date).years, relativedelta(today, self.birth_date).months)

    def _admin_is_published(self):
        if self.is_published() == True:
            return 'Ja'
        else:
            return 'Nee'

    def get_absolute_url(self):
        return self.link

    _admin_is_published.short_description = 'Actief?'
    _admin_is_published.allow_tags = True