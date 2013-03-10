import System.Environment
import Data.List
import Data.Char

main = do
	args <- getArgs
	allNames <- readFile (head args)
	putStrLn (show (sum (zipWith (\n w -> n * (wordScore w)) [1..] (sort (lines allNames)))))

wordScore :: String -> Int  
wordScore [] = 0
wordScore (x:xs) = (ord x - ord 'A') + 1 + (wordScore xs)