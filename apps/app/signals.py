from django.db.models.signals import post_save, post_migrate, post_delete, post_init
from django.db.models.signals import pre_save, pre_migrate, pre_delete, pre_init
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from apps.utils.shortcuts import get_object_or_none, get_list_or_none


