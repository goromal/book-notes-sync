import os

class BookNotesSyncDefaults:
    DOCS_SECRETS_FILE = os.path.expanduser("~/secrets/docs/client_secrets.json")
    DOCS_REFRESH_TOKEN = os.path.expanduser("~/secrets/docs/token.json")
    DOCS_SCOPE = [
        "https://www.googleapis.com/auth/documents.readonly"
    ]
    WIKI_URL = "https://notes.andrewtorgesen.com"
    WIKI_SECRETS_FILE = os.path.expanduser("~/secrets/wiki/secrets.json")
    ENABLE_LOGGING = True

    @staticmethod
    def getKwargsOrDefault(argname, **kwargs):
        argname_mapping = {
            "docs_secrets_file": BookNotesSyncDefaults.DOCS_SECRETS_FILE,
            "docs_refresh_token": BookNotesSyncDefaults.DOCS_REFRESH_TOKEN,
            "docs_scope": BookNotesSyncDefaults.DOCS_SCOPE,
            "wiki_url": BookNotesSyncDefaults.WIKI_URL,
            "wiki_secrets_file": BookNotesSyncDefaults.WIKI_SECRETS_FILE,
            "enable_logging": BookNotesSyncDefaults.ENABLE_LOGGING,
        }
        return kwargs[argname] if (argname in kwargs and kwargs[argname] is not None) else argname_mapping[argname]
