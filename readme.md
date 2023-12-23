# lang-lines
displays total number of lines and files for each extension (.c, .py , .go etc.) in a github repo from CLI
<br /><br />
one use case is to know feasibility of porting source code frome one programming language to  <br /> other based on
number of files and lines information.
<br /> <br />
## Usage:

### Step1: Clone this repo
```bash
git clone https://github.com/snowAvacado/lang-lines.git
```
### Step2: change directory to src
```bash
cd lang-lines/src
```
### Step3: test

python3 lang_lines.py <repo_url> 

For example: Testing with kubernetes python client repo URL

```bash
$ python3 lang_lines.py https://github.com/kubernetes-client/python.git
total: 497789 lines.
5 .txt : 54
1270 .rst : 10275
714 .py : 245527
1 .Makefile : 27
638 .md : 71003
1 .in : 9
2 .cfg : 9
2 .ini : 39
5 .yml : 168
1 .Dockerfile : 7
6 .ipynb : 1778
20 .yaml : 416
2 .OWNERS : 20
2 .json : 90891
11 .sh : 1213
2 .LICENSE : 403
2 .SECURITY_CONTACTS : 30
1 .unprocessed : 75863
2 .diff : 47
1 .bat : 10
success, time elapsed : 0.664469 seconds

```
#### output format: 
<number_of_files>  <file_extension> :  <number_of_lines>
