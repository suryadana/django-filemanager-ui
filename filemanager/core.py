import os, re
from slugify import slugify
from filemanager import signals
from django.conf import settings
from django.core.files.base import ContentFile
from filemanager.settings import DIRECTORY, STORAGE	


class Filemanager(object):
  def __init__(self):
    self.update_path(path='')

  def update_path(self, path):
    if path is None or len(path) == 0:
      self.path = ''
      self.abspath = DIRECTORY
    else:
      self.path = self.validate_path(path)
      self.abspath = os.path.join(DIRECTORY, self.path)
    self.location = os.path.join(settings.MEDIA_ROOT, self.abspath)
    self.url = os.path.join(settings.MEDIA_URL, self.abspath)

  def validate_path(self, path):
    # replace backslash with slash
    path = path.replace('\\', '/')
    # remove leading and trailing slashes
    path = '/'.join([i for i in path.split('/') if i])
    return path

  def directory_list(self):
    listing = []
    directories, files = STORAGE.listdir(self.location)

    def _helper(name, filetype):
    	perviewfull = ''
    	perview = ''
    	urlfolder = ''
    	if filetype == 'Directory':
    		filetype= ''
    		urlfolder = '/'+name+'/'
    	else:
    		nm, ext = os.path.splitext(name)
    		filetype=ext.replace('.', '')
    		perviewfull = settings.BASE_URL+os.path.join(self.url, name)
    		perview = settings.BASE_URL+os.path.join(self.url, name)

    	return {
    			'urlfolder': urlfolder,
    	    'isdir': os.path.isdir(os.path.join(self.location, name)),
    	    'filetype': filetype,
    	    'filename': name,
    	    'lastmodified': int(os.path.getmtime(os.path.join(self.location, name))),
    	    'perviewfull': perviewfull,
    	    'perview': perview,
    	    'size': STORAGE.size(os.path.join(self.path, name)),
        }

    for directoryname in directories:
      listing.append(_helper(directoryname, 'Directory'))

    for filename in files:
      listing.append(_helper(filename, 'File'))
    return listing

  def upload_file(self, filedata):
    filename = STORAGE.get_valid_name(filedata.name)
    filename, ext = os.path.splitext(filename)
    filename = slugify(re.sub("\d+", "", filename))+ext
    filepath = os.path.join(self.path, filename)
    signals.filemanager_pre_upload.send(sender=self.__class__, filename=filename, path=self.path, filepath=filepath)
    STORAGE.save(filepath, filedata)
    signals.filemanager_post_upload.send(sender=self.__class__, filename=filename, path=self.path, filepath=filepath)
    return filename

  def create_directory(self, name):
    name = STORAGE.get_valid_name(name)

    tmpfile = os.path.join(name, '.tmp')

    path = os.path.join(self.path, tmpfile)

    STORAGE.save(path, ContentFile(''))
    STORAGE.delete(path)
    return name

  def rename(self, nameold, name):
    nameold, ext = os.path.splitext(nameold)
    nameold = nameold+ext
    name = slugify(re.sub('\d+', '', STORAGE.get_valid_name(name)))+ext
    oldpath = os.path.join(self.location, nameold)
    newpath = os.path.join(self.location, name)
    if os.path.exists(newpath):
      return False
    else:
      os.rename(oldpath, newpath)
      return name
    return False

  def delete(self, name):
    path = os.path.join(self.location, name)
    if os.path.isdir(path):
      if not os.listdir(path):
        os.removedirs(path)
      else:
        return False
    else:
      os.remove(path)
    return name