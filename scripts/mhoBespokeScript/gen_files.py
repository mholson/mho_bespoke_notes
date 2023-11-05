from rich import print
from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt, Confirm
from schema import SchemaSearch
from tagid import TagId
from file_paths import *

from datetime import datetime
import shortuuid
import uuid

current_datetime = datetime.now()
day_name = current_datetime.strftime("%a")


class ContentMenu:
    tex_env = ""
    tex_title = ""
    org_tag = ""
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
                cls.org_tag = "defn"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 2:
                cls.content_name = "example"
                cls.tex_env = "example"
                cls.org_tag = "soln"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_soln()
            case 3:
                cls.tex_title_setter()
                cls.content_name = "proposition"
                cls.tex_env = "proposition"
                cls.org_tag = "prop"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_prop()
            case 4:
                cls.tex_title_setter()
                cls.content_name = "notation"
                cls.tex_env = "notation"
                cls.org_tag = "notn"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 5:
                cls.tex_title_setter()
                cls.content_name = "theorem"
                cls.tex_env = "theorem"
                cls.org_tag = "thrm"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 6:
                cls.tex_title_setter()
                cls.content_name = "axiom"
                cls.tex_env = "axiom"
                cls.org_tag = "axim"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 7:
                cls.tex_title_setter()
                cls.content_name = "algorithm"
                cls.tex_env = "algo"
                cls.org_tag = "algo"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 8:
                cls.tex_title_setter()
                cls.content_name = "law"
                cls.tex_env = "alaw"
                cls.org_tag = "laws"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 9:
                cls.tex_title_setter()
                cls.content_name = "rule"
                cls.tex_env = "arule"
                cls.org_tag = "rule"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 10:
                cls.tex_title_setter()
                cls.content_name = "objective"
                cls.tex_env = "objective"
                cls.org_tag = "objv"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 11:
                cls.tex_title_setter()
                cls.content_name = "property"
                cls.tex_env = "property"
                cls.org_tag = "prpt"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_thrm()
            case 12:
                cls.tex_title_setter()
                cls.content_name = "table"
                cls.tex_env = "table"
                cls.org_tag = "tabl"
                SchemaSearch().schema_user_input()
                GenFiles().file_templates_defn()
            case 13:
                GenFiles().file_template_tikz_image()
            case 14:
                GenFiles().file_template_python_image()
            case 15:
                GenFiles().file_template_tex_exam()
            case 16:
                GenFiles.file_template_tex_wksh()
            case _:
                sys.exit(f"Invalid choice. Please run again.")

    @classmethod
    def tex_title_setter(cls):
        """
        Generates a tex_title that can be passed into tex and org templates.
        """
        cls._tex_title = Prompt.ask("Enter a [cyan][b]tex[/cyan][/b] title")


