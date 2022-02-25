from .generate import gen
from .convert import con
from .render import ren
import os


def build(form, inst_melody, inst_bass, bpm):
    melody, bass = gen(form)

    sco = con(melody, bass, inst_melody, inst_bass, bpm)

    old_cwd = os.getcwd()
    new_cwd = "E:/xampp/htdocs/django_forms/music"
    os.chdir(new_cwd)

    file_name = ren(sco)

    os.chdir(old_cwd)

    return file_name
