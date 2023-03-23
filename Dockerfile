FROM python
WORKDIR /word_segmentation
COPY ./requirements.txt /word_segmentation/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /word_segmentation/requirements.txt
COPY . /word_segmentation
CMD ["python", "word_segmentation/service/api.py", "--port", "6969"]