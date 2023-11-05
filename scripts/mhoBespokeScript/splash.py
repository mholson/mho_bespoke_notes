from rich import print
from rich.text import Text
from rich.panel import Panel


class SplashScreen:
    _splash_content = Text()

    _splash_content.append("Welcome to ", style="bold")
    _splash_content.append("mho TeX Org", style="bold cyan")
    _splash_content.append("\n\n Generating The Necessary Files", style="italic")
    _splash_content.append(
        "\n\n A complete Organization System",
        style="bold white",
    )

    @classmethod
    def show_splash(cls):
        splash_panel = Panel(cls._splash_content, expand=False, border_style="cyan")
        print(splash_panel)


if __name__ == "__main__":
    inst = SplashScreen()
    inst.show_splash()
