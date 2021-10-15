from outdated import warn_if_outdated
from outdated.mywarnings import OutdatedPackageWarning
import qiskit
import pyquil
try:
    warn_if_outdated('qiskit', qiskit.__version__, raise_exceptions=True)
except OutdatedPackageWarning as warn:
    print(warn)
#warn_if_outdated('pyquil', pyquil.__version__)
