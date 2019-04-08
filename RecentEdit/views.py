from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
import operator
from collections import OrderedDict
from django.utils import timezone




class HomeView(TemplateView):
    template_name= 'RecentEdit/response.html'
    def get(self,request):
    	S = requests.Session()
    	URL = "https://en.wikipedia.org/w/api.php"
    	params = {"format": "json", "rcprop": "title|ids|sizes|flags|user|timestamp", "list": "recentchanges", "action": "query", "rclimit": "500"}
    	# print(params)
    	R = S.get(url=URL, params=params)
    	DATA = R.json()
    	# print(DATA)
    	q = DATA['query']
    	edits = q['recentchanges']
    	tStamp = []

    	
    	for i in range(len(edits)):
    		# print(edits[i])
    		tStamp.append(edits[i]["timestamp"])
    	# print(tStamp)
    	
    	
    	
    	now = timezone.now()
    	print("timenow")
    	print(now)
    	
    	
    	d= {}
    	
    	for i in range(0,500):
    		if edits[i]['user'] in d.keys():
    			d[edits[i]['user']]=d[edits[i]['user']]+1
    		else:
    			d[edits[i]['user']]=1
    		# print(edits[i]['title'] ,' ',  edits[i]['user'])
    	items = [(v, k) for k, v in d.items()]
    	items.sort()
    	items.reverse()
    	items = [(k, v) for v, k in items]
    	# print(items)

    	args={'edits':edits,'q':q,'params':params,'d':d,'items':items}
    	return render(request,self.template_name, args)