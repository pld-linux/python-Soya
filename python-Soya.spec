#
# TODO: unpackaged files
#
%define		module	Soya
Summary:	A practical high-level object-oriented 3D engine for Python
Summary(pl.UTF-8):	Praktyczny, wysokopoziomowy, zorientowany obiektowo silnik 3D dla Pythona
Name:		python-%{module}
Version:	0.14
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://download.gna.org/soya/%{module}-%{version}.tar.bz2
# Source0-md5:	9fa56b14d3e9d5fcee073de650b3206f
Source1:	http://download.gna.org/soya/SoyaTutorial-%{version}.tar.bz2
# Source1-md5:	241d4e56e21cf70487323b3b25f9c37c
URL:		http://home.gna.org/oomadness/en/soya3d/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenAL-devel
BuildRequires:	SDL-devel
BuildRequires:	cal3d-devel >= 0.10.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	glew-devel
BuildRequires:	ncurses-devel
BuildRequires:	ode-devel >= 0.7
BuildRequires:	python-Pyrex
BuildRequires:	python-modules >= 0.9.3
BuildRequires:	python-devel >= 2.4
BuilDrequires:	rpm-pythonprov
%pyrequires_eq	python
Requires:	python-EditObj2
Requires:	python-PIL
Obsoletes:	Soya
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Soya 3D is a high level 3D engine for Python; it aims at being to 3D
what Python is to programming: easy and powerful. It is designed with
games in mind, focusing both on performance and ease-of-use. It relies
on OpenGL, SDL and Cal3D.

%description -l pl.UTF-8
Soya 3D jest wysokopoziomowym silnikiem 3D dla Pythona, zachowującym
najlepsze cechy programowania w Pythonie: łatwość i ogromny potencjał.
Został zaprojektowany z myślą o grach, skupiając się na wydajności
oraz łatwości w użyciu. Opiera się na OpenGL, SDL i Cal3D.

%package tutorial
Summary:	Tutorial for Soya
Summary(pl.UTF-8):	Tutorial dla Soya
Group:		Development/Languages/Python
URL:		http://home.gna.org/oomadness/en/soya3d/tutorials/index.html
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Soya-tutorial

%description tutorial
Package contains a set of tutorial for Soya.

%description tutorial -l pl.UTF-8
Pakiet zawiera kompletny przewodnik dla Soya.

%prep
%setup -q -n %{module}-%{version} -a1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

install manpage/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README*
%attr(755,root,root) %{_bindir}/soya_editor
%dir %{py_sitedir}/soya
%attr(755,root,root) %{py_sitedir}/soya/*.so
%{py_sitedir}/soya/*.py[co]
%{py_sitedir}/soya/data
%dir %{py_sitedir}/soya/editor
%{py_sitedir}/soya/editor/*.py[co]
%{py_sitedir}/*.egg-info
%{_mandir}/man1/soya_editor.*

%files tutorial
%defattr(644,root,root,755)
%doc SoyaTutorial-%{version}/{AUTHORS,README,tutorial}
