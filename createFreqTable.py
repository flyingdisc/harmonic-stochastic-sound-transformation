""" 
@author soesilo wijono 2014 
Audio Signal Processing for Music Applications (UPF Barcelona and Stanford) 
Blog: http://blog.wijono.org/2015/01/sound-transformation-with-mtgs-spectral.html 
This code will print a list of frequencies from MIDI notes
""" 

import numpy as np

# midi note number to frequency
# http://subsynth.sourceforge.net/midinote2freq.html
midi2freq = {45 : 110.0000000000, 
            46 : 116.5409403795,  
            47 : 123.4708253140,  
            48 : 130.8127826503, 
            49 : 138.5913154884, 
            50 : 146.8323839587, 
            51 : 155.5634918610, 
            52 : 164.8137784564, 
            53 : 174.6141157165, 
            54 : 184.9972113558, 
            55 : 195.9977179909, 
            56 : 207.6523487900, 
            57 : 220.0000000000, 
            58 : 233.0818807590, 
            59 : 246.9416506281, 
            60 : 261.6255653006, 
            61 : 277.1826309769, 
            62 : 293.6647679174}

# array of MIDI notes in D Dorian scale
dDorian = [50,52,53,55,57,59,60,62]

# array of index to 124 MIDI D Dorian scale notes
# -1 is no sound
note1 = [-1,6,1,-1,6,1,2,3,3,-1,
        5,6,5,6,5,3,-1,6,1,-1,
        6,1,2,3,3,-1,5,6,5,6,
        5,3,-1,6,1,3,2,2,3,2,
        1,6,2,1,6,-1,6,1,3,2,
        2,3,2,1,6,2,1,6,-1,6,
        1,-1,6,1,2,3,3,-1,5,6,
        5,6,5,3,-1,6,1,-1,6,1,
        2,3,3,-1,5,6,5,6,5,3,
        -1,6,1,3,2,2,3,2,1,6,
        2,1,6,-1,6,1,3,2,2,3,
        2,1,6,2,1,6,-1,6,1,-1,
        6,1,2,3]

# array of offset to the MIDI notes above
# -1 is no sound, 0 is no scaling
diff1 = [-1,-12,0,-1,-12,0,0,0,0,-1,
        0,0,0,0,0,0,-1,-12,0,-1,
        -12,0,0,0,0,-1,0,0,0,0,
        0,0,-1,-12,0,0,0,0,0,0,
        0,-12,0,0,-12,-1,-12,0,0,0,
        0,0,0,0,-12,0,0,-12,-1,-12,
        0,-1,-12,0,0,0,0,-1,0,0,
        0,0,0,0,-1,-12,0,-1,-12,0,
        0,0,0,-1,0,0,0,0,0,0,
        -1,-12,0,0,0,0,0,0,0,-12,
        0,0,-12,-1,-12,0,0,0,0,0,
        0,0,-12,0,0,-12,-1,-12,0,-1,
        -12,0,0,0]

eps = np.finfo(np.float).eps

# index to midi note number
notes = []
for i in range(len(note1)):
    if note1[i] == -1:
        notes.append(-1)
    else:
        notes.append( dDorian[note1[i]] + diff1[i] )

# midi note number to frequency
freqs = []
for i in range(len(notes)):
    if notes[i] == -1:
        freqs.append(eps)
    else:
        freqs.append( midi2freq[notes[i]] )

print freqs        
