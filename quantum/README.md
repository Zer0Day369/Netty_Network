# Quantum Behavioral Analysis (experimental)

## Overview
This module provides quantum-inspired/computing tools to analyze user/agent behavioral logs and task update streams. It works on:
- Chat interaction logs
- Task platform update sequences
- Any canonical event list from the Netty_Network knowledge base

It uses simple vector encodings and a quantum kernel (Qiskit) if available, falling back to a classic RBF kernel if not. Outputs a similarity matrix and finds most/least similar activities. Results are intended for research.

## How to run

1. Install requirements (qiskit, scikit-learn, numpy, jupyter)
2. See [behavioral_analysis_demo.ipynb](./behavioral_analysis_demo.ipynb) for an example on dummy data
3. Adapt encoding to your event schema as needed (see encode_data)
4. Use with real KB data by passing lists of events (arrays of floats/features per event)

## Integration
- Call from agent planner/executor modules if advanced behavioral/sequence analysis is desired.
- Can be invoked as a research “introspector” or to detect novel patterns.

## Limitations
- ONLY for prototyping/research.
- Not useful for production risk/real-time yet.
- Qiskit is simulated unless you configure a quantum provider.
