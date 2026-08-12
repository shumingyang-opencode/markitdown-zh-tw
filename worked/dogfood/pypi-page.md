[Skip to main content](#content)
Switch to mobile version

Warning
Some features may not work without JavaScript. Please try enabling it if you encounter problems.

[![PyPI](/static/images/logo-small.0e0855d0.svg)](/)

Search PyPI

Search

* [Help](/help/)
* [Docs](https://docs.pypi.org/)
* [Sponsors](/sponsors/)
* [Log in](/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Fmarkitdown%2F)
* [Register](/account/register/)

Menu

* [Help](/help/)
* [Docs](https://docs.pypi.org/)
* [Sponsors](/sponsors/)
* [Log in](/account/login/?next=https%3A%2F%2Fpypi.org%2Fproject%2Fmarkitdown%2F)
* [Register](/account/register/)

Search PyPI

Search

# markitdown 0.1.7

Utility tool for converting various files to Markdown

pip install markitdown

Copy PIP instructions

* [Description](#description)
* [Download files](#files)
* [Release history](#history)

# MarkItDown

> [!TIP]
> MarkItDown is a Python package and command-line utility for converting various files to Markdown (e.g., for indexing, text analysis, etc).
>
> For more information, and full documentation, see the project [README.md](https://github.com/microsoft/markitdown) on GitHub.

> [!IMPORTANT]
> MarkItDown performs I/O with the privileges of the current process. Like open() or requests.get(), it will access resources that the process itself can access. Sanitize your inputs in untrusted environments, and call the narrowest `convert_*` function needed for your use case (e.g., `convert_stream()`, or `convert_local()`). See the [Security Considerations](https://github.com/microsoft/markitdown#security-considerations) section of the documentation for more information.

## Installation

From PyPI:

```
pip install 'markitdown[all]'
```

From source:

```
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

## Usage

### Command-Line

```
markitdown path-to-file.pdf > document.md
```

### Python API

```
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("test.xlsx")
print(result.text_content)
```

### More Information

For more information, and full documentation, see the project [README.md](https://github.com/microsoft/markitdown) on GitHub.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## Project links

* [Documentation](https://github.com/microsoft/markitdown#readme)
* [Issues](https://github.com/microsoft/markitdown/issues)
* [Source](https://github.com/microsoft/markitdown)

## Key dates

PyPI data

Data sourced directly from PyPI's database.

* **Released:**
  Jul 29, 2026

Latest release

## 2 maintainers

PyPI data

Data sourced directly from PyPI's database.

[![Avatar for afourney from gravatar.com](https://pypi-camo.freetls.fastly.net/66ba019d13e71e9e4201ed338aa195b0c397fa01/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f33326431356631643830353161316537356437666366656430346562623931323f73697a653d3335 "Avatar for afourney from gravatar.com")
afourney](/user/afourney/)
[![Avatar for bansalg from gravatar.com](https://pypi-camo.freetls.fastly.net/4465dd173368ab0c5105491b32d18036ec43b8dc/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f66323134643134326166613138636332383234383466653335636632373366373f73697a653d3335 "Avatar for bansalg from gravatar.com")
bansalg](/user/bansalg/)

## Credits

**Author:**
Adam Fourney

## License expression

MIT

[View SPDX License List](https://spdx.org/licenses/)

## Requires

**Python** >=3.10

## Provides Extra

`all`
`audio-transcription`
`az-content-understanding`
`az-doc-intel`
`docx`
`outlook`
`pdf`
`pptx`
`xls`
`xlsx`
`youtube-transcription`

## Classifiers

* Development Status
  + [4 - Beta](/search/?c=Development+Status+%3A%3A+4+-+Beta)
* Programming Language
  + [Python](/search/?c=Programming+Language+%3A%3A+Python)
  + [Python :: 3.10](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.10)
  + [Python :: 3.11](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.11)
  + [Python :: 3.12](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.12)
  + [Python :: 3.13](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+3.13)
  + [Python :: Implementation :: CPython](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+CPython)
  + [Python :: Implementation :: PyPy](/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+PyPy)

[Report project as malware](https://pypi.org/project/markitdown/submit-malware-report/)

## Download files

Download the file for your platform. If you're not sure which to choose, learn more about [installing packages](https://packaging.python.org/tutorials/installing-packages/ "External link").

### Source Distribution

[markitdown-0.1.7.tar.gz](https://files.pythonhosted.org/packages/59/93/e8a4af0c47551beb6383e226e840cbc811a577b8096eb385251b3fcc8f62/markitdown-0.1.7.tar.gz)
(51.8 kB
[view details](#markitdown-0.1.7.tar.gz))

Uploaded
Jul 29, 2026
`Source`

### Built Distribution

Filter files by name, interpreter, ABI, and platform.

If you're not sure about the file name format, learn more about [wheel file names](https://packaging.python.org/en/latest/specifications/binary-distribution-format/ "External link").

The dropdown lists show the available interpreters, ABIs, and platforms.

Enable javascript to be able to filter the list of wheel files.

Copy a direct link to the current filters

Copy

File name

Interpreter

Interpreter
py3

ABI

ABI
none

Platform

Platform
any

[markitdown-0.1.7-py3-none-any.whl](https://files.pythonhosted.org/packages/fc/16/51d269a754d690ec31d3faa0686c8c14ac955dbc0580c358f256ba3391ec/markitdown-0.1.7-py3-none-any.whl)
(71.1 kB
[view details](#markitdown-0.1.7-py3-none-any.whl))

Uploaded
Jul 29, 2026
`Python 3`

## File details

Details for the file `markitdown-0.1.7.tar.gz`.

### File metadata

* Download URL: [markitdown-0.1.7.tar.gz](https://files.pythonhosted.org/packages/59/93/e8a4af0c47551beb6383e226e840cbc811a577b8096eb385251b3fcc8f62/markitdown-0.1.7.tar.gz)
* Upload date:
  Jul 29, 2026
* Size: 51.8 kB
* Tags: Source
* Uploaded using Trusted Publishing? No
* Uploaded via: Hatch/1.16.2 cpython/3.12.3 HTTPX/0.28.1

### File hashes

Hashes for markitdown-0.1.7.tar.gz

| Algorithm | Hash digest |  |
| --- | --- | --- |
| SHA256 | `4d1f3c69cd43b82288fdc3653686d759dcf355ee7c681aa6a855aed98a1e4f44` | Copy |
| MD5 | `1d9de78a3377505d188f01fca3f7bc97` | Copy |
| BLAKE2b-256 | `5993e8a4af0c47551beb6383e226e840cbc811a577b8096eb385251b3fcc8f62` | Copy |

[See more details on using hashes here.](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")

## File details

Details for the file `markitdown-0.1.7-py3-none-any.whl`.

### File metadata

* Download URL: [markitdown-0.1.7-py3-none-any.whl](https://files.pythonhosted.org/packages/fc/16/51d269a754d690ec31d3faa0686c8c14ac955dbc0580c358f256ba3391ec/markitdown-0.1.7-py3-none-any.whl)
* Upload date:
  Jul 29, 2026
* Size: 71.1 kB
* Tags: Python 3
* Uploaded using Trusted Publishing? No
* Uploaded via: Hatch/1.16.2 cpython/3.12.3 HTTPX/0.28.1

### File hashes

Hashes for markitdown-0.1.7-py3-none-any.whl

| Algorithm | Hash digest |  |
| --- | --- | --- |
| SHA256 | `4eca912c87c6aa6897284a7f4bf6769a23bccf8544530f5d8b175fbe3797c916` | Copy |
| MD5 | `f9c8503217562fbfbddd478d6caf5b6d` | Copy |
| BLAKE2b-256 | `fc1651d269a754d690ec31d3faa0686c8c14ac955dbc0580c358f256ba3391ec` | Copy |

[See more details on using hashes here.](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode "External link")

## Release history [Release notifications](/help/#project-release-notifications) | [RSS feed](/rss/project/markitdown/releases.xml)

This release

![](https://pypi.org/static/images/blue-cube.572a5bfb.svg)

[0.1.7

Jul 29, 2026](/project/markitdown/0.1.7/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.6

May 26, 2026](/project/markitdown/0.1.6/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.5

Feb 20, 2026](/project/markitdown/0.1.5/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.5b1
pre-release

Jan 8, 2026](/project/markitdown/0.1.5b1/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.4

Dec 1, 2025](/project/markitdown/0.1.4/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.3

Aug 26, 2025](/project/markitdown/0.1.3/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.2

May 28, 2025](/project/markitdown/0.1.2/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.2a1
pre-release

May 21, 2025](/project/markitdown/0.1.2a1/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.1

Mar 25, 2025](/project/markitdown/0.1.1/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0

Mar 22, 2025](/project/markitdown/0.1.0/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a6
pre-release

Mar 21, 2025](/project/markitdown/0.1.0a6/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a5
pre-release

Mar 20, 2025](/project/markitdown/0.1.0a5/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a4
pre-release

Mar 17, 2025](/project/markitdown/0.1.0a4/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a3
pre-release

Mar 13, 2025](/project/markitdown/0.1.0a3/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a2
pre-release

Mar 12, 2025](/project/markitdown/0.1.0a2/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.1.0a1
pre-release

Mar 6, 2025](/project/markitdown/0.1.0a1/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.2

Mar 8, 2025](/project/markitdown/0.0.2/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1

Mar 6, 2025](/project/markitdown/0.0.1/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1a5
pre-release

Feb 28, 2025](/project/markitdown/0.0.1a5/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1a4
pre-release

Feb 11, 2025](/project/markitdown/0.0.1a4/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1a3
pre-release

Dec 17, 2024](/project/markitdown/0.0.1a3/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1a2
pre-release

Dec 2, 2024](/project/markitdown/0.0.1a2/)

![](https://pypi.org/static/images/white-cube.2351a86c.svg)

[0.0.1a1
pre-release

Nov 13, 2024](/project/markitdown/0.0.1a1/)

![](/static/images/white-cube.2351a86c.svg)

## Help

* [Installing packages](https://packaging.python.org/tutorials/installing-packages/ "External link")
* [Uploading packages](https://packaging.python.org/tutorials/packaging-projects/ "External link")
* [User guide](https://packaging.python.org/ "External link")
* [Project name retention](https://www.python.org/dev/peps/pep-0541/ "External link")
* [FAQs](/help/)

## About PyPI

* [PyPI Blog](https://blog.pypi.org "External link")
* [Infrastructure dashboard](https://dtdg.co/pypi "External link")
* [Statistics](/stats/)
* [Logos & trademarks](/trademarks/)
* [Our sponsors](/sponsors/)

## Contributing to PyPI

* [Bugs and feedback](/help/#feedback)
* [Contribute on GitHub](https://github.com/pypi/warehouse "External link")
* [Translate PyPI](https://hosted.weblate.org/projects/pypa/warehouse/ "External link")
* [Sponsor PyPI](/sponsors/)
* [Development credits](https://github.com/pypi/warehouse/graphs/contributors "External link")

## Using PyPI

* [Terms of Service](https://policies.python.org/pypi.org/Terms-of-Service/ "External link")
* [Report security issue](/security/)
* [Code of conduct](https://policies.python.org/python.org/code-of-conduct/ "External link")
* [Privacy Notice](https://policies.python.org/pypi.org/Privacy-Notice/ "External link")
* [Acceptable Use Policy](https://policies.python.org/pypi.org/Acceptable-Use-Policy/ "External link")

---

Status:[all systems operational](https://status.python.org/ "External link")

Developed and maintained by the Python community, for the Python community.
[Donate today!](https://donate.pypi.org)

"PyPI", "Python Package Index", and the blocks logos are registered [trademarks](/trademarks/) of the [Python Software Foundation](https://www.python.org/psf-landing).

© 2026 [Python Software Foundation](https://www.python.org/psf-landing/ "External link")

[Site map](/sitemap/)

Deployed from [`f10462c`](https://github.com/pypi/warehouse/commit/f10462c23b30f9ce4c336f8df217412d91716553 "External link")

Switch to desktop version

* English
* español
* français
* 日本語
* português (Brasil)
* українська
* Ελληνικά
* Deutsch
* 中文 (简体)
* 中文 (繁體)
* русский
* עברית
* Esperanto
* 한국어

Supported by

[![](https://pypi-camo.freetls.fastly.net/ed7074cadad1a06f56bc520ad9bd3e00d0704c5b/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6177732d77686974652d6c6f676f2d7443615473387a432e706e67)
AWS

Cloud computing and Security Sponsor](https://aws.amazon.com/)
[![](https://pypi-camo.freetls.fastly.net/8855f7c063a3bdb5b0ce8d91bfc50cf851cc5c51/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f64617461646f672d77686974652d6c6f676f2d6668644c4e666c6f2e706e67)
Datadog

Monitoring](https://www.datadoghq.com/)
[![](https://pypi-camo.freetls.fastly.net/60f709d24f3e4d469f9adc77c65e2f5291a3d165/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f6465706f742d77686974652d6c6f676f2d7038506f476831302e706e67)
Depot

Continuous Integration](https://depot.dev)
[![](https://pypi-camo.freetls.fastly.net/df6fe8829cbff2d7f668d98571df1fd011f36192/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f666173746c792d77686974652d6c6f676f2d65684d3077735f6f2e706e67)
Fastly

CDN](https://www.fastly.com/)
[![](https://pypi-camo.freetls.fastly.net/420cc8cf360bac879e24c923b2f50ba7d1314fb0/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f676f6f676c652d77686974652d6c6f676f2d616734424e3774332e706e67)
Google

Download Analytics](https://careers.google.com/)
[![](https://pypi-camo.freetls.fastly.net/d01053c02f3a626b73ffcb06b96367fdbbf9e230/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f70696e67646f6d2d77686974652d6c6f676f2d67355831547546362e706e67)
Pingdom

Monitoring](https://www.pingdom.com/)
[![](https://pypi-camo.freetls.fastly.net/67af7117035e2345bacb5a82e9aa8b5b3e70701d/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f73656e7472792d77686974652d6c6f676f2d4a2d6b64742d706e2e706e67)
Sentry

Error logging](https://sentry.io/for/python/?utm_source=pypi&utm_medium=paid-community&utm_campaign=python-na-evergreen&utm_content=static-ad-pypi-sponsor-learnmore)
[![](https://pypi-camo.freetls.fastly.net/b611884ff90435a0575dbab7d9b0d3e60f136466/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f707970692d6173736574732f73706f6e736f726c6f676f732f737461747573706167652d77686974652d6c6f676f2d5467476c6a4a2d502e706e67)
StatusPage

Status page](https://statuspage.io)