Summary:	3D objects visualizer
Summary(pl):	Wizualizer obiektów 3D
Name:		superficie
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.linuxsupportline.com/~superficie/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel >= 1.0.0
URL:		http://www.linuxsupportline.com/~superficie/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Superficie is a small program that allows to visualize 3D surfaces and
other objects, and to manipulate them. It allows to rotate, to move
away, to show illumination, etc. on the surface at issue.

%description -l pl
Superficie to niewielki program pozwalający wizualizować powierzchnie
3D i inne obiekty, oraz manipulować nimi. Pozwala obracać, przesuwać,
pokazywać oświetlenie itp. na powierzchni.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fpermissive -fno-exceptions"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rpm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.save_eps NEWS AUTHORS ChangeLog doc/data.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/superficie.desktop
%{_datadir}/gnome/help/superficie
%{_pixmapsdir}/*
%{_datadir}/superficie
