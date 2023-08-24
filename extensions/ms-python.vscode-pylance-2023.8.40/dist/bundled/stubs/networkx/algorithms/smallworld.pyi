from ..classes.graph import Graph
from ..utils import not_implemented_for, py_random_state

__all__ = ["random_reference", "lattice_reference", "sigma", "omega"]

@py_random_state(3)
def random_reference(G: Graph, niter=1, connectivity=True, seed=None): ...
@py_random_state(4)
def lattice_reference(G: Graph, niter=5, D=None, connectivity=True, seed=None): ...
@py_random_state(3)
def sigma(G: Graph, niter=100, nrand=10, seed=None) -> float: ...
@py_random_state(3)
def omega(G: Graph, niter=5, nrand=10, seed=None) -> float: ...
