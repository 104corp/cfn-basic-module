#
.PHONY: default

#
default:
	@echo 'Building docs ...'
	cat HEADER.md > README.md
	cfn-docs templates/main.yaml >> README.md
	cat MAINTAINERS.md >> README.md
