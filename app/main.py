# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import templates, keepalive
from contextlib import contextmanager
from .database import init_db
from .setup_main import configure_cors

# --- SYNC LIFESPAN ---
@contextmanager
def lifespan(app: FastAPI):
    """
    Synchronous lifespan function.
    Runs 'init_db()' on startup.
    """
    init_db()  
    yield

# calling an instance of fast api
app = FastAPI(
    title="Template Service",         
    description="Manages notification templates, versions, and rendering.", 
    version="1.0.0",
    lifespan=lifespan            
)

# Include your API routes
app.include_router(templates.router)
app.include_router(keepalive.router)

# defining the cors function
configure_cors(app)


# --- Main entry point to run the app for local pdevelopment---
if __name__ == "__main__":
    import uvicorn
    # Use 0.0.0.0 to be accessible inside Docker
    # Use port 3004 as requested
    uvicorn.run(app, host="0.0.0.0", port=3004)