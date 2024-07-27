import xml.etree.ElementTree as ET
from collections import defaultdict
import os

def parse_filesystem_structure(xml_file):
    """Parse the filesystem structure from the XML file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

def analyze_filesystem(root):
    """Analyze the filesystem structure and return relevant information."""
    structure = defaultdict(list)
    tasks = defaultdict(list)
    olog_structure = defaultdict(list)

    def traverse(element, path):
        if element.tag == 'directory':
            dir_name = element.get('name')
            new_path = f"{path}/{dir_name}" if path else dir_name
            structure[path].append(dir_name)

            if 'OLOG' in new_path:
                olog_structure[path].append(dir_name)

            for child in element:
                if child.tag == 'syncComputation':
                    for task in child.findall('task'):
                        tasks[new_path].append({
                            'name': task.get('name'),
                            'status': task.get('status')
                        })

                traverse(child, new_path)

    traverse(root, '')
    return dict(structure), dict(tasks), dict(olog_structure)

def reflow_information(structure, tasks, olog_structure):
    """Reflow information based on the analyzed filesystem structure."""
    reflowed_info = []

    reflowed_info.append("OLOG Structure:")
    for path, directories in olog_structure.items():
        reflowed_info.append(f"Path: {path}")
        reflowed_info.append(f"Subdirectories: {', '.join(directories)}")
        reflowed_info.append("")

    reflowed_info.append("Full Structure:")
    for path, directories in structure.items():
        reflowed_info.append(f"Path: {path}")
        reflowed_info.append(f"Subdirectories: {', '.join(directories)}")
        
        if path in tasks:
            reflowed_info.append("Tasks:")
            for task in tasks[path]:
                reflowed_info.append(f"  - {task['name']} (Status: {task['status']})")
        
        reflowed_info.append("")  # Add a blank line for readability

    return "\n".join(reflowed_info)

def examine_project_evolution(file_path):
    """Examine the project_evolution.md file."""
    if not os.path.exists(file_path):
        return "project_evolution.md file not found."

    with open(file_path, 'r') as file:
        content = file.read()

    # Here you can add more sophisticated analysis of the file content
    return f"project_evolution.md content:\n\n{content}"

def main(xml_file):
    root = parse_filesystem_structure(xml_file)
    structure, tasks, olog_structure = analyze_filesystem(root)
    reflowed_info = reflow_information(structure, tasks, olog_structure)
    print(reflowed_info)

    project_evolution_path = "/Users/barton/topos/OLOG/project_evolution.md"
    print(examine_project_evolution(project_evolution_path))

if __name__ == "__main__":
    main("filesystem_structure.xml")
