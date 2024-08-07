# EasyDNS 1.7

I tried to build an easy tool for windows to test dns-responses. You easily can build and send a custom dns-query and get displayed the answer.
ECS is also available - depending on the dns-server.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Inhaltsverzeichnis

- [EasyDNS 1.7](#easydns-17)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Installation](#installation)
  - [Using](#using)
  - [License](#license)

## Installation

1. Using the finished version
   1. Just download the easyDNS.zip
   2. Unzip the .zip and go into main.dist
   3. click on main.exe and use the tool
      1. Scapy needs a cmd-window to perform correctly. So if you use the .exe just ignore the cmd-window.
         I'm searching for a better solution.

2. You can also clone this repo and modify it as you want

## Using

1. If you just want to use the program:
   The GUI is (in my eyes) very simple and easy to use.
   I implemented also some error-messages if something went wrong - but unfortunately only in german at the moment.
   At the moment I only implemented the dns-methods A-Record, SRV and NAPTR because these three I need for my work.
   In future maybe some more will be available in future-versions.

2. If you use the source-code:
   GUI is made with Qt-framework and Qt-community-editor.
   - build.py: just make the GUI useable with python
   - main.py: the main source-code
   - error.py: module for the error-handling

## License

This project is under MIT-licens. [LICENSE](LICENSE)
