keys = "A Bb B C Db D Eb E F F# G Ab".split(" ")

def modes_in_chord(chord):
    "chord can be minor with 'm' in front"
    #if minor, get relative major (go up three)
    if chord[-1] == "m":
        chord = chord[:-1]
        chord = move_up(chord, 3)
    
    dark_sig = get_dark_sig(chord)
    bright_sig = get_bright_sig(chord)
    return [dark_sig, chord, bright_sig]

def get_dark_sig(chord):
    return move_up(chord, 5)

def get_bright_sig(chord):
    return move_up(chord, 7)

def get_index(chord):
    for i in range(len(keys)):
        if chord ==keys[i]:
            return i

def move_up(chord, semitones):
    index = get_index(chord)
    new_index = (index + semitones) % 12
    return keys[new_index]

def print_modes_for_chord_list(chord_list):
    for chord in chord_list:
        print(f"Given The Chord {chord} Use Key Centres:", modes_in_chord(chord))

def demos():
    print("=== DEMO1 ===\nHere is a list of key centres for C Major...")
    cmaj = "C Dm Em F G Am".split(" ")
    print_modes_for_chord_list(cmaj)
    print("=== DEMO2 ===\nHere is how you might use this system over the 'Autumn Leaves' Jazz standard")
    standard = "Cm F Bb Eb Am D Gm G".split(" ")
    print_modes_for_chord_list(standard)

demos()
