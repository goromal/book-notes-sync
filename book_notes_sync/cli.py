import click
import csv
import os

from book_notes_sync.defaults import BookNotesSyncDefaults as BNSD
from book_notes_sync.sync import syncBookNotes

@click.group()
@click.pass_context
@click.option(
    "--docs-secrets-file",
    "docs_secrets_file",
    type=click.Path(exists=True),
    default=BNSD.DOCS_SECRETS_FILE,
    show_default=True,
    help="Google Docs client secrets file.",
)
@click.option(
    "--docs-refresh-token",
    "docs_refresh_token",
    type=click.Path(),
    default=BNSD.DOCS_REFRESH_TOKEN,
    show_default=True,
    help="Google Docs refresh file (if it exists).",
)
@click.option(
    "--wiki-url",
    "wiki_url",
    type=str,
    default=BNSD.WIKI_URL,
    show_default=True,
    help="URL of the DokuWiki instance (https).",
)
@click.option(
    "--wiki-secrets-file",
    "wiki_secrets_file",
    type=str,
    default=BNSD.WIKI_SECRETS_FILE,
    show_default=True,
    help="Path to the DokuWiki login secrets JSON file.",
)
@click.option(
    "--enable-logging",
    "enable_logging",
    type=bool,
    default=BNSD.ENABLE_LOGGING,
    show_default=True,
    help="Whether to enable logging.",
)
def cli(ctx: click.Context, docs_secrets_file, docs_refresh_token, wiki_url, wiki_secrets_file, enable_logging):
    """Synchronize Google Docs book notes with corresponding DokuWiki notes."""
    ctx.obj = {
        "docs_secrets_file": docs_secrets_file,
        "docs_refresh_token": docs_refresh_token,
        "wiki_url": wiki_url,
        "wiki_secrets_file": wiki_secrets_file,
        "enable_logging": enable_logging,
    }

@cli.command()
@click.pass_context
@click.option(
    "--docs-id",
    "docs_id",
    type=str,
    required=True,
    help="Document ID of the Google Doc.",
)
@click.option(
    "--page-id",
    "page_id",
    type=str,
    required=True,
    help="ID of the DokuWiki page.",
)
def sync(ctx: click.Context, docs_id, page_id):
    """Sync a single Google Doc with a single DokuWiki page."""
    try:
        syncBookNotes([(docs_id, page_id)], **ctx.obj)
    except Exception as e:
        print(f"Program error: {e}")
        exit(1)

@cli.command()
@click.pass_context
@click.option(
    "--sync-csv",
    "sync_csv",
    type=click.Path(exists=True),
    default=os.path.expanduser("~/configs/book-notes.csv"),
    show_default=True,
    help="CSV specifying (docs-id, page-id) pairs.",
)
def sync_from_csv(ctx: click.Context, sync_csv):
    """Sync a list of Google Docs with DokuWiki pages from a CSV."""
    with open(sync_csv, "r") as csvfile:
        reader = csv.reader(csvfile)
        try:
            syncBookNotes([(line[0], line[1]) for line in reader], **ctx.obj)
        except Exception as e:
            print(f"Program error: {e}")
            exit(1)

def main():
    cli()

if __name__ == "__main__":
    main()
