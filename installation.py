# This is for qiskit installatin 
!pip install qiskit[visualization]==0.43.3 --user

#check versions
import qiskit
versions = qiskit.__qiskit_version__
print("The version of Qiskit is",versions['qiskit'])
print()
print("The version of each component:")
for key in versions:
    print(key,"->",versions[key])
