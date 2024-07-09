# Hana Route, Chapter 1, Part 1 Start
# Branches to: KaleiAssist, NoAssist
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
    show k 15 at farleft
    k "Well I suppose that is true, but we should remember we are trying to get into Utopia together."
    k "A good first step would be learning how to share and work together! Think about how much you want this cabin. What if others feel the same way as you?"
    haq ""
    "Wow, this girl is really stubborn. I can't help but wonder if she shared this attitude on Earth or if it's just because of our.. current situation."
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
# Branches to: HanaReluctance
label HanaRouteCh1P1_KaleiAssist:
    Player "Kalei, could you stick around for a minute and maybe help us figure this out?"
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
    jump HanaRouteCh1P1_HanaReluctance

# Hana Route, Chapter 1, Part 1 - If player doesn't ask Kalei to stick around
# Branches to: HanaReluctance
label HanaRouteCh1P1_NoAssist:
    $hana_needed_kalei = False
    "I watch as Kalei makes a quick escape, leaving you to deal with the situation."
    show k 24 at lefttooff
    with ease
    show ha 05 at farright 
    with Dissolve(0.3)
    haq "W-why did he leave? Now what am I supposed to do?!"
    "Hana looks around anxiously, clearly upset and confused."
    show ha 06 at farright
    haq "I weally wanted the big house... I called dibs and evewything!! No fair.."
    "Hana pouts and crosses her arms, looking like she's on the verge of tears."
    show ha 07 at farright
    Player "Hey, I'm not that bad. I'm sure there's plenty of space for the both of us!"
    show ha 06 at farright
    haq "B-but sharing means.. less space for me.. {size=-10}and my bone collection..{size=-10}"
    "How does she have a bone collection in the afterlife? Maybe it's best not to question it."
    jump HanaRouteCh1P1_HanaReluctance

# Hana Route, Chapter 1, Part 1 - How to respond to Hana's reluctance
# Branches to: CalmHana, InsistShare, SkipHana
label HanaRouteCh1P1_HanaReluctance:
    # Divert between how to handle Hana's reluctance (stat change + option to leave route)
    menu:
        "She really doesn't seem to like the idea of sharing. Maybe I should say something.."
        "Hey, relax. We'll figure it out!":
            jump HanaRouteCh1P1_CalmHana
        "C'mon.. it'll be fun! We can be roomies!":
            jump HanaRouteCh1P1_InsistShare
        "You know what, nevermind. The house is all yours.":
            Player "You know what, nevermind. The house is all yours."
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

# Hana Route, Chapter 1, Part 1 - If the player chooses to calm Hana
label HanaRouteCh1P1_CalmHana:
    # Reward this route with trust and love
    $hatrust += 1
    $halove += 1
    # Continue the conversation
    "Your face lights up a bit and you speak with a genuine tone to try and calm her down."
    Player "Hey, try and rela a little for me. I'm positive we'll figure it out!"
    show ha 06 at farright
    haq "{size=-10}I guess.. I could twy..{/size}"
    "She looks a little less upset, but still really.. hesistant? Scared? I wonder if it's something about me or if she's always like this."
    Player "See, that's the spirit! And trust me, I don't have any interest in touching your bone collection."
    "{i}Mostly out of fear that I'd become part of it...{/i}"
    show ha 09 at farright
    "The girl finally lets a small smile form on her face. I think it's the first time I've seen her smile since arriving in Limbo."
    # Show Kalei leaving if he was present
    if hana_needed_kalei:
        show k 09 at farleft
        with Dissolve(0.3)
        k "Well, I'm glad to see you two are getting along! I'll be off now, but I'm sure you'll sort things out."
        show k 02 at farleft
        with Dissolve(0.3)
        k "{size=-5}At least I hope so...{/size}"
        show k 02 at lefttooff
        with ease
        "Kalei leaves, leaving you alone with the anxious girl and what looks like the nicest house in the trials."
    # This might look awkward if Kalei wasn't present, so additional logic might be needed
    show ha 09 at charcenter
    with ease
    haq "Do you weally think we'll figure this out? Most people on Earth said they couldn't stand me.."
    haq "Or that I was so annoying and intowerable to be around..."
    haq "Or that I was my voice was awful to listen to..."
    "She anxiously looks away, her voice barely above a whisper. She really is a mess, huh?"
    show ha 05 at charcenter
    Player "I think I get the picture. But really, I don't want you to worry about that stuff. I mean, we're dead, right? That seems like a pretty big thing to focus on instead."
    Player "Think of Limbo as a fresh start! I've never met that girl who got called annoying, I only met someone who also really wanted that big house."
    show ha 09 at charcenter
    with Dissolve(0.3)
    "She looks back at me with a little more hope in her eyes. Maybe I'm actually getting through to her."
    haq "U-um.. th-thank you.. this is the first time anyone has ever said something like that to me."
    haq "I think we can make this work and maybe even.. {size=-10}be fwiends..{size=-10}"
    haq "I just weally hope you don't change your mind later after being awound me.."
    Player "We're both here for the same reason after all. Having someone to share this journey with might make it a little easier, don't you think?"
    "Hana gives a small nod and stays silent. I think this might be one of the first times she's thought about us being in the afterlife."
    jump HanaRouteCh1P1_Merge

# Hana Route, Chapter 1, Part 1 - If the player insists on sharing the house
label HanaRouteCh1P1_InsistShare:
    # Reward this route with confidence
    $haconfidence += 1
    # Continue the conversation
    "I lean in a little closer and put on the most confident expression you can muster."
    Player "C'mon, you know what? Sharing could actually be kind of fun! We could be like, roomies or something!"
    haq "R-roomies? I.. I dunno.. we'd have to share the bathroom and the kitchen and the living room and the-"
    show ha 03 at hop2
    "She's starting to spiral, and I can't help but feel a little bad for pushing her so hard."
    "Not that I really pushed her that hard, but.. she seem's so fragile."
    # Kalei looks anxious and I wonder if this girl might actually be holding him back from something important.
    pass

# Hana Route, Chapter 1, Part 1 - Merge back after choosing what to do with Hana
label HanaRouteCh1P1_Merge:
    # Merge at the discussion of them in the Afterlife
    # Mention bone collection and if player chooses to point it out to her, more trust
    "Dummy Text"
    pass