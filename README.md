*For my Programming Midterm project, I chose to create a Python version of the popular card game known as "War".

*One creative freedom that I took when creating my game was to add a theme following the popular video game series called "Halo".

*Another small difference between my version of War in python and the version that would typically be played with cards is that when
you play it in real life with cards you obviously would have a second player to play with. In my version of the game, I programmed
an AI player that you play against and try to beat in order to win the game. It is also important to note that my game does not have
much actual gameplay due to the fact that war is more of a game of chance rather than a game of skill so there are no actual decisions
that you can make in the game because you just draw random cards each round. Due to this fact, when you run my game it runs through the
entire game instantaneously and gives you a very detailed description of each round, who won the game, how many times war was played, etc.
The reason that I did not incorporate a function to allow the player to draw their own card is because War can technically go on forever
so if I did that the game may never end and the player would get bored or their computer would crash before they finish the game.

*The basic rules of War are that a standard 52 card deck is split in half between two players and each player has a hand of 26 cards that
are randomly ordered and face down so that the player cannot see their own cards. At the start of each round, each player flips over the
top card from their pile and which ever card has a higher value (Jack is worth 11; Queen, 12; King, 13; Ace, 14 respectively), wins both
cards and adds them to the bottom of their hand. When two players draw the same value card, it is called "war" and the players each draw
three more cards face down, and then flip over a fourth card and these are the cards that they compare values of. If each player's fourth
card have the same value as each other, they enter double war and repeat the same war process until a winner is determined. The game is
over once one player gains all 52 cards in the deck, meaning that technically this game can last for an infinite number of rounds.

*While programming my game, I used a few sources for reference in how to set up my code and used some other resources including my friend
to learn a few new python commands that helped me simplify my code and make it work more smoothly

*Some of the new python commands that I learned to use were "from random import shuffle", ".split()", "len()", "index()", "try:" and "except:"

*When using these new commands that I had to learn, the most difficult to incorporate was the try and except command because it was somewhat
confusing to understand where exactly to use it. Originally in my code I was using if, elif, and else exclusively but in some places that didn't
work very well (the double war section), so I consulted a friend who knows a decent amount about coding and he told me to try using try and except
to replicate a similar effect so that if the code in the try block did not work then it would advance down to the except block and run that instead.

Resources:
https://www.pythonforbeginners.com/error-handling/python-try-and-except
https://docs.python.org/3/genindex-all.html
https://stackoverflow.com/questions/19804154/war-card-game-help-python

Flowchart: https://drive.google.com/file/d/11IWyBOLD9niKOVH93YpSarIgoDQZc3fH/view?usp=sharing




