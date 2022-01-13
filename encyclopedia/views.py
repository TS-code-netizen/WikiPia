from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import random
from . import util
import markdown2


class NewEntry(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'id':'exampleFormControlInput1', 
        'placeholder':'Title'
    }))

    description = forms.CharField(label="Leave your description here", widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'id':'floatingTextarea2', 
        'placeholder':'Enter your content here',
        'style':'height: 350px'
    }))

    def clean(self):
        data = self.cleaned_data
        data_title = data.get('title')
        for item in util.list_entries():
            if item == data_title:
                raise ValidationError("This title exists!")
        return data

class EditEntry(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'id':'exampleFormControlInput1', 
    }))

    description = forms.CharField(label="Leave your description here", widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'id':'floatingTextarea2', 
        'style':'height: 350px'
    }))
   

# util.list_entries() = ['CSS', 'Django', 'Git', 'HTML', 'Python']
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    if util.get_entry(name) == None:
        return render(request, "encyclopedia/error.html", {
            "name": name
        })         

    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "content": markdown2.markdown(util.get_entry(name))
    })


def random_page(request):
    choice = random.randint(0, len(util.list_entries())-1)
    page = util.list_entries()
    return HttpResponseRedirect(reverse("entry", args=(page[choice],)))

  
def search(request):
    input_search = request.GET.get('q')
    for search_item in util.list_entries():
        if search_item == input_search:
            return HttpResponseRedirect(reverse("entry", args=(input_search,)))

    result = []
    for substring in util.list_entries():
        if input_search.casefold() in substring.casefold():
            result.append(substring)
        
    return render(request, "encyclopedia/search.html", {
        "result": result
    })


def new_entry(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title"]
            content = ('# ' + new_title + '\n\n' )
            new_content = form.cleaned_data["description"]
            content = content + new_content
            util.save_entry(new_title, content)
            return HttpResponseRedirect(reverse("entry", args=(new_title,)))
        else:
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })

    return render(request, "encyclopedia/new_entry.html", {
        "form": NewEntry()
    })


def edit(request, name):
    if request.method == "POST":
        form = EditEntry(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title"]
            new_content = form.cleaned_data["description"]
            util.save_entry(new_title, new_content)
            return HttpResponseRedirect(reverse("entry", args=(new_title,)))
        else:
            return render(request, "encyclopedia/editEntry.html", {
                "name": name,
                "form": form
            })

    description = util.get_entry(name)
    return render(request, "encyclopedia/editEntry.html", {
        "name": name,
        "form" : EditEntry(initial={'title':name, 'description':description})
    })

