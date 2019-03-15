Name: swayidle	
Version:	1.2
Release:	1%{?dist}
Summary:	An idle daemon for wayland compositors

License:	MIT
URL:		https://github.com/swaywm/swayidle
Source:	    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson >= 0.48.0
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
swayidle is an idle management daemon for Wayland compositors

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/swayidle.fish
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Fri Mar 15 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-1
- Initial packaging
