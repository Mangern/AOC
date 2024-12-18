package com.magnus.app;

import java.util.ArrayList;
import java.util.List;

import com.magnus.app.Instruction.InstructionResult;

public class Machine {
    final static Instruction[] INSTRUCTION_TABLE = {
        new ADV(),
        new BXL(),
        new BST(),
        new JNZ(),
        new BXC(),
        new OUT(),
        new BDV(),
        new CDV()
    };
    long regA, regB, regC;
    int regPC;
    List<Integer> currentProgram;
    ArrayList<Long> output = new ArrayList<>();

    public void run(long initA, long initB, long initC, List<Integer> program) {
        currentProgram = program;
        regA = initA;
        regB = initB;
        regC = initC;
        regPC = 0;
        output.clear();

        while (regPC < currentProgram.size() - 1) {
            int instruction = currentProgram.get(regPC);
            int operand = currentProgram.get(regPC + 1);

            InstructionResult result = INSTRUCTION_TABLE[instruction].execute(this, operand);
            if (result.writeA != null)
                regA = result.writeA;
            if (result.writeB != null)
                regB = result.writeB;
            if (result.writeC != null)
                regC = result.writeC;

            if (result.writePC != null)
                regPC = result.writePC.intValue();
            else
                regPC += 2;

            if (result.writeOut != null)
                output.add(result.writeOut);
        }
    }

    public void dump(List<Integer> program) {
        for (int pc = 0; pc < program.size(); pc += 2) {
            Instruction instr = INSTRUCTION_TABLE[program.get(pc)];
            Integer operand   = program.get(pc+1);
            System.out.println(instr.getClass().toString() + "    " + operand);
        }
    }

    public long readA() {
        return regA;
    }

    public long readB() {
        return regB;
    }

    public long readC() {
        return regC;
    }

    public long getCombo(long operand) {
        if (operand <= 3) return operand;
        if (operand == 4) return regA;
        if (operand == 5) return regB;
        if (operand == 6) return regC;
        throw new IllegalArgumentException("Unexpected combo operand: " + operand);
    }
}
