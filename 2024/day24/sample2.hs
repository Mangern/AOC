import Data.Bits
x00 = 0
x01 = 1
x02 = 0
x03 = 1
x04 = 0
x05 = 1

y00 = 0
y01 = 0
y02 = 1
y03 = 1
y04 = 0
y05 = 1

z :: Int -> Int
z 00 = x05 .&. y05
z 01 = x02 .&. y02
z 02 = x01 .&. y01
z 03 = x03 .&. y03
z 04 = x04 .&. y04
z 05 = x00 .&. y00

main :: IO ()
main = do
    print $ foldl (\acc bit -> acc * 2 + bit) 0 $ reverse [z x | x <- [0..5]]
