# Blind Auction Game

## Description

A _blind auction_  is a type of auction where all bidders submit secret bids at the same time so that no bidder knows the bid of any other participant. The bidder with the highest bid amount wins the auction.

## Code structure

**art.py** file contains the ASCII logo of the Blind Auction game.

**main.py** file contains the code for Blind Auction.

! Please make sure to keep all files in one folder when running the code.

## _main.py_ structure

The program will ask the user to input his/her name and the bid amount. After the user provides the information required, the program will ask if there are any other bidders. If there are more bidders, then the program will clear the console and ask for the inputs of all the bidders.

All the the data of the bidders are stored in a dictionary.

The winner of the auction is the person with the highest bid. In case when 2 or more bidders have provided 2 or more equal bids, and their bids are the highest, all the bidders with the highest bids are declared as winners.

In the end, the program reveals the winner(s) and the highest bid amount.  
