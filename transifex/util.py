import re
from hashlib import md5


def force_unicode(s, encoding='utf-8'):
    if isinstance(s, unicode):
        return s

    if hasattr(s, '__unicode__'):
        s = unicode(s)
    else:
        s = unicode(str(s), encoding)

    return s

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.

    Taken from https://code.djangoproject.com/browser/django/trunk/django/template/defaultfilters.py
    """
    import unicodedata
    value = force_unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)

def translation_hash(source_entity, context='None'):
    """
    Returns a Transifex specific hash to lookup or push specific strings.

    Taken from http://docs.transifex.com/api/translation_strings/
    """
    if isinstance(context, list):
      if context:
          keys = [source_entity] + context
      else:
          keys = [source_entity, '']
    else:
        if context == 'None' or not context:
            keys = [source_entity, '']
        else:
            keys = [source_entity, context]
    return md5(':'.join(keys).encode('utf-8')).hexdigest()
