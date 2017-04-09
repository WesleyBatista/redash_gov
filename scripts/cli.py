#!/usr/bin/env python
# coding: utf-8

import os
import click
import email_etl
import transform as trans


@click.group()
def cli():
    pass


class Context(object):

    def __init__(self):
        self.home = os.getcwd()


pass_context = click.make_pass_decorator(Context, ensure=True)


@cli.command()
@click.argument('email')
@click.argument('password')
@click.argument('subject')
@click.option('--imap', default='imap.gmail.com')
@click.option('--days', default=5)
@pass_context
def download(ctx, email, password, subject, imap, days):
    currentPath = ctx.home
    pathDir = os.path.dirname(__file__)
    credentials_json_file = '{}/redash-84b560aec623.json'.format(pathDir)
    conn = email_etl.login(email, password, imap)
    searchResults = email_etl.search_inbox(conn, subject, days)
    email_etl.download_files(conn, searchResults, currentPath, credentials_json_file)


@cli.command()
@click.argument('in_path', type=click.Path(exists=True))
@click.argument('out_path')
@click.argument('dict_path', type=click.Path(exists=True))
@pass_context
def transform(ctx, in_path, out_path, dict_path):
    pathDir = os.path.dirname(__file__)
    trans.generate_csv(in_path, dict_path, out_path)


@cli.command()
@click.argument('table')
@click.argument('src')
@pass_context
def update_table(ctx, src, table):
    trans.generate_csv(in_path, dict_path, out_path)


if __name__ == '__main__':
    cli()
