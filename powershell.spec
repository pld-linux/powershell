Summary:	X11 Terminal Emulator
Summary(pl):	Emulator Terminala X11
Name:		powershell
Version:	0.8
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://powershell.pdq.net/download/%{name}-%{version}.tar.gz
URL:		http://rush.baked.net/~spong/powershell/
BuildRequires:	gnome-libs => 1.0.13
BuildRequires:	gtk+ >= 1.2.1
BuildRequires:	imlib-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
Terminal Emulater for the X11 Window System. Features:
- Full GNOME support.
- Support for many terminal windows in a single window, separated by
  "notebook" tabs.
- Menu options to open a new tab with various programs running,
  including bash, tcsh, pine, and emacs.
- Ability to change menu options through ~/.pshellrc as well as the
  Preferences dialog box.
- Ability to switch terms with Ctrl-1, Ctrl-2, etc...
- Support for transparency, pixmap backgrounds, etc...
- Full support for color.

%description -l pl
Emulator Terminala dla systemu X11 Window. Mo¿liwo¶ci:
- Pe³ne wsparcie dla GNOME
- Wsparcie dla wielu okien terminali w jednym oknie XWindow
- Opcje menu by otworzyæ programy typi bash, tcsh, pine, emacs.
- Mo¿liwo¶æ zmiany opcji menu poprzez plik konfiguracyjny jak i
  Ustawienia
- Mo¿liwo¶æ prze³±czania siê pomiêdzy terminalami z klawiatury z
  Ctrl-1, Ctrl-2
- Wsparcie dla prze¼roczysto¶ci, obrazków t³a itp
- Pe³ne wsparcie dla kolorów

%prep
%setup  -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}


%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS README
%attr(755,root,root) %{_bindir}/*
