import cirq
import random

def quantum_random_number(bits=2):
    # Create a quantum circuit with multiple qubits
    qubits = [cirq.GridQubit(0, i) for i in range(bits)]
    circuit = cirq.Circuit()

    # Apply Hadamard gates to create superposition for each qubit
    for qubit in qubits:
        circuit.append(cirq.H(qubit))

    # Apply random quantum gates (X, Y, Z) to each qubit
    for idx, qubit in enumerate(qubits):
        random_exponent = random.uniform(0, 1)
        circuit.append(cirq.X(qubit)**random_exponent)  # X gate with a random exponent

        random_exponent = random.uniform(0, 1)
        circuit.append(cirq.Y(qubit)**random_exponent)  # Y gate with a random exponent

        random_exponent = random.uniform(0, 1)
        circuit.append(cirq.Z(qubit)**random_exponent)  # Z gate with a random exponent

        random_exponent = random.uniform(0, 1)
        circuit.append(cirq.H(qubit)**random_exponent)

    circuit.append(cirq.measure(*qubits, key='result1'))

    for idx, qubit in enumerate(qubits):
        circuit.append(cirq.CNOT(qubit, qubits[(idx + 1) % len(qubits)]))

    for idx, qubit in enumerate(qubits):
        circuit.append(cirq.CNOT(qubit, qubits[(idx + 1) % len(qubits)]))


    # Measure the qubits
    circuit.append(cirq.measure(*qubits, key='result2'))

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit)

    # Extract the measurement result
    random_number_1 = result.measurements['result1'][0]
    random_number_2 = result.measurements['result2'][0]

    print(circuit)

    return random_number_1, random_number_2

# Generate a random 2-bit binary number
random_number_1, random_number_2 = quantum_random_number(bits=8)

print(f"Generated random 2-bit binary number: {random_number_1}")
print(int("".join(map(str, random_number_1)), 2))

print(f"Generated random 2-bit binary number: {random_number_2}")
print(int("".join(map(str, random_number_2)), 2))
