# import json
# from django.test import TestCase
# from requests import Session

# s = Session()
# payload = {
#             "id": 1,
#             "title": "راکیزه چیست؟",
#             "slug": "راکیزه-چیست",
#             "writer": "راکیزه ژن",
#             "thumbnail": "http://127.0.0.1:8000/media/images/blog/thumbnails/Forex.jpg",
#             "date": "2022-11-23T21:30:16.596002Z",
#             "content": r"<h1><span style=\"color:#2980b9\">راکیزه چیست؟</span></h1>\r\n\r\n<address><strong>راکیزه میتوکندری است.</strong></address>\r\n\r\n<p>راکیزه در واقع همان میتوکندری است.</p>",
#             "tags": "راکیزه,میتوکندری,باکتری",
#             "category": 1
#     },

# data  = s.put(url='http://127.0.0.1:8000/blog/راکیزه-چیست',json=payload)
# print(data.status_code,'\n',json.loads(data.content))


perms_map = {
    'GET': [],
    'OPTIONS': [],
    'HEAD': [],
    'POST': ['%(app_label)s.add_%(model_name)s'],
    'PUT': ['%(app_label)s.change_%(model_name)s'],
    'PATCH': ['%(app_label)s.change_%(model_name)s'],
    'DELETE': ['%(app_label)s.delete_%(model_name)s'],
}

def get_required_object_permissions():
    kwargs = {
        'app_label':' model_cls._meta.app_label',
        'model_name': 'model_cls._meta.model_name'
    }


    return [perm % kwargs for perm in perms_map['POST']]
kwargs = {
    'app_label':' model_cls._meta.app_label',
    'model_name': 'model_cls._meta.model_name'
}
a = get_required_object_permissions()
print('%(app_label)s.change_%(model_name)s' % kwargs)