class GenFiles:
    course_code = ""
    term_code = ""
    name = ""
    level = ""

    @classmethod
    def file_templates_defn(cls):
        """
        Returns
        =======
        Generates the tex files for files of type defn
        """

        if TagId().gen_tex_and_org_files_flag == True:
            GenTexFiles.gen_tex_core_files()
            GenTexFiles.gen_tex_note_files()
            GenTexFiles.gen_tex_slide_files()
        else:
            pass
        GenOrgFiles().gen_org_files(False, False, True, True, False, False)

    @classmethod
    def file_templates_soln(cls):
        """
        Returns
        =======
        Generates the tex files for files of type example
        """
        if TagId().gen_tex_and_org_files_flag == True:
            GenTexFiles.gen_tex_core_files()
            GenTexFiles.gen_tex_soln_files()
            GenTexFiles.gen_tex_marks_files()
            GenTexFiles.gen_tex_note_soln_files()
            GenTexFiles.gen_tex_exam_files()
            GenTexFiles.gen_tex_slide_soln_files()
        else:
            pass
        GenOrgFiles().gen_org_files(True, False, True, True, True, True)

    @classmethod
    def file_templates_thrm(cls):
        """
        Returns
        =======
        Generates the tex and org files for files of type thrm
        """
        if TagId().gen_tex_and_org_files_flag == True:
            GenTexFiles().gen_tex_core_files()
            GenTexFiles().gen_tex_proof_files()
            GenTexFiles().gen_tex_note_proof_files()
            GenTexFiles().gen_tex_slide_proof_files
        else:
            pass
        GenOrgFiles().gen_org_files(True, False, True, True, True, True)

    @classmethod
    def file_template_image_python(cls):
        """
        Returns
        =======
        Generates the for files of type python image
        """
        GenImageFiles().gen_python_files()
        # if TagId().gen_tex_and_org_files_flag == True:
        # else:

    @classmethod
    def file_template_image_tikz(cls):
        """
        Returns
        =======
        Generates the for files of type python image
        """
        GenImageFiles().gen_tikz_files()
        # if TagId().gen_tex_and_org_files_flag == True:
        # else:

    @classmethod
    def file_template_tex_exam(cls):
        """
        Returns
        =======
        Generates the tex files for files of type exam
        """
        # Generate tex.exam files
        cls.course_code = Prompt.ask("Enter the course code")
        cls.term_code = Prompt.ask(
            "Enter the term code [cyan]htYY[/cyan] or [cyan]vtYY[/cyan]"
        )
        cls.name = Prompt.ask("Enter the exam name [cyan]exam-01[/cyan]")
        cls.level = Prompt.ask("Enter exam level [cyan]e,ec,ca,eca[/cyan]")

        if TagId().gen_tex_and_org_files_flag == True:
            GenTexFiles().gen_tex_exam_swedish_files()
        else:
            pass

        GenOrgFiles().gen_org_exam_swedish_files()

    @classmethod
    def file_template_tex_wksh(cls):
        """
        Returns
        =======
        Generates the tex files for files of type worksheet
        """
        cls.name = Prompt.ask("Enter the exam name [cyan]exam-01[/cyan]")
        cls.level = Prompt.ask("Enter exam level [cyan]e,ec,ca,eca[/cyan]")
        if TagId().gen_tex_and_org_files_flag == True:
            GenTexFiles().gen_tex_wksh_files()
        else:
            pass
        GenOrgFiles().gen_org_wksh_files()


