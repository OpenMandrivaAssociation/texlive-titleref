Name:		texlive-titleref
Version:	18729
Release:	1
Summary:	A "\titleref" command to cross-reference section titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titleref
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titleref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titleref.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a command \titleref that allows you to cross-reference
section (and chapter, etc) titles and captions just like \ref
and \pageref. The package does not interwork with hyperref; if
you need hypertext capabilities, use nameref instead.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titleref/titleref.sty
%doc %{_texmfdistdir}/doc/latex/titleref/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/titleref/titleref.pdf
%doc %{_texmfdistdir}/doc/latex/titleref/titleref.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
