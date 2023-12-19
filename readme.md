# lang-lines

shows number of lines in a file for each extension (.c, .py , .go etc.)
<br />in a github repo.

usage:

Step1: clone this repo, i.e
```bash
git clone https://github.com/snowAvacado/lang-lines.git
```
Step2: cd to src
```bash
cd lang-lines/src
```
step3: test

usage: python3 lang_lines.py <repo_url> 

for example: with kubernetes python client repo url , shows below info

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

another example using this repo, 
<br /> src/lang_extns.py has 1574 lines
<br /> src/lang_lines.py has 76 lines
<br /> readme.md has 46 has lines

```bash
$ python3 lang_lines.py https://github.com/snowAvacado/lang-lines.git
total: 1696 lines.
.py : 1650
.md : 46
success, time elapsed : 0.002009 seconds
```
