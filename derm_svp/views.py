# -*- coding: utf-8 -*-

import datetime
from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from pages.models import Page
from fingerprints.forms import FingerPrintForm

def home_page(request):
    c = {}
    c.update(csrf(request))
    c['res'] = Page.get_page_by_slug('res')
    c['how'] = Page.get_page_by_slug('how')
    c['plus'] = Page.get_page_by_slug('plus')
    c['svp'] = Page.get_page_by_slug('svp')
    c['derm'] = Page.get_page_by_slug('derm')
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def add_fingerprint_page(request):
    c = {}
    c.update(csrf(request))
    c['form_finger'] = FingerPrintForm()
    return render_to_response('add_fingerprint.html', c, context_instance=RequestContext(request))