DEST = ../_papers

gssi:
	git rm $(DEST)/gssi_*
	python3 importgssi.py
	git add $(DEST)/gssi_*
	git commit -am "gssi bib updated"
	git push

imt:
	git rm $(DEST)/imt_*
	python3 importimt.py
	git add $(DEST)/imt_*
	git commit -am "imt bib updated"
	git push

isti:
	git rm $(DEST)/isti_*
	python3 importisti.py
	git add $(DEST)/isti_*
	git commit -am "isti bib updated"
	git push

unicam:
	git rm $(DEST)/unicam_*
	python3 importunicam.py
	git add $(DEST)/unicam_*
	git commit -am "unicam bib updated"
	git push

unipi:
	git rm $(DEST)/unipi_*
	python3 importunipi.py
	git add $(DEST)/unipi_*
	git commit -am "unipi bib updated"
	git push

uniud:
	git rm $(DEST)/uniud_*
	python3 importuniud.py
	git add $(DEST)/uniud_*
	git commit -am "uniud bib updated"
	git push

test:
	touch $(DEST)/test_.md
	git add $(DEST)/test_*
	git commit -am "make is testing"
	git rm $(DEST)/test_*
	python3 importtest.py
	git add $(DEST)/test_*
	git commit -am "test bib updated"
	@echo "test updated"


