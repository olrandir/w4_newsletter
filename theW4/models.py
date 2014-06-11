# -*- coding: utf-8 -*-
from django.db import models
from django.template import Context
from django.template.loader import get_template
from datetime import datetime


class Language(models.Model):
    language_code = models.CharField(max_length=3, db_index=True, default="el")
    culture_code = models.CharField(max_length=3)

    def __unicode__(self):
        return "%s_%s" % (self.language_code, self.culture_code if self.culture_code else "")

class Item(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True,null=True)
    link = models.URLField(max_length=256)
    language = models.ForeignKey(Language,null=True)
    
    created = models.DateTimeField(blank=True,null=True)
    updated = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = 'item'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return "%s [%s] (%s)" % (self.title if self.title else "untitled", 
            self.link,
            self.language if self.language else "unknown language"
            )

    def save(self, *args, **kwargs):
        if not self.id:
            # if the item has no id, then it's the first time it's been saved.
            # This means it was just created, so set the created date.
            self.created = datetime.now()
        self.updated = datetime.now()
        super(Item, self).save(*args, **kwargs) # Call the "real" save() method      

class Newsletter(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    intro = models.TextField(blank=True,null=True)
    items =  models.ManyToManyField(Item)
    outro = models.TextField(blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    language = models.ForeignKey(Language,null=True)

    created = models.DateTimeField(blank=True,null=True)
    updated = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table = 'newsletter'
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
    
    def __unicode__(self):
        return "Newsletter for %s" % (self.date)

    def save(self, *args, **kwargs):
        from settings import W4_SETTING_HTML_DIR, W4_SETTING_URL

        created = False
        if not self.id:
            # if the item has no id, then it's the first time it's been saved.
            # This means it was just created, so set the created date.
            self.created = datetime.now()
            created = True
            # find the latest newsletter id
            latest = Newsletter.objects.order_by('-id')[0]

        self.updated = datetime.now()
        super(Newsletter, self).save(*args, **kwargs) # Call the "real" save() method      
        
        if created:
            import os
            os.mkdir(os.path.join(W4_SETTING_HTML_DIR, "%s" % self.id))

        dirname = "%s%s/" % (W4_SETTING_HTML_DIR, self.id)

        # print self.items.all()
        # print dirname
        # create static html file
        context = Context({
            'title': self.title,
            'intro': self.intro,
            'outro': self.outro,
            'items': self.items.all(),
            'date': self.date,
            'url': W4_SETTING_URL,
            'id': self.id,
        })
        template = get_template('newsletter.html')
        content = template.render(context)
        
        import codecs
        f = codecs.open(dirname+"index.html","w", "utf-8")
        f.write(content)
        f.close

        #if this is the latest newsletter, create a symlink
        if created and not self.language is None and self.language.language_code=="en":
            if self.id > latest.id:
                import os
                try:
                    os.symlink(dirname+"index.html", W4_SETTING_HTML_DIR+"latest")
                except OSError, e:
                    os.remove(W4_SETTING_HTML_DIR+"latest")
                    os.symlink(dirname+"index.html", W4_SETTING_HTML_DIR+"latest")
