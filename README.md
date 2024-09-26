# dcat-NFDI-ap

This is an extention of the DCAT Application Profile in LinkML. It is intended to be used by NFDI consortia as a core that can further be extended in profiles to provide domain specific metadata for a dataset.

## Website

[https://StroemPhi.github.io/dcat-NFDI-ap](https://StroemPhi.github.io/dcat-NFDI-ap)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [dcat_nfdi_ap](src/dcat_nfdi_ap)
    * [schema](src/dcat_nfdi_ap/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/dcat_nfdi_ap/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
