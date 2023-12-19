# lang-line
This tool displays total number of lines for each extension (.c, .py , .go etc.) in a github repo.

Usage:

Step1: Clone this repo
```bash
git clone https://github.com/snowAvacado/lang-lines.git
```
Step2: change directory to src
```bash
cd lang-lines/src
```
Step3: test

Usage: python3 lang_lines.py <repo_url> 

For example: Testing with kubernetes python client repo URL

```bash
$ python3 lang_lines.py https://github.com/kubernetes-client/python.git
total: 491219 lines.
.txt : 54
.rst : 10147
.py : 242512
.Makefile : 27
.md : 69903
.in : 9
.cfg : 9
.ini : 39
.yml : 168
.Dockerfile : 7
.ipynb : 1778
.yaml : 416
.OWNERS : 20
.json : 89631
.sh : 1213
.LICENSE : 403
.SECURITY_CONTACTS : 30
.unprocessed : 74796
.diff : 47
.bat : 10
success, time elapsed : 0.781032 seconds
```

