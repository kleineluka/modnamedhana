init:

    # hana character values
    default halove = 0
    default hatrust = 0
    default haconfidence = 0
    # Would it be funny to implement a "Hana's Cleanliness" stat? Or too mean..

    # flags for events that happened (or didn't)
    default hana_needed_kalei = True # Ch1 P1
    default hana_calmed = False # Ch1 P1 

    # added transformations
    transform lefttooff:
        linear 0.1 xpos 0.2
        linear 1.0 xpos -0.5

    # persistent choices in hana's route
    $ persistent.hana_ch1_p1_knowhana_bones = False
    $ persistent.hana_ch1_p1_knowhana_voice = False
    $ persistent.hana_ch1_p1_knowhana_interests = False 

init python:
    
    # function to change hana's stats
    def hanastats(love_change, trust_change, confidence_change):
        global halove, hatrust, haconfidence
        halove += love_change
        hatrust += trust_change
        haconfidence += confidence_change