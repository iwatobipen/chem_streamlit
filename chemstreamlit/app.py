import pickle
import streamlit as st
import datamaker
st.title('Streamlit + RDKit :rocket:')
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps
from io import BytesIO
from functools import partial
from PIL import Image
from rdkit.Chem.Draw import rdDepictor
rdDepictor.SetPreferCoordGen(True)
#rfc = pickle.load(open('rf.pkl', 'rb'))
#for streamlit app
rfc = pickle.load(open('/app/chem_streamlit/chemstreamlit/rf.pkl', 'rb'))
fpfunc = partial(SimilarityMaps.GetMorganFingerprint, radius=2)

#mols = [m for m in Chem.SDMolSupplier('./solubility.test.sdf')]
mols = [m for m in Chem.SDMolSupplier('/app/chem_streamlit/chemstreamlit/solubility.test.sdf')]

option = st.selectbox(
    'Please select index of test molecules',
    [i for i in range(len(mols))]
)

st.write('you selected:', option, Chem.MolToSmiles(mols[option]))
fp = [datamaker.mol2fp(mols[option])]
kls = rfc.predict(fp)


img = Draw.MolToImage(mols[option])
bio = BytesIO()
img.save(bio, format='png')
st.image(img)

st.write('predicted class:', datamaker.rclasses[kls[0]])
