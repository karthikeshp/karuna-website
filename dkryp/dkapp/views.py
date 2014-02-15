import os
import time
import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from datetime import datetime
from models import *

def home(request):
    return render_to_response('dkryp/home.html',
        {}, context_instance=RequestContext(request))

def events(request):
    events = Event.objects.all()
    return render_to_response('dkryp/events.html',
        {
            'events': events,
        }, context_instance=RequestContext(request))

def gallery(request):
    gallery = Gallery.objects.all()
    return render_to_response('dkryp/gallery.html',
        {
            'gallery': gallery,
        }, context_instance=RequestContext(request))