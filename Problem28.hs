main = do
	putStrLn (show $ sumSpriralDiagonals 1001)

sumSpriralDiagonals :: Int -> Int
sumSpriralDiagonals 0 = error("Whoops")
sumSpriralDiagonals 1 = 1
sumSpriralDiagonals x = (4 * x * x) - (6 * x) + 6 + sumSpriralDiagonals(x-2)