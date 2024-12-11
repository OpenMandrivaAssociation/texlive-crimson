Name:		texlive-crimson
Version:	73074
Release:	1
Summary:	Crimson fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/crimson
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crimson.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crimson.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX
support for the Crimson family of fonts, designed by Sebastian
Kosch. The Crimson family is for book production in the
tradition of beautiful oldstyle typefaces, inspired
particularly by the work of people like Jan Tschichold (Sabon),
Robert Slimbach (Arno, Minion), and Jonathan Hoefler (Hoefler
Text). Support for small caps and old-style numerals is still
"under construction"; these features are not supported by this
version of the package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/crimson
%{_texmfdistdir}/fonts/vf/kosch/crimson
%{_texmfdistdir}/fonts/type1/kosch/crimson
%{_texmfdistdir}/fonts/tfm/kosch/crimson
%{_texmfdistdir}/fonts/opentype/kosch/crimson
%{_texmfdistdir}/fonts/map/dvips/crimson
%{_texmfdistdir}/fonts/enc/dvips/crimson
%doc %{_texmfdistdir}/doc/fonts/crimson

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
