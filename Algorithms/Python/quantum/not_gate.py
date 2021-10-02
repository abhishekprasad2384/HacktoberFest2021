#!/usr/bin/env python3
"""
Build a simple bare-minimum quantum circuit that starts with a single
qubit (by default, in state 0) and inverts it. Run the experiment 1000
times and print the total count of the states finally observed.
Qiskit Docs: https://qiskit.org/documentation/getting_started.html
"""

import qiskit as q


def single_qubit_measure(qubits: int, classical_bits: int) -> q.result.counts.Counts:
    """
    >>> single_qubit_measure(2, 2)
    {'11': 1000}
    >>> single_qubit_measure(4, 4)
    {'0011': 1000}
    """
    # Use Aer's qasm_simulator
    simulator = q.Aer.get_backend("qasm_simulator")

    # Create a Quantum Circuit acting on the q register
    circuit = q.QuantumCircuit(qubits, classical_bits)

    # Apply X (NOT) Gate to Qubits 0 & 1
    circuit.x(0)
    circuit.x(1)

    # Map the quantum measurement to the classical bits
    circuit.measure([0, 1], [0, 1])

    # Execute the circuit on the qasm simulator
    job = q.execute(circuit, simulator, shots=1000)

    # Return the histogram data of the results of the experiment.
    return job.result().get_counts(circuit)


if __name__ == "__main__":
    counts = single_qubit_measure(2, 2)
    print(f"Total count for various states are: {counts}")
