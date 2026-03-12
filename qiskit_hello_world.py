# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
#     "pylatexenc",
#     "qiskit[all]==2.3.0",
#     "qiskit-ibm-runtime",
#     "ipython==9.10.0",
#     "seaborn==0.13.2",
#     "sympy==1.14.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Install Qiskit and co.
    Install following packages (using `pip` or `uv`):
    - `qiskit[all]`
    - `pylatexenc` _(for drawing circuits)_
    - `matplotlib` _(for drawing circuits)_
    - `qiskit_ibm_runtime` _(for simulation via IBM)_

    Marimo requires a few more package like: `marimo, ipython, seaborn, sympy` etc. But since this file uses PEP723 with uv, all of this will be auto installed when ran with:

    ```sh
    uvx marimo edit *.py --sandbox
    ```
    """)
    return


@app.cell
def _():
    import qiskit, qiskit_ibm_runtime
    print(f"qiskit = {qiskit.version.get_version_info()}") # 2.0.0
    print(f"qiskit_ibm_runtime = {qiskit_ibm_runtime.version.get_version_info()}") # 0.38.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create and Draw a Quantum Circuit
    """)
    return


@app.cell
def _():
    from qiskit import QuantumCircuit

    return (QuantumCircuit,)


@app.cell
def _(QuantumCircuit):
    # Create a new circuit with two qubits
    qc = QuantumCircuit(2)

    # Add a Hadamard gate to qubit 0
    qc.h(0)

    # Perform a controlled-X gate on qubit 1, controlled by qubit 0
    qc.cx(0, 1)

    # Return a drawing of the circuit using text (useful for running in terminal).
    qc.draw()
    return (qc,)


@app.cell
def _(qc):
    # Return a drawing of the circuit using MatPlotLib/LaTeX.
    # 'text' | 'mpl' | 'latex' (LaTeX is needed) | 'latex_source'
    qc.draw('mpl')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Parametric and Controlled Quantum Gates
    """)
    return


@app.cell
def _(QuantumCircuit):
    from qiskit.circuit import Parameter
    theta = Parameter('θ')
    pqc = QuantumCircuit(4)
    pqc.ry(theta, 0)
    pqc.h(0)
    pqc.cx(0,1, ctrl_state='0')
    pqc.ccx(0,2,3)
    pqc.mcx([0,1,2],3,ctrl_state='001')
    pqc.ch(0,2)
    pqc.cz(0,3)

    phi = Parameter('φ')
    lam = Parameter('λ')
    gamma = Parameter('γ')
    pqc.cu(theta, phi, lam, gamma, 1,2)

    pqc.assign_parameters({theta: 3.14159}, inplace=True)
    pqc.draw("mpl")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Statevector Simulation
    """)
    return


@app.cell
def _():
    from qiskit.quantum_info import Statevector

    return (Statevector,)


@app.cell
def _(Statevector, qc):
    # Set the initial state of the system
    psi = Statevector.from_label("00")
    # or psi = Statevector([1,0,0,0])

    # Evolve the state by the quantum circuit
    psi = psi.evolve(qc)
    psi #or state.data -> np array
    return (psi,)


@app.cell
def _(psi):
    # 'text' | 'latex' | 'latex_source' | 'qsphere' | 'hinton' | 'bloch' | 'city' | 'paulivec'
    psi.draw('latex')
    return


@app.cell
def _(psi):
    psi.draw('qsphere')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Unitary Matrix for the Circuit
    """)
    return


@app.cell
def _(qc):
    from qiskit.quantum_info import Operator

    U = Operator(qc)

    # Show the results
    U #or U.data -> np array
    return Operator, U


@app.cell
def _(U):
    # 'text' | 'latex' | 'latex_source'
    U.draw('latex')
    return


@app.cell
def _(Operator):
    Z = Operator([[1,0],[0,-1]])
    Z.draw('latex')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Measurement using Sampler
    """)
    return


@app.cell
def _(psi):
    psi.draw('latex')
    return


@app.cell
def _(psi):
    # computational basis measurement probabilities
    print(psi.probabilities())
    return


@app.cell
def _(Statevector, psi):
    # probability of getting some state phi using Born rule
    phi_1 = Statevector.from_label('++')
    abs(phi_1.inner(psi)) ** 2
    return


@app.cell
def _(qc):
    # Measure all qubits and store the results in a classical register
    qc.measure_all()
    qc.draw('mpl')
    return


