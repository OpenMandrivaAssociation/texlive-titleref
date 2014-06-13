# revision 18729
# category Package
# catalog-ctan /macros/latex/contrib/titleref
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license pd
# catalog-version 2.0
Name:		texlive-titleref
Version:	2.0
Release:	7
Summary:	A "\titleref" command to cross-reference section titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titleref
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titleref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titleref.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 756923
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719756
- texlive-titleref
- texlive-titleref
- texlive-titleref

