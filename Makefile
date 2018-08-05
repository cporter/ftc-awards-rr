IMAGE=blang/latex:ubuntu
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

# exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" "$@"

IMG_AWARD = img-generated/awards_4628.png img-generated/awards_8496.png img-generated/awards_inspire.png img-generated/awards_strong_inspire.png
IMG_PRES = img-generated/pres_gt_work.png img-generated/work_gt_pres.png img-generated/work_pres_balance.png
IMGDIR = img-generated

all: main.pdf

$(IMG_AWARD) $(IMG_PRES): | $(IMGDIR)

$(IMGDIR):
	mkdir -p $(IMGDIR)

$(IMGDIR)/awards_4628.png: img-generated
	python3 inspire_charts.py

$(IMGDIR)/pres_gt_work.png: img-generated
	python3 product_charts.py

main.pdf: main.tex $(IMG_AWARD) $(IMG_PRES)
	docker run --rm -i --net=none -v "$(ROOT_DIR):/data" $(IMAGE) \
    pdflatex main.tex

.PHONY: clean neat
clean:
	rm -f *.aux *.toc *.pdf
neat: clean
	rm -fr $(IMGDIR)
