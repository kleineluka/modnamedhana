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
# Branches to: Merge
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
    # Show Kalei leaving if he was present
    if hana_needed_kalei:
        show k 08 at farleft
        with Dissolve(0.3)
        "Kalei is starting to look really anxious. I wonder if this girl might actually be holding him back from something important."
        show k 01 at farleft
        with Dissolve(0.3)
        k "I truly do believe that it would be a great learning experience for you two to share the house!"
        show k 24 at farleft
        k "But, if you must excuse me, I really do need to get going right now..."
        k "[Player], I trust you will take care of this, yeah?"
        show k 24 at lefttooff
        with ease
        "Before I even get a chance to respond, Kalei is already out of my sight."
    # This might look awkward if Kalei wasn't present, so additional logic might be needed
    show ha 04 at charcenter
    with ease
    haq "Do you weally think it'll be fun to be w-woomies? I mean.. I've never had a woomie before.."
    haq "Most people on Earth hated being awound me.."
    "She looks like she's about to cry.. but hopefully I can reason with her."
    show ha 05 at charcenter
    Player "I think it could be! I mean, we're in Limbo, right? This is a fresh start for both of us."
    "She looks up at me with the tiniest amount of hope I've seen in her so far."
    show ha 09 at charcenter
    with Dissolve(0.3)
    haq "I.. I guess.. I could twy.."
    haq "I'm not weally used to being around people.. {size=-10}not by my choice..{size=+10} but maybe it could be fun.."
    Player "Exactly! Plus, it'll help having someone around while trying to get into Utopia."
    Player "Solo-ing this whole thing might be a little too much, don't you think?"
    "Hana gives a small nod and stays silent. I think this might be one of the first times she's thought about us being in the afterlife."
    jump HanaRouteCh1P1_Merge

# Hana Route, Chapter 1, Part 1 - Merge back after choosing what to do with Hana
# Branches to: GetToKnowHana
label HanaRouteCh1P1_Merge:
    "If I'm going to be living with her, I should probably get to know her a little better."
    Player "So, we should do some icebreakers or something now that we're living together!"
    show ha 04 at charcenter
    with Dissolve(0.3)
    haq "Icebweakers? Like.. what?"
    Player "Well, for starters, I'm [Player]. What's your name?"
    haq "I'm Hana.."
    "Ah, finally, a name to the face. Hana, huh?"
    Player "Well it's nice to formally meet you, Hana."
    # reset the persistent flags for getting to know Hana, for testing or going back to this point
    $ persistent.hana_ch1_p1_knowhana_bones = False
    $ persistent.hana_ch1_p1_knowhana_voice = False
    $ persistent.hana_ch1_p1_knowhana_interests = False
    jump HanaRouteCh1P1_GetToKnowHana

# Hana Route, Chapter 1, Part 1 - Getting to know Hana
label HanaRouteCh1P1_GetToKnowHana:
    menu: 
        "There's a lot of.. interesting quirks about Hana. Maybe I should ask her about them."
        "You mentioned a bone collection?" if not persistent.hana_ch1_p1_knowhana_bones:
            jump HanaRouteCh1P1_Bones
        "You have a really unique voice." if not persistent.hana_ch1_p1_knowhana_voice:
            jump HanaRouteCh1P1_Voice
        "What did you enjoy back on Earth?" if not persistent.hana_ch1_p1_knowhana_interests:
            jump HanaRouteCh1P1_Interests
        "I think that's enough for now.":
            pass

