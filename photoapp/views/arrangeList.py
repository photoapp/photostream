

def arrangeListItems(imgList):
    jpgsrc = []
    linksrc = []
    urlsrc = []
    for x in imgList:
        if 'jpg' in x:
            jpgsrc.append(x)
        elif 'https%3A' in x:
            linksrc.append(x)
        else:
            urlsrc.append(x)
    imgsrc = []
    cntr = 0
    for x in urlsrc:
        try:
            imgsrc.append(jpgsrc[cntr])
            imgsrc.append(urlsrc[cntr])
            imgsrc.append(linksrc[cntr])
        except Exception as e:
            pass
        cntr = cntr + 1
    return imgsrc
