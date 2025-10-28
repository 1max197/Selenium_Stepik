cd "Page Object" 

pip install -r requirements.txt - установить зависимости
pytest -v -s -rx --browser_name=chrome --language=ru tests/тест (запустить тестовый файл отдельно) 
pytest -v -s -rx --browser_name=chrome --language=ru tests (запустить всю папку с тестами) --browser_name=chrome или firefox --language=ru, en, fr
