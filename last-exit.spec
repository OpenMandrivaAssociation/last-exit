%define name last-exit
%define version 4
%define release %mkrel 1

Summary: Last.fm web radio player
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.o-hand.com/~iain/last-exit/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://www.o-hand.com/~iain/last-exit/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gnome-sharp2 mono-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libGConf2-devel
BuildRequires: gtk+2-devel
BuildRequires: perl-XML-Parser
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
Requires: mono

%description
This is a radio player program for last.fm with a GNOME user interface.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Audio;Player" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
rm -f %buildroot%_libdir/%name/*a

%post
%update_icon_cache hicolor
%define schemas last-exit lastfm
%post_install_gconf_schemas %schemas

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS
%_bindir/%name
%_datadir/applications/%name.desktop
%_libdir/%name
%_datadir/icons/hicolor/*/apps/*
%_datadir/icons/hicolor/*/actions/*
%_sysconfdir/gconf/schemas/last-exit.schemas
%_sysconfdir/gconf/schemas/lastfm.schemas


