
function Main()
    local n = 103
    local m = 101
    local mt = {}
    for i=1,2 do
        mt[i] = {}
        for j=1,2 do
            mt[i][j] = 0
        end
    end
    for line in io.lines() do
        local _, _, px, py, vx, vy = string.find(line, "p=(-?%d+),(-?%d+)%sv=(-?%d+),(-?%d+)")
        px = tonumber(px)
        py = tonumber(py)
        vx = tonumber(vx)
        vy = tonumber(vy)

        px = px + 100 * vx
        py = py + 100 * vy

        px = px % m
        py = py % n

        if px == (m >> 1) then
            goto continue
        end
        if py == (n >> 1) then
            goto continue
        end

        local i = 1
        local j = 1

        if px > (m >> 1) then
            j = j + 1
        end

        if py > (n >> 1) then 
            i = i + 1
        end

        mt[i][j] = mt[i][j] + 1

        ::continue::
    end

    local ans = mt[1][1] * mt[1][2] * mt[2][1] * mt[2][2]

    print(ans)

end

Main()
