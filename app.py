
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import graph

app = FastAPI()

origins = ['http://0.0.0.0:6161', 'http://192.168.201.75:6161']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes

app.include_router(graph.router)


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=6060,
                reload=True, workers=4)
