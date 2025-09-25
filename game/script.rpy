# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pl = Character("Bash Mustard")
image bash = "Bash.png"
image beach = "Beach.png"
image forest = "Forest.png"
image desert = "Desert.png"
image funeral = "Funeral.png"
image village = "village.png"
image bombardiro = "Bombardiro.png"
image bombombini = "Bombombini.png"
image brr = "Brr.png"
image lirili = "Lirili.png"
image tralalero = "Tralalero.png"
image trippi = "Trippi.png"
image tung = "Tung.png"
image blackout = Solid("#000000")

define n_bombardiro = Character("Bombardiro Crocodrillo")
define n_bombombini = Character("Bombombini Gusini")
define n_brr = Character("Brr Brr Patapim")
define n_lirili = Character("Lirili Larila")
define n_tralalero = Character("Tralalero Tralala")
define n_trippi = Character("Trippi Troppi")
define n_tung = Character("Tung Tung Sahur")

# The game starts here.

label start:

    scene forest
    show bash
    pl "Hello, my name is Bash Mustard. I'm an adventurer, and I like to explore far away lands such as these. I seem to have made a wrong turn; I was trying to go to streamercity but I ended up here. I wonder what this place is about."
    
    "Bash meets a new creature."
    
    hide bash
    show bash at left
    show brr:
        right
        xzoom -1.0
    
    pl "Woah! Who are you!"
    
    n_brr "Ho ho! Don't you know! I am Brr Brr Patapim, a good friend of a blue frog named Slim."
    
    pl "I don't know Slim... I don't even know where I am!"

    n_brr "Don't worry friend, for my hand I can lend. We are in Brainrotia, where everything is named after an onomatepia!"

    pl "Are you going to rhyme every word..."

    n_brr "Quick! There's not much time to waste! We must seek shelter at haste!"

    pl "Slow down. What do you mean by that?"

    n_brr "Tung Tung Sahur is a mean one. There is a lot of bad he has done. He has taken to fighting us until there is none."

    pl "I need to get out of here then!"

    n_brr "You'll need a guide if you want to get through. But then again that is only up to you!"
    
    menu: 
        "What should I do?" 
        "I'll be good. Thanks.":
            jump c1_no
        "Lets go!":
            jump c1_yes
    
    return
    
label c1_no:
    n_brr "You'll need vast experience if you want to make it. Surely your hubris isn't making you fake it."
    pl "..."
    
    pl "Nah... I'm about 6 or 7 months old. I think I can make it myself!"
    
    "Bash makes his way towards the nearby beach"
    
    hide brr
    scene beach
    show bash at left

    "Bash meets a new creature."
    
    show tralalero at right
    
    pl "Woah..."

    n_tralalero "Do you think I'm a freak?"

    pl "What?"

    n_tralalero "Nobody likes me. My whole life I've been tossed aside, especially Tung Tung Sahur let go of me."

    pl "!!"

    n_tralalero "Relax. I'm not a threat."

    pl "What happened between you and Tung Tung Sahur?"

    n_tralalero "He was there for me at my lowest, and he got me on my feet. Next thing you know, he has me doing small crimes for him and it just got too crazy. One day, he wanted me to go pop Boneca Ambalabu!"

    pl "Oh man. Thats a tough break."

    n_tralalero "I'm so tired of hiding from him. It's time to face my destiny."

    "Bash and Tralalero meet a new character."
    
    hide tralalero
    show tralalero at center
    show trippi:
        right
        xzoom -1.0

    n_trippi "Tung Tung Sahur sends his regards!"

    "Tralalero dodges the sudden attack!"

    pl "What is your problem!"

    n_trippi  "You're not a part of the deal. Get out of here before I destroy you like I did to my copycat version. He sleeps with the fishes now."
    
    menu: 
        "What should I do?" 
        "Help Tralalero Tralala fight.":
            "Bash tries to help Tralalero."

            n_tralalero "Save yourself!"

            "Trippi blares an ion beam at Tralalero, eviscerating him instantly. Bash loses the will to fight and runs south quickly."
            
        "Run!":
            n_tralalero "It was good to talk to someone who understood me. Make sure I'm remembered..."

            "Bash's eyes well up as he runs away. Tralalero tries to block the attack from Trippi but succumbs to injury."
    
    scene village
    show bash at left
    
    "Bash finds Brr at the village."
    
    show brr:
        right
        xzoom -1.0
        
    n_brr "Are you OK traveler? I sense that you met a foe of a higher caliber."

    pl "I realize that I do need help getting out of here. But first we need to end this pain."
    
    jump converge_path
    
    return

