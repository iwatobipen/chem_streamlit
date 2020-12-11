from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np
classes = {'(A) low':0, '(B) medium':1, '(C) high':2 }
rclasses = {0:'(A) low', 1:'(B) medium', 2: '(C) high'}
def mol2fp(mol):
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)
    arr = np.zeros((0,))
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr

def make_data(sdf):
    mols = [m for m in Chem.SDMolSupplier(sdf) if m !=None]
    X = np.array([mol2fp(m) for m in mols])
    Y = [classes[m.GetProp('SOL_classification')] for m in mols]
    Y = np.array(Y)
    return (X, Y)

