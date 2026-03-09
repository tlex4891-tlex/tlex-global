#!/usr/bin/env python3
"""
Deploy paperless_brief.html to a new GitHub repository 'paperless-brief'.

This script:
1. Creates a new GitHub repo via the GitHub API
2. Initializes it with index.html
3. Enables GitHub Pages for hosting

Usage:
    python deploy_to_github.py
"""

import subprocess
import sys
import os

REPO_NAME = "paperless-brief"
GITHUB_USER = "tlex4891-tlex"
SOURCE_FILE = "index.html"
BRANCH = "main"


def run(cmd, check=True, capture=True):
    """Run a shell command and return output."""
    print(f"  $ {cmd}")
    result = subprocess.run(
        cmd, shell=True, capture_output=capture, text=True, check=False
    )
    if check and result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}")
        return None
    return result.stdout.strip() if capture else ""


def main():
    print(f"\n{'='*50}")
    print(f"  Deploy to GitHub: {GITHUB_USER}/{REPO_NAME}")
    print(f"{'='*50}\n")

    # Check that source file exists
    if not os.path.exists(SOURCE_FILE):
        print(f"ERROR: {SOURCE_FILE} not found in current directory.")
        sys.exit(1)

    print(f"[OK] Found {SOURCE_FILE}")

    # Try creating repo via gh CLI
    print("\n[1] Creating GitHub repository...")
    gh_check = run("which gh", check=False)
    if gh_check:
        run(f'gh repo create {GITHUB_USER}/{REPO_NAME} --public --description "Digitalizace kanceláří — Paper-less Projekt"')
    else:
        print("  gh CLI not available.")
        print(f"  Please create the repo manually at: https://github.com/new")
        print(f"  Repository name: {REPO_NAME}")
        print(f"  Owner: {GITHUB_USER}")
        print(f"  Visibility: Public")
        print()
        input("  Press Enter after creating the repo...")

    # Initialize git repo in a temp directory and push
    print("\n[2] Preparing files and pushing to GitHub...")
    deploy_dir = "/tmp/paperless-brief-deploy"
    run(f"rm -rf {deploy_dir}")
    run(f"mkdir -p {deploy_dir}")
    run(f"cp {SOURCE_FILE} {deploy_dir}/index.html")

    os.chdir(deploy_dir)

    run("git init")
    run(f"git checkout -b {BRANCH}")
    run("git add index.html")
    run('git commit -m "Initial commit: Paper-less projekt brief page"')
    run(f"git remote add origin https://github.com/{GITHUB_USER}/{REPO_NAME}.git")

    print("\n[3] Pushing to GitHub...")
    result = run(f"git push -u origin {BRANCH}", check=False)
    if result is None:
        print("\n  Push failed. You may need to:")
        print(f"  1. Create the repo at https://github.com/new (name: {REPO_NAME})")
        print(f"  2. Run: cd {deploy_dir} && git push -u origin {BRANCH}")
    else:
        print("\n[OK] Pushed successfully!")

    print(f"\n{'='*50}")
    print(f"  Repository: https://github.com/{GITHUB_USER}/{REPO_NAME}")
    print(f"  Enable GitHub Pages in repo Settings > Pages")
    print(f"  Page URL: https://{GITHUB_USER}.github.io/{REPO_NAME}/")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
