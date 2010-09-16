Name: gnome-gmail
Version: 1.7.0
Release: 1
Group: Applications/Communications
Vendor: David Steele
URL: http://sourceforge.net/projects/%{name}
License: GPLv2
Summary: Make Gmail an option for the default Gnome mail handler
Source: %{name}-%{version}.tgz
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: control-center
Requires: python >= 2.6
Requires: pygobject2
Requires: gconf-editor

%description
This package makes Gmail a choice in the Gnome control panel for the default
mail handler. It opens in the default web browser.

%prep
%setup -q

%build

%install
rm -Rf %{buildroot}
make prefix=%{buildroot} install

%clean
rm -Rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule /etc/gconf/schemas/gnome-gmail.schemas > /dev/null



%files
%doc README COPYING
%attr( 0755, root, root) /usr/bin/gnome-gmail
%attr( 0644, root, root) /usr/share/gnome-control-center/default-apps/gnome-gmail.xml
%attr( 0644, root, root) /usr/lib/gnome-gmail/gnomegmail.glade
%attr( 0755, root, root) /usr/share/icons/hicolor/16x16/apps/gmail.png
%attr( 0755, root, root) /usr/share/icons/hicolor/24x24/apps/gmail.png
%attr( 0755, root, root) /usr/share/icons/hicolor/32x32/apps/gmail.png
%attr( 0755, root, root) /usr/share/icons/hicolor/48x48/apps/gmail.png
%attr( 0644, root, root) /etc/gconf/schemas/gnome-gmail.schemas
%attr( 0644, root, root) /usr/share/applications/gnome-gmail.desktop
%attr( 0755, root, root) /usr/lib/gnome-gmail/evolution
%attr( 0755, root, root) /usr/bin/setOOmailer
%attr( 0644, root, root) /usr/share/gnome/autostart/setOOmailer.desktop


%changelog
* Sun Jan 17 2010 Dave Steele <daves@users.sourceforge.net> - 1.4-1
- Support for Nautilus - Send files via GMail
- Added mailto test cases - improved mailto handling

* Wed Nov 04 2009 Dave Steele <daves@users.sourceforge.net> - 1.3-1
- Web page updated with resources for mailto: test and Send Link bookmarklet
- Fixes to broken 1.2 RPM install
- Better mailto: argument handling
- Fixed to launch web browser instead of "HTML handler"

* Wed Sep 09 2009 Dave Steele <daves@users.sourceforge.net> - 1.2-1
- Better gmail URL

* Mon Sep 07 2009 Dave Steele <daves@users.sourceforge.net> - 1.1-1
- initial package release

