import re

from src.correction import Correction
from src.segmentation import Segmentation

seg = Segmentation(corpus="wiki_corpus")
cor = Correction(corpus="wiki_corpus")

class Inference:

    def segment(self, text):
        txt = re.sub(r"([a-zA-Z])-\s", r"\1", text)
        txt = re.sub(r"((\d%|\d)\-)\s", r"\1", txt)
        splits = txt.split()
        segmented = [seg.segment(spl) for spl in splits]
        segmented = " ".join(segmented)
        txt = re.sub(r"^\"\s", "\"", segmented)
        txt = re.sub(r"\s\.", ".", txt)
        txt = re.sub(r"\s\,", ",", txt)
        txt = re.sub(r"\(\s", "(", txt)
        txt = re.sub(r"\/\s", "/", txt)
        txt = re.sub(r"\s-\s", "-", txt)
        txt = re.sub(r"\s\s", " ", txt)
        txt = re.sub(r"(\d\.)\s(\d+)", r"\1\2", txt)
        txt = re.sub(r"(\d,)\s(\d+)", r"\1\2", txt)
        txt = re.sub(r"([A-Z])\s(\d)\s", r"\1\2", txt)
        txt = re.sub(r"^([a-zA-Z])\.\s", r"\1", txt)
        txt = re.sub(r"^\'\s", r"'", txt)
        txt = re.sub(r"\.\s(\")\s([a-zA-Z\d])", r"\. \1\2", txt)

        return txt
    

    def correct(self, text):
        txt = re.sub(r"([a-zA-Z])-\s", r"\1", text)
        txt = re.sub(r"((\d%|\d)\-)\s", r"\1", txt)
        splits = txt.split()
        corrected = [cor.correct(spl) for spl in splits]
        corrected = " ".join(corrected)
        txt = re.sub(r"^\"\s", "\"", corrected)
        txt = re.sub(r"\s\.", ".", txt)
        txt = re.sub(r"\s\,", ",", txt)
        txt = re.sub(r"\(\s", "(", txt)
        txt = re.sub(r"\/\s", "/", txt)
        txt = re.sub(r"\s-\s", "-", txt)
        txt = re.sub(r"\s\s", " ", txt)
        txt = re.sub(r"(\d\.)\s(\d+)", r"\1\2", txt)
        txt = re.sub(r"(\d,)\s(\d+)", r"\1\2", txt)
        txt = re.sub(r"([A-Z])\s(\d)\s", r"\1\2", txt)
        txt = re.sub(r"^([a-zA-Z])\.\s", r"\1", txt)
        txt = re.sub(r"^\'\s", r"'", txt)
        txt = re.sub(r"\.\s(\")\s([a-zA-Z\d])", r"\. \1\2", txt)

        return cor.correct(text)
