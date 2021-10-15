from outdated import warn_if_outdated
import qiskit
import pyquil
warn_if_outdated('qiskit', qiskit.__version__)
warn_if_outdated('pyquil', pyquil.__version__)
