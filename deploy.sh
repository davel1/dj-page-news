#! /bin/bash
virtualenv dj && cd ./dj
source ./bin/activate
pip install --upgrade pip
pip install django
pip install django-import-export
pip install python-social-auth
pip install django-wysiwyg
pip install django-ckeditor
pip install Pillow
git clone https://github.com/davel1/dj-page-news
rm -rf ./*migrations* 


