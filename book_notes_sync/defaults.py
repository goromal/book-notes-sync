import os

class BookNotesSyncDefaults:
    DOCS_SECRETS_FILE = os.path.expanduser("~/secrets/google/client_secrets.json")
    DOCS_REFRESH_TOKEN = os.path.expanduser("~/secrets/google/refresh.json")
    WIKI_URL = "https://notes.andrewtorgesen.com"
    WIKI_SECRETS_FILE = os.path.expanduser("~/secrets/wiki/secrets.json")
    ENABLE_LOGGING = True

    @staticmethod
    def getKwargsOrDefault(argname, **kwargs):
        argname_mapping = {
            "docs_secrets_file": BookNotesSyncDefaults.DOCS_SECRETS_FILE,
            "docs_refresh_token": BookNotesSyncDefaults.DOCS_REFRESH_TOKEN,
            "wiki_url": BookNotesSyncDefaults.WIKI_URL,
            "wiki_secrets_file": BookNotesSyncDefaults.WIKI_SECRETS_FILE,
            "enable_logging": BookNotesSyncDefaults.ENABLE_LOGGING,
        }
        return kwargs[argname] if (argname in kwargs and kwargs[argname] is not None) else argname_mapping[argname]
