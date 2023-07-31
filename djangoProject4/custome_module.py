
def my_filter(dic: dict, kys:list):
    """
    filter a dictionary by custome keys
    """
    _d = dic.copy()
    for i in dic.keys():

        if i not in kys:
            del _d[i]
    return _d


def slugify(title):
    title = [i for i in title if i.isalnum() or i == ' ']
    slug = ''.join(title).replace(' ', '-')
    return slug

