# Team 14 SheHacks Challenge 3
# one player must enter "yes" to start the game
startGame = input("Would you like to play hangman?(yes, no): ")
if startGame == "yes":
    playHangman = True
else:
    playHangman = False


# while loop entered and game started if player said "yes" 
while playHangman:    
    print("Let's play hangman")

    # player 1 is asked to enter a word to be guessed by player 2
    playerOneWord = input("Player 1, please enter a word: ")
    
    wordEntered = False
    
    # player 1 continually prompted until they enter a valid word
    while not wordEntered:
        if playerOneWord.isalpha():
            # if valid word entered then player 1 is asked to enter the number of guesses allowed  
            playerOneNumGuesses = input("Player 1, please enter the number of guesses: ")
            wordEntered = True
        else:
            playerOneWord = input("Player 1, please enter a word: ")
    
    
    guessesLeft = int(playerOneNumGuesses)
    
    lettersGuessed = ""
    
    
    # player 2 is prompted to guess letters in the word
    letterGuess = input("Player 2, enter a letter that you think is in the word: ")
    
    correctWordGuessed = False
    
    
    # player 2 continually prompted to guess letters as long as correct word has not yet been guessed
    # and player 2 still has guesses left 		
    while guessesLeft > 0 and not correctWordGuessed : 
        if letterGuess in playerOneWord:
            if letterGuess not in lettersGuessed:
                print("Correct! " + letterGuess + " is in the word.")
                print("Guesses Left:", guessesLeft)
                lettersGuessed += letterGuess
            else:
                print("This letter has already been guessed")
        elif letterGuess not in playerOneWord:
            print("Incorrect. Letter is not in the word")
            lettersGuessed += letterGuess
            guessesLeft -= 1
            print("Guesses Left:", guessesLeft)
        else:
            print("invalid input")
        
        playerTwoWordGuess = ""
        for letter in playerOneWord:
            if letter in lettersGuessed:
                print(letter, end="")
                playerTwoWordGuess += letter
            else:
                print("_ ", end="")
        
        print()
        
	# once player 2 has successfully guessed the word then the game will end 
        if playerTwoWordGuess == playerOneWord:
            correctWordGuessed = True
        else:
            letterGuess = input("Player 2, enter a letter that you think is in the word: ")
    
    
    if correctWordGuessed == True:
        print("Congratulations! " + playerOneWord + " is the correct word")
    else:
        print("You are out of guesses " + playerOneWord + " was the correct word")
    
    # players will be continually prompted to play again until they answer "no" 
    startGame = input("Would you like to play again?(yes, no): ")
    
    # if a player entered "yes" to play again then players will be reminded to switch roles
    if startGame == "yes":
        print("Player 1 will now be player 2 and vice versa")
