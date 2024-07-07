# (Insert @ 801) Edited by Mod Named Hana
label HanaDivert:
    hide br
    with Dissolve(0.5)
    show ha 01 at farright
    with ease
    $ renpy.notify("Choice diverts to seperate routes")
    menu:
        "A big cabin does sound nice... but then again, there's the whole being dead thing. And trying to prove I'm not a bad person to get into Utopia. Should I even contest it?"
        "Wait.. who says you get the biggest cabin!?":
            jump HanaRouteCh1P1
        "Um, okay then. It's all yours.":
            pass
