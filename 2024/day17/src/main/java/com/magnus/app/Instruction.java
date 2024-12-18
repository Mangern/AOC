package com.magnus.app;

public interface Instruction {
    public class InstructionResult {
        Long writeA, writeB, writeC, writePC, writeOut;

        public InstructionResult() {
            this.writeA = null;
            this.writeB = null;
            this.writeC = null;
            this.writePC = null;
            this.writeOut = null;
        }
    }

    InstructionResult execute(Machine machine, long operand);
}
