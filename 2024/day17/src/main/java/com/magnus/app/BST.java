package com.magnus.app;

public class BST implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        InstructionResult result = new InstructionResult();
        long op1 = machine.getCombo(operand);
        result.writeB = op1 % 8;
        return result;
    }
}
