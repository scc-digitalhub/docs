import os
import yaml

tutorials_dir = "/tutorials/docs"
metadata_filename = "metadata.yaml"
catalog_filename = "./tutorials-metadata-new.yaml"
mkdocs_file = "./tutorials/mkdocs.yml"

stable_version = os.environ["STABLE_VERSION"]
docs = f"https://scc-digitalhub.github.io/docs/{stable_version}/tutorials"
repo = f"https://github.com/scc-digitalhub/docs/tree/{stable_version}/tutorials/docs"
raw_base = f"https://raw.githubusercontent.com/scc-digitalhub/docs/refs/heads/{stable_version}/tutorials/docs"

def load_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return next(yaml.load_all(f, Loader=yaml.SafeLoader))

def initialize_catalog():
    catalog = {}
    catalog["base_path"] = tutorials_dir
    catalog["repository"] = repo
    catalog["docs"] = docs
    catalog["tutorials"] = autobuild_catalog()
    return catalog

def autobuild_catalog():
    in_nav = False
    nav_content = ""
    with open(mkdocs_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("nav:"):
                in_nav = True
            if in_nav:
                nav_content += line

    navigation = []
    nav = yaml.safe_load(nav_content)["nav"]
    for t in nav:
        if t != "index.md":
            for k, v in t.items():
                tutorial = {}
                tutorial["name"] = k

                first = v[0]
                tutorial["docs"] = f'{docs}/{first.replace(".md", "")}'
                tutorial["dir"] = first[:first.find("/")]
                tutorial["repository"] = f'{repo}/{tutorial["dir"]}'

                steps = []
                for step in v:
                    step_info = {}
                    step_info["file"] = step
                    step_info["docs"] = f'{docs}/{step.replace(".md", "")}'
                    step_info["url"] = f'{raw_base}/{step}'
                    with open(f'.{tutorials_dir}/{step}', "r", encoding="utf-8") as f:
                        for line in f:
                            if line.startswith("#"):
                                step_info["name"] = line[1:].strip()
                                break
                    steps.append(step_info)
                tutorial["steps"] = steps

                navigation.append(tutorial)

    return sorted(navigation, key=lambda d: d['name'])

def main():
    catalog = initialize_catalog()
    updated_tutorials = []

    for t in catalog["tutorials"]:
        tutorial_path = f'.{tutorials_dir}/{t["dir"]}'
        if os.path.isdir(tutorial_path):
            # Read metadata file, if present
            metadata_path = f'{tutorial_path}/{metadata_filename}'
            if os.path.isfile(metadata_path):
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    metadata = f.read()
                metadata = metadata.replace("STABLE_VERSION", stable_version)
                t = t | yaml.safe_load(metadata)
        updated_tutorials.append(t)

    catalog["tutorials"] = updated_tutorials

    with open(catalog_filename, 'w', encoding='utf-8') as file:
        yaml.dump(catalog, file, allow_unicode=True)
        #json.dump(catalog, file, indent=4, default=str)

if __name__ == "__main__":
    main()