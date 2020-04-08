from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.

    Updates index if fields exercise_title or related muscle groups is updated
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'feed':
        if model_name == 'exercise':
            instances = instance.exercises.all()
            for _instance in instances:
                print(_instance)
                registry.update(_instance)
        if model_name == 'muscleGroup':
            instances = instance.exercises.all()
            for _instance in instances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
    """Deletes document on deleted records.

    Deletes index if Exercise is deleted from database
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']
    if app_label == 'feed':
        if model_name == 'exercise':
            instances = instance.exercises.all()
            for _instance in instances:
                # registry.update(_instance)
                registry.delete(_instance, raise_on_error=False)
        if model_name == 'muscleGroup':
            instances = instance.exercises.all()
            for _instance in instances:
                # registry.update(_instance)
                registry.delete(_instance, raise_on_error=False)
