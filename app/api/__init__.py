from fastapi import FastAPI
from fastapi.responses import StreamingResponse


from app.infrastructure.database import init_db
from app.api.routes import products, users, auth
from scripts.create_first_admin import create_first_admin

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()
    create_first_admin()



app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
