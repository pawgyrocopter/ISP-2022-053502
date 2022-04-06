FROM python:3.10-slim
ADD main.py /
ADD methods.py /
ADD solution.py /
CMD [ "python", "./main.py" ]
