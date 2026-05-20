Summary:	LDoc - a Lua documentation tool
Summary(pl.UTF-8):	LDoc - narzędzie do dokumentowania kodu źródłowego Lua
Name:		ldoc
Version:	1.5.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://github.com/lunarmodules/LDoc/archive/v%{version}/LDoc-%{version}.tar.gz
# Source0-md5:	9aed933dae505d5831be81f1735a342a
URL:		https://lunarmodules.github.io/ldoc/
Requires:	lua-penlight
Requires:	lua51
Requires:	lua51-filesystem
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDoc is a LuaDoc-compatible documentation generator which can also
process C extension source. Markdown may be optionally used to render
comments, as well as integrated readme documentation and
pretty-printed example files.

%description -l pl.UTF-8
LDoc to kompatybilny z LuaDoc generator dokumentacji, który potrafi
także przetwarzać kod rozszerzeń C. Komentarze mogą być opcjonalnie
renderowane przy użyciu Markdowna, podobnie jak dołączona dokumentacja
README i podświetlone pliki przykładowe.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LUA_BINDIR=%{_bindir} \
	LUA_SHAREDIR=%{_datadir}/lua/5.1

%{__sed} -i -e 's,^lua ,lua5.1 ,' $RPM_BUILD_ROOT%{_bindir}/ldoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md COPYRIGHT manual.md
%attr(755,root,root) %{_bindir}/ldoc
%{_datadir}/lua/5.1/ldoc.lua
%dir %{_datadir}/lua/5.1/ldoc
%{_datadir}/lua/5.1/ldoc/*.lua
%{_datadir}/lua/5.1/ldoc/SciTE.properties
%{_datadir}/lua/5.1/ldoc/config.ld
%dir %{_datadir}/lua/5.1/ldoc/builtin
%{_datadir}/lua/5.1/ldoc/builtin/*.lua
%dir %{_datadir}/lua/5.1/ldoc/html
%{_datadir}/lua/5.1/ldoc/html/*.lua
