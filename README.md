# Template CLI Tool (Templater)

A simple command-line tool for managing and copying templates.
You can list available templates from a specified directory and copy them to any directory.

## 📦 Features

- **List available templates** — Easily check which templates are ready to use
- **Copy templates into a new project** — Bootstrap your project with one command

## 📚 Requirements

- python >= 3.8

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/show-t/project-templates.git
cd project-templates
chmod +x scripts/templater.py
```

### 2. Add the PATH
Add the `scripts` directory to your PATH so you can run the tool from anywhere
```bash
export PATH="$PATH:/path/to/templater/scripts"
```
Add this line to your shell profile (e.g., ~/.bashrc or ~/.zshrc) for persistence.

### 3. Verify

```bash
templater.py --help
```

## 📖 Usage
### Show help

```bash
templater.py --help
```

### List available templates

```bash
templater.py --list
```

### Copy a template

```bash
templater.py --use TEMPLATE_NAME --target ./my-project
```

### Overwrite copy (e.g., force copy into an existing directory)
```bash
templater.py --use TEMPLATE_NAME --target ./my-project --overwrite
```

## 🛠️ Options

| Option                        | Description                                           |
|-------------------------------|-------------------------------------------------------|
| `--list`                      | List available templates                              |
| `--use TEMPLATE_NAME`         | Specify the name of the template to use               |
| `-t`, `--target TARGET_NAME`  | Target directory to copy the template into            |
| `-d` `--dir TEMPLATE_DIR`     | Directory containing templates (default: `templates`) |
| `--overwrite`                 | Overwrite target if it already exists                 |

## 📁 Project Structure

```
.
├── scripts/              # Script files
│    └── templater.py
├── templates/            # Template files
│    ├── python/
│    │    └── ...
│    └── typescript/
│         └── ...
└── template.json         # Template meta data
```

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more details.