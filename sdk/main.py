def define_env(env):
    @env.macro
    def entity_overview_cards(entity):
        """Render standard Create, Manage, and Use cards for an entity."""
        singular, plural = (entity, f"{entity}s")
        cards = [
            ("Create", "./create.md", f"Create a new {singular}."),
            ("Manage", "./manage.md", f"Read, update, or delete {plural}."),
            ("Use", "./use.md", f"Work with {singular} objects."),
        ]
        card_markdown = "\n\n".join(
            f'- [**{title}**]({link}){{ .card-link }}\n\n'
            f'    ---\n\n    {description}'
            for title, link, description in cards
        )
        return f"""<div class="grid cards entity-overview-cards" markdown>

{card_markdown}

</div>"""

    @env.macro
    def framework_card(title, link, description, use_cases):
        use_case_markdown = "\n".join(f"- {use_case}" for use_case in use_cases)
        return f"""<div class=\"framework-card\" markdown>

<div class=\"framework-details\" markdown>

- ## [{title}]({link}){{ .framework-title-link }}

<div markdown>

**Description**

{description}

</div>

<div markdown>

**Use cases**

{use_case_markdown}

</div>

</div>

</div>"""

    @env.macro
    def function_doc(name, import_path, caller):
        """Render a collapsible function reference with its example."""
        example = caller().strip("\n")
        return f"""??? example "{name}"

    === "Function documentation"

        ::: {import_path}
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_docstring_parameters: true
                show_docstring_returns: true
                show_root_heading: false
                show_symbol_type_heading: true
                show_source: false
                members:
                    - {name}

{example}"""

    @env.macro
    def member_doc(name, class_path):
        """Render a collapsible class method or property reference."""
        return f"""??? example "{name}"

    ::: {class_path}.{name}
        options:
            heading_level: 6
            show_signature: false
            show_docstring_description: true
            show_source: false
            show_root_heading: true
            show_symbol_type_heading: true
            show_root_full_path: false
            show_root_toc_entry: true"""
