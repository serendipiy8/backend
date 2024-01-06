# set basic mirror
FROM python:3.10-slim-bullseye

# set timezone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Build folder
RUN mkdir -p /my_project/my_api
WORKDIR /my_project/my_api
COPY ./api/. /my_project/my_api

# copy requirements.txt.   others will be mounted by -v
COPY ./api/requirements.txt /my_project/my_api/requirements.txts

# Create a virtual environment
RUN pip install -r /my_project/my_api/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn \
&& pip install gunicorn==20.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

# RUN sed -i 's/import name 'secure_filename' from 'werkzeug'/from werkzeug.utils import secure_filename/g' /usr/local/lib/python3.10/site-packages/werkzeug/__init__.py

# RUN sed -i 's/from werkzeug import secure_filename, FileStorage/from werkzeug.datastructures import FileStorage\nfrom werkzeug.utils import secure_filename/g' /usr/local/lib/python3.10/site-packages/flask_uploads.py

RUN sed -i 's/from flask._compat import text_type/from flask_script._compat import text_type/g' /usr/local/lib/python3.10/site-packages/flask_script/__init__.py