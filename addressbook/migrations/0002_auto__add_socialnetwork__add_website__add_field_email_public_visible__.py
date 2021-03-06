# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialNetwork'
        db.create_table('addressbook_socialnetwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='20')),
            ('public_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['SocialNetwork'])

        # Adding model 'Website'
        db.create_table('addressbook_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressbook.Contact'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='20')),
            ('public_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact_visible', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('addressbook', ['Website'])

        # Adding field 'Email.public_visible'
        db.add_column('addressbook_email', 'public_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Email.contact_visible'
        db.add_column('addressbook_email', 'contact_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Email.type'
        db.alter_column('addressbook_email', 'type', self.gf('django.db.models.fields.CharField')(max_length='20'))
        # Adding field 'PhoneNumber.public_visible'
        db.add_column('addressbook_phonenumber', 'public_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PhoneNumber.contact_visible'
        db.add_column('addressbook_phonenumber', 'contact_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'PhoneNumber.type'
        db.alter_column('addressbook_phonenumber', 'type', self.gf('django.db.models.fields.CharField')(max_length='20'))
        # Adding field 'Contact.blurb'
        db.add_column('addressbook_contact', 'blurb',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.profile_image'
        db.add_column('addressbook_contact', 'profile_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.qr_image'
        db.add_column('addressbook_contact', 'qr_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Address.public_visible'
        db.add_column('addressbook_address', 'public_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Address.contact_visible'
        db.add_column('addressbook_address', 'contact_visible',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Address.type'
        db.alter_column('addressbook_address', 'type', self.gf('django.db.models.fields.CharField')(max_length='20'))

    def backwards(self, orm):
        # Deleting model 'SocialNetwork'
        db.delete_table('addressbook_socialnetwork')

        # Deleting model 'Website'
        db.delete_table('addressbook_website')

        # Deleting field 'Email.public_visible'
        db.delete_column('addressbook_email', 'public_visible')

        # Deleting field 'Email.contact_visible'
        db.delete_column('addressbook_email', 'contact_visible')


        # Changing field 'Email.type'
        db.alter_column('addressbook_email', 'type', self.gf('django.db.models.fields.CharField')(max_length='8'))
        # Deleting field 'PhoneNumber.public_visible'
        db.delete_column('addressbook_phonenumber', 'public_visible')

        # Deleting field 'PhoneNumber.contact_visible'
        db.delete_column('addressbook_phonenumber', 'contact_visible')


        # Changing field 'PhoneNumber.type'
        db.alter_column('addressbook_phonenumber', 'type', self.gf('django.db.models.fields.CharField')(max_length='4'))
        # Deleting field 'Contact.blurb'
        db.delete_column('addressbook_contact', 'blurb')

        # Deleting field 'Contact.profile_image'
        db.delete_column('addressbook_contact', 'profile_image')

        # Deleting field 'Contact.qr_image'
        db.delete_column('addressbook_contact', 'qr_image')

        # Deleting field 'Address.public_visible'
        db.delete_column('addressbook_address', 'public_visible')

        # Deleting field 'Address.contact_visible'
        db.delete_column('addressbook_address', 'contact_visible')


        # Changing field 'Address.type'
        db.alter_column('addressbook_address', 'type', self.gf('django.db.models.fields.CharField')(max_length='5'))

    models = {
        'addressbook.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': "'10'"})
        },
        'addressbook.contact': {
            'Meta': {'object_name': 'Contact'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.ContactGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'", 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'blank': 'True'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qr_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'40'", 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'addressbook.contactgroup': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'ContactGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'addressbook.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        'addressbook.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        'addressbook.socialnetwork': {
            'Meta': {'object_name': 'SocialNetwork'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        'addressbook.website': {
            'Meta': {'object_name': 'Website'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['addressbook']
