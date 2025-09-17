#!/usr/bin/env python3

import argparse
import os
import shutil

def list_templates(template_dir: str) -> None:
    templates = [entry.name for entry in os.scandir(template_dir) if entry.is_dir()]
    print('Avalable templates:')
    for template in templates:
        print(f'- {template}')

def copy_template(template_dir: str, template_name: str, target_dir: str, overwrite: bool) -> None:
    src_path = os.path.join(template_dir, template_name)
    dst_path = os.path.abspath(target_dir)
    
    if not os.path.exists(src_path):
        print(f'Template `{template_name}` does not exist in `{template_dir}`')
        return
    
    if os.path.exists(dst_path):
        if overwrite:
            shutil.rmtree(dst_path)
        else:
            print(f'Error: Target `{target_dir}` already exists')
            return
    
    shutil.copytree(src_path, dst_path)
    print(f'Template `{template_name}` has been copied to `{target_dir}`')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.abspath(os.path.join(script_dir, '..', 'templates'))

    parser = argparse.ArgumentParser(description='Template CLI Tool')
    parser.add_argument('--list', action='store_true', help='List available templates')
    parser.add_argument('--use', metavar='TEMPLATE_NAME', help='Name of the template to use')
    parser.add_argument('-t', '--target', metavar='TARGET_DIR', help='Target directory to copy the template to')
    parser.add_argument('-d', '--dir', metavar='TEMPLATE_DIR', default=template_dir, help='Directory containing templates')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite target directory if it exists')

    args = parser.parse_args()

    if args.list:
        list_templates(args.dir)
    elif args.use and args.target:
        copy_template(args.dir, args.use, args.target, args.overwrite)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()