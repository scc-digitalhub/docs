def define_env(env):
    def render_overview_cards(cards):
        card_markdown = "\n\n".join(
            f'- [**{title}**]({link}){{ .card-link }}\n\n'
            f'    ---\n\n    {description}'
            for title, link, description in cards
        )
        return f"""<div class="grid cards entity-overview-cards" markdown>

{card_markdown}

</div>"""

    @env.macro
    def entity_overview_cards(entity):
        """Render standard Create, Manage, and Use cards for an entity."""
        singular, plural = entity, f"{entity}s"
        return render_overview_cards([
            ("Create", "./create.md", f"Create a new {singular}."),
            ("Manage", "./manage.md", f"Read, update, or delete {plural}."),
            ("Use", "./use.md", f"Work with {singular} objects."),
        ])

    @env.macro
    def overview_cards(cards):
        """Render overview cards from title, link, and description entries."""
        return render_overview_cards(cards)

    @env.macro
    def page_navigation(left=None, right=None):
        """Render optional left and right page navigation buttons."""
        links = []
        if left is not None:
            label, link = left
            links.append(f"[{label}]({link}){{ .md-button }}")
        if right is not None:
            label, link = right
            links.append(f"[{label}]({link}){{ .md-button }}")

        if not links:
            return ""

        link_markdown = "\n\n".join(links)
        return f"""<div class="runtime-page-navigation" markdown>

{link_markdown}

</div>"""

    @env.macro
    def kind_cards(kinds):
        """Render cards linking to kind-specific documentation."""
        card_markdown = "\n\n".join(
            f'- [**{name}**]({link}){{ .list-card-link }} - {description} - `{kind}`'
            for name, link, description, kind in kinds
        )
        return f"""<div class="list-cards" markdown>

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
    def function_doc(name, import_path, caller=None, separate_examples=False):
        """Render a collapsible function reference with an optional example tab."""
        if separate_examples:
            example = f"""    === "Example"

        ::: {import_path}.{name}
            options:
                heading_level: 6
                show_signature: false
                show_docstring_attributes: false
                show_docstring_classes: false
                show_docstring_description: false
                show_docstring_examples: true
                show_docstring_functions: false
                show_docstring_modules: false
                show_docstring_other_parameters: false
                show_docstring_parameters: false
                show_docstring_raises: false
                show_docstring_receives: false
                show_docstring_returns: false
                show_docstring_type_aliases: false
                show_docstring_type_parameters: false
                show_docstring_warns: false
                show_docstring_yields: false
                show_root_heading: false
                show_symbol_type_heading: false
                show_source: false"""
            show_docstring_examples = "false"
        else:
            example = caller().strip("\n") if caller is not None else ""
            show_docstring_examples = "true"

        return f"""??? example "{name}"

    === "Function documentation"

        ::: {import_path}.{name}
            options:
                heading_level: 6
                show_signature: false
                show_docstring_description: true
                show_docstring_examples: {show_docstring_examples}
                show_docstring_parameters: true
                show_docstring_returns: true
                show_root_heading: false
                show_symbol_type_heading: false
                show_source: false

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
