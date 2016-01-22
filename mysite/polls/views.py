from django.shortcuts import render

import datetime
from datetime import date
from datetime import datetime, timedelta
import email, getpass, imaplib, os
import subprocess, sys
import re
import operator
import time
import datetime
import subprocess, sys
import base64

# Create your views here.
from django.http import HttpResponse


def index(request):
    print "hola"
    trello_list = "5633690ea78921c88e065a9f"
    trello_creds = "key=bb81236a659a975e9be39d630988f319&token=47da9dc1581e9e0b05052a347cf9ff8e4ba70e08c176897b07ac0516709e1a04"
    output = subprocess.check_output(["curl","-s","-XGET","https://api.trello.com/1/lists/" + trello_list + "?fields=name&cards=open&card_fields=name&" + trello_creds]);
    print output

    #user = raw_input("Ingresar usuario de correo: ")
    return HttpResponse("Hello, world. You're at the polls index." + str(output))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

