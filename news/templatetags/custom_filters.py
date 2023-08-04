from django import template

register = template.Library()

FORBIDDEN_WORDS = ["петербург", "Петербург", "министр", "Министр"]


@register.filter()
def censor(text):
    for word in FORBIDDEN_WORDS:
        text = text.replace(word, word[0] + "*" * (len(word) - 1))
    return text
