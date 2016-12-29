#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-jsch-agent-proxy
Version  : 0.0.8
Release  : 1
URL      : https://github.com/ymnk/jsch-agent-proxy/archive/0.0.8.tar.gz
Source0  : https://github.com/ymnk/jsch-agent-proxy/archive/0.0.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jdk-jsch-agent-proxy-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jna
BuildRequires : jdk-jsch
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-source-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-sonatype-oss-parent
BuildRequires : jdk-sshj
BuildRequires : jdk-surefire
BuildRequires : jdk-trilead-ssh2
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
jsch-agent-proxy -- a proxy to ssh-agent and Pageant in Java.
Description
===========
jsch-agent-proxy is a proxy program to OpenSSH's ssh-agent and Pageant
included Putty.  It will be easily integrated into JSch, and users
will be allowed to use those programs in authentications.
This software has been developed for JSch, but it will be easily
applicable to other ssh2 implementations in Java.
This software is licensed under BSD style license.

%package data
Summary: data components for the jdk-jsch-agent-proxy package.
Group: Data

%description data
data components for the jdk-jsch-agent-proxy package.


%prep
%setup -q -n jsch-agent-proxy-0.0.8

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n jsch-agent-proxy -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.connector-factory.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.core.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.jsch.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.pageant.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.sshagent.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.sshj.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.svnkit-trilead-ssh2.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.usocket-jna.jar
/usr/share/java/jsch-agent-proxy/jsch.agentproxy.usocket-nc.jar
/usr/share/maven-metadata/jsch-agent-proxy.xml
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.connector-factory.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.core.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.jsch.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.pageant.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.sshagent.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.sshj.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.svnkit-trilead-ssh2.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.usocket-jna.pom
/usr/share/maven-poms/jsch-agent-proxy/jsch.agentproxy.usocket-nc.pom
