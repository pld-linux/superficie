%define  ver     0.7.2
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define  prefix  /usr


Summary: 3D objects visualizer

Name:      superficie
Version:   %ver
Release:   %rel
Copyright: GPL
Group:     Applications/Graphics
Packager:  Juan Pablo Romero Méndez
URL:       http://www.linuxsupportline.com/~superficie/
Source:    http://www.linuxsupportline.com/~superficie/superficie-%{ver}.tar.gz
BuildRoot: /var/tmp/gnumeric-%{PACKAGE_VERSION}-root
Docdir:    %{prefix}/doc

Requires: gnome-libs >= 1.0.0

%description 
Superficie is a small program that allows to visualize
3D surfaces and other objects, and to manipulate them. It allows to
rotate, to move away, to show illumination, etc. on the surface at
issue. 



%prep
%setup -q


%build

CXXFLAGS="$RPM_OPT_FLAGS $CXXFLAGS" ./configure --prefix=%{prefix}

if [ "$SMP" != "" ]; then
	make -j$SMP "MAKE=make -j$SMP"
else
	make
fi


%install

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-, root, root)

%doc README README.save_eps NEWS AUTHORS COPYING ChangeLog doc/data.ps

%{prefix}/bin/*
%{prefix}/share/gnome/apps/Graphics/superficie.desktop
%{prefix}/share/gnome/help/superficie
%{prefix}/share/pixmaps/*
%{prefix}/share/superficie
