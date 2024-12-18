package com.magnus.app;

public class ADV implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        InstructionResult result = new InstructionResult();
        long op1 = machine.readA();
        long op2 = machine.getCombo(operand);
        result.writeA = op1 >> op2;
        return result;
    }
}
