main = do
	putStrLn (show (sum $ filter (amicable 10000) [1..10000]))

amicable :: Int -> Int -> Bool
amicable n x =
    let sumOfXDivisors = (sum $ divisors x)
        correspondingSum = (sum $ divisors sumOfXDivisors)
    in (x == correspondingSum) && (sumOfXDivisors < n) && (sumOfXDivisors /= x)

divisors :: Int -> [Int]
divisors m = [x | x <- [1..(div m 2)], m `mod` x == 0]