# Revision history for tictactoe

## 0.1.0.0 -- YYYY-mm-dd

* First version. Released on an unsuspecting world.(in Haskell)

## 0.2.0.0 -- 2020.12.15

* Second version. Added some artificial intelligent function. So that the 
* computer tic-tac-toe player can be unbeatable.(in Haskell)

## 0.3.0.0 -- 2020.12.16 - 2020.12.25

* Third version, changing the haskell file into python.(in Python3)
* Used pygame to provide a gui for the game.

## 0.4.0.0 -- 2020.12.26 - 2020.12.31

* Fourth version, improved the heuristic algorithm, increased proportion of success. 

### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ###
##    Things need to be improved     ##
## 1.too much duplicated codes       ##        -> abstract them to become a function. 
## 2.didn't use pygame properly,     ##
## don't really understand how to get##        -> try to find out how to use pygame to achieve this
## the mouse event using pygame, so  ##
## I used pyautogui, which causes it ##
## doesn't work properly after       ##
## moving the position of the window ##
## 3.The speed is so terribly        ##        -> 1.didn't define classes properly, did not use the 
## terribly slow.                    ##           characteristic of OOP.
## 4.The proportion of success can   ##           2.use trees, not nested lists.
## still be increased using cleverer ##           3.a-b pruning
## heuristic.                        ##        -> improve the rules of heuristic.
## 5.No test modules.                ##        -> wrote some unit test for each small unit.
### ### ### ### ### ### ### ### ### ###
### ### ### ### ### ### ### ### ### ###