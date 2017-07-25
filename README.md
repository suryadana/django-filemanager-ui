# django-filemanager-ui


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

The application already support with tinymce editor.

### Installing

Get script from github with command:
```
git clone https://github.com/suryadana/django-filemanager-ui.git
```
Copy **filemanager** folder to your project
Add `filemanager` to your `INSTALLED_APPS`:
```   
    INSTALLED_APPS = (
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