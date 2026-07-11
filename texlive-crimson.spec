%global tl_name crimson
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Crimson fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/crimson
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crimson.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crimson.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
the Crimson family of fonts, designed by Sebastian Kosch. The Crimson
family is for book production in the tradition of beautiful oldstyle
typefaces, inspired particularly by the work of people like Jan
Tschichold (Sabon), Robert Slimbach (Arno, Minion), and Jonathan Hoefler
(Hoefler Text). Small caps and old-style numerals are mostly available,
except old-style numerals are not supported in Bold or Semibold.

