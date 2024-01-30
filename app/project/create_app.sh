#!/bin/bash
echo "Введите имя приложения:"
read appname
cd apps
../manage.py startapp $appname
cd ..