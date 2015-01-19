""" 
@author soesilo wijono 2014 
Audio Signal Processing for Music Applications (UPF Barcelona and Stanford) 
Blog: http://blog.wijono.org/2015/01/sound-transformation-with-mtgs-spectral.html

This code do multiple passes Harmonic plus stochastic (HPS) transformation
Tool: 
http://mtg.upf.edu/technologies/sms 
https://github.com/MTG/sms-tools

You need to download first all source sounds from freesound.org (URLs are in my blog) 
""" 

import numpy as np
import matplotlib.pyplot as plt
import random
import sys, os
pth0 = os.path.dirname(os.path.realpath("__file__"))
pth = os.path.join(pth0, '../../software/transformations_interface/')
sys.path.append(os.path.normpath(pth))
pth = os.path.join(pth0, '../../software/models/')
sys.path.append(os.path.normpath(pth))
import hpsTransformations_function2 as HTF
import utilFunctions as UF

eps = np.finfo(np.float).eps 
freqs = [2.2204460492503131e-16, 130.8127826503, 164.8137784564,
        2.2204460492503131e-16, 130.8127826503, 164.8137784564,
        174.6141157165, 195.9977179909, 195.9977179909,
        2.2204460492503131e-16, 246.9416506281, 261.6255653006,
        246.9416506281, 261.6255653006, 246.9416506281,
        195.9977179909, 2.2204460492503131e-16, 130.8127826503,
        164.8137784564, 2.2204460492503131e-16, 130.8127826503,
        164.8137784564, 174.6141157165, 195.9977179909,
        195.9977179909, 2.2204460492503131e-16, 246.9416506281,
        261.6255653006, 246.9416506281, 261.6255653006,
        246.9416506281, 195.9977179909, 2.2204460492503131e-16,
        130.8127826503, 164.8137784564, 195.9977179909,
        174.6141157165, 174.6141157165, 195.9977179909,
        174.6141157165, 164.8137784564, 130.8127826503,
        174.6141157165, 164.8137784564, 130.8127826503,
        2.2204460492503131e-16, 130.8127826503, 164.8137784564,
        195.9977179909, 174.6141157165, 174.6141157165,
        195.9977179909, 174.6141157165, 164.8137784564,
        130.8127826503, 174.6141157165, 164.8137784564,
        130.8127826503, 2.2204460492503131e-16, 130.8127826503,
        164.8137784564, 2.2204460492503131e-16, 130.8127826503,
        164.8137784564, 174.6141157165, 195.9977179909,
        195.9977179909, 2.2204460492503131e-16, 246.9416506281,
        261.6255653006, 246.9416506281, 261.6255653006,
        246.9416506281, 195.9977179909, 2.2204460492503131e-16,
        130.8127826503, 164.8137784564, 2.2204460492503131e-16,
        130.8127826503, 164.8137784564, 174.6141157165,
        195.9977179909, 195.9977179909, 2.2204460492503131e-16,
        246.9416506281, 261.6255653006, 246.9416506281,
        261.6255653006, 246.9416506281, 195.9977179909,
        2.2204460492503131e-16, 130.8127826503, 164.8137784564,
        195.9977179909, 174.6141157165, 174.6141157165,
        195.9977179909, 174.6141157165, 164.8137784564,
        130.8127826503, 174.6141157165, 164.8137784564,
        130.8127826503, 2.2204460492503131e-16, 130.8127826503,
        164.8137784564, 195.9977179909, 174.6141157165,
        174.6141157165, 195.9977179909, 174.6141157165,
        164.8137784564, 130.8127826503, 174.6141157165,
        164.8137784564, 130.8127826503, 2.2204460492503131e-16,
        130.8127826503, 164.8137784564, 2.2204460492503131e-16,
        130.8127826503, 164.8137784564, 174.6141157165,
        195.9977179909]

f_bassdrum = "90150__menegass__bd05.wav"
f_snaredrum1 = "82238__kevoy__snare-drum.wav"
f_snaredrum2 = "2103__opm__sn-set4.wav"
f_cowbell = "22759__franciscopadilla__56-cowbell.wav"
f_hihat1 = "67210__akosombo__xbhhopen.wav"
f_hihat2 = "100054__menegass__gui-drum-ch.wav"

