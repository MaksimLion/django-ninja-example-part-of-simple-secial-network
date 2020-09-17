from typing import List
from ninja import Query, Router
from base.auth import auth
from .services import (
    send_message,
    get_dialogs,
    create_new_dialog,
    get_messages_by_dialog,
    get_is_my_message,

)
from .schemas import (
    MessageFilters,
    MessageRequestSchema,
    MessageResponseSchema,
    DialogSchema,
    CreateDialogSchema
)


router = Router()


@router.get("/dialogs/", auth=auth, response=List[DialogSchema])
def my_dialogs(request):
    dialogs = get_dialogs(request.auth.id)
    return dialogs


@router.post("/dialogs/", auth=auth, response=DialogSchema)
def create_dialog(request, dialog: CreateDialogSchema):
    dialog = create_new_dialog(dialog.users)
    return dialog


@router.post("/dialog/{dialog_id}/messages", auth=auth, response=MessageResponseSchema)
def send_message_to_dialog(request, dialog_id, message: MessageRequestSchema):
    message = send_message(request.auth.id, dialog_id, message.text)
    return message


@router.get("/dialog/{dialog_id}/messages", auth=auth, response=List[MessageResponseSchema])
def messages_by_dialog(request, dialog_id):
    messages = get_messages_by_dialog(dialog_id)

    for message in messages:
        message.is_my_message = get_is_my_message(message, request.auth.id)
    return messages

