import os
from django.shortcuts import render

from django.db import models, transaction
from django.views.generic import (ListView, FormView)

from yangpt_app.models import User, Chat

# Create your views here.


class YanGptLV(ListView):
    model = Chat
    template_name = 'index.html'
    context_object_name = 'chats'
