package com.magnus.app;

public class JNZ implements Instruction {
	@Override
	public InstructionResult execute(Machine machine, long operand) {
        if (machine.readA() == 0) {
            return new InstructionResult();
        }
        InstructionResult result = new InstructionResult();
        result.writePC = operand;
        return result;
    }
}
