import os
import json

def get_directory_structure(rootdir):
    def _get_structure(path):
        structure = {"name": os.path.basename(path), "path": path, "children": []}
        try:
            for entry in os.scandir(path):
                if entry.is_dir(follow_symlinks=False):
                    structure["children"].append(_get_structure(entry.path))
                elif entry.is_file(follow_symlinks=False):
                    structure["children"].append({"name": entry.name, "path": entry.path})
        except PermissionError:
            # Skip directories that we don't have permission to access
            pass
        return structure

    return _get_structure(rootdir)

root_directory = "D:/projects/LIDO"
directory_structure = get_directory_structure(root_directory)

with open("structure.json", "w", encoding="utf-8") as f:
    json.dump(directory_structure, f, ensure_ascii=False, indent=4)
