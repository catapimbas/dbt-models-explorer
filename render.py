from typing import Iterable

from rich.console import Console
from rich.table import Table as RichTable

from loader import Table

console = Console()


def make_table(model_table: Table):
    table = RichTable(title=(table.name))
    table.add_column("Name", style="cyan", no_wrap=True)
    return table


def print_relationships(tables: Iterable[Table]):
    rich_table = RichTable(title=('Relationships'))
    rich_table.add_column('Table name', style="bold green")
    rich_table.add_column('Column', style="bold green")
    rich_table.add_column('Ref table', style="bold blue")
    rich_table.add_column('Field', style="bold blue")
    for table in tables:
        for column in table.columns:
            if column.props:
                for prop in column.props:
                    if isinstance(prop, dict):
                        for attr in prop:
                            if 'relationships' in attr:
                                rel = prop['relationships']
                                rich_table.add_row(
                                    table.name, column.name, rel['to'], rel['field'])
    console.print(rich_table)
