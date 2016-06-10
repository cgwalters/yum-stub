include Makefile.inc

bin_programs = yum

all: $(bin_programs)

install: $(bin_programs)
	mkdir -p $(DESTDIR)$(bindir)
	for prog in $(bin_programs); do \
		install -m 0755 $$prog $(DESTDIR)$(bindir)/$$prog; \
	done
	ln -s yum $(DESTDIR)$(bindir)/dnf
