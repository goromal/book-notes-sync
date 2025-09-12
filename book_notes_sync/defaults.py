import os

class BookNotesSyncDefaults:
    DOCS_SECRETS_FILE = "~/secrets/google/client_secrets.json"
    DOCS_REFRESH_TOKEN = "~/secrets/google/refresh.json"
    WIKI_URL = "https://notes.andrewtorgesen.com"
    ENABLE_LOGGING = True

    @staticmethod
    def getKwargsOrDefault(argname, **kwargs):
        argname_mapping = {
            "docs_secrets_file": BookNotesSyncDefaults.DOCS_SECRETS_FILE,
            "docs_refresh_token": BookNotesSyncDefaults.DOCS_REFRESH_TOKEN,
            "wiki_url": BookNotesSyncDefaults.WIKI_URL,
            "enable_logging": BookNotesSyncDefaults.ENABLE_LOGGING,
        }
        return kwargs[argname] if (argname in kwargs and kwargs[argname] is not None) else argname_mapping[argname]