@app.cell
def _(qc):
    # Create a sampler to simulate computational basis measurement
    from qiskit.primitives import StatevectorSampler

    sampler = StatevectorSampler()

    # Simulate running the circuit 1024 times (default) to get probability dist.
    # `qc` is entered as a list because sample can run multiple circuits,
    # each of them will be run 1024 times. Here we are only running one circuit.
    job = sampler.run([qc], shots=1024)
    print(f"Job id: {job.job_id()}")
    return StatevectorSampler, job


@app.cell
def _(job):
    # Grab the result of the circuit at index 0 from the job.
    result = job.result()[0]

    # classical reg that stores the measurement data
    for creg, data in result.data.items():
      counts = data.get_counts()
      print(f"{creg}: {counts}")
    return (counts,)


@app.cell
def _(counts):
    from qiskit.visualization import plot_histogram
    plot_histogram(counts)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Measurement in a Different Basis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Registers
    """)
    return


@app.cell
def _():
    # Let's implement Deutsch-Jozsa (DJ) algorithm
    # It returns all 0's if function is constant
    import random, math
    # dim: bit length of input to function
    # prob_const: probability of getting a constant function
    def generate_balanced_or_constant_function(dim, prob_const=None):
      if not prob_const: # all 0's, all 1's and all balanced
        prob_const = 2/(2 + math.comb(dim,dim//2))
      is_gen_const = random.choices([True, False],
                                    weights=[prob_const, 1-prob_const])[0]
      if is_gen_const:# constant
        return [random.randint(0,1)]*dim
      else:
        balanced_func = [0]*(dim//2) + [1]*(dim//2)
        random.shuffle(balanced_func)
        return balanced_func

    generate_balanced_or_constant_function(2**4)
    return (generate_balanced_or_constant_function,)


@app.cell
def _(QuantumCircuit, generate_balanced_or_constant_function):
    # You may use quantum and classical registers, and name them.
    from qiskit import QuantumRegister, ClassicalRegister

    # oracle generation
    n = 3
    f = generate_balanced_or_constant_function(2**n, 1)

    # Create circuit with 2 quantum registers and 1 classical register
    x_qreg = QuantumRegister(n, 'xqr')
    y_qreg = QuantumRegister(1, 'yqr')
    x_creg = ClassicalRegister(n, 'xcr')
    dj = QuantumCircuit(x_qreg,y_qreg,x_creg)

    # Construct circuit for DJ algorithm
    dj.h(x_qreg) # notice it applies H gate to each qubit in x register
    # create |-> state by applying HX on zero state
    dj.x(y_qreg)
    dj.h(y_qreg)
    dj.barrier()
    # query oracle (inside box)
    # with dj.box():
    for x,fx in enumerate(f):
      if fx:
        dj.mcx(x_qreg,y_qreg,ctrl_state=x)
    dj.barrier()
    # remaining part of DJ algo
    dj.h(x_qreg)
    dj.measure(x_qreg, x_creg)

    dj.draw('mpl')
    return dj, f, n


@app.cell
def _(StatevectorSampler, dj, f, n):
    sampler_1 = StatevectorSampler()
    job_1 = sampler_1.run([dj])
    print(f'Job id: {job_1.job_id()}')
    result_1 = job_1.result()[0]
    counts_1 = result_1.data.xcr.get_counts()
    print(f'Counts: {counts_1}')
    all_0s_count = counts_1.get('0' * n, 0)
    is_const_func = all_0s_count == result_1.data.xcr.num_shots
    # if we get all 0s every shot, 100% of the times, then const
    print(f"Output: {('Constant' if is_const_func else 'Balanced')}")
    # reveal oracle
    print(f'Oracle: {f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Observables and Expectation value calculation
    """)
    return


@app.cell
def _(dj):
    from qiskit.primitives import StatevectorEstimator
    from qiskit.quantum_info import SparseObservable, SparsePauliOp
    observables = [SparsePauliOp.from_sparse_observable(SparseObservable('000I'))]
    estimator = StatevectorEstimator()
    dj.remove_final_measurements()
    job_2 = estimator.run([(dj, observables)])
    print(f'Job id: {job_2.job_id()}')
    result_2 = job_2.result()[0]
    print(f'Expected value: {result_2.data.evs[0]:0.3f}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Noise Simulation
    """)
    return


@app.cell
def _(QuantumCircuit):
    qc_1 = QuantumCircuit(1)
    return


if __name__ == "__main__":
    app.run()
