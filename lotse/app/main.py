import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from guidance_strategies.app.main import app as guidance_engine


app = FastAPI()

# define the directory from which strategies should be loaded
base_path = os.path.dirname(__file__)
strategy_path = os.path.join(base_path, "strategy_configs")
state_path = os.path.join(base_path, "state_vector", "vector.yaml")

# setup the guidance engine: parse strategies and set first context
guidance_engine.setup_engine(strategy_path, state_path)
# start the guidance event loops
guidance_engine.start()
# make guidance engine endpoints available under /guidance
app.mount('/guidance', guidance_engine)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
