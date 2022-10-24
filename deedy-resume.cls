% Intro Options
\ProvidesClass{deedy-resume}[2014/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass{article}

% Package Imports
\usepackage[hmargin=1.25cm, vmargin=0.7cm]{geometry}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage[hidelinks]{hyperref}
\usepackage{titlesec}
\usepackage[absolute]{textpos}
\usepackage[UKenglish]{babel}
\usepackage[UKenglish]{isodate}
\usepackage{fontspec,xltxtra,xunicode}

% Cite publications
\usepackage{cite}
\renewcommand\refname{\vskip -1.5cm}

% Color definitions
\RequirePackage{mhocolorthemenord}

\definecolor{date}{HTML}{4C566A} 
\definecolor{primary}{HTML}{2E3440} 
\definecolor{headings}{HTML}{3B4252}
\definecolor{subheadings}{HTML}{434C5E}

% Set main fonts
%\defaultfontfeatures{Mapping=tex-text}
%\setmainfont[Color=primary]{Flama}
%\setsansfont[Mapping=tex-text]{FlamaLight}
% > > > Fonts
\RequirePackage[warnings-off={mathtools-colon,mathtools-overbracket}]{unicode-math}
\RequirePackage{libertinus-otf}
\RequirePackage{metalogo}


% Date command
\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\textblockorigin{0mm}{5mm} % start everyth
\newcommand{\lastupdated}{\begin{textblock}{60}(155,0)
\color{date}\fontsize{8pt}{10pt}\selectfont 
Last Updated on
\today
\end{textblock}}

\newcommand{\leftdetails}[1]{\begin{textblock}{60}(170,5)
\color{date}\fontsize{8pt}{10pt}\selectfont 
#1
\end{textblock}}

% Name command
\newcommand{\namesection}[3]{
	\centering{
		\sffamily
		\fontsize{40pt}{10cm}\selectfont #1 
		\selectfont #2
	} \\
	\vspace{5pt}
	\centering{\color{nordTwo}\fontsize{11pt}{14pt}\selectfont #3}
	\noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}
	\vspace{-15pt}
}
\titlespacing{\section}{0pt}{0pt}{0pt}

% Headings command
\titleformat{\section}{\color{nordOne}
\scshape\fontsize{16pt}{24pt}\selectfont \raggedright\uppercase}{} {0em}{}

% Subeadings command
\titleformat{\subsection}{\color{nordOne}
\fontsize{12pt}{12pt}\selectfont\uppercase}{}{0em}{}
\titlespacing{\subsection}{0pt}{\parskip}{-\parskip}
\titlespacing{\subsubsection}{0pt}{\parskip}{-\parskip}
\newcommand{\runsubsection}[1]{\color{nordTwo}
\fontsize{12pt}{12pt}\selectfont\uppercase {#1} \normalfont}

% Descriptors command
\newcommand{\descript}[1]{\color{nordTen}\raggedright\scshape\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}

% Location command
\newcommand{\location}[1]{\color{nordOne}\raggedright\scshape\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}

% Section seperators command
\newcommand{\sectionsep}[0]{\vspace{8pt}}

% Bullet Lists with fewer gaps command
\newenvironment{tightemize}{\vspace{-\topsep}\begin{itemize}\itemsep1pt \parskip0pt \parsep0pt}{\end{itemize}\vspace{-\topsep}}


