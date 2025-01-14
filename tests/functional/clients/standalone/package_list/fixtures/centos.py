pkgfiles_all = {
    "/usr/bin/db_hotbackup": "RPMFILE",
    "/usr/lib64/python3.6/email/_encoded_words.py": "RPMFILE",
    "/usr/lib64/python3.6/urllib/response.py": "RPMFILE",
    "/etc/profile.d/gawk.csh": "RPMFILE",
    "/usr/bin/chacl": "RPMFILE",
    "/usr/bin/find": "RPMFILE",
    "/usr/lib64/gconv/ISO8859-3.so": "RPMFILE",
    "/bin": "RPMFILE",
    "/etc/libaudit.conf": "RPMFILE",
}

pkgs_all = {
    "pam": "1.3.1-8.el8",
    "crontabs": "1.11-16.20150630git.el8",
    "rpm": "4.14.2-37.el8",
    "libseccomp": "2.4.1-1.el8",
    "zlib": "1.2.11-13.el8",
    "libfdisk": "2.32.1-22.el8",
    "libnghttp2": "1.33.0-3.el8_2.1",
    "audit-libs": "3.0-0.17.20191104git1c2f876.el8",
    "gmp": "1:6.1.2-10.el8",
    "libdb": "5.3.28-37.el8",
}

pkgs_allinfo = {
    "libmnl": {
        "version": "1.0.4",
        "release": "6.el8",
        "arch": "x86_64",
        "size": "53687",
        "license": "LGPLv2+",
        "sourcepkg": "libmnl-1.0.4-6.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libmnl:libmnl:1.0.4-6.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libmnl:1.0.4-6.el8:*:*:*:*:*:*:*",
        ],
    },
    "libdb": {
        "version": "5.3.28",
        "release": "37.el8",
        "arch": "x86_64",
        "size": "2515048",
        "license": "BSD and LGPLv2 and Sleepycat",
        "sourcepkg": "libdb-5.3.28-37.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libdb:libdb:5.3.28-37.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libdb:5.3.28-37.el8:*:*:*:*:*:*:*",
        ],
    },
    "libseccomp": {
        "version": "2.4.1",
        "release": "1.el8",
        "arch": "x86_64",
        "size": "402960",
        "license": "LGPLv2",
        "sourcepkg": "libseccomp-2.4.1-1.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libseccomp:libseccomp:2.4.1-1.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libseccomp:2.4.1-1.el8:*:*:*:*:*:*:*",
        ],
    },
    "libsepol": {
        "version": "2.9",
        "release": "1.el8",
        "arch": "x86_64",
        "size": "996264",
        "license": "LGPLv2+",
        "sourcepkg": "libsepol-2.9-1.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libsepol:libsepol:2.9-1.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libsepol:2.9-1.el8:*:*:*:*:*:*:*",
        ],
    },
    "libunistring": {
        "version": "0.9.9",
        "release": "3.el8",
        "arch": "x86_64",
        "size": "1855932",
        "license": "GPLv2+ or LGPLv3+",
        "sourcepkg": "libunistring-0.9.9-3.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libunistring:libunistring:0.9.9-3.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libunistring:0.9.9-3.el8:*:*:*:*:*:*:*",
        ],
    },
    "libkcapi": {
        "version": "1.1.1",
        "release": "16_1.el8",
        "arch": "x86_64",
        "size": "82828",
        "license": "BSD or GPLv2",
        "sourcepkg": "libkcapi-1.1.1-16_1.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libkcapi:libkcapi:1.1.1-16_1.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libkcapi:1.1.1-16_1.el8:*:*:*:*:*:*:*",
        ],
    },
    "tzdata": {
        "version": "2020a",
        "release": "1.el8",
        "arch": "noarch",
        "size": "1904256",
        "license": "Public Domain",
        "sourcepkg": "tzdata-2020a-1.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:tzdata:tzdata:2020a-1.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:tzdata:2020a-1.el8:*:*:*:*:*:*:*",
        ],
    },
    "cracklib": {
        "version": "2.9.6",
        "release": "15.el8",
        "arch": "x86_64",
        "size": "239047",
        "license": "LGPLv2+",
        "sourcepkg": "cracklib-2.9.6-15.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:cracklib:cracklib:2.9.6-15.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:cracklib:2.9.6-15.el8:*:*:*:*:*:*:*",
        ],
    },
    "bash": {
        "version": "4.4.19",
        "release": "10.el8",
        "arch": "x86_64",
        "size": "6930068",
        "license": "GPLv3+",
        "sourcepkg": "bash-4.4.19-10.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:bash:bash:4.4.19-10.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:bash:4.4.19-10.el8:*:*:*:*:*:*:*",
        ],
    },
    "libnsl2": {
        "version": "1.2.0",
        "release": "2.20180605git4a062cf.el8",
        "arch": "x86_64",
        "size": "147122",
        "license": "BSD and LGPLv2+",
        "sourcepkg": "libnsl2-1.2.0-2.20180605git4a062cf.el8.src.rpm",
        "origin": "CentOS",
        "type": "rpm",
        "cpes": [
            "cpe:2.3:a:libnsl2:libnsl2:1.2.0-2.20180605git4a062cf.el8:*:*:*:*:*:*:*",
            "cpe:2.3:a:*:libnsl2:1.2.0-2.20180605git4a062cf.el8:*:*:*:*:*:*:*",
        ],
    },
}
