# Unbeatable_Tictactoe
This is a tic-tac-toe game. The first version uses language Haskell, I rewrote it, added some artificial intelligence algorithm to make it unbeatable, made a GUI for it using pygame, and wrote a test for it to reveal the increase of the rate of success after each time of algorithm improvement. 
# python version == 3.x

# name:                Unbeatable_Tictactoe
# version:             0.4.0.0
synopsis:
description:
bug-reports:
* license:
# license-file:        LICENSE
# author:              U70-TK
# maintainer:          wtkuan@163.com
-- copyright:
-- category:
# build-type:          Simple
# extra-source-files:  CHANGELOG.md    
            Descriptions of modification of each version, and things need to be improved.

* executable tictactoe
##  main-is:             Tictactoe
##  other-modules:       test     ## to test the rate of success. 
##  -- other-extensions:
    backgroud.jpg      ## The first backgroud.
    backgroud2.jpg     ## The second backgroud.
    O.jpg              ## The case O operate or win.
    X.jpg              ## The case X operate or win.
    draw.jpg           ## The case a draw happens.
    Restart1.png       ## The image shows when one of the two players wins 
                       ## and inform the player to press keys to restart. 
    O1.txt-O9.txt      ## Uses the function which builds a tree, store the tree(using nested lists)
                       ## at these files, so that the action of invoking the tree later can be faster. 
##  build-depends:       base >=4.13 && <4.14
##  -- py-source-dirs:  os,sys,pyautogui,time,pygame
##  default-language:    python3

* test-suite tictactoe-test
##  type:               exitcode-stdio-1.0
##  main-is:            
##  other-modules:      TicTacToe
##  build-depends:      
##  default-language: 	
