import os
import time
import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from datetime import datetime
from models import *

def home(request):
    return render_to_response('dkryp/home.html',
        {}, context_instance=RequestContext(request))

def products(request):
    product_list = Product.objects.order_by('-launched')
    paginator = Paginator(product_list, settings.NUM_OF_PDT)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    
    return render_to_response('dkryp/products.html',
        {
            'products': products,
        }, context_instance=RequestContext(request))

def events(request):
    event_list = Event.objects.order_by('-date_of_event')
    paginator = Paginator(event_list, settings.NUM_OF_EVT)

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
    
    return render_to_response('dkryp/events.html',
        {
            'events': events,
        }, context_instance=RequestContext(request))

def gallery(request):
    gallery_list = Gallery.objects.order_by('-event')
    paginator = Paginator(gallery_list, settings.NUM_OF_IMG)

    page = request.GET.get('page')
    try:
        gallery = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        gallery = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        gallery = paginator.page(paginator.num_pages)
    
    return render_to_response('dkryp/gallery.html',
        {
            'gallery': gallery,
        }, context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response('dkryp/aboutus.html',
        {}, context_instance=RequestContext(request))

def contactus(request):
    return render_to_response('dkryp/contactus.html',
        {}, context_instance=RequestContext(request))
