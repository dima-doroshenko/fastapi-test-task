from fastapi import FastAPI

import uvicorn

from router import router

app = FastAPI()

app.include_router(router)

uvicorn.run(app)

''' 
Улучшения для прода:

Добавить CORS Middleware
Изменить структуру проекта
Добавить тесты
Добавить обработку ошибок
Создать SQL базу данных
Добавить хэндлер для обновления текущих задач
Добавить разбиение на страницы в хэндлере получения задач
'''