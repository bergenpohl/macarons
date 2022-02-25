from django.shortcuts import render
from django.http import HttpResponse
from .forms import custom_form
from .run import build
import os


def index(request):

    return render(request, 'index.html')


def quick(request):

    if request.method == "POST":
        file_name = build(('a', 'a', 'b', 'a'), 'i1', 'i1', 120)

        mus_dir = "E:/xampp/htdocs/django_forms/music/"

        with open("%s%s" % (mus_dir, file_name), "rb") as raw:
            file = raw.read()

        os.remove("%s%s" % (mus_dir, file_name))

        response = HttpResponse(file, content_type="audio/wav")
        response['Content-Disposition'] = 'attachment; filename="music.wav"'
        return response

    return render(request, 'quick.html')


def custom(request):

    if request.method == "POST":
        form = custom_form(request.POST)
        if form.is_valid():
            bpm = form.cleaned_data['bpm']
            melody = form.cleaned_data['melody']
            bass = form.cleaned_data['bass']
            first_eight = form.cleaned_data['first_eight']
            second_eight = form.cleaned_data['second_eight']
            third_eight = form.cleaned_data['third_eight']
            fourth_eight = form.cleaned_data['fourth_eight']

            form = (first_eight, second_eight, third_eight, fourth_eight)

            file_name = build(form, melody, bass, bpm)

            mus_dir = "E:/xampp/htdocs/django_forms/music/"

            with open("%s%s" % (mus_dir, file_name), "rb") as raw:
                file = raw.read()

            os.remove("%s%s" % (mus_dir, file_name))


            response = HttpResponse(file, content_type="audio/wav")
            response['Content-Disposition'] = 'attachment; filename="music.wav"'
            return response

        else:
            file_name = run.build(('a', 'a', 'b', 'a'), 'i1', 'i2', 120)

            mus_dir = "E:/xampp/htdocs/django_forms/music/"

            with open("%s%s" % (mus_dir, file_name), "rb") as raw:
                file = raw.read()

            os.remove("%s%s" % (mus_dir, file_name))

            response = HttpResponse(file, content_type="audio/wav")
            response['Content-Disposition'] = 'attachment; filename="music.wav"'
            return response

    form = custom_form()
    return render(request, 'custom.html', {'form': form})


def contact(request):

    return render(request, 'contact.html')
