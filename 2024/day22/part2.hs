import Prelude
import System.IO( isEOF )
import Data.Bits
import Control.Monad (forM_)
import Data.Containers.ListUtils (nubOrd)
import qualified Data.Map.Strict as Map

type Quad = (Int, Int, Int, Int)
type QuadTreeMap = Map.Map Quad Int

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

processLine :: String -> [Int]
processLine line = map (`mod` 10) $ iterate step (stoi line)

delta :: [Int] -> [Int]
delta [] = []
delta (x:[]) = []
delta (x:y:xs) = (y - x) : (delta (y:xs))

quads :: [Int] -> [(Int, Int, Int, Int)]
quads [] = []
quads (x:y:z:[]) = []
quads (x:y:z:w:xs) = (x,y,z,w) : (quads (y:z:w:xs))

evalseq :: [QuadTreeMap] -> (Int, Int, Int, Int) -> Int
evalseq (qtm:qtms) (c1, c2, c3, c4) = 
    (Map.findWithDefault 0 (c1, c2, c3, c4) qtm) + (evalseq qtms (c1, c2, c3, c4))
evalseq [] _ = 0

-- Build the lookup table for a set of prices
buildMap :: QuadTreeMap -> [Int] -> QuadTreeMap
buildMap qtm (a:b:c:d:e:xs) = 
    if Map.member (b-a, c-b, d-c, e-d) qtm then
        buildMap qtm (b:c:d:e:xs)
    else
        buildMap (Map.insert (b-a, c-b, d-c, e-d) e qtm) (b:c:d:e:xs)
buildMap qtm _ = qtm


main :: IO ()
main = do
    input <- getContents
    let inputLines = lines input
    let prices = map (take 2001) $ map processLine inputLines
    let qs = nubOrd $ concat $ map quads $ map delta prices
    let maps = map (buildMap Map.empty) prices
    print $ foldr1 max $ map (evalseq maps) qs
