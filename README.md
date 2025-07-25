# 🌐 QGIS Planet Website [![DPG Badge](https://img.shields.io/badge/Verified-DPG-3333AB?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzEiIGhlaWdodD0iMzMiIHZpZXdCb3g9IjAgMCAzMSAzMyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjIwMDggMjEuMzY3OEwxMC4xNzM2IDE4LjAxMjRMMTEuNTIxOSAxNi40MDAzTDEzLjk5MjggMTguNDU5TDE5LjYyNjkgMTIuMjExMUwyMS4xOTA5IDEzLjYxNkwxNC4yMDA4IDIxLjM2NzhaTTI0LjYyNDEgOS4zNTEyN0wyNC44MDcxIDMuMDcyOTdMMTguODgxIDUuMTg2NjJMMTUuMzMxNCAtMi4zMzA4MmUtMDVMMTEuNzgyMSA1LjE4NjYyTDUuODU2MDEgMy4wNzI5N0w2LjAzOTA2IDkuMzUxMjdMMCAxMS4xMTc3TDMuODQ1MjEgMTYuMDg5NUwwIDIxLjA2MTJMNi4wMzkwNiAyMi44Mjc3TDUuODU2MDEgMjkuMTA2TDExLjc4MjEgMjYuOTkyM0wxNS4zMzE0IDMyLjE3OUwxOC44ODEgMjYuOTkyM0wyNC44MDcxIDI5LjEwNkwyNC42MjQxIDIyLjgyNzdMMzAuNjYzMSAyMS4wNjEyTDI2LjgxNzYgMTYuMDg5NUwzMC42NjMxIDExLjExNzdMMjQuNjI0MSA5LjM1MTI3WiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+Cg==)](https://blog.qgis.org/2025/02/08/qgis-recognized-as-digital-public-good/)

![Screenshot](./img/qgis-planet.webp)


