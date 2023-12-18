# lang-lines

simple script to show nr of lines for each language type used.

"usage: lang_lines.py <repo_url> 
`
 below example is for kuberenetes python client
```bash
/repo/lang-lines/src$ python3 lang_lines.py https://github.com/kubernetes-client/python.git
lang_lines.py: test Folder /repo/lang-lines/src/lang_lines created
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

