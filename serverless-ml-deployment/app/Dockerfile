FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ./


RUN yum install -y \
    freetype-devel \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    curl \
    tar \
    gzip \
    && yum clean all

RUN python3.10 -m pip install -r requirements.txt -t .

RUN pip uninstall -y pillow 

RUN CC="cc -mavx2" pip install -U --force-reinstall pillow-simd

COPY app.py ./

# Download ResNet50 and store it in a directory
#RUN mkdir -p /opt/ml/model 
#RUN curl -L https://www.kaggle.com/api/v1/models/google/resnet-v1/tensorFlow2/50-classification/2/download -o /opt/ml/model/resnet.tar.gz

#RUN tar -xf /opt/ml/model/resnet.tar.gz -C /opt/ml/model 
#RUN rm -rf /opt/ml/model/resnet.tar.gz

# Download ImageNet labels
#RUN curl https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt -o /opt/ml/model/ImageNetLabels.txt

CMD ["app.lambda_handler"]
