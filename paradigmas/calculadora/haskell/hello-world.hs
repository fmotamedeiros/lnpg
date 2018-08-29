#!/usr/bin/env stack
-- stack --install-ghc runghc

sucessor n = n + 1
antecessor n = n - 1

fatorial n = if n == 0 then 1 else n * fatorial (n - 1)

main = do 
    print (sucessor 3)
    print (antecessor 3)
    print (fatorial 4)
          