label c1_yes:
    pl "Ok Brr Brr Patapim. I will folow you."

    scene desert
    show bash at left
    show brr at center
    "Bash and Brr meet a new character."
    show lirili:
        right
        xzoom -1.0
        
    n_brr "Oh how long has it been. Admittedly, you used to be thin!"

    n_lirili "Hello Brr Brr Patapim. It has been a while, that is for sure. What is this thing next to you?"

    n_brr "He is Bash Mustard, he is a traveler from a city made of custard. He can talk, but he's just a bit flustered." 

    pl "No, I'm not flustered!"

    n_lirili "What is the purpose of this visit?"

    n_brr "Our friend here needs help going home. He can't remember from off the dome."

    n_lirili "I will see what I can manage."

    "The three meet a new character"
    
    hide bash
    hide brr
    hide lirili
    show bash:
        xalign -0.3
    
    show brr:
        left
        
    show lirili:
        xalign 0.7
        
    show bombardiro:
        xalign 1.2

    n_bombardiro "Hahaha! I'm back for round two baby!"

    n_lirili "You reptilian menace. You came for revenge when I least expect it. This is a low blow."

    n_bombardiro "Do you think I care who these people are? You should suffer their loss as well because I wont. HAHAHA!"

    n_lirili "You guys need to run south now! All of the lands will be hunted shortly. Seek shelter at the Village."

    n_brr "I wish it didn't end like this..."
    
    menu: 
        "What should I do?" 
        "Help Lirili Larila fight.":
            pl "And it doesn't have to!"
            "Bash tries to help Lirili Larila."
            n_lirili "You fool!"
            "Bombardiro drops the bomb over everyones head. Lirili sprints towards it"
            "Lirili uses its clock to stop time. The effects are localized at the bomb, but he froze himself as well. Lirili is trapped and has no way to escape..."
            n_brr "We must run, or else we will be done!"
            "Bash and Brr Brr Patapim run south."
            
        "Run!":
            pl "I won't let you down..."

            n_lirili "I'm sorry it had to end this way, Brr Brr Patapim."

            n_brr "We will remember you, that you didn't surrender too."

            "Bombardiro drops the bomb over Lirili's head."

            "Lirili uses its clock to stop time. The effects are localized at the bomb, but he froze itself as well. Lirili is trapped and has no way to escape..."

            "Bash and Brr run south."

    scene village
    show bash at left
    show brr at center

    n_brr "We made it..."

    pl "There is an ominous feeling coming from this place..."
    
    jump converge_path
    
    return
    
label converge_path:
    
    scene blackout
    
    "Bash and Brr Brr Patapim get dizzy and fall to the ground."

    "Bash and Brr Brr Patapim wake up to find themselves tied up."
    
    scene village
    
    show bash at left
    show brr at right

    n_tung "Well wakey-wakey! How was your nap!"

    pl "Oh no! Are you..."
    
    hide bash
    hide brr
    
    show bash at left
    show brr:
        xalign 0.3
        
    show tung at right
    
    n_tung "Yes I am Tung Tung Sahur. Nice to meet you."

    n_brr "You are a monster! Let us go, you have us tied like the claws of a lobster!"

    n_tung "Well, Brr Brr Patapim. I have some news for you, I wont let you go that easy. The newcomer can leave, but he has to take a life with him"

    pl "What do you mean."
    
    hide bash
    hide brr
    hide tung
    
    show bombardiro at left
    show trippi at right
    
    n_tung "Behold! The henchmen who are worthless at their jobs!"

    "Bombardiro and Trippi" "Help! Get me out!"

    n_tung "Quiet down now. So, the deal is you have to choose one of them and I'll make sure they are sent to their creator. Then I'll untie you and keep the other as my prisoner. Sounds good right?"
    
    menu: 
        "Who should I pick..." 
        "Trippi Troppi":
            jump trippi_k
        "Bombardiro Crocodrillo":
            jump bombardiro_k
    
    return
    
label trippi_k:
        
    "Bash chooses Trippi with great anguish."

    n_tung "Smart choice. I always prefered the bear version over him..."
    hide trippi
    "Tung takes care of Trippi Troppi."

    "A jet flys overhead."
    hide bombardiro
    show tung:
        left
        xzoom -1.0
    show bombombini at right
    
    n_bombardiro "Bombombini Gusini!"

    n_bombombini "I'm not letting you get away with this! I'm ending this!"

    n_tung "Nooo!!! This isn't how this is supposed to go!"

    "Bombombini drops a bomb on Tung Tung Sahur. There is a great deal of destruction, but Brr Brr Patapim, Bash, and Bombardiro Crocodrillo remain untouched. Bombombini unties everyone."

    hide tung
    show bombardiro:
        left
        xzoom -1.0
     
    n_bombardiro "Bro, I'm sorry for everything. I'm gonna miss Trippi Troppi too."
    
    n_bombombini "You are my brother, and I forgive you. Trippi was misguided too. You don't have to worry about him anymore..."

    scene funeral

    "All of the characters left reminisce on past events. Lirili Larila, Trippi Troppi, and Tralalero Tralala lie peacefully."
    scene blackout
    "The End." 
    "Start over and try to get a different ending! (2 endings)"
    return
    
label bombardiro_k:
    
    "Bash chooses Bombardiro Crocodrillo with great anguish."

    n_tung "Good choice. I've been meaning to get rid of him and his meddling brother. Now I have an excuse!"
    hide bombardiro
    
    "Tung takes care of Bombardiro Crocodrillo."
    hide trippi
    show tung:
        left
        xzoom -1.0
    show bombombini at right
    
    n_bombombini "I'm not letting you get away with this! I'm ending this!"

    n_tung "Nooo!!! This isn't how this is supposed to go!"

    "Bombombini drops a bomb on Tung Tung Sahur. There is a great deal of destruction, but Brr Brr Patapim, Bash, and Trippi Troppi remain untouched. Bombombini unties everyone."
    
    hide tung
    show trippi at left
    
    n_trippi "How did things go so wrong..."

    n_bombombini "What's done is done. I hope my bro was in peace in his last moments. I wish I was there in time. We won't have to worry about him anymore..."

    scene funeral

    "All of the characters left reminisce on past events. Lirili Larila, Bombardiro Crocodrillo, and Tralalero Tralala lie peacefully."

    scene blackout
    "The End." 
    "Start over and try to get a different ending! (2 endings)"

    return
    
