package com.magnus.app;

public class BXC implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        InstructionResult result = new InstructionResult();
        long op1 = machine.readB();
        long op2 = machine.readC();

        result.writeB = op1 ^ op2;
        return result;
    }
}
