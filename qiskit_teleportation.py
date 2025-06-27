#Creating circuit

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer
from random import randrange

quantum_register=QuantumRegister(3)
classical_register=ClassicalRegister(2)
circuit=QuantumCircuit(quantum_register,classical_register)

circuit.h(quantum_register[0]) #this line is for making an arbitary state ∣ψ⟩

circuit.h(quantum_register[2])
circuit.cx(quantum_register[2],quantum_register[1])
circuit.cx(quantum_register[0],quantum_register[1])
circuit.h(quantum_register[0])

circuit.measure(quantum_register[0],classical_register[1])
circuit.measure(quantum_register[1],classical_register[1])

circuit.x(quantum_register[2]).c_if(classical_register[1],1)
circuit.x(quantum_register[2]).c_if(classical_register[0],1)

#running several times
task=execute(circuit,Aer.get_backend('qasm_simulator'),shots=1024)
count=task.result().get_counts(circuit)
print(count)
