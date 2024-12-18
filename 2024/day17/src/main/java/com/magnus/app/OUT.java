package com.magnus.app;

public class OUT implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        InstructionResult result = new InstructionResult();
        long out = machine.getCombo(operand);
        result.writeOut = out % 8;
        return result;
    }
}
