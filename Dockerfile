FROM python:3.5
LABEL version="1.0"
LABEL name="CMSC495 Chatbot"
LABEL description="A TensorFlow chatbot for Slack. This container is \
specifically for serving chatbot info, not for training the model or \
testing the model."
RUN mkdir /chatbot; \
    mkdir /chatbot/data; \
    mkdir /chatbot/slack_integration; \
    mkdir /chatbot/working_dir
ADD requirements.txt /chatbot/
ADD data/* /chatbot/data/
ADD slack_integration/* /chatbot/slack_integration/
ADD working_dir/* /chatbot/working_dir/
ADD __init__.py /chatbot/
ADD data_utils.py /chatbot/
ADD punkt_dl.py /chatbot/
ADD run.py /chatbot/
ADD seq2seq_model.py /chatbot/
ADD seq2seq_serve.ini /chatbot/
ADD slackbot_settings_template.py /chatbot/
EXPOSE 80
EXPOSE 443
RUN ["/bin/bash", "-c", "pip install --upgrade virtualenv; \
    virtualenv --system-site-packages /chatbot/venv/tensorflow; \
    source /chatbot/venv/tensorflow/bin/activate; \
    pip install --upgrade -r /chatbot/requirements.txt; \
    python /chatbot/punkt_dl.py"]
ENTRYPOINT ["/bin/bash", "-c", "/chatbot/venv/tensorflow/bin/python3.5 /chatbot/run.py"]