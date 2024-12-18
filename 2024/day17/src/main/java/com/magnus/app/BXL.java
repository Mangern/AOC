package com.magnus.app;

public class BXL implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        InstructionResult result = new InstructionResult();
        long op1 = machine.readB();

        result.writeB = op1 ^ operand;
        return result;
    }
}
