Name:		texlive-supertabular
Version:	53658
Release:	1
Summary:	A multi-page tables package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/supertabular
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Generally longtable is a little easier to use and more
flexible, but supertabular has its place, since it will work in
a few situations where longtable won't.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/supertabular/supertabular.sty
%doc %{_texmfdistdir}/doc/latex/supertabular/CATALOG
%doc %{_texmfdistdir}/doc/latex/supertabular/ChangeLog
%doc %{_texmfdistdir}/doc/latex/supertabular/MANIFEST
%doc %{_texmfdistdir}/doc/latex/supertabular/README
%doc %{_texmfdistdir}/doc/latex/supertabular/supertabular.pdf
#- source
%doc %{_texmfdistdir}/source/latex/supertabular/supertabular.dtx
%doc %{_texmfdistdir}/source/latex/supertabular/supertabular.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
