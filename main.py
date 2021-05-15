# Printing the welcome message
# Asking for confirmation to play
# Defining the initial score and number of total questions

print('Welcome to the Ultimate Gaming Quiz! This is made using Python, by Bedanta.')
answer=input('Are you ready to play the quiz? (yes/no) : ')
score=0
total_questions=6


# Question 1: Minecraft | Steve


if answer.lower()=='yes':
    answer=input("Question 1: What is the name of the male character from the sandbox game 'Minecraft'? (steve/alex/enderman) " )
    if answer.lower()=='steve':
        score += 1
        print('Good job! Now let us continue to mine!' )
    else:
        print('Are you on kelp? The correct answer is STEVE.' )


# Question 2: Ace Attorney | Defense Attorney
 
 
    answer=input("Question 2: What profession is Phoenix Wright, in the series of 'Phoenix Wright: Ace Attorney'? (prosecutor/defense attorney/bailiff) ")
    if answer.lower()=='defense attorney':
        score += 1
        print('Good job! No objections!')
    else:
        print('OBJECTION! You got it wrong! Phoenix Wright is a DEFENSE ATTORNEY.' )


# Question 3: PUBG | Brendan Greene

 
    answer=input("Question 3: Who was the creator of the FPS game 'Playerunknown's Battlegrounds'? (brendan greene/marcus persson/david baszucki) " )
    if answer.lower()=='brendan greene':
        score += 1
        print("You're going in first, as usual! Correct answer!" )
    else:
        print("Ambush, but don't panic! The correct answer is BRENDAN GREENE." )


# Question 4: Undertale | Sans

    
    answer=input("Question 4: Which of these characters is identified as a skeleton in the game 'Undertale'? (undyne/sans/asgore) " )
    if answer.lower()=='sans':
        score += 1
        print("* YOU GOT THE CORRECT ANSWER. * YOU EARN 0 XP AND 0 GOLD." )
    else:
        print("You monster. The correct answer was SANS." )


# Question 5: Game Development | Capcom


    answer=input("Question 5: Kenzo Tsujimoto is the founder, owner and CEO of which game publisher company? (nintendo/sega/capcom) " )
    if answer.lower()=='capcom':
        score += 1
        print("TAKE THAT! You got a point... seriously." )
    else:
        print("Do you think that you know a lot about the greatest personalities alive? Don't get your hopes up. One day you will find someone who is far more superior and intelligent than you. That day, you will realize that how bad and unintelligent you are. Oh, I forgot. The answer was CAPCOM." )


# Question 6: Localisation...? | Pokemon
    
    answer=input("Question 6 (The last question): Translate this! ポケモン (pokemon/beyblade/yugioh) " )
    if answer.lower()=='pokemon':
        score += 1
        print("Gotcha! The point was caught!" )
    else:
        print("Oh no! The point broke out! It was POKEMON." )

# Printing a thank you message and calculating the points.
 
print('Thank you for playing this small and AMAZING ULTIMATE GAMING QUIZ, you attempted',score,"questions correctly!")
points=(score/total_questions)*100
print('Points obtained:',points)
print('Bye! See you later!')
