from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from html.parser import HTMLParser
import feedparser
from urllib.parse import quote
from photoapp.views.fetchFeeds import *

def main_page(request):

    if request.method=='POST':

        http_url = 'https://api.flickr.com/services/feeds/photos_public.gne?tags=' #url of Flickr API https://www.flickr.com/services/feeds/docs/photos_public/

        searchTerm = request.POST.get('searchText') #text to search for.

        imgsrc = feedParser(http_url, searchTerm)

        variables2 = RequestContext(request,{'photoposts':imgsrc})
        return render_to_response('index.html', variables2)

    else:

        http_url = 'https://api.flickr.com/services/feeds/photos_public.gne' #Flickr feed API

        imgsrc = feedParser(http_url,'')

        variables = RequestContext(request,{'photoposts':imgsrc})
        return render_to_response('index.html', variables)
