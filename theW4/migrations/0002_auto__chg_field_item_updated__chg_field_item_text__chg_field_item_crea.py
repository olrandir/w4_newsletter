# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.updated'
        db.alter_column('item', 'updated', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Item.text'
        db.alter_column('item', 'text', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Item.created'
        db.alter_column('item', 'created', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Newsletter.date'
        db.alter_column('newsletter', 'date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Item.updated'
        db.alter_column('item', 'updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 9, 0, 0)))

        # Changing field 'Item.text'
        db.alter_column('item', 'text', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Item.created'
        db.alter_column('item', 'created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 9, 0, 0)))

        # Changing field 'Newsletter.date'
        db.alter_column('newsletter', 'date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 9, 0, 0)))

    models = {
        'theW4.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'theW4.newsletter': {
            'Meta': {'object_name': 'Newsletter', 'db_table': "'newsletter'"},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['theW4.Item']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['theW4']