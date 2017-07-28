# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from filemanager.core import Filemanager
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# Basic view
@login_required
@staff_member_required # Require admin role user
def basic(request):
	return render(request, 'basic.html')

@login_required
@staff_member_required
def connector(request):
	fm = Filemanager()
	response = {
	  "data": [],
	  "msg": {
	    "query": "",
	    "params": [None, None],
	  },
	  "status": 1,
	}
	if request.POST:
	  action = request.POST.get('action')
	  path = request.POST.get('path')
	  fm.update_path(path[1:])
	  if action == "getfolder":
			response['data'] = fm.directory_list()
			return JsonResponse(response)
	  elif action == "uploadfile":
			files = request.FILES
			if files and path:
				response['msg']['params'][0] = 0
				response['msg']['params'][1] = len(files)
				for name in files:
					f = files.get(name, None)
					upload_name = fm.upload_file(f)
					if upload_name:
						response['msg']['params'][0] += 1
				response['msg']['query'] = "BE_UPLOADALL_UPLOADS %s / %s"
	  elif action == 'newfolder':
	  	folder_name = fm.create_directory(request.POST.get('name'))
	  	if folder_name != '' and folder_name != None:
	  		response['data'] = {path: "/", 'namefile': folder_name}
	  		response['msg']['query'] = "BE_NEW_FOLDER_CREATED %s"
	  		response['msg']['params'] = ['/%s/' % folder_name]
	  elif action == 'renamefile':
	  	nameold = request.POST.get('nameold')
	  	name = request.POST.get('name')
	  	rename = fm.rename(nameold, name)
	  	if rename:
	  		response['data'] = {'newnamefile': rename, 'odlnamefile': nameold}
	  		response['msg']['params'] = "BE_RENAME_MODIFIED"
	  elif action == 'deletefile':
	  	names = request.POST.getlist('name[]')
	  	for name in names:
	  		delete_name = fm.delete(name)
	  		if delete_name:
		  		response['data'].append({'namefile': delete_name, 'status': 1, 'params': [], 'query': "BE_DELETE_DELETED"})
		  	else:
		  		response['msg']['params'] = "BE_DELETE_NOT_EMPTY"
	  			response['msg']['query'] = name+' is not empty'
	  			response['status'] = 0
	return JsonResponse(response)
