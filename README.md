# Run with `marimo`
The [qiskit_hello_world.py](./qiskit_hello_world.py) file is a `marimo` notebook.
At the start of the file, necessary depedencies are mentioned following PEP723.
This is managed by `uv`. And `marimo` uses `--sandbox` to manage the dependencies.
Run using the command:

```sh
uvx marimo edit *.py --sandbox
```

# Alternatively, Run the `.ipynb`
If you prefer jupyter notebook, use the `.ipynb` file. 
The marimo notebook was generated from this `.ipynb` file.

```sh
uvx jupyter notebook *.ipynb
```

# Convert
The marimo notebook was coverted from jupyter notebook using the following command:

```sh
uvx marimo convert *.ipynb -o qiskit_hello_world.py
```