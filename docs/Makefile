# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

TUT_DST_DIR := tutorials
TUT_SRC_DIR := ../tutorials

NOTEBOOKS := \
	using_frank_as_a_module.ipynb \
	running_fits_in_loop.ipynb \
	prior_sensitivity_and_uncertainty.ipynb \
	AS209_clean_profile.dat \
	AS209_continuum.npz \


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf $(TUT_DST_DIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile $(NOTEBOOK_TARGETS)

NOTEBOOK_TARGETS := $(patsubst %, $(TUT_DST_DIR)/%, $(NOTEBOOKS))


$(TUT_DST_DIR)/%: $(TUT_SRC_DIR)/% $(TUT_DST_DIR)
	cp $< $@

.PHONY: help Makefile

$(TUT_DST_DIR):
	mkdir -p $(TUT_DST_DIR)


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: Makefile $(NOTEBOOK_TARGETS)
	@echo $(NOTEBOOK_TARGETS)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
