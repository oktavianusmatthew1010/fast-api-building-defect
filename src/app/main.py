from .api import router
from .core.config import settings
from .core.setup import create_application
from fastapi.middleware.cors import CORSMiddleware

app = create_application(router=router, settings=settings)
origins = [
    "http://localhost:3000",  # React/Vite frontend
    # Add more if needed, like deployed URLs
]

# Add the CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)