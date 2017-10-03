from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.


class UserDetails(models.Model):
    username = models.CharField(_('Username'), max_length=250, unique=True)
    email = models.EmailField(
        _('email address'), max_length=250, blank=True, null=True)
    avatar_url = models.CharField(
        _('Avatar Url'), max_length=250, blank=True, null=True)
    gravatar_id = models.CharField(
        _('Gravatar Url'), max_length=250, blank=True, null=True)
    url = models.CharField(_('Url'), max_length=250, blank=True, null=True)
    html_url = models.CharField(
        _('Html Url'), max_length=250, blank=True, null=True)
    followers_url = models.CharField(
        _('Followers Url'), max_length=250, blank=True, null=True)
    following_url = models.CharField(
        _('Following Url'), max_length=250, blank=True, null=True)
    gists_url = models.CharField(
        _('Gists Url'), max_length=250, blank=True, null=True)
    starred_url = models.CharField(
        _('Starred Url'), max_length=250, blank=True, null=True)
    subscriptions_url = models.CharField(
        _('Subscriptions Url'), max_length=250, blank=True, null=True)
    organizations_url = models.CharField(
        _('Organizations Url'), max_length=250, blank=True, null=True)
    repos_url = models.CharField(
        _('Repos Url'), max_length=250, blank=True, null=True)
    events_url = models.CharField(
        _('Events Url'), max_length=250, blank=True, null=True)
    received_events_url = models.CharField(
        _('Received Events Url'), max_length=250, blank=True, null=True)
    user_type = models.CharField(
        _('User type'), max_length=250, blank=True, null=True)
    site_admin = models.CharField(
        _('Site Admin'), max_length=250, blank=True, null=True)
    score = models.CharField(_('Score'), max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to='%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.username)

    def image_tag(self):
        return u'<img src="%s" />' % "{0}/{1}".format(settings.STATIC_URL,self.image)
    image_tag.allow_tags = True

class Hits(models.Model):
    key = models.CharField(max_length=250, blank=True, null=True)
    value = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated = models.DateField(auto_now=True, null=True)

    def __unicode__(self):
        return unicode(self.key)