label HanaRouteCh1P1_Bones:
    $ persistent.hana_ch1_p1_knowhana_bones = True
    Player "So.. you mentioned a bone collection? Like, animal bones?"
    "{i}Please be animal bones...{/i}"
    show ha 08 at charcenter
    with Dissolve(0.3)
    Hana "Y-yeah.. I've always had a thing for bones! Animal bones, I mean.."
    Hana "It kinda started when my bird died and my dad taught me how debone it.. He had a wab and everything, so I got to wearn a lot!"
    Hana "I made a wittle birdy necklace and I've been collecting bones ever since.."
    Player "That's.. really interesting! I've never met someone who collected bones before."
    Player "Should I be worried about you collecting my bones, too?"
    "I try to say it as light-hearted as I could, but I really hope she doesn't take it the wrong way."
    show ha 02 at charcenter
    Hana "I would never take your bones! I mostly got them from a hunting store neawby.."
    Hana "Although.."
    show ha 11 at charcenter
    Hana "There was one time I got some fwom woadkill on the side of the woad.. I just couldn't help myself!"
    "I genuinely have no clue how to respond to that."
    "I mean.. I guess it's.. good to have hobbies..?"
    show ha 04 at charcenter
    Hana "Eek! I hope that doesn't make me sound too cwazy.."
    Player "N-no! Not at all! It's.. really unique, actually. Most people wouldn't have the guts to do that."
    show ha 09 at charcenter
    Hana "T-thank you.. Most people run away fwom me when I talk about bones.."
    Hana "Or before I had the chance to talk about bones.."
    Hana "But.. I'm weally glad you're still here. It's actually nice to be able to talk about it!"
    menu:
        "How do I move on to another topic?"
        "Just.. keep them away from me, please.": # True neutral
            Player "I'm glad just.. maybe keep them away from me, okay?"
            Player "Anatomy stuff kind of freaks me out.."
            "I hope she isn't too upset about that, but I really don't want to see any bones when I'm already dead."
            Hana "I-I understand.. I'll keep them in my room, I pwomise!"
            pass 
        "Maybe some time you could show me your collection?": # stat boost
            $ hana_stats(1, 2, 1)
            Player "Well.. maybe you could show me your collection sometime? I'm actually kind of curious!"
            "Hana's eyes light up at that and she nods excitedly."
            show ha 08 at charcenter
            with Dissolve(0.3)
            Hana "W-weally? You weally wanna see my collection?"
            Hana "I mean, I've never shown anyone befowe.. but I think I could make an exception for you!"
            Player "I'd be honored! But.. how have you even started a collection in Limbo?"
            "Hana looks away, a little embarrassed. She shrugs and giggles."
            Hana "I-I.. I guess I just found them.. I'm not suwe how it happened!"
            Hana "I thought maybe it would be a good idea to twy and continue things I did on Earth.."
            Hana "You know, to make this all seem.. a little less scawy.."
            "That's actually pretty sound logic. I hope I'll have time to find some hobbies while here in Limbo.."
            Player "Having something familiar would make this place a little less daunting."
            "Hana looks the calmest she's been all day. Maybe sharing a house with her was the right call."
            Hana "I'm weally glad you think so.. I think.. I think we could be good fwiends.."
            Hana "I mean, if you want to be fwiends with me.."
            Player "I'd really like that, Hana. And maybe we can even find some hobbies to do together while we're stuck here!"
            "Hana looks taken aback by that, but not in a bad way. Just in a way that seems like nobody has ever been kind to her before."
            pass 
        "I guess people really thought you were a freak, huh?": # stat drop
            $ hana_stats(-1, -1, -2)
            Player "I guess people back on Earth really thought you were a freak, huh?"
            show ha 01 at charcenter
            with Dissolve(0.3)
            Hana "I-I.. I guess so.. a wot of people were weally mean to me.."
            Player "I mean, you can't blame them, right? Collecting bones is a little.. out there."
            Hana "I-I guess so.. I just.. I just thought it was something special that made me happy.."
            Player "I'm sure it does! But.. maybe it's best to keep it to yourself for now, okay?"
            "Hana looks down at the ground and nods. That was a little harsh, wasn't it?"
            pass
    jump HanaRouteCh1P1_GetToKnowHana

label HanaRouteCh1P1_Voice:
    $ persistent.hana_ch1_p1_knowhana_voice = True
    Player "So.. I couldn't help but notice that you have a really unique voice."
    show ha 05 at charcenter
    with Dissolve(0.3)
    Hana "Y-yeah.. I've always had a weally high voice.. Most people on Earth said it was annoying.."
    Hana "And then there's the fact that I have a st-stutter.. and kind of have a weird way of tawking.."
    "I can't help but feel a little bad for her. She seems so.. self-conscious about it."
    Player "Is it something that caused a lot of trouble for you on Earth?"
    "Hana looked down and began fidgeting with the straps of her overalls."
    Hana "It made it weally hard to make friends, so I was mostly by myself.."
    Hana "I ended up spending a wot of time online where I didn't have to use my voice."
    show ha 06 at charcenter
    with Dissolve(0.3)
    Hana "I can't control it.. and even hewe, where we awe supposed to be moving on, I still get self-concious."
    # extra dialogue if not cis
    if not_cisgender():
        Player "I know how you feel.. even with my voice, I still get a little self-conscious."
        Player "But beyond that, people judging you for something out of your control. It sucks."
    Player "Is that why you wanted the big house to yourself? Not having to deal with or talk to others, right?"
    "Hana gives a tiny nod, still having a hard time maintaining eye contact."
    Hana "There isn't exactly a s-screen hewe to hide behind, after all.. so being awone is the next best thing."
    menu:
        "What do I think about Hana's voice?"
        "I think it's kind of cute, actually.": # stat boost
            pass 
        "You shouldn't be so hard on yourself.": # neutral-ish
            pass
        "It sounds like nails on a chalkboard.": # stat drop
            pass
    jump HanaRouteCh1P1_GetToKnowHana

label HanaRouteCh1P1_Interests:
    $ persistent.hana_ch1_p1_knowhana_interests = True
    jump HanaRouteCh1P1_GetToKnowHana