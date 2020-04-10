FROM nikolaik/python-nodejs:python3.7-nodejs12

ENV PATH "/root/.local/bin:$PATH"
ENV NODE_PATH="/usr/lib/node_modules"

ARG siteurl
ENV SITEURL=$siteurl
ARG offenaccountid
ENV OFFEN_ACCOUNT_ID=$offenaccountid

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN npm install -g postcss-cli@^6.1.3 autoprefixer@^9.7.0 svgo@^1.3.0 cssnano@^4.1.10
RUN apt-get update \
	&& apt-get install -y libjpeg-progs optipng \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /code/homepage
COPY ./homepage/requirements.txt /code/homepage/requirements.txt
RUN pip install --user -r requirements.txt

COPY ./homepage /code/homepage
RUN make publish && rm -rf output/theme/.webassets-cache
