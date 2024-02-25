# rethinking-modes
Suggests scales to improvise over chords.
### Explaination: tl;dr
rethinking-modes is a simple program to help musicians improvise and conceptualise the bigger tonal picture when experimenting with accidental notes. It is a framework to write, understand and improvise non diatonic music (music that exists outside of any one key signature).

## Demos
### C Major Scale
Improvisation suggestions for the C Major Scale
```
=== DEMO1 ===
Here is a list of key centres for C Major.
Given The Chord C , Use Key Centres: ['F', 'C', 'G']
Given The Chord Dm , Use Key Centres: ['Bb', 'F', 'C']
Given The Chord Em , Use Key Centres: ['C', 'G', 'D']
Given The Chord F , Use Key Centres: ['Bb', 'F', 'C']
Given The Chord G , Use Key Centres: ['C', 'G', 'D']
Given The Chord Am , Use Key Centres: ['F', 'C', 'G']
```
### Jazz Standard
Improvisation suggestions for the ['Autumn Leaves'](https://cdn.learnjazzstandards.com/wp-content/uploads/2017/11/Autumn-Leaves-Guide-Tones.png) Jazz standard.
```
=== DEMO2 ===
Here is how you might use this system over the 'Autumn Leaves' Jazz standard
Given The Chord Cm , Use Key Centres: ['Ab', 'Eb', 'Bb']
Given The Chord F , Use Key Centres: ['Bb', 'F', 'C']
Given The Chord Bb , Use Key Centres: ['Eb', 'Bb', 'F']
Given The Chord Eb , Use Key Centres: ['Ab', 'Eb', 'Bb']
Given The Chord Am , Use Key Centres: ['F', 'C', 'G']
Given The Chord D , Use Key Centres: ['G', 'D', 'A']
Given The Chord Gm , Use Key Centres: ['Eb', 'Bb', 'F']
Given The Chord G , Use Key Centres: ['C', 'G', 'D']
```

### Explaination pt.2 : Too Long, DID read
It's possible to use set theory to understand harmony, with notes being the smallest unit. If we consider a chord to be a set of three notes and a key signature to be a set of seven notes, we can determine which chords can be played in a key signature, and therefore the inverse, which key signatures can be overlayed over a chord. These key signatures, also sometimes referred to as key centres, scales, or "modes" are what we are interested in. 

To calculate them slightly faster, we can use a musical concept called the circle of fifths, which says that the key signatures available for a chord will always be certain distances away from it (one fifth above and below, + the current chord. e.g. `Cmaj` chord exists in `C`, `G`, & `F`). The circle of fifths is accessed in this program using the `move_up` function.
