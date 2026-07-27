import os
import yaml
import json

base_mkdocs_file = "./base.yml"
index_path = "/site/search/"
index_filename = "search_index.json"
main_portal = "user"

def load_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return next(yaml.load_all(f, Loader=yaml.SafeLoader))

def portal_list():
    valid_yml = ""
    with open(base_mkdocs_file, "r", encoding="utf-8") as f:
        for line in f:
            if not "!ENV" in line:
                valid_yml += line

    portals = []
    portal_info = yaml.safe_load(valid_yml)["extra"]["portals"]
    for portal in portal_info:
        portal_name = portal["path"]
        if portal_name == "":
            portal_name = main_portal
        elif portal_name.startswith("/"):
            portal_name = portal_name[1:]

        # Only consider it a valid portal if it has a search index file
        if os.path.isfile(f'./{portal_name}{index_path}{index_filename}'):
            portals.append(portal_name)

    return portals

def external(prefix, index):
    updated_index = []
    for section in index["docs"]:
        updated_section = section.copy()
        updated_section["location"] = f'{prefix}/{updated_section["location"]}'
        updated_index.append(updated_section)
    return updated_index

def external_for_main(portal_name, index):
    return external(portal_name, index)

def external_for_others(portal_name, index):
    prefix = ".." if portal_name == main_portal else f'../{portal_name}'
    return external(prefix, index)

def merge(portal_name, searches):
    merged_index = searches[portal_name]["unchanged"]
    for name, portal_indices in searches.items():
        if name != portal_name:
            if portal_name == main_portal:
                merged_index["docs"] += portal_indices["external_for_main"]
            else:
                merged_index["docs"] += portal_indices["external_for_others"]
    return merged_index

def main():
    portals = portal_list()

    searches = {}
    for portal in portals:
        searches[portal] = {}
        with open(f'./{portal}{index_path}{index_filename}', "r", encoding="utf-8") as f:
            search_index = json.load(f)
        searches[portal]["unchanged"] = search_index
        searches[portal]["external_for_main"] = external_for_main(portal, search_index)
        searches[portal]["external_for_others"] = external_for_others(portal, search_index)
    
    for portal in portals:
        merged_index = merge(portal, searches)
        with open(f'./{portal}{index_path}{index_filename}', "w", encoding="utf-8") as f:
            json.dump(merged_index, f)

if __name__ == "__main__":
    main()