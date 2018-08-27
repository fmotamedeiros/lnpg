#!/usr/bin/env stack
-- stack --install-ghc runghc

import System.Exit

soma x y = x + y 
sub x y = x - y 
mul x y = x * y 
divisao x y = x / y 

calcular op = do  

    putStrLn "Digite o primeiro operando:"  
    op1 <- getLine

    putStrLn "Digite o segundo operando:"  
    op2 <- getLine

    let x = (read op1 :: Double)
    let y = (read op2 :: Double)

    if op == "1"
        then print (soma x y)
        else putStrLn ""
    if op == "2"
        then print (sub x y)
        else putStrLn ""
    if op == "3"
        then print (mul x y)
        else putStrLn ""
    if op == "4"
        then print (divisao x y)
        else putStrLn ""

    menu
    putStrLn "Digite a operação desejada:"  
    op <- getLine

    if op == "5"
        then exitSuccess
        else putStrLn ""

    calcular op

menu = do
  putStrLn "(1) Soma"
  putStrLn "(2) Sub"
  putStrLn "(3) Mul"
  putStrLn "(4) Divisao"
  putStrLn "(5) Sair"

main = do
  menu
  putStrLn "Digite a operação desejada:"  
  op <- getLine

  if op == "5"
    then exitSuccess
    else putStrLn ""

  calcular op