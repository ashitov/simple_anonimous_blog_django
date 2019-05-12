# -*- coding: utf-8 -*-
from django.shortcuts import render

from blog.models import Note


def get_blog(request):
    if request.method == 'POST':
        _text = request.POST.get('text', False)
        if _text:
            _note = Note(text=_text)
            _note.save()
        print(_text)
    notes = Note.objects.all()
    return render(request, 'blog/index.html', {'notes': notes})
