import Prelude
import System.IO( isEOF )
import Data.Bits
import Control.Monad (forM_)

stoi :: String -> Int
stoi s = read s

mix :: Int -> Int -> Int
mix x y = xor x y 

prune :: Int -> Int
prune x = x `mod` 16777216

step1 :: Int -> Int
step1 x = prune $ mix x $ x * 64

step2 :: Int -> Int
step2 x = prune $ mix x $ x `div` 32

step3 :: Int -> Int
step3 x = prune $ mix x $ x * 2048

step :: Int -> Int
step x = step3 $ step2 $ step1 x

processLine :: String -> Int
processLine line = iterate step (stoi line) !! 2000

main :: IO ()
main = do
    input <- getContents
    let inputLines = lines input
    let results = map processLine inputLines
    print $ sum results
