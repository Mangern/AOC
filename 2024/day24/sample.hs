import Data.Bits
x00 = 1
x01 = 0
x02 = 1
x03 = 1
x04 = 0
y00 = 1
y01 = 1
y02 = 1
y03 = 1
y04 = 1

tnw = (y02 .|. x01)
bfw = (vdt .|. tnw)
bqk = (ffh .|. nrd)
djm = (y00 .&. y03)
ffh = x03 `xor` y03
fgs = (y04 .|. y02)
frj = (tnw .|. fst1)
fst1 = (x00 .|. x03)
gnj = (tnw .|. pbm)
hwm = (nrd .&. vdt)
kjc = (x04 .&. y00)
kpj = (pbm .|. djm)
kwq = (ntg .|. kjc)
mjb = ntg `xor` fgs
nrd = (y03 .|. x01)
ntg = x00 `xor` y04
pbm = (y01 .&. x02)
psh = (y03 .|. y00)
qhw = (djm .|. pbm)
rvg = (kjc .&. fst1)
tgd = psh `xor` fgs
vdt = (x03 .|. x00)
wpb = nrd `xor` fgs

z :: Int -> Int
z 00 = bfw `xor` mjb
z 01 = tgd `xor` rvg
z 02 = gnj .&. wpb
z 03 = hwm .&. bqk
z 04 = frj `xor` qhw
z 05 = kwq .|. kpj
z 06 = bfw .|. bqk
z 07 = bqk .|. frj
z 08 = bqk .|. frj
z 09 = qhw `xor` tgd
z 10 = bfw .&. frj
z 11 = gnj .&. tgd
z 12 = tgd `xor` rvg

main :: IO ()
main = do
    print $ foldl (\acc bit -> acc * 2 + bit) 0 $ reverse [z x | x <- [0..12]]
