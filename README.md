![GitHub Banner](/assets/images/bespoke_notes.png)
# mho Bespoke Notes 

This repository serves as a collection of my public-facing notes which are currently typeset using LaTeX (often pronounced "Lay-tech" or "Lah-tech").  
It also contains the custom style files, the python scripts, some of the assets, and parts of my org-mode denote knowledge system that I use to annotate and link my notes.

In addition to my notes, you will also find the templates that I use to create slide decks, generate exams and produce worksheets. 

Please be aware that some of these files might not compile successfully right out-of-the-box. This is mainly due to certain assets, like images, that are required but not included in this repository due to size constrains.

I genuinely hope that my work sparks a bit of LaTeX inspiration in your projects. I've been greatly inspired by the generous contributions of the community, and I aim to give back in the same spirit.

As of November 2023, I am contemplating making the switch to [Typst](https://github.com/typst/typst), which is a markup-based typesetter built using Rust. While it has a much cleaner syntax, easier to program and is super fast to compile documents, I am waiting for the platform to mature a little more.

Happy TeX-ing!

# Scripts
## Generating TeX and Org Files
![mho Bespoke Script](/assets/images/mho_bespoke_script.png)
# Cheatsheets
## Doom Emacs Cheatsheet
![Doom Emacs Cheatsheet](/assets/images/latex-cheatsheet-doomEmacs.png)

**Dependencies**
- [mhocheatsheet.sty](/texmf/mhocheatsheet.sty)
- [mhocolorpalettesthlmnord.sty](/texmf/mhocolorpalettesthlmnord.sty)
- [mhominted.sty](/texmf/mhominted.sty)

 
**Files** 
- [0-reference_emacs_doom.tex](/main/0-reference_emacs_doom.tex)
- [0-reference_emacs_doom.pdf](/main/0-reference_emacs_doom.pdf)

# Notebooks

# Exams

# Generated Images

## Images Generated using TiKz

| &nbsp; | &nbsp; |
| :----: | :----: |
| ![058w](/assets/png/imgs_tikz-058w.png) | ![05wm](/assets/png/imgs_tikz-05wm.png) |
| [`058w.tex`](/assets/tikz/imgs_tikz-058w.tex) | [`05wm.tex`](/assets/tikz/imgs_tikz-05wm.tex) |
| ![059t](/assets/png/imgs_tikz-059t.png) | ![0136](/assets/png/imgs_tikz-0136.png) |
| [`059t.tex`](/assets/tikz/imgs_tikz-059t.tex) | [`0136.tex`](/assets/tikz/imgs_tikz-0136.tex) |
| ![05c9](/assets/png/imgs_tikz-05c9.png) | ![01pk](/assets/png/imgs_tikz-01pk.png) |
| [`05c9.tex`](/assets/tikz/imgs_tikz-05c9.tex) | [`01pk.tex`](/assets/tikz/imgs_tikz-01pk.tex) |
 
## Images Generated using TkZ

| &nbsp; | &nbsp; |
| :----: | :----: |
| ![05ee](/assets/png/imgs_tikz-05ee.png) | ![05ej](/assets/png/imgs_tikz-05ej.png) |
| [`05ee.tex`](/assets/tikz/imgs_tikz-05ee.tex) | [`05ej.tex`](/assets/tikz/imgs_tikz-05ej.tex) |

## Images Generated using PythonTex

### Generating Factor Trees

![mho_pythontex_prime_tree_generator](/assets/images/mho_pythontex_prime_tree_generator.png) 

The files `mho_primetree_texfile_generator.py` and `mho_pythontex_factortree.tex` need to be placed in the same directory.  For me this is `~/../assets/pytex`.  

**Step 1:** 

``` shell
python mho_primetree_textfile_generator.py
```

This will generate an individual tex file of the form `imgs_pytex_primetree-###.tex`
for each composite integer on a given range included in the script file (default: 4-1001). 
Each of these files need to be individually compiled and have `pythontex` run.  
In my workflow, this is automatically taken care of by the `tex_all.py` script that 
automates the compilation of all my LaTeX files.

The code used to generate the trees using pythontex, forest and python
was referenced from [Stack Exchange](https://tex.stackexchange.com/a/132145).

If you just want to create a specific factor tree, then you can create a tex file, 
such as the example given and place the following code in it.  Notice that the 
argument passed into the `PrimeTree{990}` command is the composite integer that 
you want to generate a tree that includes it's prime factors.

```latex
\documentclass[crop, varwidth]{standalone}
\input{mho_pythontex_factortree}
\begin{document}
\PrimeTree{990}
\end{document}

```

#### Dependencies 

##### LaTex

- [mhocolorpalettesthlmnord.sty](/texmf/mhocolorpalettesthlmnord.sty)
- [mhofonts.sty](/texmf/mhofonts.sty)
- [mhomacros.sty](/texmf/mhomacros.sty)
- [mhotikz.sty](/texmf/mhotikz.sty)
- [forest](https://ctan.org/pkg/forest) 
- [pythontex](https://ctan.org/pkg/pythontex)

##### Python

- math

#### Files

- [`mho_primetree_texfile_generator.py`](/assets/pytex/mho_primetree_texfile_generator.py)
- [`mho_pythontex_factortree.tex`](/assets/pytex/mho_pythontex_factortree.tex) 
- [`imgs_pytex_primetree-990.tex`](/assets/pytex/imgs_pytex_primetree-990.tex)
