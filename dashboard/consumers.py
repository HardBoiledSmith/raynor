from channels import Group


def connect_log_stream(message):
    Group('stream').add(message.reply_channel)


def disconnect_log_stream(message):
    Group('stream').discard(message.reply_channel)