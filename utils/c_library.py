import ctypes
import os

# Load your compiled C library
lib_path = os.path.join(os.path.dirname(__file__), "viable.so") # Use Viable.dll on Windows
clibrary = ctypes.CDLL(lib_path)

# Define C function interfaces
clibrary.initialize_system.restype = None
clibrary.set_aeration.argtypes = [ctypes.c_int]
clibrary.set_aeration.restype = None
clibrary.compute_with_cosmos.argtypes = [ctypes.c_int]
clibrary.compute_with_cosmos.restype = ctypes.c_int

def use_clibrary(cosmos_value):
    clibrary.initialize_system()
    clibrary.set_aeration(5)
    result = clibrary.compute_with_cosmos(cosmos_value)
    return result
