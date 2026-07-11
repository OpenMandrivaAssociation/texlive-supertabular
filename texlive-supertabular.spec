%global tl_name supertabular
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2c
Release:	%{tl_revision}.1
Summary:	A multi-page tables package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/supertabular
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/supertabular.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package was a predecessor of longtable; the newer package (designed
on quite different principles) is easier to use and more flexible, in
many cases, but supertabular retains its usefulness in a few situations
where longtable has problems.

