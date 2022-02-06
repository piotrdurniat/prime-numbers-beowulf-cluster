# Parallel Sieve of Eratosthenes algorithm for Beowulf clusters

Sieve of Eratosthenes algorithm implementation written to test the performance of parallel computing on a Beowulf cluster.
The algorithm uses the MPI standard for node communication and is written in Python using the mpi4py package.

## Files in the repository:

- `eratosthenes.py` contains a standard (serial) implementation of the Sieve of Eratosthenes algorithm.
- `eratosthenes-cluster.py` contains a parallel version of the Sieve of Eratosthenes algorithm.
- `trial-division.py` contains an implementation of Trial Division algorithm for a single processor.
- `trial-division-cluster.py` contains a parallel version of the Trial Division algorithm.
- `beowulf-copy.sh` is a script to copy a given file to every node of the cluster.
- `beowulf-test.sh` is a script to test if the configured cluster is working.
- `beowulf-exec.sh` executes the provided command on every node of the custer.
