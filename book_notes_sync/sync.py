import logging
import sys
from typing import List, Tuple
from wiki_tools.wiki import WikiTools

from easy_google_auth.auth import getGoogleService

from book_notes_sync.defaults import BookNotesSyncDefaults as BNSD
from book_notes_sync.parsers import extractElements

def syncBookNotes(sync_ids: List[Tuple[str, str]], **kwargs) -> None:
    docs_secrets_file = BNSD.getKwargsOrDefault("docs_secrets_file", **kwargs)
    docs_refresh_token = BNSD.getKwargsOrDefault("docs_refresh_token", **kwargs)
    docs_scope = BNSD.getKwargsOrDefault("docs_scope", **kwargs)
    wiki_url = BNSD.getKwargsOrDefault("wiki_url", **kwargs)
    wiki_secrets_file = BNSD.getKwargsOrDefault("wiki_secrets_file", **kwargs)
    enable_logging = BNSD.getKwargsOrDefault("enable_logging", **kwargs)

    if enable_logging:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    
    service = getGoogleService("docs", "v1", docs_secrets_file, docs_refresh_token, docs_scope)

    wikitools = WikiTools(wiki_url=wiki_url, wiki_secrets_file=wiki_secrets_file, enable_logging=enable_logging)

    for docs_id, wiki_id in sync_ids:
        document = None
        if enable_logging:
            logging.info(f"Synchronizing {docs_id} -> {wiki_id}")
        try:
            document = service.documents().get(documentId=docs_id).execute()
        except Exception as err:
            if enable_logging:
                logging.error(err)
                continue
        title, elements = extractElements(document)
        wikidoc_str = f"{title}\n"
        for element in elements:
            wikidoc_str += f"\n{element}\n"
        if enable_logging:
            logging.info(f"Writing to {wiki_id}")
            wikitools.putPage(id=wiki_id, content=wikidoc_str)

    if enable_logging:
        logging.info("Done.")
