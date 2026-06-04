# src/exceptions.py — re-export from canonical core.exceptions
# All exceptions are defined in core/exceptions.py. This shim keeps
# existing `from src.exceptions import X` imports working.
from core.exceptions import *  # noqa: F401,F403
from core.exceptions import (  # explicit re-exports for IDE visibility
    SessionNotFoundError,
    InvalidFileUploadError,
    LLMServiceError,
    WebSearchError,
)
