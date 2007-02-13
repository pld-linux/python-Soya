%define		module	Soya
Summary:	A practical high-level object-oriented 3D engine for Python
Summary(pl.UTF-8):	Praktyczny, wysokopoziomowy, zorientowany obiektowo silnik 3D dla Pythona
Name:		python-%{module}
Version:	0.9.2
Release:	0.2
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://download.gna.org/soya/%{module}-%{version}.tar.bz2
# Source0-md5:	da59d3fa714076af9c03da6cbbdb5e86
Source1:	http://download.gna.org/soya/SoyaTutorial-0.9.tar.bz2
# Source1-md5:	0b078cbd53a25c12a8bd0f974b2d4dc5
URL:		http://oomadness.tuxfamily.org/en/soya/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	cal3d-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	ncurses-devel
BuildRequires:	ode-devel
BuildRequires:	python-modules
BuildRequires:	python-devel >= 2.2
%pyrequires_eq	python
Requires:	python-EditObj
Requires:	python-Imaging
Requires:	python-tkinter
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
URL:		http://oomadness.tuxfamily.org/en/soya_tuto/
Requires:	%{name} = %{version}-%{release}
Obsoletes:	Soya-tutorial

%description tutorial
Package contains a set of tutorial for Soya.

%description tutorial -l pl.UTF-8
Pakiet zawiera kompletny tutorial dla Soya.

%prep
%setup -q -n %{module}-%{version} -a1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

install manpage/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

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
%{_mandir}/man1/*

%files tutorial
%defattr(644,root,root,755)
%doc SoyaTutorial-0.9/{AUTHORS,README,tutorial}
