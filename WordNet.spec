Summary:	Online lexical reference system, ie. smart dictionary
Summary(pl.UTF-8):	System referencji słownikowych, czyli mądry słownik
Name:		WordNet
Version:	3.0
Release:	4
License:	Free to use (see COPYING)
Group:		Applications/Dictionaries
Source0:	http://wordnetcode.princeton.edu/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	89b4db7c6840ce69a8e315a3f83d996b
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-dictdir.patch
Patch3:		%{name}-build.patch
URL:		http://wordnet.princeton.edu/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WordNet is an online lexical reference system. Word forms in WordNet
are represented in their familiar orthography; word meanings are
represented by synonym sets (synset) - lists of synonymous word forms
that are interchangeable in some context. Two kinds of relations are
recognized: lexical and semantic. Lexical relations hold between word
forms; semantic relations hold between word meanings.

%description -l pl.UTF-8
WordNet to system referencji słownikowych. Formy słów w WordNet są
reprezentowane w ich pisowni; znaczenia słów są reprezentowane przez
zestawy synonimów (synset) - listy form synonimów, które są zamienne w
pewnym kontekście. Są rozpoznawane dwa rodzaje relacji: leksykalna i
semantyczna. Leksykalne zachodzą między formami słów; semantyczne
między ich znaczeniami.

%package devel
Summary:	Header files, library, and development documentation for WordNet
Summary(pl.UTF-8):	Pliki nagłówkowe, biblioteka i dokumentacja do WordNet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for WordNet.

%description devel -l pl.UTF-8
Pliki nagłówkowe, biblioteka i dokumentacja do WordNet.

%package static
Summary:	Static WordNet library
Summary(pl.UTF-8):	Statyczna biblioteka WordNet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WordNet library.

%description static -l pl.UTF-8
Statyczna biblioteka WordNet.

%package browser
Summary:	WordNet browser
Summary(pl.UTF-8):	Przeglądarka WordNet
Group:		Applications/Dictionaries
Requires:	%{name} = %{version}-%{release}

%description browser
A graphical interface to the WordNet online lexical database.

%description browser -l pl.UTF-8
Graficzny interfejs do sieciowej bazy danych słownika WordNet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-DUSE_INTERP_RESULT %{rpmcppflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/{html,ps,pdf}
# program not included
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/grind.1
# just a copy of tk headers
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/tk

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/wn
%attr(755,root,root) %{_libdir}/libWN.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWN.so.0
%{_mandir}/man1/wn.1*
%{_mandir}/man1/wnintro.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dict

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWN.so
%{_libdir}/libWN.la
%{_includedir}/wn.h
%{_mandir}/man3/binsrch.3*
%{_mandir}/man3/morph.3*
%{_mandir}/man3/wn*.3*
%{_mandir}/man5/cntlist.5*
%{_mandir}/man5/lexnames.5*
%{_mandir}/man5/senseidx.5*
%{_mandir}/man5/wn*.5*
%{_mandir}/man7/morphy.7*
%{_mandir}/man7/uniqbeg.7*
%{_mandir}/man7/wn*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libWN.a

%files browser
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wishwn
%attr(755,root,root) %{_bindir}/wnb
%{_datadir}/%{name}/wnres
%{_mandir}/man1/wnb.1*
