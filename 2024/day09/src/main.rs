use std::{io, usize};
use std::collections::VecDeque;
use std::cmp;

fn part1(buf: &String) -> usize {
    // count, id
    let mut deq: VecDeque<(usize, usize)> = VecDeque::new();

    for (i, c) in buf.chars().enumerate() {
        if i % 2 == 0 {
            deq.push_back((c.to_digit(10).unwrap() as usize, ((i+1) >> 1) as usize));
        }
    }

    let mut res = Vec::new();

    for (i, c) in buf.chars().enumerate() {
        let mut cnt = c.to_digit(10).unwrap() as usize;
        if deq.is_empty() {
            break;
        }
        if i % 2 == 0 {
            let (count, id) = deq.pop_front().unwrap();
            for _ in 0..count {
                res.push(id);
            }
        } else {
            loop {
                let (count, id) = deq.pop_back().unwrap();

                for _ in 0..cmp::min(count, cnt) {
                    res.push(id);
                }

                if cnt < count {
                    deq.push_back((count - cnt, id));
                    break;
                }
                if deq.is_empty() {
                    break;
                }
                cnt -= count;
            }
        }
    }

    res.iter().enumerate().fold(0, |acc, (i, &e)| acc + e * i)
}

fn part2(buf: &String) -> i64 {
    let mut res: Vec<i64> = Vec::new();

    // count, id, pos
    let mut deq: Vec<(usize, usize, usize)> = Vec::new();

    let mut spaces: Vec<Vec<usize>> = Vec::new();

    for _ in 0..10 {
        spaces.push(Vec::new());
    }

    for (i, c) in buf.chars().enumerate() {
        let cnt = c.to_digit(10).unwrap();
        if i % 2 == 0 {
            let id = (i + 1) >> 1;
            deq.push((cnt as usize, id, res.len()));
            for _ in 0..cnt {
                res.push(id as i64);
            }
        } else {
            spaces[cnt as usize].push(res.len());
            for _ in 0..cnt {
                res.push(-1);
            }

        }
    }

    for i in 0..10 {
        spaces[i].reverse();
    }

    while !deq.is_empty() {
        let (cnt, id, pos) = deq.pop().unwrap();
        let mut wpos = pos;
        let mut mspc = 0;

        for i in cnt..10 {
            let candidate = *spaces[i].last().unwrap();
            if !spaces[i].is_empty() && candidate < pos {
                if candidate < wpos {
                    wpos = candidate;
                    mspc = i;
                }
            }
        }

        if wpos < pos {
            for i in 0..cnt {
                let idx = wpos + i;
                res[idx] = id as i64;
                res[pos+i] = -1;
            }

            spaces[mspc].pop();
            if mspc > cnt {
                spaces[mspc - cnt].push(wpos + cnt);
            }
        }

    }
    res.iter().enumerate().fold(0i64, |acc, (i, &e)| acc + i as i64 * (if e >= 0 { e } else { 0 }))
}

fn main() {
    let mut buf = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut buf).unwrap();
    buf.pop();

    println!("Part 1: {}", part1(&buf));
    println!("Part 2: {}", part2(&buf));
}
