# 
SECRET_KEY = 'd4YWXjAIJUdWvadYgTGmWxZ17hP4Ehq2NIuYtNrQKiqqTofoWVG145KR8Ee4PzjpiOhEnz6de9pFTfrcU37nzQ'
GUEST_TOKEN_JWT_SECRET = '46765dbcafdba7ac8193fd2bf7dc35aefe271a4cd5037da40be26c31762c9c64'  # BEARER
FEATURE_FLAGS = {
    'EMBEDDED_SUPERSET' :True,
    'DASHBOARD_RBAC':True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}
WTF_CSRF_ENABLED = False
GUEST_TOKEN_JWT_EXP_SECONDS = 3600  # Tempo di validità del token
ENABLE_CORS = True
CORS_OPTIONS = {
    "origins": ["http://localhost:5000"],  # Indirizzo dell'app Flask
    "allow_headers": ["Content-Type", "Authorization"],
    "methods": ["GET", "POST", "OPTIONS"]
}

OVERRIDE_HTTP_HEADERS  = {"X-Frame-Options": "ALLOWALL"}


TALISMAN_ENABLED = False #utils.cast_to_boolean(os.environ.get("TALISMAN_ENABLED", True))

# If you want Talisman, how do you want it configured??
#TALISMAN_CONFIG = {
#    "content_security_policy": {
#        "base-uri": ["'self'"],
#        "default-src": ["'self'", 'https://localhost:5000'],
#        "img-src": [
#            "'self'",
#            "blob:",
#            "data:",
#            "https://apachesuperset.gateway.scarf.sh",
#            "https://static.scarf.sh/",
#            # "https://avatars.slack-edge.com", # Uncomment when SLACK_ENABLE_AVATARS is True
#        ],
#        "worker-src": ["'self'", "blob:"],
#        "connect-src": [
#            "'self'",
#            "https://api.mapbox.com",
#            "https://events.mapbox.com",
#        ],
#        "object-src": "'none'",
#        "style-src": [
#            "'self'",
#            "'unsafe-inline'",
#        ],
#        "script-src": ["'self'", "'strict-dynamic'"],
#    },
#    "content_security_policy_nonce_in": ["script-src"],
#    "force_https": False,
#    "session_cookie_secure": False,
#}