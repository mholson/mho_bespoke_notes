import csv
import sys
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt, Confirm
from rich.text import Text
from rich.panel import Panel


class TagId:
    tag_id = ""
    tag_id_remove_flag = False
    tag_id_list = None
    gen_tex_and_org_files_flag = True
    tag_id_csv_filename = "tagid.csv"

    @classmethod
    def readListFromCSV(cls):
        with open(cls.tag_id_csv_filename, "r") as file:
            reader = csv.reader(file)
            cls.tag_id_list = [row[0] for row in reader]

    @classmethod
    def writeListToCSV(cls):
        with open(cls.tag_id_csv_filename, "w", newline="") as file:
            writer = csv.writer(file)
            for item in cls.tag_id_list:
                writer.writerow([item])

    @classmethod
    def genTagId(cls):
        # Read in The CSV file
        cls.readListFromCSV()

        cls.gen_tex_and_org_files_flag = Confirm.ask(
            f"[b]Generate both [cyan]TeX[/cyan] and [red]Org[/red] files[/b].\n[i]Otherwise only [red]Org[/red] files[/i].",
            default=True,
        )
        tag_id_choice = Prompt.ask(
            "Generate a [b]manual[/b] or [b]automatic[/b] TagId or [red][b]quit[/b][/red]",
            choices=["m", "a", "q"],
            default="a",
        )
        if tag_id_choice == "m":
            cls.tag_id = Prompt.ask("Enter the four character TagID: ")
        elif tag_id_choice == "a":
            cls.tag_id = cls.tag_id_list[0]
        else:
            sys.exit(
                f"Nothing more to do here. Please run again if you change your mind."
            )

        if cls.tag_id in cls.tag_id_list or not cls.gen_tex_and_org_files_flag:
            print(f"The tag_id [cyan][b]{cls.tag_id}[/b][/cyan] is available")
            tag_id_confirm_usage = Confirm.ask(
                f"Confirm you want to use the TagID: [cyan][b]{cls.tag_id}[/b][/cyan]"
            )
            if tag_id_confirm_usage and cls.gen_tex_and_org_files_flag:
                cls.tag_id_remove_flag = True
            elif not cls.gen_tex_and_org_files_flag:
                pass
            else:
                sys.exit(f"The tag_id {cls.tag_id} was not removed. Please run again.")
        elif not cls.gen_tex_and_org_files_flag:
            pass
        else:
            sys.exit(f"The tag_id {cls.tag_id} is not available. Please run again.")

    def tagIdRemove(cls):
        if cls.tag_id_remove_flag == True:
            del cls.tag_id_list[0]
            cls.writeListToCSV()
            print(f"The tag_id {cls.tag_id} has been removed.")
        else:
            print(f"The tag_id {cls.tag_id} has NOT been removed.")


if __name__ == "__main__":
    TagId.genTagId()
