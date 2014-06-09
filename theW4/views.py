from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from models import Newsletter, Language
from settings import W4_SETTING_HTML_DIR, W4_SETTING_URL

def list(request):
	try:
		english	= Language.objects.get(language_code="en")
		list_en = Newsletter.objects.filter(language__id=english.id).order_by('-date')
	except DoesNotExist:
		list_en = []

	try:
		greek = Language.objects.get(language_code="el")
		list_gr = Newsletter.objects.filter(language__id=greek.id).order_by('-date')
	except ObjectDoesNotExist:
		list_gr = []

	return render_to_response('list.html', {
		'url': W4_SETTING_URL,
        'list_en': list_en,
        'list_gr': list_gr,
    }, context_instance = RequestContext(request))
