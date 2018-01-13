label dokiextended:
    stop music fadeout 2.0
    play music t2
    scene bg residential_day
    with dissolve_scene_full
    show sayori 1bh at t11 zorder 2
    mc'Sayori, you will always be my dearest friend'
    show sayori 1bh at t11 zorder 1
    scene dark
    with dissolve_scene_full
    stop music fadeout 2.0
    mc 'Let me step back a bit.'
    play music m1
    'After Monika had deleted everyone, she let me go backward to the begening of the script.'
    m 'Give me in the past a chance and I\'ll let you go.'
    m 'Bye [player].'
    scene bg residential_day
    with dissolve_scene_full
    stop music fadeout 2.0
    play music t2
    show sayori 1bh at t11 zorder 2
    show screen invert(0.15,0.3)
    mc'Sayori, you will always be my dearest friend.'
    scene dark
    with wipeleft_scene
    stop music fadeout 2.0
    mc'I gently open the door.'
    scene sayori_bedroom
    mc 'Sayori?'
    play music t10
    show sayori 1bh at t11 zorder 2
    s '[player]?'
    'Sayori stood in her room, with a thick rope in her hand.'
    mc 'WHAT ARE YOU DOING WITH THAT ROPE!'
    show screen invert(0.15,0.3)
    s '...'
    s 1bp 'Uouwa!'
    mc 'You shouldn\'t be doing anything with that rope, Sayori!'
    'I take the rope from Sayori, setting it aside.'
    s 1bm 'I was going to...'
    s '...hang myself.'
    mc 'You said my happiness was important to you, right?'
    s 'Yeah...'
    mc 'If you had hanged yourself, it would hurt me.'
    s 1bv 'Yeah...'
    'Sayori starts to cry, and I hugged her.'
    s 1bu 'Why did I think that killing myself would help anything?'
    mc 'All that matters now is that you are alive.'
    mc 'How about you change into your school uniform.'
    s 'Okay...'
    hide sayori 1bh at l11 zorder 1 with dissolve
    'I pick up the rope and throw it into a nearby trashcan.'
    show sayori 1f at t11 zorder 2
    s 'I don\'t know if I can perform at the festival today...'
    mc 'We can decide that later.'
    show sayori 1f at t11 zorder 1
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t5
    show monika 1d at t11 zorder 2
    'As Monika sees Sayori, she tries to hide her horror.'
    'Monika mutters something about a game.'
    show monika 1a at t41 zorder 3
    show natsuki 1g at t42 zorder 4
    show yuri 1a at t43 zorder 3
    show sayori 1f at t44 zorder 4
    n 'Are you ok, Sayori?'
    show natsuki 1g at f42 zorder 4
    show natsuki 1g at t42 zorder 4
    s '...no...'
    hide sayori 1v at l44 zorder 1
    'Sayori ran out of the room.'
    show natsuki 1g at f42 zorder 4
    n 'Do you know what happened with Sayori, [player]?'
    mc 'She almost hanged herself this morning.'
    show monika 1p at f41 zorder 3
    show natsuki 1p at f42 zorder 4
    show yuri 1p at f43 zorder 3
    n 'WHAT!!!!'
    mc 'Sayori has serious depression and may not be able to perform today.'
    'Natsuki pulls me in the closet.'
    scene bg closet
    with wipeleft_scene
    hide monika
    hide yuri
    hide natsuki
    show natsuki 1u at t11 zorder 2
    n 'Did she attempt suicide because of me?'
    mc 'WHAT??!'
    n 1r 'Outside of your house...She might have taken that the wrong way.'
    mc 'She told me she had this depression for her whole life so it couldn\'t have been you.'
    n 1x 'It may have gotten worse because of that.'
    mc 'It wasn\'t your fault, Natsuki'
    n 5r 'maybe...'
    'Natsuki still doesn\'t look convinced.'
    show natsuki 5r at t21 zorder 2
    show sayori 1f at t22 zorder 3
    s '...Hi Natsuki...'
    s '...[player] and Natsuki, do you guys think I can perform?'
    n 5w '[player], you know her best.'
    menu:
        mc 'Sayori,...'
        '...You can perform at the festival':
            jump festival

        '...You aren\'t ready to perform':
            jump nofestival