class GenTexFiles:
    @classmethod
    def gen_tex_core_files(cls):
        with open(
            f"{path_tex}/tex_core-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("")
        with open(
            f"{path_tex}/tex_core_sv-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("")

    @classmethod
    def gen_tex_soln_files(cls):
        with open(
            f"{path_tex}/tex_core_soln-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("")

    @classmethod
    def gen_tex_proof_file(cls):
        with open(
            f"{path_tex}/tex_core_proof-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("")

    @classmethod
    def gen_tex_note_files(cls):
        with open(
            f"{path_tex}/tex_note-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(
                rf"\begin{{{ContentMenu().tex_env}}}[{ContentMenu().tex_title}]\label{{{TagId().tag_id}}}\index{{TAG!{TagId().tag_id}}}\index{{{ContentMenu().content_name.capitalize()}!{ContentMenu().tex_title}}}"
                "\n"
            )
            the_file.write(rf"\input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{{ContentMenu().tex_env}}}" "\n")

    @classmethod
    def gen_tex_note_soln_files(cls):
        with open(
            f"{path_tex}/tex_note-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(
                rf"\begin{{{ContentMenu().tex_env}}}\label{{{TagId().tag_id}}}\index{{TAG!{TagId().tag_id}}}\index{{{ContentMenu.content_name.capitalize()}!{TagId().tag_id}}}"
                "\n"
            )
            the_file.write(rf"\input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{{ContentMenu().tex_env}}}" "\n")
            the_file.write(rf"\begin{{solution}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_core_soln-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{solution}}" "\n")

    @classmethod
    def gen_tex_note_proof_files(cls):
        with open(
            f"{path_tex}/tex_note-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(
                rf"\begin{{{ContentMenu().tex_env}}}[{ContentMenu().tex_title}]\label{{{TagId().tag_id}}}\index{{TAG!{TagId().tag_id}}}\index{{{ContentMenu().content_name.capitalize()}!{ContentMenu().tex_title}}}"
                "\n"
            )
            the_file.write(rf"\input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{{ContentMenu().tex_env}}}" "\n")
            the_file.write(rf"\begin{{proof}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_core_proof-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{proof}}" "\n")

    @classmethod
    def gen_tex_slide_files(cls):
        with open(
            f"{path_tex}/tex_slide-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}{{{ContentMenu().tex_title}}}"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"\input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{frame}}" "\n")
            the_file.write(
                rf"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(rf"\end{{document}}")
            with open(
                f"{path_tex}/tex_slide_sv-{TagId().tag_id}.tex", "a", encoding="utf-8"
            ) as the_file:
                the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
                the_file.write("\n")
                the_file.write(rf"\begin{{document}}" "\n")
                the_file.write(
                    rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                    "\n"
                )
                the_file.write(
                    rf"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                    "\n"
                )
                the_file.write(
                    rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}{{{ContentMenu().tex_title}}}"
                    "\n"
                )
                the_file.write("\n")
                the_file.write(
                    rf"\prob \input{{0-tex/tex_core_sv-{TagId().tag_id}}}" "\n"
                )
                the_file.write("\n")
                the_file.write(rf"\end{{frame}}" "\n")
                the_file.write(
                    rf"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                    "\n"
                )
                the_file.write(
                    rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                    "\n"
                )
                the_file.write(rf"\end{{document}}")

    @classmethod
    def gen_tex_slide_soln_files(cls):
        with open(
            f"{path_tex}/tex_slide-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%   frame start   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"\prob \input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write("\n")
            the_file.write("\\framebreak")
            the_file.write("\n")
            the_file.write(rf"\soln")
            the_file.write(rf"\input{{0-tex/tex_core_soln-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{frame}}" "\n")
            the_file.write(
                rf"%   frame end   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(rf"\end{{document}}")
        with open(
            f"{path_tex}/tex_slide_sv-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"\prob \input{{0-tex/tex_core_sv-{TagId().tag_id}}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\end{{frame}}" "\n")
            the_file.write(
                rf"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(rf"\end{{document}}")

    @classmethod
    def gen_tex_slide_proof_files(cls):
        with open(
            f"{path_tex}/tex_slide-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}{{{ContentMenu().tex_title}}}"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"\input{{0-tex/tex_core-{TagId().tag_id}}}" "\n")
            the_file.write("\n")
            the_file.write("\\framebreak")
            the_file.write("\n")
            the_file.write(r"\proof")
            the_file.write(rf"\input{{0-tex/tex_core_proof-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{frame}}" "\n")
            the_file.write(
                rf"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(rf"\end{{document}}")
        with open(
            f"{path_tex}/tex_slide_sv-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[../deck_main.tex]{{subfiles}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%   FRAME START   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"\begin{{frame}}[allowframebreaks, allowdisplaybreaks, t]{{{ContentMenu().content_type.capitalize()}}}{{{ContentMenu().tex_title}}}"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"\input{{0-tex/tex_core_sv-{TagId().tag_id}}}" "\n")
            the_file.write("\n")
            the_file.write(rf"\end{{frame}}" "\n")
            the_file.write(
                rf"%   FRAME END   --==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(
                rf"%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
                "\n"
            )
            the_file.write(rf"\end{{document}}")

    @classmethod
    def gen_tex_exam_files(cls):
        with open(
            f"{path_tex}/tex_exam-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(
                rf"\question[\input{{0-tex/tex_exam_marks_swedish-{TagId().tag_id}}}] \input{{0-tex/tex_core-{TagId().tag_id}}}"
                "\n"
            )
            the_file.write(rf"\begin{{\solnboxtype}}[\stretch{1}]" "\n")
            the_file.write(rf"\tagid{{{TagId().tag_id}}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_exam_ms-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_core_soln-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{\solnboxtype}}" "\n")
        with open(
            f"{path_tex}/tex_exam_sv-{TagId().tag_id}.tex", "a", encoding="utf-8"
        ) as the_file:
            the_file.write(
                rf"\question[\input{{0-tex/tex_exam_marks_swedish-{TagId().tag_id}}}] \input{{0-tex/tex_core_sv-{TagId().tag_id}}}"
                "\n"
            )
            the_file.write(rf"\begin{{\solnboxtype}}[\stretch{1}]" "\n")
            the_file.write(rf"\tagid{{{TagId().tag_id}}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_exam_ms-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_core_soln-{TagId().tag_id}}}" "\n")
            the_file.write(rf"\end{{\solnboxtype}}" "\n")

    @classmethod
    def gen_tex_exam_swedish_files(cls):
        with open(
            rf"{path_mho_tex}/{GenOrgFiles().org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-en-{GenFiles().level}__exam.tex",
            "x",
            encoding="utf-8",
        ) as the_file:
            the_file.write("")
            the_file.write(
                rf"% -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                "\n"
            )
            the_file.write(rf"% DOCUMENT INFORMATION")
            the_file.write(
                rf"% -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                "\n"
            )
            the_file.write("")
            the_file.write(rf"% > > > DOCUMENT CLASS" "\n")
            the_file.write(rf"\documentclass[a4paper,12pt]{{exam}}" "\n")
            the_file.write(rf"% \printanswers%" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > COURSE" "\n")
            the_file.write(rf"\newcommand{{\course}}{{{GenFiles().course_code}}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > TERM" "\n")
            the_file.write(
                rf"\newcommand{{\courseterm}}{{{GenFiles().term_code}}} " "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% > > > EXAM NUMBER" "\n")
            the_file.write(rf"\newcommand{{\examnumber}}{{}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- TOTAL POINTS" "\n")
            the_file.write(rf"\newcommand{{\epoints}}{{1}}" "\n")
            the_file.write(rf"\newcommand{{\cpoints}}{{1}}" "\n")
            the_file.write(rf"\newcommand{{\apoints}}{{1}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- DURATION" "\n")
            the_file.write(rf"\newcommand{{\examduration}}{{90 minutes}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > KEYWORDS" "\n")
            the_file.write(rf"\newcommand{{\documentkeywords}}{{}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > EXAM SUBJECT" "\n")
            the_file.write(rf"\newcommand{{\examsubject}}{{}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > VERSION" "\n")
            the_file.write(rf"\newcommand{{\documentversion}}{{\today}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- CALCULATOR PERMISSION" "\n")
            the_file.write(
                rf"%\newcommand{{\calculatorpermission}}{{Calculator \textbf{{PERMITTED}}}}"
                "\n"
            )
            the_file.write(
                rf"\newcommand{{\calculatorpermission}}{{Calculator \textbf{{NOT PERMITTED}}}}"
                "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- WRITE SOLUTIONS" "\n")
            the_file.write(
                rf"\newcommand{{\writesolutions}}{{on the \textbf{{squared paper}}}}"
                "\n"
            )
            the_file.write(
                rf"% \newcommand{{\writesolutions}}{{in the \textbf{{test booklet}}}}"
                "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- FORMULA BOOKLET PERMISSION" "\n")
            the_file.write(
                rf"%\newcommand{{\formulabooklet}}{{No Formula Booklet Provided}} " "\n"
            )
            the_file.write(
                rf"\newcommand{{\formulabooklet}}{{Formula Booklet Provided}}" "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- SOLUTION BOX TYPE" "\n")
            the_file.write(
                rf"% \newcommand{{\solnboxtype}}{{solutionordottedlines}}" "\n"
            )
            the_file.write(rf"% \newcommand{{\solnboxtype}}{{solutionorbox}}" "\n")
            the_file.write(rf"\newcommand{{\solnboxtype}}{{solution}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > >  CUSTOM GRADING TABLE" "\n")
            the_file.write(rf"% \newcommand{{\customgradetable}}{{" "\n")
            the_file.write(rf"% = SingleRow" "\n")
            the_file.write(rf"% \gradetable[h][questions]" "\n")
            the_file.write(rf"% = MultiRow" "\n")
            the_file.write(rf"% \setlength{{\doublerulesep}}{{0.25in}}" "\n")
            the_file.write(rf"% \multirowgradetable{{2}}[questions]" "\n")
            the_file.write(rf"% }}" "\n")
            the_file.write(rf"\usepackage{{mhoexamgy}}" "\n")
            the_file.write(rf"%\usepackage{{mhominted}}" "\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(rf"%\makecoverpage%" "\n")
            the_file.write(rf"%\newpage\null\thispagestyle{{empty}}\newpage" "\n")
            the_file.write(rf"\begin{{questions}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_exam-}}" "\n")
            the_file.write(rf"\end{{questions}}" "\n")
            the_file.write(rf"\end{{document}}" "\n")
        with open(
            rf"{path_mho_tex}/{GenOrgFiles().org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-sv-{GenFiles().level}__exam.tex",
            "x",
            encoding="utf-8",
        ) as the_file:
            the_file.write("" "\n")
            the_file.write(
                rf"% -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                "\n"
            )
            the_file.write(rf"% DOCUMENT INFORMATION" "\n")
            the_file.write(
                rf"% -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
                "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% > > > DOCUMENT CLASS" "\n")
            the_file.write(rf"\documentclass[a4paper,12pt]{{exam}}" "\n")
            the_file.write(rf"% \printanswers%" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > COURSE" "\n")
            the_file.write(rf"\newcommand{{\course}}{{{GenFiles().course_code}}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > TERM" "\n")
            the_file.write(
                rf"\newcommand{{\courseterm}}{{{GenFiles().term_code}}} " "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% > > > EXAM NUMBER" "\n")
            the_file.write(rf"\newcommand{{\examnumber}}{{}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- TOTAL POINTS" "\n")
            the_file.write(rf"\newcommand{{\epoints}}{{1}}" "\n")
            the_file.write(rf"\newcommand{{\cpoints}}{{1}}" "\n")
            the_file.write(rf"\newcommand{{\apoints}}{{1}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- DURATION" "\n")
            the_file.write(rf"\newcommand{{\examduration}}{{90 minutes}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > KEYWORDS" "\n")
            the_file.write(rf"\newcommand{{\documentkeywords}}{{}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > EXAM SUBJECT" "\n")
            the_file.write(rf"\newcommand{{\examsubject}}{{}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > > > VERSION" "\n")
            the_file.write(rf"\newcommand{{\documentversion}}{{\today}} " "\n")
            the_file.write("" "\n")
            the_file.write(rf"% -- CALCULATOR PERMISSION" "\n")
            the_file.write(
                rf"%\newcommand{{\calculatorpermission}}{{Calculator \textbf{{PERMITTED}}}}"
                "\n"
            )
            the_file.write(
                rf"\newcommand{{\calculatorpermission}}{{Calculator \textbf{{NOT PERMITTED}}}}"
                "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- WRITE SOLUTIONS" "\n")
            the_file.write(
                rf"\newcommand{{\writesolutions}}{{on the \textbf{{squared paper}}}}"
                "\n"
            )
            the_file.write(
                rf"% \newcommand{{\writesolutions}}{{in the \textbf{{test booklet}}}}"
                "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- FORMULA BOOKLET PERMISSION" "\n")
            the_file.write(
                rf"%\newcommand{{\formulabooklet}}{{No Formula Booklet Provided}} " "\n"
            )
            the_file.write(
                rf"\newcommand{{\formulabooklet}}{{Formula Booklet Provided}}" "\n"
            )
            the_file.write("" "\n")
            the_file.write(rf"% -- SOLUTION BOX TYPE" "\n")
            the_file.write(
                rf"% \newcommand{{\solnboxtype}}{{solutionordottedlines}}" "\n"
            )
            the_file.write(rf"% \newcommand{{\solnboxtype}}{{solutionorbox}}" "\n")
            the_file.write(rf"\newcommand{{\solnboxtype}}{{solution}}" "\n")
            the_file.write("" "\n")
            the_file.write(rf"% > >  CUSTOM GRADING TABLE" "\n")
            the_file.write(rf"% \newcommand{{\customgradetable}}{{" "\n")
            the_file.write(rf"% = SingleRow" "\n")
            the_file.write(rf"% \gradetable[h][questions]" "\n")
            the_file.write(rf"% = MultiRow" "\n")
            the_file.write(rf"% \setlength{{\doublerulesep}}{{0.25in}}" "\n")
            the_file.write(rf"% \multirowgradetable{{2}}[questions]" "\n")
            the_file.write(rf"% }}" "\n")
            the_file.write(rf"\usepackage{{mhoexamgy}}" "\n")
            the_file.write(rf"%\usepackage{{mhominted}}" "\n")
            the_file.write(rf"\begin{{document}}" "\n")
            the_file.write(rf"%\makecoverpage%" "\n")
            the_file.write(rf"%\newpage\null\thispagestyle{{empty}}\newpage" "\n")
            the_file.write(rf"\begin{{questions}}" "\n")
            the_file.write(rf"\input{{0-tex/tex_exam-}}" "\n")
            the_file.write(rf"\end{{questions}}" "\n")
            the_file.write(rf"\end{{document}}" "\n")

    @classmethod
    def gen_tex_marks_files(cls):
        with open(
            f"{path_tex}/tex_exam_ms-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("")
        with open(
            f"{path_tex}/tex_exam_marks_swedish-{TagId().tag_id}.tex",
            "x",
            encoding="utf-8",
        ) as the_file:
            the_file.write("%")
        with open(
            f"{path_tex}/tex_exam_marks-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write("%")

    @classmethod
    def gen_tex_wksh_files(cls):
        with open(
            rf"{path_mho_tex}/{GenOrgFiles().org_identifier}=={TagId().tag_id}--{GenFiles().name}-en-{GenFiles().level}__wksh.tex",
            "x",
            encoding="utf-8",
        ) as the_file:
            the_file.gen("")
        with open(
            rf"{path_mho_tex}/{GenOrgFiles().org_identifier}=={TagId().tag_id}--{GenFiles.name}-sv-{GenFiles.level}__wksh.tex",
            "x",
            encoding="utf-8",
        ) as the_file:
            the_file.gen("")


class GenOrgFiles:
    org_id = uuid.uuid1()
    org_timestamp = current_datetime.strftime("[%Y-%m-%d " + day_name + " %H:%M]")
    org_identifier = current_datetime.strftime("%Y%m%dT%H%M%S")

    @classmethod
    def gen_org_files(cls, soln, proof, notes, slides, exams, marks):
        with open(
            f"{path_org}/{cls.org_identifier}=={TagId().tag_id}--{SchemaSearch().schema_search_choice_value}__{ContentMenu().org_tag}.org",
            "a",
            encoding="utf-8",
        ) as the_file:
            the_file.write(rf":PROPERTIES:" "\n")
            the_file.write(rf":ID: {cls.org_id}" "\n")
            the_file.write(rf":END:" "\n")
            the_file.write(
                rf"#+title: {SchemaSearch().schema_search_choice_value}" "\n"
            )
            the_file.write(rf"#+date: {cls.org_timestamp}" "\n")
            the_file.write(rf"#+filetags: :{ContentMenu().org_tag}:" "\n")
            the_file.write(rf"#+identifier: {cls.org_identifier}" "\n")
            the_file.write(rf"#+signature: {TagId().tag_id}" "\n")
            the_file.write("\n")
            the_file.write(rf"[[{path_png}/tex_slide-{TagId().tag_id}.png]]" "\n")
            the_file.write("\n")
            the_file.write(r"* TeX Core Files" "\n")
            the_file.write(
                rf"+ [[file:{path_mho_tex}/0-tex/tex_core-{TagId().tag_id}.tex][Core-English]]"
                "\n"
            )
            the_file.write(
                rf"+ [[file:{path_mho_tex}/0-tex/tex_core_sv-{TagId().tag_id}.tex][Core-Swedish]]"
                "\n"
            )
            if soln == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_core_soln-{TagId().tag_id}.tex][Solution]]"
                    "\n"
                )
            else:
                pass
            if proof == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_core_proof-{TagId().tag_id}.tex][Proof]]"
                    "\n"
                )
            else:
                pass
            if marks == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_exam_marks_swedish-{TagId().tag_id}.tex][Marks-Swedish]]"
                    "\n"
                )
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_exam_marks-{TagId().tag_id}.tex][Marks-Points]]"
                    "\n"
                )
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_exam_ms-{TagId().tag_id}.tex][Mark Scheme]]"
                    "\n"
                )
            else:
                pass
            the_file.write(r"* TeX Template Files" "\n")
            if notes == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_note-{TagId().tag_id}.tex][Note]]"
                    "\n"
                )

            else:
                pass
            if slides == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_slide-{TagId().tag_id}.tex][Slide-English]]"
                    "\n"
                )
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_slide_sv-{TagId().tag_id}.tex][Slide-Swedish]]"
                    "\n"
                )

            else:
                pass
            if exams == True:
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_exam-{TagId().tag_id}.tex][Exam-English]]"
                    "\n"
                )
                the_file.write(
                    rf"+ [[file:{path_mho_tex}/0-tex/tex_exam_sv-{TagId().tag_id}.tex][Exam-Swedish]]"
                    "\n"
                )

            else:
                pass
            the_file.write(rf"* Backlinks" "\n")
            the_file.write(rf"#+BEGIN: denote-backlinks" "\n")
            the_file.write("\n")
            the_file.write("#+END:")
        pass

    @classmethod
    def gen_org_exam_swedish_files(cls):
        with open(
            rf"{path_org}/{cls.org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-{GenFiles().level}__exam_moc.org",
            "a",
            encoding="utf-8",
        ) as the_file:
            the_file.write(
                rf"#+title: courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-{GenFiles().level}"
                "\n"
            )
            the_file.write(rf"#+date: {cls.org_timestamp}" "\n")
            the_file.write(rf"#+filetags: :exam:moc:" "\n")
            the_file.write(rf"#+identifier: {cls.org_identifier}" "\n")
            the_file.write(rf"#+signature: {TagId().tag_id}" "\n")
            the_file.write("\n")
            the_file.write("* Files")
            the_file.write("\n")
            the_file.write(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-en-{GenFiles().level}__exam.tex][English Exam]]"
                "\n"
            )
            the_file.write(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-en-{GenFiles().level}__exam.pdf][English Exam (pdf)]]"
                "\n"
            )
            the_file.write(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-sv-{GenFiles().level}__exam.tex][Swedish Exam]]"
                "\n"
            )
            the_file.write(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--courses-{GenFiles().course_code}-{GenFiles().name}-{GenFiles().term_code}-sv-{GenFiles().level}__exam.tex][Swedish Exam (pdf)]]"
                "\n"
            )
            the_file.write("\n")
            the_file.write(rf"* Questions" "\n")
            the_file.write(rf"1." "\n")
            the_file.write(rf"* Backlinks" "\n")
            the_file.write("\n")
            the_file.write(rf"#+BEGIN: denote-backlinks" "\n")
            the_file.write("\n")
            the_file.write("#+END:")

    @classmethod
    def gen_org_wksh_files(cls):
        with open(
            rf"{path_org}/{cls.org_identifier}=={TagId().tag_id}--{GenFiles().name}-{GenFiles().level}__wksh_moc.org",
            "a",
            encoding="utf-8",
        ) as the_file:
            the_file.gen(rf"#+title: {GenFiles().name}-{GenFiles().level}" "\n")
            the_file.gen(rf"#+date: {cls.org_timestamp}" "\n")
            the_file.gen(rf"#+filetags: :wksh:moc:" "\n")
            the_file.gen(rf"#+identifier: {cls.org_identifier}" "\n")
            the_file.gen(rf"#+signature: {TagId().tag_id}" "\n")
            the_file.gen("\n")
            the_file.gen("* Files")
            the_file.gen("\n")
            the_file.gen(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--{GenFiles().name}-en-{GenFiles().level}__wksh_moc.tex]]"
                "\n"
            )
            the_file.gen(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--{GenFiles().name}-en-{GenFiles().level}__wksh_moc.pdf]]"
                "\n"
            )
            the_file.gen(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--{GenFiles().name}-sv-{GenFiles().level}__wksh_moc.tex]]"
                "\n"
            )
            the_file.gen(
                rf"+ [[file:~/Library/CloudStorage/Dropbox/mho_tex/{cls.org_identifier}=={TagId().tag_id}--{GenFiles().name}-sv-{GenFiles().level}__wksh_moc.tex]]"
                "\n"
            )
            the_file.gen("\n")
            the_file.gen(rf"* Backlinks" "\n")
            the_file.gen("\n")
            the_file.gen(rf"#+BEGIN: denote-backlinks" "\n")
            the_file.gen("\n")
            the_file.gen("#+END:")


