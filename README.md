# Endo's Blog

This repository contains a minimal static blog generator written in Python.
Posts are written in Markdown and placed in the `posts/` directory.
Running `build.py` converts them into HTML files inside the `dist/` directory.

## Requirements

- Python 3.7+
- The `markdown` package (`pip install markdown`)

## Usage

1. Add new Markdown files to the `posts/` directory. Each file should start
   with a top-level heading that will be used as the post title.
2. Run the build script:

```bash
python3 build.py
```

3. Open `dist/index.html` in your browser to view the site.

Feel free to customize the HTML template under `templates/base.html` and
extend the generator to suit your needs.
