import re


def select_regex(txt, regex=r"Conclusie:(.*?)DISCLAIMER"):
    if not txt:
        return None
    txt = str(txt).replace("\n", "").replace("\t", "")
    list = []
    for item in re.finditer(regex, txt):
        list.append(txt[item.start(): item.end()])
    return "\n".join(list)


def regex_missing(txt, regex=r"Conclusie:(.*?)DISCLAIMER"):
    if not txt:
        return True
    if len(list(re.finditer(regex, txt))) == 0:
        return True
    return False


def normalize_regex(txt, targets):
    for target in targets:
        if len(list(re.finditer(re.compile(target['Regex'], re.IGNORECASE), txt))) > 0:
            return target['Type']
    return ""


