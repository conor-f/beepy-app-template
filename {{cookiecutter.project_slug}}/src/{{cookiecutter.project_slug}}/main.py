from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Label,
)


class TemplateApp(App):
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Get writing your new app!")
        yield Footer()

    def on_mount(self) -> None:
        pass


def main() -> None:
    TemplateApp().run()


if __name__ == "__main__":
    main()
