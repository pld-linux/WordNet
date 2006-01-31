Summary:	Online lexical reference system, ie. smart dictionary
Summary(pl):	System referencji s³ownikowych, czyli m±dry s³ownik
Name:		WordNet
Version:	2.1
Release:	0.11
License:	Free to use (see COPYING)
Group:		Applications/Dictionaries
Source0:	ftp://ftp.cogsci.princeton.edu/pub/wordnet/2.1/%{name}-%{version}.tar.gz
# Source0-md5:	081aa25baaccac602cebb61f6cb949e7
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-typo.patch
URL:		http://wordnet.princeton.edu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WordNet is an online lexical reference system. Word forms in WordNet
are represented in their familiar orthography; word meanings are
represented by synonym sets (synset) - lists of synonymous word forms
that are interchangeable in some context. Two kinds of relations are
recognized: lexical and semantic. Lexical relations hold between word
forms; semantic relations hold between word meanings.

Information about WordNet, an online interface, and the various
WordNet packages are available from our Web site at
<%URL>.

%description -l pl
WordNet to system referencji s³ownikowych. Formy s³ów w WordNet s±
reprezentowane w ich pisowni; znaczenia s³ów s± reprezentowane przez
zestawy synonimów (synset) - listy form synonimów, które s± zamienne w
pewnym kontek¶cie. S± rozpoznawane dwa rodzaje relacji: leksykalna i
semantyczna. Leksykalne zachodz± miêdzy formami s³ów; semantyczne
miêdzy ich znaczeniami.

%package devel
Summary:	Header files, library, and development documentation for WordNet
Summary(pl):	Pliki nag³ówkowe, biblioteka i dokumentacja do WordNet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for WordNet.

%description devel -l pl
Pliki nag³ówkowe, biblioteka i dokumentacja do WordNet.

%package static
Summary:	Static WordNet library
Summary(pl):	Statyczna biblioteka WordNet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WordNet library.

%description static -l pl
Statyczna biblioteka WordNet.

%package browser
Summary:	WordNet browser
Summary(pl):	Przegl±darka WordNet
Group:		Applications/Dictionaries
Requires:	%{name} = %{version}-%{release}

%description browser
A graphical interface to the WordNet online lexical database.

%description browser -l pl
Graficzny interfejs do sieciowej bazy danych s³ownika WordNet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dunno. anyone needs this?
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/{html,ps,pdf}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/wn
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_mandir}/man1/wn.1*
%{_mandir}/man1/wnintro.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dict

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
# funny. manual is there but no such program. rm -f it?
%{_mandir}/man1/grind.1*
%{_mandir}/man[357]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files browser
%defattr(644,root,root,755)
%{_datadir}/%{name}/wnres
# anyone? is this prog needed?
%attr(755,root,root) %{_bindir}/wishwn
%attr(755,root,root) %{_bindir}/wnb
%{_mandir}/man1/wnb.1*
