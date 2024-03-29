Name: swayidle
Version: 1.2
Release: 3%{?dist}
Summary: An idle daemon for wayland compositors

License: MIT
URL: https://github.com/swaywm/swayidle
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson >= 0.48.0
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
swayidle is an idle management daemon for Wayland compositors.

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
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/fish/completions/swayidle.fish
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Mar 18 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-3
- Flip changelog
* Fri Mar 15 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-2
- Fix directory ownership
- Clean up spec file
* Fri Mar 15 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-1
- Initial packaging

