from random import randint





notes = {'1' : 0.00, '2' : 0.02, '3' : 0.03, '4' : 0.05, '5' : 0.07, '6' : 0.08, '7' : 0.10}

def rand_inst():
    return "i%d" % (randint(1, 6))



def con(melody, bass, inst_melody, inst_bass, bpm):

    if inst_melody == 'rand':
        inst_melody = rand_inst()
    if inst_bass == 'rand':
        inst_bass = rand_inst()

    melody_pitch = 8.00
    bass_bitch = melody_pitch - 1

    score = """"""

    score += "t 0 %d \n" % (bpm)
    score += "\n"

    beat = 0
    for note in melody.notes:
        pitch = melody_pitch + note.octave + notes[str(note.position)]
        print(pitch)
        score += "%s %d %d %s %s \n" % (inst_melody, beat, note.length, .5, pitch)
        beat += note.length

    #score += "%s %d 4, .5, %s \n" % (inst_melody, beat, melody_pitch)
    score += "\n"

    beat = 0
    for note in bass.notes:
        pitch = bass_bitch + note.octave + notes[str(note.position)]
        score += "%s %d %d %s %s \n" % (inst_bass, beat, note.length, .5, pitch)
        beat += note.length

    score += "%s %d 4, .5, %s \n" % (inst_bass, beat, bass_bitch - 2)


    return score
