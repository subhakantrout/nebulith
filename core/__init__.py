# core/__init__.py
"""
Chat Core — the essential chat experience.

This package contains only what's needed for:
- Streaming LLM responses
- Session management
- Model routing
- Authentication
"""

# Re-export `core.llm` symbols via lazy module-level access so
# `from core import llm_call` still works, but `src.llm_core` (which
# depends on `core.database`) is not loaded until the first actual
# access.  This breaks the circular chain:
#   `core.__init__`  →  `src.llm_core`  →  `core.database`
#   ^                                        │
#   └────────────────────────────────────────┘
# because `core.__init__` no longer eagerly imports `src.llm_core`.
_LLM_LAZY = None

def __getattr__(name):
    if name in {
        "llm_call", "llm_call_async", "stream_llm",
        "list_model_ids", "normalize_model_id", "LLMConfig",
    }:
        global _LLM_LAZY
        if _LLM_LAZY is None:
            from src.llm_core import (
                llm_call, llm_call_async, stream_llm,
                list_model_ids, normalize_model_id, LLMConfig,
            )
            _LLM_LAZY = {
                "llm_call": llm_call,
                "llm_call_async": llm_call_async,
                "stream_llm": stream_llm,
                "list_model_ids": list_model_ids,
                "normalize_model_id": normalize_model_id,
                "LLMConfig": LLMConfig,
            }
        return _LLM_LAZY[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

from .auth import AuthManager
from .constants import *
from .middleware import SecurityHeadersMiddleware
from .exceptions import (
    SessionNotFoundError,
    InvalidFileUploadError,
    LLMServiceError,
    WebSearchError,
)
from .models import Session, ChatMessage
from .session_manager import SessionManager

__all__ = [
    # LLM
    "llm_call",
    "llm_call_async",
    "stream_llm",
    "list_model_ids",
    "normalize_model_id",
    "LLMConfig",
    # Auth
    "AuthManager",
    # Middleware
    "SecurityHeadersMiddleware",
    # Exceptions
    "SessionNotFoundError",
    "InvalidFileUploadError",
    "LLMServiceError",
    "WebSearchError",
    # Models
    "Session",
    "ChatMessage",
    "SessionManager",
]
