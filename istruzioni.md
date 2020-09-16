---
content: true
home: true
---

# Getting access to the repository
Email you github ID to [Michele Loreti](mailto:michele.loreti@unicam.it) or [Emilio Tuosto](mailto:emilio.tuosto@gssi.it)
in order to get the right to modify the files.

# Starting an editing session
If you've a github account then you should know how to execute the steps below on your favourite OS and or git client.
Below are the steps to follow from a Linux shell

1. update your local copies of the files with
   ```bash
   > git pull
   ```
   Forgetting this step will probably introduce clashes.

2. Now you can modify the files; see the next section for a
   description of the directory structure.

3. When your editing is done, do ```bash > git commit -am "write a
meaningful (and memorable) comment" > git push ``` The 'commit' part
will commit your changes to your local copy only; you can commit as
many times as you like, but your changes won't be visible until you
execute the 'push' command which synchronises the local changes on the
remote server.

Note that the changes may not be immediately visible on the site since
the server has to re-generate the pages (re-generation could take up
to 10 minutes).

