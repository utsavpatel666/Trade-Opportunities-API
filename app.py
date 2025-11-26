from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

from routers.analyze import router

# Create limiter object
limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

# Attach limiter to the app state  ✅ IMPORTANT
app.state.limiter = limiter

# Add middleware for rate limiting
app.add_middleware(SlowAPIMiddleware)

# Routers
app.include_router(router)

@app.get("/")
def home():
    return {"msg": "API running"}
