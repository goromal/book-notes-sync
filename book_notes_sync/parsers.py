class Title:
    def __init__(self, title_str):
        self.title_str = title_str.strip()
    def __repr__(self):
        return f"====== {self.title_str} ======"

class ChapterTitle:
    def __init__(self, title_str):
        self.title_str = title_str
    def __repr__(self):
        return f"===== {self.title_str} ====="

class Annotation:
    def __init__(self, highlight, annotation, link):
        self.hl = highlight
        self.an = annotation
        self.li = link
    def __repr__(self):
        return f"[[{self.li}|Reference]]:\n\n> {self.hl}\n\n{self.an}"

def extractMetaTitle(elem):
    try:
        if elem["paragraph"]["paragraphStyle"]["namedStyleType"] == "HEADING_1":
            return elem["paragraph"]["elements"][0]["textRun"]["content"].strip()
        else:
            return None
    except:
        return None

def extractChapterTitle(elem):
    try:
        if elem["paragraph"]["paragraphStyle"]["namedStyleType"] == "HEADING_2":
            return ChapterTitle(elem["paragraph"]["elements"][0]["textRun"]["content"].strip())
        else:
            return None
    except:
        return None

def extractHighlightAndAnnotation(cell):
    try:
        highlight = None
        annotation = ""
        for content in cell["content"]:
            if "paragraph" in content and "elements" in content["paragraph"]:
                for element in content["paragraph"]["elements"]:
                    if "textRun" in element and "content" in element["textRun"] and element["textRun"]["content"].strip() != "" and "textStyle" in element["textRun"]:
                        if "backgroundColor" in element["textRun"]["textStyle"]:
                            highlight = element["textRun"]["content"]
                        elif "20" not in element["textRun"]["content"]:
                            annotation = element["textRun"]["content"]
        return highlight, annotation
    except:
        return None, ""

def extractLink(cell):
    try:
        url = None
        for content in cell["content"]:
            if "paragraph" in content and "elements" in content["paragraph"]:
                for element in content["paragraph"]["elements"]:
                    if "textRun" in element and "textStyle" in element["textRun"] and "link" in element["textRun"]["textStyle"]:
                        url = element["textRun"]["textStyle"]["link"]["url"]
        return url
    except Exception as e:
        return None

def extractAnnotation(elem):
    if "table" in elem:
        try:
            highlight = None
            annotation = ""
            link = None
            for cell in elem["table"]["tableRows"][0]["tableCells"]:
                if "content" in cell:
                    for content in cell["content"]:
                        if "table" in content and "tableRows" in content["table"] and "tableCells" in content["table"]["tableRows"][0]:
                            for cellcell in content["table"]["tableRows"][0]["tableCells"]:
                                maybe_highlight, maybe_annotation = extractHighlightAndAnnotation(cellcell)
                                if maybe_highlight is not None:
                                    highlight = maybe_highlight
                                    annotation = maybe_annotation
                                maybe_link = extractLink(cellcell)
                                if maybe_link is not None:
                                    link = maybe_link
            if highlight is not None and link is not None:
                return Annotation(highlight, annotation, link)
            else:
                return None
        except:
            return None
    else:
        return None

def extractElements(document):
    title = Title(document["title"])
    recording_elements = False
    elements = []
    for elem in document["body"]["content"]:
        if recording_elements:
            comp = extractChapterTitle(elem)
            if comp is not None:
                elements.append(comp)
                continue
            comp = extractAnnotation(elem)
            if comp is not None:
                elements.append(comp)
        else:
            meta_title = extractMetaTitle(elem)
            if meta_title is not None and meta_title == "All your annotations":
                recording_elements = True
    return title, elements
