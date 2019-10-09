# Django webapp

I created a Django app that consumes the API, and provides a web-based ui to see some cameras and then show 20 images from one. The actual fetching is done by leveraging gevent.pool to ensure there are 5 downloads ocurring concurrently.

The project was created using python 3.7, Django and anaconda (version 3).

The environment.yml file that I used is included so that it can be run anywhere

## Steps to run

    conda env create

ran from within the root folder. default name is `EagleEyeTest`

    conda activate EagleEyeTest

and finally run the Django project

    python manage.py runserver

## Documentation

I added a pdf file with some documentation here: [EagleEyeNetwork(48hr).pdf](docs/EagleEyeNetwork(48hr).pdf)

## Previous version

This is the second "version" of this skill test (at the 48 hr mark), the first one (at the 24 hr mark) can be found here: [https://github.com/loucho/image-download](https://github.com/loucho/image-download)
