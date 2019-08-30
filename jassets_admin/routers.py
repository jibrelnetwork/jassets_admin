from django.db import models
from django.db.models import QuerySet


# class JAssetsManager(models.Manager):
#     def get_queryset(self):
#         qs = QuerySet(self.model)
#         qs = qs.using('jassets')
#         return qs


class JAssetsRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """

    def get_db(self, model, **hints):
        if model._meta.app_label == 'jassets_admin':
            return 'jassets'
        return 'default'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        return self.get_db(model, **hints)

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        return self.get_db(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if (obj1._meta.app_label == 'jassets_admin' or
                obj2._meta.app_label == 'jassets_admin'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'jassets_admin':
            return db == 'jassets'
        return None
