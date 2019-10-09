from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import een
import random
import base64
from gevent import getcurrent
from gevent.pool import Pool
api = een.login("demo@een.com", "bettercloud")

# Create your views here.

def index(request):
    camera_list = api.camera_list()
    camera_list = random.sample(camera_list, k=9)
    context = {
        'camera_list': camera_list,
    }
    return render(request, 'cameras/index.html', context)

def preview(request, camera_id):
    img_list = api.image_list(esn=camera_id, asset_type="preview", time=een.timestamp("now"), count=-1)
    try:
        image_data = api.fetch_image(esn=camera_id, time=img_list.pop()['s'], asset_type="preview")
    except:
        raise Http404("Image does not exist")
    return HttpResponse(image_data, content_type="image/jpg")

def images(request, camera_id):
    img_list = api.image_list(esn=camera_id, asset_type="preview", time=een.timestamp("now"), count=-20)
    for image in img_list:
        #img = api.fetch_image(esn=camera_id, time=image['s'], asset_type="preview")
        #image['binary'] = base64.b64encode(img).decode('ascii')
        image['camera_id'] = camera_id
    
    #fetch them using a pool of 5 greenlets
    pool = Pool(5)
    pool.map(fetch_image, img_list)
    
    context = {
        'image_list': img_list
    }
    return render(request, 'cameras/images.html', context)

def fetch_image(image):
	print('Task %s started' % id(getcurrent())) #get the thread id so we can see the concurrence at work
	img = api.fetch_image(esn=image['camera_id'], time=image['s'], asset_type="preview")
	image['binary'] = base64.b64encode(img).decode('ascii')
	print('Task %s done' % id(getcurrent()))

#fetch them all!
#threads = [gevent.spawn(fetch_image, val, index) for index, val in enumerate(img_list)]
#threads = [gevent.spawn(fetch_image, image) for image in img_list]
#gevent.joinall(threads)
