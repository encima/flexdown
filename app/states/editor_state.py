import reflex as rx


class EditorState(rx.State):
    """The state for the editor page."""

    notes: dict[str, str] = {
        "home/welcome/getting-started": '# Welcome to Reflex Markdown Editor!\n\nThis is a simple markdown editor with a live preview. Start typing on the left and see the result on the right.\n\n## Features\n\n- **Live Preview**: Updates as you type.\n- **Markdown Support**: Uses standard markdown syntax.\n- **Syntax Highlighting**: For code blocks.\n\n### Example Code Block\n\n\nimport reflex as rx\n\ndef my_app():\n    return rx.el.div("Hello, Reflex!")\n\n\n### Task List\n- [x] Create a markdown editor\n- [ ] Add slash commands\n- [ ] Implement autocompletion for tags\n\nStart editing to see the magic happen!\n'
    }

    @rx.var
    def path_parts(self) -> list[str]:
        """The parts of the path from the URL."""
        return self.router.page.params.get("splat", [])

    @rx.var
    def context(self) -> str:
        return self.path_parts[0] if len(self.path_parts) > 0 else "home"

    @rx.var
    def stream(self) -> str:
        return self.path_parts[1] if len(self.path_parts) > 1 else "welcome"

    @rx.var
    def note_name(self) -> str:
        return self.path_parts[2] if len(self.path_parts) > 2 else "getting-started"

    @rx.var
    def current_path(self) -> str:
        """The full path of the current note."""
        return f"{self.context}/{self.stream}/{self.note_name}"

    @rx.var
    def current_note_content(self) -> str:
        return self.notes.get(self.current_path, f"# New Note\n\nStart writing...")

    def set_current_note_content(self, text: str):
        self.notes[self.current_path] = text

    @rx.event
    def on_load(self):
        """Handle page load."""
        if len(self.path_parts) == 0:
            return rx.redirect("/home/welcome/getting-started")
        if self.current_path not in self.notes:
            self.notes[self.current_path] = (
                f"# {self.note_name.replace('-', ' ').title()}\n\nStart writing your note here..."
            )