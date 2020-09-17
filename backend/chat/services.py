from django.shortcuts import get_object_or_404
from users.models import User
from .models import Dialog, Message


def send_message(from_user_id, to_dialog, text):
    dialog = get_object_or_404(Dialog, pk=to_dialog)
    message = dialog.messages.create(from_user_id=from_user_id, to_dialog=to_dialog, text=text)
    dialog.save()

    return message


def get_dialogs(user_id):
    dialogs = Dialog.objects.filter(users__id=user_id)
    return dialogs


def create_new_dialog(users):
    dialog = Dialog.objects.get_or_create_dialog(users)
    return dialog


def get_messages_by_dialog(dialog_id):
    return Message.objects.filter(to_dialog_id=dialog_id)


def get_is_my_message(message, user_id):
    return message.from_user_id == user_id
