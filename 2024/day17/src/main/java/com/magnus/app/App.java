package com.magnus.app;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String line = in.nextLine();
        long initA = Long.parseLong(line.split(":")[1].trim());
        line = in.nextLine();
        long initB = Long.parseLong(line.split(":")[1].trim());
        line = in.nextLine();
        long initC = Long.parseLong(line.split(":")[1].trim());
        in.nextLine();
        line = in.nextLine();
        String[] programValues = line.split(":")[1].trim().split(",");

        List<Integer> program = new ArrayList<>();
        for (String value : programValues) {
            program.add(Integer.parseInt(value.trim()));
        }

        in.close();

        Machine machine = new Machine();
        machine.run(initA, initB, initC, program);

        StringBuilder out = new StringBuilder();

        for (var x : machine.output) {
            if (out.length() > 0) {
                out.append(',');
            }
            out.append(x);
        }
        System.out.println(out.toString());
    }
}