def thps1():
    # percussions,
    # M = 801 N 2048, t -100, minSineDur 0.005, nH 80, minf0 10, maxf0 400,
    # f0et 7, harmDevSlope 0.01, stocf 0.1
    # bassdrum
    print "analyze HPS transform: bassdrum"
    a_bassdrum, bd_fs, bd_hfreq, bd_hmag, bd_mYst = HTF.analysis(inputFile=f_bassdrum, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)
    # snaredrum1
    print "analyze HPS transform: snaredrum1"
    a_snaredrum1, sd1_fs, sd1_hfreq, sd1_hmag, sd1_mYst = HTF.analysis(inputFile=f_snaredrum1, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)
    # snaredrum2
    print "analyze HPS transform: snaredrum2"
    a_snaredrum2, sd2_fs, sd2_hfreq, sd2_hmag, sd2_mYst = HTF.analysis(inputFile=f_snaredrum2, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)
    # cowbell
    print "analyze HPS transform: cowbell"
    a_cowbell, cb_fs, cb_hfreq, cb_hmag, cb_mYst = HTF.analysis(inputFile=f_cowbell, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)
    # hihat1
    print "analyze HPS transform: hihat1"
    a_hihat1, hh1_fs, hh1_hfreq, hh1_hmag, hh1_mYst = HTF.analysis(inputFile=f_hihat1, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)
    # hihat2
    print "analyze HPS transform: hihat2"
    a_hihat2, hh2_fs, hh2_hfreq, hh2_hmag, hh2_mYst = HTF.analysis(inputFile=f_hihat2, 
                                window="blackman", M=801, N=2048, t=-100,
                                minSineDur=0.005, nH=80, minf0=10, maxf0=400,
                                f0et=7, harmDevSlope=0.01, stocf=0.1)

    print "bassdrum", len(bd_hmag), bd_fs
    print "snaredrum1", len(sd1_hmag), sd1_fs
    print "snaredrum2", len(sd2_hmag), sd2_fs
    print "cowbell", len(cb_hmag), cb_fs
    print "hihat1", len(hh1_hmag), hh1_fs
    print "hihat2", len(hh2_hmag), hh2_fs

    inputFile = "92004__jcveliz__voilinpart2compress.wav"
    freq = 901.546  # 883.323
    
    window = "blackman" 
    M = 601 
    N = 2048 
    t = -90 
    minSineDur = 0.01 
    nH = 100 
    minf0 = 400
    maxf0 = 1200
    f0et = 5 
    harmDevSlope = 0.01 
    stocf = 0.2

    inputFile, fs, hfreq, hmag, mYst = HTF.analysis(inputFile, 
                                window, M, N, t, minSineDur, 
                                nH, minf0, maxf0, f0et, 
                                harmDevSlope, stocf)

    song = np.array([])
    clip = 16000
    print "transformation and synthesis phase 1"
    for i in range(len(freqs)): 
        
        if freqs[i] <= eps: 
            scale = eps 
        else: 
            scale = float(freqs[i]) / float(freq) 
            
        # transformation and synthesis 
        freqScaling = np.array([0, scale, 1, scale]) 
        freqStretching = np.array([0, random.uniform(0.8,0.9), 1, random.uniform(0.9,1.0)]) 
        timbrePreservation = 0 
        timeScaling = np.array([0, 0, 1, 1])
        # transformation_systhesis() is modified to return y
        y = HTF.transformation_synthesis(inputFile, fs, hfreq, hmag, mYst, 
                                 freqScaling, freqStretching, 
                                 timbrePreservation, timeScaling)
        
        #print i, len(y)
        song = np.append(song, y[:clip] * 2.0)

    # add bass drum, snare drum, cowbell, hi-hat
    print "add bassdrum, snaredrum1, snaredrum2, cowbell, hihat1, hihat2"
    for i in range(len(freqs)): 
        beat = i % 8

        # bass drum
        if (( beat == 0 ) or ( beat == 4 )):
            scale = random.uniform(0.8, 1.1)
            # transformation_systhesis() is modified to return y
            bassdrum = HTF.transformation_synthesis(a_bassdrum, bd_fs, bd_hfreq, bd_hmag, bd_mYst, 
                                    freqScaling=np.array([0, scale, 1, scale]))
            # default transformation parameters
            #                        freqStretching=np.array([0, 1, 1, 1]), 
            #                        timbrePreservation=0,
            #                        timeScaling=np.array([0, 0, 1, 1]))
            start = i*clip
            song[start:start+len(bassdrum)] += bassdrum * 0.6
        
        # snare drum #1
        if (( beat == 2 ) or ( beat == 6 )):
            scale = random.uniform(0.7, 1.2)
            # transformation_systhesis() is modified to return y
            snaredrum1 = HTF.transformation_synthesis(a_snaredrum1, sd1_fs, sd1_hfreq, sd1_hmag, sd1_mYst,
                                    freqScaling=np.array([0, scale, 1, scale]))
            start = i*clip
            song[start:start+len(snaredrum1)] += snaredrum1 * 0.4

        # snare drum #2 every beat
        scale = random.uniform(0.6, 1.4)
        # transformation_systhesis() is modified to return y
        snaredrum2 = HTF.transformation_synthesis(a_snaredrum2, sd2_fs, sd2_hfreq, sd2_hmag, sd2_mYst,
                                    freqScaling=np.array([0, scale, 1, scale]))
        start = i*clip
        song[start:start+len(snaredrum2)] += snaredrum2 * 0.4

        # cowbell
        if (( beat == 3 ) or ( beat == 7 )):
            scale = random.uniform(0.8, 1.1)
            # transformation_systhesis() is modified to return y
            cowbell = HTF.transformation_synthesis(a_cowbell, cb_fs, cb_hfreq, cb_hmag, cb_mYst,
                                    freqScaling=np.array([0, scale, 1, scale]))
            start = i*clip
            song[start:start+len(cowbell)] += cowbell * 0.7

        # hihat #1 random beat
        if ( beat == random.randint(0,7) ):
            scale = random.uniform(0.8, 1.2)
            # transformation_systhesis() is modified to return y
            hihat1 = HTF.transformation_synthesis(a_hihat1, hh1_fs, hh1_hfreq, hh1_hmag, hh1_mYst,
                                    freqScaling=np.array([0, scale, 1, scale]))
            start = i*clip
            song[start:start+len(hihat1)] += hihat1 * 0.5

        # hihat #2
        if ( beat == 5 ):
            scale = random.uniform(0.7, 1)
            # transformation_systhesis() is modified to return y
            hihat2 = HTF.transformation_synthesis(a_hihat2, hh2_fs, hh2_hfreq, hh2_hmag, hh2_mYst,
                                    freqScaling=np.array([0, scale, 1, scale]))
            start = i*clip
            song[start:start+len(hihat2)] += hihat2 * 0.5
        

    # write temp output sound
    print "write temp1 output sound"
    tempFile = 'output_sounds/' + os.path.basename(inputFile)[:-4] + '_hpsModelTemp.wav'
    UF.wavwrite(song, fs, tempFile)

    size_song = len(song)

    # analyze for next phase of transformation
    print "analyze of phase 2"
    window = "blackman" 
    M = 601 
    N = 2048 
    t = -90 
    minSineDur = 0.01 
    nH = 100 
    minf0 = 400
    maxf0 = 1200
    f0et = 5 
    harmDevSlope = 0.01 
    stocf = 0.2

    inputFile, fs, hfreq, hmag, mYst = HTF.analysis(tempFile, 
                                window, M, N, t, minSineDur, 
                                nH, minf0, maxf0, f0et, 
                                harmDevSlope, stocf)
    
    # transformation and synthesis
    print "transformation and synthesis of phase 2"
    freqScaling = np.array([0, 1, 1, 1]) 
    freqStretching = np.array([0, 1, 1, 1]) 
    timbrePreservation = 0
    factor = 0.75
    timefactor = 1. / float(len(freqs))
    timescale = [0., 0.]
    for i in range(len(freqs)):
        timescale.append(timefactor * i)
        timescale.append(timefactor * i * factor)
    timeScaling = np.array([0, 0, 1, 1])
    # transformation_systhesis() is modified to return y
    y = HTF.transformation_synthesis(inputFile, fs, hfreq, hmag, mYst, 
                             freqScaling, freqStretching, 
                             timbrePreservation, timeScaling)

    size_song *= factor
        
    # write temp output sound
    print "write output sound"
    outputFile = os.path.basename(tempFile)[:-4] + '_output.wav'
    UF.wavwrite(song[:int(size_song)], fs, outputFile)

thps1()
