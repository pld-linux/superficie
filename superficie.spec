Summary:	3D objects visualizer
Name:		superficie
Version:	0.7.2
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	http://www.linuxsupportline.com/~superficie/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel >= 1.0.0
URL:		http://www.linuxsupportline.com/~superficie/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description 
Superficie is a small program that allows to visualize 3D surfaces and
other objects, and to manipulate them. It allows to rotate, to move away,
to show illumination, etc. on the surface at issue.

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -fpermissive -fno-exceptions"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure

make

%install
rpm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README README.save_eps NEWS AUTHORS ChangeLog doc/data.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%doc *.gz doc/*.gz

%{_bindir}/*
%{_datadir}/gnome/apps/Graphics/superficie.desktop
%{_datadir}/gnome/help/superficie
%{_datadir}/pixmaps/*
%{_datadir}/superficie
