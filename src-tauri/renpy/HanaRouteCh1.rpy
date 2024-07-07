# Hana Route, Chapter 1, Part 1 Start
label HanaRouteCh1P1:
    # The reason for this will be explained later.
    if gn == "man":
        $hatrust -= 1
    # Start the chapter
    $ renpy.notify("Hana- Chapter 1")
    show ha 03 at hop2
    haq "WAAAAHHH? B-but.. I called dibs.."
    show k 08 at farleft 
    k "Please, everyone, I'm sure we can sort this out-"
    show ha 02 at farright
    haq "{size=+20}I CALLED DIBS!!!{size=+20}"
    k ""
    haq ""
    show k 24 at farleft
    k "I-I think I hear someone calling me, I better go attend to it!"
    # Divert between Kalei's help (small change in menu)
    menu:
        "Kalei seems anxious to leave. Should I ask him to stick around?"
        "Wait! Kalei, can you help out with this?":
            jump HanaRouteCh1P1_KaleiAssist
        "Say nothing as Kalei hurries away.":
            jump HanaRouteCh1P1_NoAssist

# Hana Route, Chapter 1, Part 1 - If player asks Kalei to mediate the housing
label HanaRouteCh1P1_KaleiAssist:
    show k 02 at farleft
    with Dissolve(0.3)
    show ha 04 at farright
    with Dissolve(0.3)
    k "Well, there is always the option of sharing the house. It is the biggest, after all!"
    haq "Share? With someone else? But... but..."
    haq "{sc=1}What if they touch my stuff?{/sc}"
    haq "{sc=3}Or find my bone collection?!{/sc}"
    "How does she have a bone collection in the afterlife? Maybe it's best not to question it."
    k "I'm sure we can work out a system. You could even become friends!"
    show ha 06 at farright
    with Dissolve(0.3)
    haq "Fwiends? I... I dunno about that..."
    haq "{size=-10}who would wanna be fwiends with me..{size=-10}"
    # Divert between how to handle Hana's reluctance (stat change + option to leave route)
    # To-Do: Maybe make the better choice more obvious?
    menu:
        "She really doesn't seem to like the idea of sharing. Maybe I should say something.."
        "Hey, relax. We'll figure it out!":
            jump HanaRouteCh1P1_CalmHana
        "C'mon.. it'll be fun! We can be roomies!":
            jump HanaRouteCh1P1_InsistShare
        "You know what, nevermind. The house is all yours.":
            show ha 08 at farright
            haq "R-really? You mean it? Like, for realsies?"
            haq "{size=+20}AUAUAUA!!!!{size=+20} Ohmygodohmygodohmygod!"
            "The girl looks at Kalei awkwardly."
            haq "I-I mean, oh my gosh.. y-yeah, ohmygosh.."
            "She seems happy. Maybe it's for the best."
            # Seems weird to change stats at a path outing but there will be more opportunities to access this route
            $hatrust -= 1
            $halove -= 1
            jump SkipHana

# Hana Route, Chapter 1, Part 1 - If player doesn't ask Kalei to stick around
label HanaRouteCh1P1_NoAssist:
    "You watch as Kalei makes a quick escape, leaving you to deal with the situation."
    show k 24 at lefttooff
    with ease
    "Dummy Text"
    pass

# Hana Route, Chapter 1, Part 1 - If the player chooses to calm Hana
label HanaRouteCh1P1_CalmHana:
    "Dummy Text"
    pass

# Hana Route, Chapter 1, Part 1 - If the player insists on sharing the house
label HanaRouteCh1P1_InsistShare:
    "Dummy Text"
    pass