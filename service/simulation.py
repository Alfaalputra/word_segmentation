import os
import sys

import streamlit as st

path_this = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(path_this, ".."))
src_path = os.path.join(root_path, "src")
sys.path.append(src_path)

from inference import Inference


st.header("Bahasa Indonesia Word Segmentation")
inf = Inference()
text = st.text_area('Input here')

process = st.button("Process")
if process:
    result = {}
    segment = inf.segment(text)

    result["text"] = text
    result["result"] = segment
    st.write(result)