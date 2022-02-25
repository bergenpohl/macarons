import ctcsound
import random
import string

orc = """
sr=44100
ksmps=32
nchnls=2
0dbfs=1

instr 1
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .8
outs aout, aout
endin

instr 2
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .7
outs aout, aout
endin

instr 3
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .6
outs aout, aout
endin

instr 4
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .5
outs aout, aout
endin

instr 5
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .4
outs aout, aout
endin

instr 6
ipch = cps2pch(p5, 12)
kenv linsegr 0, .05, 1, .05, .7, .4, 0
aout vco2 p4 * kenv, ipch
aout moogladder aout, 2000, .3
outs aout, aout
endin
"""

def rand_string():
    size = 5
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return ''.join(random.choice(chars) for x in range(size))


def ren(sco):
    file_name = rand_string() + ".wav"

    c = ctcsound.Csound()
    c.setOption("-o%s" % (file_name))

    c.compileOrc(orc)
    c.readScore(sco)
    c.start()
    c.perform()
    c.reset()

    return file_name
