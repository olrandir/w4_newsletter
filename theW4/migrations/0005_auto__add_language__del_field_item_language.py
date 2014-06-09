# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table('theW4_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(default='el', max_length=3, db_index=True)),
            ('culture_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('theW4', ['Language'])

        # Deleting field 'Item.language'
        db.delete_column('item', 'language')

        # Adding M2M table for field language on 'Item'
        db.create_table('item_language', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['theW4.item'], null=False)),
            ('language', models.ForeignKey(orm['theW4.language'], null=False))
        ))
        db.create_unique('item_language', ['item_id', 'language_id'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table('theW4_language')

        # Adding field 'Item.language'
        db.add_column('item', 'language',
                      self.gf('django.db.models.fields.CharField')(default='el_gr', max_length=20, db_index=True),
                      keep_default=False)

        # Removing M2M table for field language on 'Item'
        db.delete_table('item_language')


    models = {
        'theW4.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'item'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['theW4.Language']", 'symmetrical': 'False'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'theW4.language': {
            'Meta': {'object_name': 'Language'},
            'culture_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "'el'", 'max_length': '3', 'db_index': 'True'})
        },
        'theW4.newsletter': {
            'Meta': {'object_name': 'Newsletter', 'db_table': "'newsletter'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['theW4.Item']", 'symmetrical': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['theW4']