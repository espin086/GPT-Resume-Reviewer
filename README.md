# GPT-Resume-Reviewer

A Streamlit app for reviewing resumes with GPT. Right now the repository is an early
skeleton: the UI accepts a PDF or DOCX upload and prints a placeholder string back.
The GPT call is not written yet, so nothing is sent to OpenAI and no real analysis
happens. The scaffolding around it is in place: package layout, Makefile targets,
pytest and tox config, Sphinx docs, an `OPEN_AI_KEY` environment template, and a
console-script entry point.

Read the rest of this file as a description of what exists, not of a finished product.

## Status

| Piece | State |
| --- | --- |
| Streamlit upload UI (`app.py`) | works |
| Resume text processing / GPT review | placeholder, returns a fixed string |
| CLI (`cli.py`) | cookiecutter stub, prints its arguments |
| `gpt_resume_reviewer.py` | empty module, docstring only |
| Tests | one commented-out sample test |

## Features

- File upload widget that accepts `.pdf` and `.docx`.
- `process_resume(file)` hook where the review logic is meant to go.
- `make run` target that starts the Streamlit server.
- Packaging via `setup.py` with a `gpt_resume_reviewer` console script.
- Lint (flake8 + black), test (pytest), coverage, and docs targets in the Makefile.

## Requirements

- Python 3.6 or newer (`python_requires=">=3.6"` in `setup.py`).
- `streamlit==1.25.0` and `watchdog==3.0.0` (`requirements.txt`).
- Dev extras in `requirements_dev.txt`: pytest, black, flake8, tox, coverage, Sphinx, twine, bump2version.
- An OpenAI API key if you implement the GPT call. The environment template at the repo
  root defines one variable, `OPEN_AI_KEY`.

No code currently reads `OPEN_AI_KEY`. The template is there for when the review logic
lands.

## Installation

```bash
git clone https://github.com/espin086/GPT-Resume-Reviewer
cd GPT-Resume-Reviewer
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

For development work:

```bash
pip install -r requirements_dev.txt
```

To install the package itself:

```bash
make install     # runs python setup.py install
```

Copy the environment template to a local dotenv file if you plan to wire up the API key.

## Usage

Start the app:

```bash
make run
```

That expands to:

```bash
streamlit run gpt_resume_reviewer/app.py
```

Streamlit prints a local URL (default `http://localhost:8501`). Open it, upload a PDF
or Word file, and the page prints the placeholder text under "Processed Resume:".

The installed console script exists but does no work yet:

```bash
gpt_resume_reviewer            # prints "Arguments: []" and a TODO message
```

Other Makefile targets:

```bash
make help        # list every target with its description
make test        # pytest
make test-all    # tox across py36, py37, py38, flake8
make lint        # flake8 + black --check
make coverage    # coverage run + report + HTML, opens the report
make docs        # sphinx-apidoc + HTML build, opens the result
make clean       # remove build, pyc, test, and coverage artifacts
make dist        # sdist + bdist_wheel
make release     # twine upload dist/*
```

## Project structure

```
gpt_resume_reviewer/
  __init__.py                 package metadata (author, email, version)
  app.py                      Streamlit UI and the process_resume placeholder
  cli.py                      argparse console-script stub
  gpt_resume_reviewer.py      empty main module, reserved for the review logic
tests/
  test_gpt_resume_reviewer.py sample pytest fixture and test, body commented out
docs/                         Sphinx sources (index, installation, usage, contributing, history)
Makefile                      run, test, lint, coverage, docs, dist, release targets
requirements.txt              runtime pins (streamlit, watchdog)
requirements_dev.txt          tooling pins
setup.py                      packaging, entry point, long_description from README.rst
setup.cfg                     bumpversion, flake8, pytest config
tox.ini                       py36/py37/py38 + flake8 environments
LICENSE                       MIT
```

## How it works

One process. `app.py` calls `st.file_uploader` with `type=["pdf", "docx"]`, and when a
file is present it passes the uploaded object to `process_resume` and writes the return
value to the page. `process_resume` currently ignores its argument and returns a fixed
sentence, so the file is never parsed. To make this a real reviewer, add PDF/DOCX text
extraction and an OpenAI call inside `process_resume` (or in
`gpt_resume_reviewer/gpt_resume_reviewer.py`, which was created for that), and read the
key from `OPEN_AI_KEY`.

The repo came from the audreyr cookiecutter-pypackage template, which explains the
Sphinx docs, tox matrix, bumpversion config, and the unused CLI stub.

Note: the badges in `README.rst` point at PyPI, Travis CI, and Read the Docs for
`gpt_resume_reviewer`. Those services are not currently wired up in this repo, and there
is no CI config checked in.

## Docs

Sphinx sources live in `docs/`. Build them with `make docs`, or serve them with live
reload via `make servedocs`.

## License

MIT. See [LICENSE](LICENSE).
