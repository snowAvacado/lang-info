# lang-lines

simple script to show nr of lines for each language in git repo.

usage:

step1: clone this repo, i.e
```bash
git clone https://github.com/snowAvacado/lang-lines.git
```
step2: cd to src
```bash
cd lang-lines/src
```
step3: test our script 

usage: lang_lines.py <repo_url> 

for example: using kubernetes python client shows below info

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
