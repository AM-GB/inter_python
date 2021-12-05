FROM python:3.8.6

RUN pip install --upgrade pip
COPY ./ ./
RUN pip install -r requirements.txt
RUN pip install gunicorn

# # create directory for the app user
# RUN mkdir -p /home/catalog_product

# # create the app user
# RUN addgroup -S catalog_product && adduser -S catalog_product -G app

# # create the appropriate directories
# ENV HOME=/home/catalog_product
# ENV APP_HOME=/home/catalog_product/backend
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/static
# RUN mkdir $APP_HOME/media
# WORKDIR $APP_HOME

# # copy project
# COPY . $APP_HOME

# # chown all the files to the app user
# RUN chown -R catalog_product:catalog_product $APP_HOME

# # change to the app user
# USER app

# # run entrypoint.prod.sh
# ENTRYPOINT ["/home/catalog_product/backend/entrypoint.prod.sh"]