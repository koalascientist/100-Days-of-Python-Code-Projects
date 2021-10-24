# Blackjack Game

## Description

_Blackjack_  is one of the most popular casino card games in the world and it involves a player and a dealer. The goal of the game is to beat the dealer.

A player beats the dealer when:  
 1. he gets Blackjack (i.e. first two cards equal to 21), and the dealer does not get Blackjack. If both the player and the dealer get Blackjack, the player loses; or
 2. he has the final card count higher than that of the dealer, and player's total score does not exceed 21; or
 3. his total card count is lower than 21 but the dealer's total score is above 21.

Cards from 2 to 10 are counted as their face value. A jack, queen or king has a value of 10, and an ace has a value of either 11 or 1. An ace will always be assigned a value of 11 as long as total card score is below 21. When total card score is above 21, the value of the ace will be equal to 1. 

## Logic of the game

In the beginning of the game, 2 cards are drawn for each party: the player and the dealer. The 2 cards of the player are known to both parties, while the player can only see the first card of the dealer. Immediately, each party's total card scores are checked for Backjack condition.

If there is no Blackjack, then the game continues. The player is asked if he wants an additional card. The question will not be asked again if the player's total card score goes above 21 or if the player decides that he does not need additional cards. 

Meanwhile, the computer will continue to draw cards as long as the total card score is below 17. When the total card is score goes above 17, the computer will not draw any additional cards.

The winner of the game is declared according to the rules stated in the description of the game. 

## Other assumptions

 1. The deck in unlimited in size. This means that the cards in the list have equal probability of being drawn and cards are not removed from the deck as they are drawn.
 2. There are no jokers involved. 