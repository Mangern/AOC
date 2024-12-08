import Prelude
import System.IO( isEOF )

splitColon :: String -> [String]
splitColon s = case dropWhile (==':') s of
                    "" -> []
                    s' -> w : splitColon s''
                        where (w, s'') = break (==':') s'

stoi :: String -> Int
stoi s = read s

toString :: Int -> String
toString x = show x

concatInts :: Int -> Int -> Int
concatInts x y = stoi $ (toString x) ++ (toString y)

-- we want: a left fold with both + and * at each point
-- for part two: concat || simply part of the opset
foldOp :: (Int, [Int]) -> Int -> (Int, [Int])
foldOp (target, []) x = (target, [x])
foldOp (target, zs) x = (target, filter (<=target) $ (map (+x) zs) ++ (map (*x) zs) ++ (map (flip concatInts x) zs))

processLine :: IO Int
processLine = do
    end <- isEOF
    if not end then do
        line <- getLine
        let [targets, xss] = splitColon line
        let target = stoi targets
        let (_, numbers) = foldl foldOp (target, []) $ map stoi $ words $ xss
        rem <- processLine
        if (target `elem` numbers) then
            return $ rem + target
        else
            return rem
    else
        return 0

main :: IO ()
main = do
    res <- processLine
    print res
