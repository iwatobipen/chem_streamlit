import pickle
import datamaker
import streamlit as st
st.title('Streamlit + RDKit :rocket:')
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps
from io import BytesIO
from functools import partial
from PIL import Image
from rdkit.Chem.Draw import rdDepictor
rdDepictor.SetPreferCoordGen(True)

import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
            "chemstreamlit",
            url="http://localhost:3001"
            )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)

def my_component():
    component_value = _component_func()
    return component_value

res = my_component()
rfc = pickle.load(open('rf.pkl', 'rb'))
fpfunc = partial(SimilarityMaps.GetMorganFingerprint, radius=2)


mol = Chem.MolFromSmiles(res)
fp = [datamaker.mol2fp(mol)]
kls = rfc.predict(fp)

st.write('predicted class:', datamaker.rclasses[kls[0]])
img = Draw.MolToImage(mol)
bio = BytesIO()
img.save(bio, format='png')
st.image(img)

