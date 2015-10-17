# photostream
Website that shows photos from Flickr using Django.

For more info about Flickr API, please visit this link:
Flickr: http://www.flickr.com/services/feeds/

Public feeds: → https://api.flickr.com/services/feeds/photos_public.gne

Features:
- On page load the web app loads the public feed images.
- The user can enter a keyword and click on the search button and the app returns images with relevant tags.
- The user could Facebook 'like' the images.

Required Python Libraries:
- feedparser
- HTMLParser
- urllib

When using the app, you must first configure the setting.py:
- Put in your template directory, which is located under photostream->photoapp->templates.

For production, follow the django project instructions:
- https://docs.djangoproject.com/en/1.8/

Author:
Fernando Cuevas Jr.
