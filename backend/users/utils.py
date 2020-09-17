def get_user_photo_path(instance, filename):
    return "photos/{}/{}".format(instance.username, filename)