label festival:
    scene dark
    with dissolve_scene_full
    call updateconsole(">os.rm(\"game/script.rpa\")", "script.rpa removed")
    pause 1.5
    call updateconsole(">os.rn(\"game/bG9sDQo.rpa\",\"script\")", "bG9sDQo=.rpa renamed.")
    scene bg house
    with dissolve_scene_full
    hide natsuki
    hide sayori
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    $ gtext = glitchtext(10)
    mc 'Sayori, hurry up!'
    s 'Why do you have to run so quickly, [player]?'
    show sayori 1l at t11 zorder 2
    mc 'You gotta get ready for the festival!'
    scene bg kitchen
    with wipeleft_scene
    show sayori 1by at t11 zorder 2
    s 'We need to carry the cupcakes right?'
    mc 'Yeah'
    'Sayori suddenly grabs my arm.'
    s 1bv 'Are you sure I can perform?'
    mc 'I am 100\% certain, Sayori'
    s 1by 'I can trust you.'


    scene bg club_day
    with wipeleft_scene
    show sayori 1y at t41 zorder 2
    show natsuki 5g at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show monika 2a at t44 zorder 5


    n 'Sayori, can you really perform at the festival?'
    s 'I can do it.'
    m 3a 'Is everyone ready?'
    mc 'Yeah.'
    'Around the room, I can see all the work put into the festival.'
    'Monika steps up to the podium.'


    hide natsuki
    hide sayori
    hide yuri
    show monika 2b at f11 zorder 2


    m 3b 'Hello Everyone! I am Monika, the president of The Literature Club. First I should start with our mission. We provide a space where everyone, even not as avid readers, can read and socialize.'
    m 4a 'We write and share poems everyday! Here at the festival, we will perform some of these poems!'
    m 5a 'I will start with my poem, Hole In The Wall.'
    m 2a 'It couldn\'t have been me.'
    m 5b 'See, the direction of the sparkle protrudes.'
    m 4c 'A noisy neighbor? An angry boyfriend? I\'ll never know. I wasn\'t home.'
    m 1q 'I peer inside for a clue.'
    m 2i 'NO! I can\'t see. I reel, blind, like a film left out in the sun.'
    m 1q 'But it\'s too late. My retinas.'
    m 1q 'Already scorched with a permanent copy of the meaningless image.'
    m 2i 'It\'s just a little hole. It wasn\'t too bright.'
    m 2q 'It was too deep.'
    m 1q 'Stretching forever into everything'
    m 2q 'A hole of infinite choices.'
    m 1q 'I realize now, that I wasn\'t looking in.'
    m 1i 'I was looking out.'
    m 1i 'And he, on the other side, was looking in.'
    'The whole audience bursts into aplause, including us.'


    show monika 1a at t21 zorder 2
    show natsuki 4d at t22 zorder 3


    n 'You did really well, Monika.'
    m 'I guess.'


    show monika 1a at t31 zorder 2
    show natsuki 4d at t32 zorder 3
    show yuri 1a at t33 zorder 4


    y 'That was excellent performing.'


    show monika 1a at t41 zorder 2
    show natsuki 4d at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show sayori 1a at t44 zorder 5

    s 'I\'m next right?'
    m 'You then Natsuki, then Yuri, then [player].'
    s 'Ok.'
    'Sayori takes a deep breath.'
    s 'Wish me luck guys.'
    mc 'You bet.'


    hide natsuki
    hide monika
    hide yuri
    show sayori 1a at t11 zorder 2


    s 'Hi everyone, so um I am Sayori, the vice president of the Literature Club'
    s 'I am going to recite my poem, Dear Sunshine.'
    s '...'
    'Sayori takes a deep breath.'
    s 'Dear Sunshine.'
    s 2a 'The way you glow through my blinds in the morning,'
    s 2b 'It makes me feel like you miss me.'
    s 3r 'Kissing my forehead to help me out of bed.'
    s 1j 'Making me rub the sleepy from my eyes.'
    s 3d 'Are you asking me to come out and play?'
    s 3c 'Are you trusting me to with away a rainy day?'
    s 2d 'I look above. The sky is blue.'
    s 1d 'It\'s a secret, but I trust you too.'
    s 3h 'If it wasnt for you, I could sleep forever.'
    s 1a 'But I\'m not mad.'
    s 3y 'I want breakfast.'
    'Everyone in the room starts clapping.'

    show sayori 1a at t41 zorder 2
    show natsuki 4a at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show monika 2a at t44 zorder 5


    'When I look at Sayori, she looks genuinly happy for the first time since I had rejected her.'
    mc 'Sayori, you did extremely well!'
    s 5b '...Maybe...'
    n 5l 'Sayori, stop trying to deny it! Yours was way better than mine will be!'
    s 1m 'Yours is better! Its about [player]!'
    n 5o 'How do you know!'
    y 1d 'Natsuki, we all know it!'
    n 52c 'You all don\'t know what you are talking about do you.'
    mc 'Yeah we do.'
    n 52b 'Uhhhhhhh...'
    'Natsuki tries to run but I grab her wrist.'
    n 5u 'Huh?'
    mc 'You still need to perform.'
    n 5h 'Fine.'
    'Natsuki steps up to the podium.'


    hide monika
    hide yuri
    hide sayori
    show natsuki 1i at t11 zorder 2


    n 2j 'Hello! I am Natsuki, a member at the Literature Club.'
    n 1d 'This is my poem, Eagles Can Fly.'
    n 2d 'Monkeys can climb'
    n 2d 'Crickets can leap'
    n 2j 'Horses can race'
    n 3j 'Cheetahs can run'
    n 3d 'Eagles can fly'
    n 1d 'People can try'
    n 4d 'But that\'s about it.'
    'Once again, the audience applauds.'


    show natsuki 4d at t41 zorder 2
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show monika 2a at t44 zorder 5


    mc 'That was really good, Natsuki!'
    n 5a 'Of course it was.'
    mc 'Wait. You said you were going to perform {i}Because You{/i}.'
    n 'I didn\'t want to'
    mc 'Okay?'
    y 4b 'Its my turn right?'
    mc 'Yep. You can do this!'
    y 1k 'Ok.'


    hide natsuki
    hide sayori
    hide monika
    show yuri 1m at t11 zorder 2

    y 4b 'I am Yuri, a member of the Literature Club, and this is my poem, Ghost Under the Light'
    y 1m 'The tendrils of my hair illuminate beneath the amber glow.'
    y 2k'Bathing.'
    y 1k'It must be this one.'
    y 1m'The last remaining streetlight to have withstood the test of time.'
    y 1n'The last yet to be replaced by the sickening blue-green hue of the future.'
    y 2l'I bathe. Calm; breathing air of the present but living in the past.'
    y 1f'The light flickers.'
    y 1i'I flicker back.'


    show natsuki 1a at t41 zorder 2
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show monika 2a at t44 zorder 5


    n 1y'That was really good!'
    y 1f'Are you saying that just to be nice?'
    n 5f'Hey!'


    'As I think about my speach, the Nat and Yuri\'s conversation starts to fade away.'


    mc 'Ok. I\'m ready.'

    scene dark
    with dissolve_scene_full
    hide natsuki
    hide sayori
    hide yuri
    hide monika
    'I recite my poem.'
    scene bg club_day
    with dissolve_scene_full
    'The audience applauds.'
    show natsuki 1a at t41 zorder 2
    show sayori 1a at t42 zorder 3
    show yuri 1a at t43 zorder 4
    show monika 2a at t44 zorder 5
    s 'That was really good [player]!'
    mc 'It was ok...'
    n 'You could have improved more.'
    mc 'Yeah.'
    scene bg corridor
    with wipeleft_scene
    hide sayori
    hide yuri
    hide monika
    show natsuki 5a at face zorder 2
    'As everyone starts to leave, Natsuki and I are the only ones left.'
    'As we clean up I find Natsuki suprisingly close.'
    mc 'Umm...What were you going to do at my house before you left'
    show natsuki 5g at t11 zorder 2
    n 'Jeez, just because were alone doesn\'t mean you have to make it weird.'
    mc 'That implies that it would have been \'weird\'.'
    n 5n 'No it doesn\'t...'
    n 5a 'You know what?'
    n 'I was going to do this.'
    show natsuki 5a at face zorder 2 with dissolve
    scene bg corridor
    with dissolve_scene_full
    show natsuki 5a at t11 zorder 2
    n 'Haha!'
    mc 'Ummmmm...Uhhhhhhh...'
    mc 'Uhhhhmmmmm..........'
    n 5z 'Your face!'
    mc '...'
    mc 'Ummm...'
    '...'
    '...'
    '...'
    n 1k '[player], can I talk to Sayori?'
    mc 'Ask Sayori.'
    scene dark with dissolve_scene_full
    'The whole way home I blush and look away.'
    scene bg house with wipeleft_scene
    n 'Are you going in first?'
    mc 'Okay...'
    'I go inside, still avoiding Natsuki\'s eyes.'
    jump afterfestival
    return
label nofestival:
    scene dark with dissolve_scene_full
    hide natsuki
    hide sayori
    s
    return
label afterfestival:
    scene bg sayori_bedroom with wipeleft_scene
    'Natsuki collapses.{nw}'
    scene dark with dissolve_scene_full
    call updateconsole_clearall()
    call updateconsole("os.promote(\"characters/natsuki.chr\")", "Natsuki.chr promoted to MC.")
    pause 1.5
    call updateconsole("os.demote(\"mc\")", "Mc demoted to character(mc.chr).")
    scene sayori_bedroom with dissolve_scene_full
    show sayori 1a at t22 zorder 3
    show protag 1a at t21 zorder 3
    show protag 1b at t21 zorder 3
    mc 'Hi Natsuki!'
    return
