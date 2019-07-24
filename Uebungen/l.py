%% Erläuterungen zu den Befehlen erfolgen unter
%% diesem Beispiel.

\documentclass{scrartcl}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[ngerman]{babel}
\usepackage{amsmath}

\title{Ein Testdokument}
\author{Otto Normalverbraucher}
\date{5. Januar 2004}
\begin{document}

\maketitle
\tableofcontents
\section{Einleitung}

Hier kommt die Einleitung. Ihre Überschrift kommt
automatisch in das Inhaltsverzeichnis.

\subsection{Formeln}

\LaTeX{} ist auch ohne Formeln sehr nützlich und
einfach zu verwenden. Grafiken, Tabellen,
Querverweise aller Art, Literatur- und
Stichwortverzeichnis sind kein Problem.

Formeln sind etwas schwieriger, dennoch hier ein
einfaches Beispiel. Zwei von Einsteins
berühmtesten Formeln lauten:
\begin{align}
E &= mc^2                 \\
m &= \frac{m_0}{\sqrt{1-\frac{v^2}{c^2}}}
\end{align}
Aber wer keine Formeln schreibt, braucht sich
damit auch nicht zu beschäftigen.
\end{document}