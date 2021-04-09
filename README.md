# Unbeatable_Tictactoe
This is a tic-tac-toe game. The first version uses language Haskell, I rewrote it, added some artificial intelligence algorithm to make it unbeatable, made a GUI for it using pygame, and wrote a test for it to reveal the increase of the rate of success after each time of algorithm improvement. 
Anyone who has some ideas on improving the things listed in CHANGELOG.md are welcome.
This program is only for non-commercial use.
这是一款井字棋游戏，最初的版本是由Haskell语言编写，我重写了它，并加入了一些人工智能算法来使得它无法被击败。我为它写了图形用户界面，并写了一个测试文件来反应每次改进算法带来的成功率增加。 
有想法改进我列在CHANGELOG.md文件中本游戏的缺点和不足的人欢迎进行改进。
这个程序仅用于非商业性用途。
# python version == 3.x

# name:                Unbeatable_Tictactoe
# version:             0.4.0.0
* synopsis:
* description:
* bug-reports:
* license:
# license-file:        LICENSE
# author:              U70-TK
# maintainer:          wtkuan@163.com
* -- copyright:
* -- category:
# build-type:          Simple
# extra-source-files:  CHANGELOG.md    
    Descriptions of modification of each version, and things need to be improved.

##  executable tictactoe
##  main-is:             Tictactoe
##  other-modules:       test     ## to test the rate of success. 
##  other-extensions:
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

##  test-suite tictactoe-test
##  type:               exitcode-stdio-1.0
##  main-is:            
##  other-modules:      TicTacToe
##  build-depends:      
##  default-language: 	
