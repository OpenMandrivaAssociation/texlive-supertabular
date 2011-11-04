# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/supertabular
# catalog-date 2009-10-10 00:51:28 +0200
# catalog-license lppl
# catalog-version 4.1a
Name:		texlive-supertabular
Version:	4.1a
Release:	1
Summary:	A multi-page tables package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/supertabular
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Generally longtable is a little easier to use and more
flexible, but supertabular has its place, since it will work in
a few situations where longtable won't.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
