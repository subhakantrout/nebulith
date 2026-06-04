# src/constants.py — re-export from canonical core.constants
# All constants are defined in core/constants.py. This shim keeps
# existing `from src.constants import X` imports working.
from core.constants import *  # noqa: F401,F403
from core.constants import (  # explicit re-exports for IDE visibility
    APP_VERSION,
    BASE_DIR,
    STATIC_DIR,
    DATA_DIR,
    SESSIONS_FILE,
    MEMORY_FILE,
    MEMORY_DOC,
    PERSONAL_DIR,
    RUNBOOK_DIR,
    UPLOAD_DIR,
    FEATURES_FILE,
    SETTINGS_FILE,
    MAX_CONTEXT_MESSAGES,
    REQUEST_TIMEOUT,
    OPENAI_COMPAT_PATH,
    DEFAULT_HOST,
    LLM_HOSTS,
    OPENAI_API_KEY,
    SEARXNG_INSTANCE,
    CLEANUP_ENABLED,
    CLEANUP_INTERVAL_HOURS,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
)
