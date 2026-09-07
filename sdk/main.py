def define_env(env):
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
