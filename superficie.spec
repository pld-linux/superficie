Summary:	3D objects visualizer
Summary(pl.UTF-8):	Wizualizer obiektów 3D
Name:		superficie
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/superficie/%{name}-%{version}.tar.gz
# Source0-md5:	e204fcc098096520d9384ef9f6f4d119
Patch0:		%{name}-gcc3.patch
Patch1:		%{name}-amfix.patch
URL:		http://superficie.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gtkglarea1-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Superficie is a small program that allows to visualize 3D surfaces and
other objects, and to manipulate them. It allows to rotate, to move
away, to show illumination, etc. on the surface at issue.

%description -l pl.UTF-8
Superficie to niewielki program pozwalający wizualizować powierzchnie
3D i inne obiekty, oraz manipulować nimi. Pozwala obracać, przesuwać,
pokazywać oświetlenie itp. na powierzchni.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
# ENABLE_NLS is workaround for gnome/libstdc++ conflict
CXXFLAGS="%{rpmcflags} -fpermissive -fno-exceptions -DENABLE_NLS"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.save_eps NEWS AUTHORS ChangeLog doc/data.ps
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/superficie.desktop
%{_pixmapsdir}/*
%{_datadir}/superficie
