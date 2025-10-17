# Resume Made with LaTeX

This résumé my academic journey, technical projects, and professional experiences in computer engineering, with a focus on embedded systems and autonomous vehicles.

Please note that this résumé might occasionally be outdated — I aim to keep it updated whenever possible.

## Compilation

> You need to have a LaTeX compiler installed on your machine (e.g., TeX Live, MiKTeX, or MacTeX).

To compile the document into a PDF:
```bash
latexmk -pdf main.tex
``` 

## Clean Temporary Files

To remove all auxiliary files generated during compilation:
```bash
latexmk -c
``` 

## Compile And Clean :

```bash
latexmk -pdf main.tex && latexmk -c
``` 