# quantum_behavioral_analysis.py
"""
Quantum Behavioral Analysis Module (Experimental)

Analyzes user/agent interactions and task update streams using quantum-inspired and classical algorithms.
Handles: KB/task history, chat logs, event sequences.

Note: Requires Qiskit for quantum kernels, but can fallback to classical methods.
"""

import numpy as np
try:
    from qiskit_machine_learning.kernels import QuantumKernel
    QISKIT_OK = True
except ImportError:
    QISKIT_OK = False

class BehavioralAnalyzer:
    def __init__(self, use_quantum=True):
        self.use_quantum = use_quantum and QISKIT_OK
        if self.use_quantum:
            from qiskit.circuit.library import ZZFeatureMap
            self.feature_map = ZZFeatureMap(feature_dimension=2, reps=2)
            self.kernel = QuantumKernel(feature_map=self.feature_map)
        else:
            from sklearn.metrics.pairwise import rbf_kernel
            self.kernel = lambda X, Y=None: rbf_kernel(X, Y)

    def encode_data(self, data):
        # Simple encoding: mean & variance as [x, y] per event
        arr = np.array([[np.mean(x), np.var(x)] for x in data])
        return arr

    def analyze(self, sequences):
        X = self.encode_data(sequences)
        sim_matrix = self.kernel.evaluate(X) if self.use_quantum else self.kernel(X)
        return sim_matrix

    def summary(self, sim_matrix):
        # Example: return pairs of most similar/least similar events
        max_pair = np.unravel_index(np.argmax(sim_matrix), sim_matrix.shape)
        min_pair = np.unravel_index(np.argmin(sim_matrix), sim_matrix.shape)
        return {
            'most_similar': max_pair,
            'least_similar': min_pair,
            'matrix': sim_matrix.tolist()
        }
