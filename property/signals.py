from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry



@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.

    Update Book document index if related `books.Publisher` (`publisher`),
    `books.Author` (`authors`), `books.Tag` (`tags`) fields have been updated
    in the database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'property':
        if model_name == 'device':
            instances = instance.devices.all()
            for _instance in instances:
                registry.update(_instance)

        if model_name == 'inpqiry':
            instances = instance.inpqiries.all()
            for _instance in instances:
                registry.update(_instance)

        