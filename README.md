# django-filemanager-ui

### Installing
Get script from github with command:
```
git clone https://github.com/suryadana/django-filemanager-ui.git
```
Copy **filemanager** folder to your project
Add `filemanager` to your `INSTALLED_APPS`:
```    INSTALLED_APPS = (
        ...
        'filemanager',
        ...
    )
```

Hook this app into your ``urls.py``:
```
    urlpatterns = patterns('',
        ...
        url(r'filemanager/', include('filemanager.urls')),
        ...
    )
```

### Thanks to
Thanks for [filemanager-ui](https://github.com/guillermomartinez/filemanager-ui)
Thanks for [django-filemanager](https://github.com/byteweaver/django-filemanager)