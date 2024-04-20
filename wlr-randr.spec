Name:           wlr-randr
Version:        0.4.1
Release:        1
Summary:        Utility to manage outputs of a Wayland compositor
License:        MIT
Group:          Productivity/Graphics/Other
URL:            https://git.sr.ht/~emersion/wlr-randr/
Source0:        https://git.sr.ht/~emersion/wlr-randr/archive/v%{version}/%{name}-v%{version}.tar.gz
# Old source
#Source0:         https://github.com/emersion/wlr-randr/releases/download/v0.2.0/wlr-randr-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)

%description
wlr-randr is a command line utility to manage outputs of a Wayland compositor.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
