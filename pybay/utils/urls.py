from urllib.parse import quote


def url_builder(path, **kwargs):
    base = "/" + "/".join(path)
    if kwargs:
        url_args = ",".join([f"{quote(k)}={quote(v)}" for k, v in kwargs.items()])
        return "?".join([base, url_args])
    return quote(base)
