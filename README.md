## Experiments with HPS (harmonic plus stochastic) sound transformation. 

Several simple experiments I made.

**Tool:** Spectral Modeling Synthesis sms-tools of MTG UPF (Music Technology Group, Universitat Pompeu Fabra, Barcelona), by Prof. Xavier Serra et.al.  (also as instructor in the Audio Signal Processing for Music Applications, Coursera).

- [http://mtg.upf.edu/technologies/sms](http://mtg.upf.edu/technologies/sms)
- [https://github.com/MTG/sms-tools](https://github.com/MTG/sms-tools)
- [https://github.com/MTG/essentia](https://github.com/MTG/essentia)

**How to?**

- (Fork and) clone Github's **sms-tools** into local repository.
- Install **sms-tools** (and **essentia** if interested) in Ubuntu (or Debian, I don't know whether it works in other Linux distribs, I compiled sms-tools in Windows 7 successfully).
- For transformation, open sms-tools/software/transformations and sms-tools/software/transformations-interface folders.
- Available transformation models: sine, STFT morph (short time Fourier transform), harmonic, stochastic, HPS (harmonic plus stochastic), HPS morph.
- Either (a) Run  python transformations_GUI.py or (b) write Python script to call transformation models' functions. 
- In the GUI or in the Python code, first to do analysis to determine best HPS model's parameters, then apply transformation. 
- To help determine f0, harmonics, and several parameters, we can use "Sonic Visualiser" (free) with its Spectogram pane and Aubio plugin (pitch detector, onset detector).

Disclaimer: I'm not musician, just amateur hobbyist in music/sound/audio =)

**Output sounds at freesound.org:**

Singing frogs (multiple sounds & passes): 
[http://www.freesound.org/people/maghas99/sounds/259308/](http://www.freesound.org/people/maghas99/sounds/259308/)

Alien speech: 
[http://freesound.org/people/maghas99/sounds/259129/](http://freesound.org/people/maghas99/sounds/259129/)

Swinging piano: 
[http://freesound.org/people/maghas99/sounds/259131/](http://freesound.org/people/maghas99/sounds/259131/)

Violin mosquito: 
[http://freesound.org/people/maghas99/sounds/259130/](http://freesound.org/people/maghas99/sounds/259130/)


**Blog post:**

[http://blog.wijono.org/2015/01/sound-transformation-with-mtgs-spectral.html](http://blog.wijono.org/2015/01/sound-transformation-with-mtgs-spectral.html) 

