@echo off
cd zpi_masterchess
cmd /k "..\env\Scripts\activate && python manage.py runserver"