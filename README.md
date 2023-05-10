# Book-Notes-Sync

![example workflow](https://github.com/goromal/book-notes-sync/actions/workflows/test.yml/badge.svg)

## Commands

```bash
Usage: book-notes-sync [OPTIONS] COMMAND [ARGS]...

  Synchronize Google Docs book notes with corresponding DokuWiki notes.

Options:
  --docs-secrets-file PATH   Google Docs client secrets file.  [default:
                             /data/andrew/secrets/docs/client_secrets.json]
  --docs-refresh-token PATH  Google Docs refresh file (if it exists).
                             [default: /data/andrew/secrets/docs/token.json]
  --wiki-url TEXT            URL of the DokuWiki instance (https).  [default:
                             https://notes.andrewtorgesen.com]
  --wiki-secrets-file TEXT   Path to the DokuWiki login secrets JSON file.
                             [default: /data/andrew/secrets/wiki/secrets.json]
  --enable-logging BOOLEAN   Whether to enable logging.  [default: True]
  --help                     Show this message and exit.

Commands:
  sync           Sync a single Google Doc with a single DokuWiki page.
  sync-from-csv  Sync a list of Google Docs with DokuWiki pages from a CSV.
```

### Sync

```bash
Usage: book-notes-sync sync [OPTIONS]

  Sync a single Google Doc with a single DokuWiki page.

Options:
  --docs-id TEXT  Document ID of the Google Doc.  [required]
  --page-id TEXT  ID of the DokuWiki page.  [required]
  --help          Show this message and exit.
```

### Sync from CSV

```bash
Usage: book-notes-sync sync-from-csv [OPTIONS]

  Sync a list of Google Docs with DokuWiki pages from a CSV.

Options:
  --sync-csv PATH  CSV specifying (docs-id, page-id) pairs.  [required]
  --help           Show this message and exit.
```