> ## 👋 Welcome to the QGIS Planet Website!
>
> **This repository hosts the source code for the official QGIS Planet Website:**  
> 🌍 [https://planet.qgis.org](https://planet.qgis.org)
>
> Here you'll find everything you need to **build, develop, and contribute** to the QGIS Planet Website.
>
> ### ⚠️ Note on Subdomain Websites
>
> **This repository is _only_ for the main QGIS Planet Website ([planet.qgis.org](https://planet.qgis.org)).**
>
> If you are looking for the source code or want to contribute to QGIS subdomain websites, please visit their respective repositories below.  
> Each subdomain has its own codebase and contribution process:
>
> - [plugins.qgis.org](https://plugins.qgis.org) ([GitHub: QGIS-Plugins-Website](https://github.com/qgis/QGIS-Plugins-Website)) – QGIS Plugins Repository
> - [hub.qgis.org](https://hub.qgis.org) ([GitHub: QGIS-Hub-Website](https://github.com/qgis/QGIS-Hub-Website)) – QGIS Resources Hub
> - [feed.qgis.org](https://feed.qgis.org) ([GitHub: qgis-feed](https://github.com/qgis/qgis-feed)) – QGIS Feed Manager
> - [qgis.org](https://qgis.org) ([GitHub: QGIS-Website](https://github.com/qgis/QGIS-Website)) – QGIS Main Website
> - [members.qgis.org](https://members.qgis.org) ([GitHub: QGIS-Members-Website](https://github.com/qgis/QGIS-Members-Website)) – QGIS Sustaining Members Portal
> - [certification.qgis.org](https://certification.qgis.org) ([GitHub: QGIS-Certification-Website](https://github.com/qgis/QGIS-Certification-Website)) – QGIS Certification Programme Platform
> - [changelog.qgis.org](https://changelog.qgis.org) ([GitHub: QGIS-Changelog-Website](https://github.com/qgis/QGIS-Changelog-Website)) – QGIS Changelog Manager
> - [uc2025.qgis.org](https://uc2025.qgis.org) ([GitHub: QGIS-UC-Website](https://github.com/qgis/QGIS-UC-Website)) – QGIS User Conference Website

![-----------------------------------------------------](./img/green-gradient.png)


<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> 📖 Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#-project-overview"> 🚀 Project Overview </a></li>
    <li><a href="#-how-to-be-referenced"> 🌟 How to be Referenced </a></li>
    <li><a href="#-qa-status"> 🚥 QA Status </a></li>
    <li><a href="#-license"> 📜 License </a></li>
    <li><a href="#-folder-structure"> 📂 Folder Structure </a></li>
    <li><a href="#-using-ai-large-language-models"> 🤖 Using 'AI' (Large Language Models) </a></li>
    <li><a href="#️-scripts-overview"> 🛠️ Scripts Overview </a></li>
    <li><a href="#-using-the-nix-flake"> 🧊 Using the Nix Flake </a></li>
    <li><a href="#-contributing"> ✨ Contributing </a></li>
    <li><a href="#-have-questions"> 🙋 Have Questions? </a></li>
    <li><a href="#-contributors"> 🧑‍💻👩‍💻 Contributors </a></li>
  </ol>
</details>

![-----------------------------------------------------](./img/green-gradient.png)


## 🚀 Project Overview

![Overview](./img/planet-qgis-org.gif)

![-----------------------------------------------------](./img/green-gradient.png)


## 🌟 How to be Referenced

To make your feed appear on this Planet:

- A website publishing a public and compliant RSS feed (we use [feedparser](https://feedparser.readthedocs.io/) under the hood) with content about the QGIS project
- Add your RSS feed in the subscribers list using a Pull Request (or an issue if you don't know how to do a fork + PR). See [below for the subscriber model](#subscriber-model).

> **NOTE**:
> Only feed items with, at least, the `QGIS` [category](https://www.rssboard.org/rss-specification#ltcategorygtSubelementOfLtitemgt) (= tag) will be listed. Although there was work done on a mechanism to customize tags per feed, we have disabled this for now. [See this discussion](https://github.com/qgis/QGIS-Planet-Website/pull/49#discussion_r1958152569).

### Subscriber model

The file `data/subscribers.json` is the main entry to fetch all feeds for the QGIS Planet Website. **You can add or update a feed by editing this file and submitting a Pull Request to this repository.** Below is the recommended data structure:

```jsonc
  {
    // The RSS Feed URL
    "feed": "https://geotribu.fr/feed_rss_created.xml",
    // Name of the subscriber
    "name": "Geotribu",
    // Shortname of the subscriber
    "shortname": "geotribu_fr",
    // Show on the Website
    "is_active": true,
    // Availables and main language of the feed.
    // The list of supported language is in the file
    // data/languages.json. Please add yours there if not listed.
    "languages": {
      "available": [
        "fr_fr"
      ],
      "main": "fr_fr"
    }
  },
```

![-----------------------------------------------------](./img/green-gradient.png)

## 🚥 QA Status

### 🪪 Badges
| Badge | Description |
|-------|-------------|
| [![E2E Tests](https://github.com/qgis/QGIS-Planet-Website/actions/workflows/playwright-e2e.yml/badge.svg)](https://github.com/qgis/QGIS-Planet-Website/actions/workflows/playwright-e2e.yml) | End-to-end tests status (Playwright) |
| [![Deploy Hugo site to Pages](https://github.com/qgis/QGIS-Planet-Website/actions/workflows/github-pages.yml/badge.svg)](https://github.com/qgis/QGIS-Planet-Website/actions/workflows/github-pages.yml) | Deployment status to GitHub Pages |
| ![Website Status](https://img.shields.io/website-up-down-green-red/https/planet.qgis.org.svg) | Website availability status |
| ![License](https://img.shields.io/github/license/qgis/QGIS-Planet-Website.svg) | Repository license |
| ![](https://img.shields.io/github/issues/qgis/QGIS-Planet-Website.svg) | Open issues count |
| ![](https://img.shields.io/github/issues-closed/qgis/QGIS-Planet-Website.svg) | Closed issues count |
| ![](https://img.shields.io/github/issues-pr/qgis/QGIS-Planet-Website.svg) | Open pull requests count |
| ![](https://img.shields.io/github/issues-pr-closed/qgis/QGIS-Planet-Website.svg) | Closed pull requests count |

### ⭐️ Project Stars

![Stars](https://starchart.cc/qgis/QGIS-Planet-Website.svg)

![-----------------------------------------------------](./img/green-gradient.png)


## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

![-----------------------------------------------------](./img/green-gradient.png)

## 📂 Folder Structure

```plaintext
QGIS-Planet-Website/
  ├── 🖼️  assets/           # Mainly used to store the schedule.csv file
  ├── ⚙️  config/           # Hugo configuration files
  ├── 📄  content/          # Markdown content files (pages, posts)
  ├── 🗄️  data/             # Data files (JSON) for site variables (feed, languages, subscribers)
  ├── 🖼️  img/              # Images files used by this README
  ├── 🧩  layouts/          # Hugo templates and partials
  ├── 🧪  playwright/       # Playwright end-to-end test scripts
  ├── 📦  public/           # Generated site output (after `hugo` build)
  ├── 🗂️  resources/        # Hugo-generated resources (e.g., minified assets)
  ├── 🛠️  scripts/          # Utility scripts for development/maintenance/harvesting
  ├── 📄  static/           # Static files served as-is (e.g., favicon, robots.txt)
  ├── 🎨  themes/           # Hugo themes
  ├── ⚙️  config.toml       # Main Hugo configuration file
  ├── 🤝  CONTRIBUTING.md   # Contribution guidelines
  ├── 🐍  fetch_feeds.py*   # Script to get sustaining members and other feeds to update the planet website
  ├── 📜  LICENSE           # Project license
  ├── ⚙️  Makefile          # Build/Deployment automation commands
  ├── 📖  README.md         # Project overview and instructions
  ├── 📋  REQUIREMENTS.txt  # Python dependencies (pip)
  ├── 🐚  flake.nix         # Nix flake environment definition
  └── 💡  vscode.sh*        # VSCode helper script for Nix development environment
```


![-----------------------------------------------------](./img/green-gradient.png)

## 🤖 Using 'AI' (Large Language Models)

We are fine with using LLM's and Generative Machine Learning to act as general assistants, but the following three guidelines should be followed:

1. **Repeatability:** Although we understand that repeatability is not possible generally, whenever you are verbatim using LLM or Generative Machine Learning outputs in this project, you **must** also provide the prompt that you used to generate the resource.
2. **Declaration:** Sharing the prompt above is implicit declaration that a machine learning assistant was used. If it is not obvious that a piece of work was generated, include the robot (🤖) icon next to a code snippet or text snippet.
3. **Validation:** Outputs generated by a virtual assistant should always be validated by a human and you, as contributor, take ultimate responsibility for the correct functionality of any code and the correct expression in any text or media you submit to this project.

![-----------------------------------------------------](./img/green-gradient.png)

## 🛠️ Scripts Overview

The `scripts/` folder contains utility scripts to assist with data loading, and project maintenance. Below is a summary of each script:


| Script Name                       | Description                                                                                  |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| `fetch_feeds.py`                  | Simple script to get sustaining members and other feeds and update the web site with them     |
| `vscode.sh`                       | Launch VSCode with all settings and extensions needed to productively work on this project    |
| `scripts/get_commit_hash.sh`  | Get the current commit hash of this repository and write it in config/commit.toml for the website version.                                       |
| `scripts/resize_image.py`  | Contains utilities to optimize images (resize, transform to webp, check validity).                                    |

> ✏️ **Note:** Run each script from the project root. Some scripts may require environment variables or configuration—see comments within each script for usage details.

![-----------------------------------------------------](./img/green-gradient.png)


## 🧊 Using the Nix Flake

The development environment is using Nix flakes. Please visit <https://nixos.wiki/wiki/Flakes> for more details.

Start the Nix development environment by running:

```sh
nix develop # Add  --experimental-features 'nix-command flakes' if you haven't enable Nix flakes
hugo server
# If you want to run VSCode:
./vscode
```

To build the website:

```sh
nix build .#packages.x86_64-linux # Add | cachix push qgis-planet-website to push it to cachix
```

![-----------------------------------------------------](./img/green-gradient.png)


## ✨ Contributing

We welcome contributions! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get started.

![-----------------------------------------------------](./img/green-gradient.png)

## 🙋 Have Questions?

Have questions or feedback? Feel free to open an issue or submit a Pull Request!  

![-----------------------------------------------------](./img/green-gradient.png)
## 🧑‍💻👩‍💻 Contributors

- [Tim Sutton](https://github.com/timlinux) – Original author and lead maintainer of the QGIS Planet Website project
- [Kontur Team](https://www.kontur.io) – Responsible for the design and development of the current website theme
- [Lova Andriarimalala](https://github.com/Xpirix) – Core developer and ongoing maintainer
- [QGIS Contributors](https://github.com/qgis/QGIS-Planet-Website/graphs/contributors) – See the full list of amazing contributors who have helped make this website possible.

![-----------------------------------------------------](./img/green-gradient.png)

Made with ❤️ by Tim Sutton (@timlinux), Lova Andriarimalala (@Xpirix) and QGIS Contributors.