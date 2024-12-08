import Prelude
import System.IO( isEOF )

splitColon :: String -> [String]
splitColon s = case dropWhile (==':') s of
                    "" -> []
                    s' -> w : splitColon s''
                        where (w, s'') = break (==':') s'

stoi :: String -> Int
stoi s = read s

-- we want: a left fold with both + and * at each point
foldOp :: [Int] -> Int -> [Int]
foldOp [] x = [x]
foldOp zs x = (map (+x) zs) ++ (map (*x) zs)

processLine :: IO Int
processLine = do
    end <- isEOF
    if not end then do
        line <- getLine
        let [targets, xss] = splitColon line
        let target = stoi targets
        let numbers = foldl foldOp [] $ map stoi $ words $ xss
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
