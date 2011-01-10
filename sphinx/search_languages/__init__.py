#! -*- encoding: utf-8 -*-

def get(lang):
    if lang == "en":
        import en
        return en
    elif lang == "ja":
        import ja
        return ja
    raise ValueError("Unsupported language code: %s" % lang)
