# Code-LatexReportTemplate
### What
This is a latex sample report which is syncred with git(hub). It (semi-)automatically syncs the code into your latex, and semi-automatically exports the plots into your report.

### Why
You don't have to do unnecessary work copy pasting pictures and creating report-layouts because it's semi-automated. (Semi- means in this case that you have to click "upload it to 'the  github cloud'", which at github is called push, and pull when you want to copy your work from the github cloud to the overleaf cloud).

### How
0. Fork this repository:

0.a 

![1](./InstructionPictures/0.fork.png)

0.b 

![1](./InstructionPictures/1.fork.png)

1. Clone=download your fork of this repository:

1.a 

![1](./InstructionPictures/2.clone.png)

1.b 

![1](./InstructionPictures/3.clone.png)

2. if you want to work in overleaf: 

2.a Get a(n) (free) overleaf account.

2.b In: https://www.overleaf.com/project click: "New project>import from github" and select your (copy/fork of this) repository.


![1](./InstructionPictures/a.png)

2.c

![1](./InstructionPictures/b.png)

2.d

![1](./InstructionPictures/c.png)

2.e Then, if you have adapted your code, and changed some pictures, or made a table, upload your change back again to your github folder.
(It also automatically s the code in your report appendices, so no more copy pasting :))

2.f

![1](./InstructionPictures/0.png)

2.g

![1](./InstructionPictures/1.png)

2.h

![1](./InstructionPictures/3.png)

2.i

![1](./InstructionPictures/4.png)

2.j

![1](./InstructionPictures/5.png)



3. Then you update your entire report, so tables, (vector) figures, and code with a single click in overleaf:

![1](./InstructionPictures/d.png)


3.a Now if you change something in your report, e.g. your code, pictures or text, you can do your first upload (called push) to github. 

3.b Note, first time you use github with command you probably need to login, but it'll ask you to do so if you need to.
3.c push your code to github by opening cmd, browsing into the directory of the repository with `cd` and use commands:
```
git status
```
4.c with that `git status` command you can see which files you changed, normally you add a particular file, but since it is a lot this time, you can also type `git add *` instead (instead of the git add commands below).

4.d Then upload your changes to your own repository with:
```
git pull
git add "some_folder/the_file_you_changed.py"
git add "some_other_folder/the_plot_you_created.jpeg"

git commit -m "Created a plot for something specific."
git push
```
