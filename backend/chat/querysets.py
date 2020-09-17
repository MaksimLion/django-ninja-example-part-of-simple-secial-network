from django.db import models


class DialogQuerySet(models.QuerySet):
    def get_or_create_dialog(self, user_ids):
        dialogs = self.annotate(users_count=models.Count('users'))\
            .filter(users_count=len(user_ids))

        for user_id in user_ids:
            dialogs.filter(users__pk=user_id)

        if dialogs:
            return dialogs.first()

        dialog = self.create()
        dialog.users.add(*user_ids)
        return dialog