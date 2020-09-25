import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text
from functools import reduce
import os.path

entry = """
@article{DBLP:journals/jlap/NicolaFPT20,
  author    = {Rocco De Nicola and
               Gian Luigi Ferrari and
               Rosario Pugliese and
               Francesco Tiezzi},
  title     = {A formal approach to the engineering of domain-specific
distributed
               systems},
  journal   = {J. Log. Algebraic Methods Program.},
  volume    = {111},
  pages     = {100511},
  year      = {2020}
}"""

def split(value):
    splitByAnd = value.replace('\n',' ').strip().split(" and ")
    return [LatexNodes2Text().latex_to_text(v.strip()) for element in splitByAnd for v in element.split(',')]

def fileNameOf(target,mdmap, inst):
    filename = os.path.join(target,inst+'_'+mdmap['type']+'_'+str(mdmap['year'])+".md")
    counter = 0
    while os.path.exists(filename):
        counter = counter + 1
        filename = os.path.join(target,inst+'_'+mdmap['type']+'_'+mdmap['year']+"_"+str(counter)+"_"+".md")
    return filename


def handleValue(mdmap,key,value):
    if key == 'ENTRYTYPE':
        mdmap['type'] = value
    elif (key.lower() in ['partner', 'wps', 'author', 'editor']):
        mdmap[key.lower()] = split(value)
    else:
        mdmap[key.lower()] = value

def parseEntry(entry):
    result = {}
    for key in entry:
        handleValue(result,key,entry[key])
    result['published'] = "true"
    return result

def stringOf(value):
    return '"'+value.replace('\n',' ').strip()+'"'

def stringOfList(lst):
    return reduce(lambda x,y: x+"\n"+y,map(lambda v: "   - "+stringOf(v),lst))

def mdmapToString(mdmap):
    result = "---\n"
    for key in mdmap:
        result = result + key +": "
        if key in ['partner', 'wps', 'author', 'editor']:
            result = result + "\n" + stringOfList(mdmap[key])+"\n"
        elif key == "year":
            result = result + mdmap[key] +"\n"
        else:
            result = result + stringOf(mdmap[key]) + "\n"
    return result+"---\n"


def writeToFile(target,mdmap,inst):
    f = open(fileNameOf(target,mdmap,inst),'w')
    f.write(mdmapToString(mdmap))
    f.close()


def loadAndParseBibFile(filename):
    with open(filename) as bibtex_file:
        bibtex_str = bibtex_file.read()
    return bibtexparser.loads(bibtex_str.replace(u'\xa0', u' '))

def importBibliography(target,filename,inst=""):
    db = loadAndParseBibFile(filename)
    for entry in db.entries:
        writeToFile(target,parseEntry(entry),inst)

importBibliography("../_papers","unipi.bib", "unipi")
importBibliography("../_papers","imt.bib", "imt")
importBibliography("../_papers","uniud.bib", "uniud")
importBibliography("../_papers","isti.bib", "isti")
importBibliography("../_papers","gssi.bib","gssi")
