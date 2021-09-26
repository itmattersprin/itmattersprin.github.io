---
content: true
home: true
---

# Getting access to the repository
Email you github ID to [Michele
Loreti](mailto:michele.loreti@unicam.it) or [Emilio
Tuosto](mailto:emilio.tuosto@gssi.it) in order to get the right to
modify the files.

Once you are notified that permissions are granted, clone the
repository into your machine as explained in the next section.

# Starting an editing session

If you've a github account then you should know how to execute the
steps below on your favourite OS and or git client.  Below are the
steps to follow from a Linux shell.

0. clone the remote repository with the command
   ```bash
   > git clone git@github.com:itmattersprin/itmattersprin.github.io.git
   ```
   (or checkout [https://github.com/itmattersprin/itmattersprin.github.io](https://github.com/itmattersprin/itmattersprin.github.io)).

1. from the directory where you stored your local copy of the files
   (if you executed the previous command the directory is called
   'itmattersprin.github.io') update your local copies of the files
   with
   ```bash
   > git pull
   ```
   Forgetting this step will probably introduce clashes.

2. Now you can modify the files; see the next section for a
   description of the directory structure. Typically, you will have to
   create a new file in the formats described below. A newly created
   file needs to be added to the git repository (otherwise changes to
   the files won't be tracked and saved on the remote server by
   git). Execute
   ```bash
   > git add path_to_the_file/my_file.md
   ```
   to add the file 'my_file.md' to the site.

3. When your editing is done, do ```bash > git commit -am "write a
meaningful (and memorable) comment" > git push ``` The 'commit' part
will commit your changes to your local copy only; you can commit as
many times as you like, but your changes won't be visible until you
execute the 'push' command which synchronises the local changes on the
remote server.

Note that the changes may not be immediately visible on the site since
the server has to re-generate the pages (re-generation could take up
to 10 minutes).

# Structure of files and directories
Below is a description of the files and directory to modify in order to add
content on the site. We invite you not to modify other files, unless you
know what you're doing.
## Directories
- _eventsIT: files of events related to It-Matters
- _msIT: projet's milestones
- _newsIT: files of news
- _papers: bibliografic information of papers published within the project
- _staff: details about people/staff working/related to the project
- _talks: descriptions of talks
- _toolkits: descriptions and references to tools of It-Matters

## Files
Each of the directories above contains a file for each element the directory is supposed to contain.
All the files are in Markdown format which basically represents a map '(key, value)' where 'key' is
a tag that the server uses to render the html pages and 'value' is a string. For example
the file describing an event in '_eventsIT' has the form
```bash
---
name: "DisCoTec 2020"
date: "15-19/06/2020"
wp: "http://www.discotec.org"
---
```
where the keys are 'name', 'date', and 'wp' respectively with values
"DisCoTec 2020", "15-19/06/2020", and "http://www.discotec.org". The
initial and final '```---```' are important and should not be omitted
and likewise for the quote symbols '"' around the values.

## An example
Suppose that you want to add a new event about the workshop
"Spatial madness" whose url is
"https://spatialmadness.org". Create a file
'madness.md' in the directory '_eventsIT' and edit it with the
following content
```bash
---
name: "Workshop on spatial galore"
date: "15/05/2021"
wp: "https://spatialmadness.org"
---
```
Then execute
```bash
> git add _eventsIT/madness.md'
> git commit -am "A workshop on spatial techniques"
> git push
```
After a while the new event will be displayed on the project's events web page.

And likewise for the other elements such as papers, staff, etc.

## Workflow for updating publications
Handling the list of publications requires a slightly more complicated workflow involving the execution of a script:

1. go to the 'script' directory
2. edit the bibtex file for your institution (it is the file named in '<your-institution>.bib' in 'script')
3. remove from the repository the files of publications already generated (if your shell is in 'script', execute 'git rm ../_papers/<your-institution>_*')
4. execute the python script import<your-institution>.py with 'python import<your-institution>.py' or 'python3 import<your-institution>.py'
5. commit the changes on the server

In step 2 it is important that you add 

```bash
partner = {GSSI},
type = {article},
published = {true},
wps = {4}
```
to any new item to be included in the list of publications. If the paper is accepted but not published yet, please append '[to appear]' in the value you set to the key 'publisher'. Optional keys of the bibtex are
```bash
OA = {...},
OAlink = {...}
```
whose values can be set to the type of open access policy and the url to the paper. In doubt, check how such keys are used for existing entry.

For instance, to generate the bibliography of gssi,
```bash
> cd script
> emacs gssi.bib
> # once done with the editing
> git rm ../_papers/gssi_*
> python3 importgssi.py
> git add ../_papers/gssi_*
> git commit -am "publications of gssi updated"
> git push
```
After about 1 minute, the server produces the new site and if you refresh the publication page you should be able to see the udpates. Note that the page does not refresh if the new bibtex generates ill-formatted files (eg. you forgot an essential key in the bibtex).

The changes should be visible The automatically generated files 

