const std = @import("std");
const mem = std.mem;

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    var grid = std.ArrayList(u8).init(allocator);
    defer grid.deinit();

    var buf: [4096]u8 = undefined;
    var N: i32 = 0;
    var M: i32 = 0;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        try grid.appendSlice(line);
        M = @intCast(line.len);
        N += 1;
    }

    const di = [_]i32{ -1, -1, -1, 0, 0, 1, 1, 1 };
    const dj = [_]i32{ -1, 0, 1, -1, 1, -1, 0, 1 };

    const search = "XMAS";
    var count: usize = 0;

    var xmascount: usize = 0;

    for (0..@intCast(N)) |i| {
        for (0..@intCast(M)) |j| {
            for (0..8) |dir| {
                var found = true;
                for (0..4) |l| {
                    const ii: i32 = @as(i32, @intCast(i)) + di[dir] * @as(i32, @intCast(l));
                    const ij: i32 = @as(i32, @intCast(j)) + dj[dir] * @as(i32, @intCast(l));

                    if (ii < 0 or ii >= N or ij < 0 or ij >= M) {
                        found = false;
                        break;
                    }

                    const idx: i32 = ii * M + ij;

                    if (grid.items[@intCast(idx)] != search[l]) {
                        found = false;
                        break;
                    }
                }
                if (found) count += 1;
            }

            if (i > 0 and i < N - 1 and j > 0 and j < M - 1) {
                const ui = @as(usize, @intCast(i));
                const uj = @as(usize, @intCast(j));
                const uM = @as(usize, @intCast(M));
                const w1 = [3]u8{ grid.items[@intCast((ui - 1) * uM + (uj - 1))], grid.items[@intCast(ui * uM + uj)], grid.items[@intCast((ui + 1) * uM + (uj + 1))] };
                const w2 = [3]u8{ grid.items[@intCast((ui - 1) * uM + (uj + 1))], grid.items[@intCast(ui * uM + uj)], grid.items[@intCast((ui + 1) * uM + (uj - 1))] };
                if ((mem.eql(u8, &w1, "MAS") or mem.eql(u8, &w1, "SAM")) and (mem.eql(u8, &w2, "MAS") or mem.eql(u8, &w2, "SAM")))
                    xmascount += 1;
            }
        }
    }

    std.debug.print("XMAS: {d}\n", .{count});
    std.debug.print("X-MAS: {d}\n", .{xmascount});
}
