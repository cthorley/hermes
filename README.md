hermes
======

`hermes` is a source-based package manager for Linux, written in Python.  It was inspired by Source Mage's [Sorcery][1], [GNU Stow][2], [Encap/epkg][3], and [Cheflex][4].  It aims to be flexible, secure by default, and to maintain accessibility by adhereing to the [Unix philosophy][5].

Usage:
------
    > hermes -h
    Usage:  hermes install [-dsvV] <pkg>...
            hermes -h | --help
            hermes --version

    Options:
        -d, --depends           Require dependency installation
        -h, --help              Display usage and options
        -s, --check-sigs        Verify package GPG signatures
        -v, --verify            Verify package checksums
        -V, --verbose           Display debugging messages
        --version               Display version number

Roadmap:
--------
At the moment, hermes is little more than a CLI (courtesy of the excellent [docopt][6] library) and the skeleton of a dependency-resolution strategy.  The current priority is teaching him how to retrieve resources via http, and to (actually) install packages on an arbitrary system.

Package removal is the obvious successor to package installation.  Once these two core pieces of functionality are stable, I want to expand Hermes to support a repository architecture.  [Homebrew][7]-style git integration is another desired enhancement with non-trivial overlap, depending on implementation, so the two may end up being addressed simultaneously.

[1]: http://wiki.sourcemage.org/Sorcery.html
[2]: http://www.gnu.org/software/stow
[3]: http://www.encap.org
[4]: http://www.selflex.org/cheflex
[5]: http://en.wikipedia.org/wiki/Unix_philosophy
[6]: http://www.docopt.orgi
[7]: http://brew.sh
