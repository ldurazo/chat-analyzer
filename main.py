import emoji


def get_emojis_in_message(row):
    message = row.text
    emojis = ""
    if message is None or type(message) != str:
        return emojis
    return emojis.join(c for c in message if c in emoji.UNICODE_EMOJI)


class Row:
    text = "Hello 🤭"

print(get_emojis_in_message(Row()))