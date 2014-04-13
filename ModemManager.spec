Summary:	Mobile broadband modem management service
Name:		ModemManager
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://www.freedesktop.org/software/ModemManager/%{name}-%{version}.tar.xz
# Source0-md5:	6e70ab7c5f96aa6a4d5612c1d5ae5bb3
URL:		http://www.freedesktop.org/wiki/Software/ModemManager
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libmbim-devel
BuildRequires:	libqmi-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
BuildRequires:	ppp-devel
BuildRequires:	udev-glib-devel
Requires(post,preun,postun):	systemd-units
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
Requires:	polkit
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ModemManager service provides a consistent API to operate many
different modems, including mobile broadband (3G) devices.

%package libs
Summary:	Library to control and monitor the ModemManager
Group:		Libraries

%description libs
This package provides library to control and monitor the ModemManager.

%package devel
Summary:	Header file defining ModemManager D-Bus interface
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header file defining ModemManager D-Bus interface.

%package apidocs
Summary:	API documentation for ModemManager
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for ModemManager.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-polkit			\
	--with-udev-base-dir=%{_prefix}/lib/udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,*/}*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%systemd_service_enable ModemManager.service

%preun
%systemd_preun ModemManager.service

%postun
%update_icon_cache hicolor
%systemd_reload

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mmcli
%attr(755,root,root) %{_sbindir}/ModemManager
%dir %{_libdir}/ModemManager
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-altair-lte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-anydata.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-cinterion.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-generic.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-gobi.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-hso.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-huawei.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-iridium.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-linktop.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-longcheer.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-mbm.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-mtk.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-motorola.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia-icera.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-nokia.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel-lte.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-novatel.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-option.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-pantech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-samsung.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-sierra.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-simtech.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-telit.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-via.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-wavecom.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-x22x.so
%attr(755,root,root) %{_libdir}/%{name}/libmm-plugin-zte.so
%{_prefix}/lib/udev/rules.d/77-mm-ericsson-mbm.rules
%{_prefix}/lib/udev/rules.d/77-mm-huawei-net-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-longcheer-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-mtk-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-nokia-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-pcmcia-device-blacklist.rules
%{_prefix}/lib/udev/rules.d/77-mm-platform-serial-whitelist.rules
%{_prefix}/lib/udev/rules.d/77-mm-simtech-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-telit-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-usb-device-blacklist.rules
%{_prefix}/lib/udev/rules.d/77-mm-usb-serial-adapters-greylist.rules
%{_prefix}/lib/udev/rules.d/77-mm-x22x-port-types.rules
%{_prefix}/lib/udev/rules.d/77-mm-zte-port-types.rules
%{_prefix}/lib/udev/rules.d/80-mm-candidate.rules
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.freedesktop.ModemManager1.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Bearer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Firmware.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Location.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Messaging.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.ModemCdma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Oma.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Simple.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Signal.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Time.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sim.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.Sms.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ModemManager1.xml
%{_datadir}/dbus-1/interfaces/wip-org.freedesktop.ModemManager1.Modem.Contacts.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.ModemManager1.service
%{_datadir}/polkit-1/actions/org.freedesktop.ModemManager1.policy
%{_iconsdir}/hicolor/*/apps/*.png
%{_mandir}/man8/ModemManager.8*
%{_mandir}/man8/mmcli.8*
%{systemdunitdir}/ModemManager.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmm-glib.so.0
%attr(755,root,root) %{_libdir}/libmm-glib.so.*.*.*
%{_libdir}/girepository-1.0/ModemManager-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmm-glib.so
%{_includedir}/ModemManager
%{_includedir}/libmm-glib
%{_pkgconfigdir}/ModemManager.pc
%{_pkgconfigdir}/mm-glib.pc
%{_datadir}/gir-1.0/ModemManager-1.0.gir
%{_datadir}/vala/vapi/libmm-glib.deps
%{_datadir}/vala/vapi/libmm-glib.vapi

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ModemManager
%{_gtkdocdir}/libmm-glib
%endif