class GenImageFile:
    @classmethod
    def gen_python_files(cls):
        """
        Returns
        =======
        Generates a python file of type defn
        """
        with open(
            f"{path_assets}/python/imgs_python-{TagId().tag_id}.py", "x"
        ) as the_file:
            the_file.write("")

    @classmethod
    def gen_tikz_files(cls):
        with open(
            f"{path_assets}/tikz/imgs_tikz-{TagId().tag_id}.tex", "x", encoding="utf-8"
        ) as the_file:
            the_file.write(rf"\documentclass[crop]{{standalone}}")
            the_file.write("\n")
            the_file.write(rf"\usepackage{{mhocolorthemenord}}")
            the_file.write("\n")
            the_file.write(rf"\usepackage{{mhomacros}}")
            the_file.write("\n")
            the_file.write(rf"\usepackage{{mhotikz}}")
            the_file.write("\n")
            the_file.write(rf"\usepackage{{mhotikzfonts}}")
            the_file.write("\n")
            the_file.write(rf"%\usepackage{{pgfplots}}")
            the_file.write("\n")
            the_file.write(rf"\begin{{document}}")
            the_file.write("\n")
            the_file.write(rf"\begin{{tikzpicture}}")
            the_file.write("\n")
            the_file.write(rf"\end{{tikzpicture}}")
            the_file.write("\n")
            the_file.write(rf"\end{{document}}")
