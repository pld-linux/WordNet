Summary:	Online lexical reference system, ie. smart dictionary
Summary(pl):	System referencji s³ownikowych, czyli m±dry s³ownik
Name:		WordNet
Version:	1.7.1
Release:	1
License:	Free to use (see LICENSE)
Group:		Applications/Dictionaries
Source0:	ftp://ftp.cogsci.princeton.edu/pub/wordnet/%{version}/WordNet-%{version}.tar.gz
# Source0-md5:	5c8e569339cf7d8e727d884234365508
Patch0:		%{name}-includes.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cogsci.princeton.edu/~wn/
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
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
%URL

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
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for WordNet.

%description devel -l pl
Pliki nag³ówkowe, biblioteka i dokumentacja do WordNet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%define wnopts "PLATFORM=linux WN_ROOT=%{_prefix} %WN_DICT=%{_datadir}/%{name}"

ff=src/include/wnconsts.h
sed 's|/usr/local/%{name}-%{version}/dict|%{_datadir}/%{name}|' < $ff > $ff.fix
mv -f $ff.fix $ff

%{__make} %{wnopts} clean
%{__make} %{wnopts} -C src/lib
%{__make} %{wnopts} LOCAL_LDFLAGS=-dynamic -C src/wn
%{__make} %{wnopts} LOCAL_LDFLAGS=-dynamic -C src/wnb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_datadir}/%{name},%{_mandir}/man{1,3,5,7}}

install src/wn/wn $RPM_BUILD_ROOT%{_bindir}
install src/wnb/{wnb,wishwn} $RPM_BUILD_ROOT%{_bindir}

%{__make} -C dict WN_INSTALLDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} install
%{__make} -C man  WN_INSTALLDIR=$RPM_BUILD_ROOT%{_mandir} install

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/wnb*

install src/lib/libwn.{a,so} $RPM_BUILD_ROOT%{_libdir}
install src/include/wn*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/*.so
%{_mandir}/man1/*
%doc CHANGES INSTALL LICENSE README.doc README.list README.tcltk UNBUNDLE

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man[357]/*
