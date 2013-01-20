# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('theW4', ['Item'])

        # Adding model 'Newsletter'
        db.create_table('newsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('theW4', ['Newsletter'])

        # Adding M2M table for field items on 'Newsletter'
        db.create_table('newsletter_items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm['theW4.newsletter'], null=False)),
            ('item', models.ForeignKey(orm['theW4.item'], null=False))
        ))
        db.create_unique('newsletter_items', ['newsletter_id', 'item_id'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('item')

        # Deleting model 'Newsletter'
        db.delete_table('newsletter')

        # Removing M2M table for field items on 'Newsletter'
        db.delete_table('newsletter_items')


    models = {
        'theW4.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'theW4.newsletter': {
            'Meta': {'object_name': 'Newsletter', 'db_table': "'newsletter'"},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['theW4.Item']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['theW4']