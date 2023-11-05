import sys
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt, Confirm

from gen_files import GenFiles
from schema import SchemaSearch


class ContentMenu:
    tex_env = ""
    tex_title = ""
    org_tag = ""
    # file_class_name >> content_type
    content_type = ""
    menu_choice = ""
    menu_options = [
        "empty",
        "definition",
        "example (including exam prob)",
        "proposition",
        "notation",
        "theorem",
        "axiom",
        "algorithm",
        "law",
        "rule",
        "objective",
        "property",
        "table",
        "tikz image",
        "python image",
        "exam",
        "wksh",
    ]

    @classmethod
    def show_menu(cls):
        """
        Shows a list of possible file class choices in a RICH table.

        Parameters
        ----------
        Requires not external class parameters.

        Returns
        -------
        An index table of
        """

        menu = Table(title="Content Classification Menu")
        menu.add_column("Choice", justify="right", style="cyan", no_wrap=True)
        menu.add_column("Content", style="magenta")
        for i in range(len(cls.menu_options)):
            menu.add_row(
                str(i),
                str(cls.menu_options[i]),
            )
        console = Console()
        console.print(menu)

        cls.menu_choice = IntPrompt.ask(
            "Choose a Content Type",
            default=2,
        )

        match cls.menu_choice:
            case 0:
                cls.tex_title_setter()
            case 1:
                cls.tex_title_setter()
                cls.content_name = "definition"
                cls.tex_env = "definition"
                .org_tag = "defn"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 2:
                cls.content_name = "example"
                cls.tex_env = "example"
                .org_tag = "soln"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_soln()
            case 3:
                cls.tex_title_setter()
                cls.content_name = "proposition"
                cls.tex_env = "proposition"
                .org_tag = "prop"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_prop()
            case 4:
                cls.tex_title_setter()
                cls.content_name = "notation"
                cls.tex_env = "notation"
                .org_tag = "notn"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 5:
                cls.tex_title_setter()
                cls.content_name = "theorem"
                cls.tex_env = "theorem"
                .org_tag = "thrm"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 6:
                cls.tex_title_setter()
                cls.content_name = "axiom"
                cls.tex_env = "axiom"
                .org_tag = "axim"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 7:
                cls.tex_title_setter()
                cls.content_name = "algorithm"
                cls.tex_env = "algo"
                .org_tag = "algo"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 8:
                cls.tex_title_setter()
                cls.content_name = "law"
                cls.tex_env = "alaw"
                .org_tag = "laws"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 9:
                cls.tex_title_setter()
                cls.content_name = "rule"
                cls.tex_env = "arule"
                .org_tag = "rule"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 10:
                cls.tex_title_setter()
                cls.content_name = "objective"
                cls.tex_env = "objective"
                .org_tag = "objv"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 11:
                cls.tex_title_setter()
                cls.content_name = "property"
                cls.tex_env = "property"
                .org_tag = "prpt"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 12:
                cls.tex_title_setter()
                cls.content_name = "table"
                cls.tex_env = "table"
                .org_tag = "tabl"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 13:
                pass
                GenFiles().file_template_tikz_image()
            case 14:
                pass
                GenFiles().file_template_python_image()
            case 15:
                pass
                GenFiles().file_template_tex_exam()
            case 16:
                pass
                GenFiles.file_template_tex_wksh()
            case _:
                sys.exit(f"Invalid choice. Please run again.")

    @classmethod
    def tex_title_setter(cls):
        """
        Generates a tex_title that can be passed into tex and org templates.
        """
        cls._tex_title = Prompt.ask("Enter a [cyan][b]tex[/cyan][/b] title")


if __name__ == "__main__":
    pass
