#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : NetworkManager-openconnect
Version  : 1.2.4
Release  : 1
URL      : http://ftp.gnome.org/pub/gnome/sources/NetworkManager-openconnect/1.2/NetworkManager-openconnect-1.2.4.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/NetworkManager-openconnect/1.2/NetworkManager-openconnect-1.2.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: NetworkManager-openconnect-lib
Requires: NetworkManager-openconnect-bin
Requires: NetworkManager-openconnect-data
Requires: NetworkManager-openconnect-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(NetworkManager)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openconnect)

%description
The files in the "shared/" directory are used by all components
inside the VPN plugin repository (src, properties, auth-dialog).

%package bin
Summary: bin components for the NetworkManager-openconnect package.
Group: Binaries
Requires: NetworkManager-openconnect-data

%description bin
bin components for the NetworkManager-openconnect package.


%package data
Summary: data components for the NetworkManager-openconnect package.
Group: Data

%description data
data components for the NetworkManager-openconnect package.


%package lib
Summary: lib components for the NetworkManager-openconnect package.
Group: Libraries
Requires: NetworkManager-openconnect-data

%description lib
lib components for the NetworkManager-openconnect package.


%package locales
Summary: locales components for the NetworkManager-openconnect package.
Group: Default

%description locales
locales components for the NetworkManager-openconnect package.


%prep
%setup -q -n NetworkManager-openconnect-1.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493823849
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493823849
rm -rf %{buildroot}
%make_install
%find_lang NetworkManager-openconnect

%files
%defattr(-,root,root,-)
/usr/lib/NetworkManager/VPN/nm-openconnect-service.name

%files bin
%defattr(-,root,root,-)
/usr/libexec/nm-openconnect-auth-dialog
/usr/libexec/nm-openconnect-service
/usr/libexec/nm-openconnect-service-openconnect-helper

%files data
%defattr(-,root,root,-)
/usr/share/appdata/network-manager-openconnect.metainfo.xml
/usr/share/gnome-vpn-properties/openconnect/nm-openconnect-dialog.ui

%files lib
%defattr(-,root,root,-)
/usr/lib64/NetworkManager/libnm-openconnect-properties.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-openconnect.so

%files locales -f NetworkManager-openconnect.lang
%defattr(-,root,root,-)

