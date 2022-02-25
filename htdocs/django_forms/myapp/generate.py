from random import randint



class Note(object):
    def __init__(self, position, octave, length):
        self.position = position
        self.octave = octave
        self.length = length

class Next_Note(object):
    def __init__(self, note):
        self.position = note.position
        self.octave = note.octave



class Current_Measure(object):
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

class Last_Measure(object):
    def __init__(self, notes):
        self.notes = notes



class Current_Section(object):
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def add_notes(self, notes):
        for note in notes:
            self.notes.append(note)

class Last_Section(object):
    def __init__(self, section):
        self.notes = section.notes



class Score(object):
    def __init__(self):
        self.notes = []

    def add_notes(self, notes):
        for note in notes:
            self.notes.append(note)

    def add_note(self, note):
        self.notes.append(note)



def chance(positions):
    num = randint(0, 100)

    if num < positions[0]:
        return 1

    elif num < positions[0] + positions[1]:
        return 2

    elif num < positions[0] + positions[1] + positions[2]:
        return 3

    elif num < positions[0] + positions[1] + positions[2] + positions[3]:
        return 4

    elif num < positions[0] + positions[1] + positions[2] + positions[3] + positions[4]:
        return 5

    elif num < positions[0] + positions[1] + positions[2] + positions[3] + positions[4] + positions[5]:
        return 6

    else:
        return 7

def change_pos(last_pos):
    option1 = [1, 3, 5]

    if last_pos in option1:
        option2 = [6, 6, 6, 6]
        option2[randint(0, 3)] = 7

        pos1 = 25
        pos2 = option2[0]
        pos3 = 25
        pos4 = option2[1]
        pos5 = 25
        pos6 = option2[2]
        pos7 = option2[3]

        return (pos1, pos2, pos3, pos4, pos5, pos6, pos7)

    else:
        option2 = [3, 3, 3, 3]
        option2[randint(0, 3)] = 4

        pos1 = 29
        pos2 = option2[0]
        pos3 = 29
        pos4 = option2[1]
        pos5 = 29
        pos6 = option2[2]
        pos7 = option2[3]

        return (pos1, pos2, pos3, pos4, pos5, pos6, pos7)

def change_oct(oct, pos):
    num = randint(0, 100)

    if oct == 1 and pos > 4:
        if num < 80:
            return 0
        else:
            return 1
    elif oct == 1 and pos < 4:
        if num < 20:
            return 0
        else:
            return 1
    elif oct == 1:
        if num < 5:
            return 0
        else:
            return 1


    elif oct == 0 and pos > 4:
        if num < 20:
            return -1
        elif num < 80:
            return 0
        else:
            return 1
    elif oct == 0 and pos < 4:
        if num < 20:
            return -1
        elif num < 80:
            return 0
        else:
            return 1
    elif oct == 0:
        if num < 5:
            return -1
        elif num < 95:
            return 0
        else:
            return 1

    elif oct == -1 and pos > 4:
        if num < 80:
            return -1
        else:
            return 0
    elif oct == -1 and pos < 4:
        if num < 20:
            return -1
        else:
            return 0
    else:
        if num < 80:
            return -1
        else:
            return 0

def new_section():
    last = Note(1, 0, 1)
    section = Current_Section()
    section.add_note(last)

    for x in range(0, 31):
        oct = change_oct(last.octave, last.position)
        chances =  change_pos(last.position)
        pos = chance(chances)
        last = Note(pos, oct, 1)
        section.add_note(last)

    return section

def place(form):
    if form == "a":
        melody.add_notes(section_a.notes)
    elif form == "b":
        melody.add_notes(section_b.notes)
    elif form == "c":
        melody.add_notes(section_c.notes)
    elif form == "d":
        melody.add_notes(section_d.notes)

def create_bass():
    global bass
    bass = Score()

    count = 0.0
    for note in melody.notes:

        if count == 0.0:
            new_note = Note(note.position, note.octave, 4)
            bass.add_note(new_note)

        count += note.length

        if count >= 4.0:
            count = 0.0



def gen(form):
    global section_a
    global section_b
    global section_c
    global section_d

    global melody

    first_8 = form[0]
    second_8 = form[1]
    third_8 = form[2]
    fourth_8 = form[3]

    melody = Score()

    section_a = new_section()
    section_b = new_section()
    section_c = new_section()
    section_d = new_section()

    place(first_8)
    place(second_8)
    place(third_8)
    place(fourth_8)

    create_bass()

    return (melody, bass)
