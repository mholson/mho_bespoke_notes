from thefuzz import fuzz
from thefuzz import process
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt, Confirm
from tagid import TagId
from mho_schema_data import SchemaData


class SchemaSearch:
    schema_search_done = False
    schema_search_query = ""
    schema_search_results = []
    schema_search_sorted_search_results = []
    schema_search_choice_value = ""

    @classmethod
    def gen_schema_search_results(cls):
        for item in SchemaData().schema_data:
            score = fuzz.ratio(cls.schema_search_query, item)
            if score >= 10:
                cls.schema_search_results.append((item, score))
        sorted_results = sorted(
            cls.schema_search_results, key=lambda x: x[1], reverse=True
        )
        cls.schema_search_sorted_search_results = sorted_results[:10]

        # Generate the table of Values
        table = Table(title="Schema Search")
        table.add_column("Choice", justify="right", style="cyan", no_wrap=True)
        table.add_column("Schema", style="magenta")
        table.add_column("% Match", justify="right", style="green")
        for i in range(10):
            table.add_row(
                str(i),
                str(cls.schema_search_sorted_search_results[i][0]),
                str(cls.schema_search_sorted_search_results[i][1]),
            )
        console = Console()
        console.print(table)

    @classmethod
    def schema_user_input(cls):
        while cls.schema_search_done == False:
            cls.schema_search_query = Prompt.ask("[b]Search[/b] for schema")
            cls.gen_schema_search_results()
            schema_search_choice = IntPrompt.ask(
                "Choose a Schema [cyan][b]0-9[/b][/cyan]"
            )
            cls.schema_search_choice_value = cls.schema_search_sorted_search_results[
                schema_search_choice
            ][0].strip()
            schema_search_check = Confirm.ask(
                f"Is [magenta][b]{cls.schema_search_choice_value}[/b][/magenta] correct?"
            )
            if schema_search_check == True:
                cls.schema_search_done = True
            else:
                cls.schema_search_done = False


if __name__ == "__main__":
    SchemaSearch().schema_user_input()
    print(SchemaSearch().schema_search_choice_value)
