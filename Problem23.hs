main = do
	putStrLn (show (sumOfNonAbundantPairs 28123))

sumOfNonAbundantPairs :: Int -> Int
sumOfNonAbundantPairs n =
    let abundants = [x | x <- [1..n], abundant x]
        abundantPairSums = [a + b | a <- abundants, b <- abundants]
        nonAbundantPairs = filter (`notElem` abundantPairSums) [1..n]
    in sum nonAbundantPairs

abundant :: Int -> Bool
abundant n = (sum $ divisors n) > n
	
divisors :: Int -> [Int]
divisors m = [x | x <- [1..(div m 2)], m `mod` x == 0]